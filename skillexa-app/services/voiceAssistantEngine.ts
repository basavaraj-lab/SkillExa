/**
 * Voice Assistant Engine for SkillExa AI
 * Implements real on-device wake-phrase detection ("Hello SkillExa!"),
 * Speech-to-Text (STT), Text-to-Speech (TTS) with Indian English accents,
 * 9 distinct state transitions, self-speech echo suppression, barge-in interruption,
 * and Web Audio synthesized chimes.
 */

export type AssistantMode = 'WAKE_WORD' | 'PUSH_TO_TALK' | 'CONTINUOUS';

export type AssistantState =
  | 'IDLE'
  | 'INITIALIZING'
  | 'WAKE_WORD_LISTENING'
  | 'ACTIVATED'
  | 'USER_LISTENING'
  | 'PROCESSING'
  | 'AI_SPEAKING'
  | 'PAUSED'
  | 'ERROR';

export interface VoiceEngineEvents {
  onStateChange: (state: AssistantState) => void;
  onTranscriptChange: (text: string, isFinal: boolean) => void;
  onSilenceCountdown?: (secondsLeft: number, text: string) => void;
  onWakeWordDetected: (ack: string) => void;
  onCommandDetected: (command: string) => void;
  onQuestionReady: (question: string) => void;
  onError: (message: string) => void;
}

const VARIED_ACKS = [
  "Hmm? I'm listening. Tell me what you need.",
  "Hmm? Yes, I'm here! What's on your mind?",
  "Hmm? What can I help you with?",
  "Hmm, go ahead, I'm listening!",
  "Hmm? I'm ready. How can I assist you?",
];

// Robust phonetic & regex patterns for "Heyy SkillExa" / "Hello SkillExa" / "SkillExa"
const WAKE_PHRASE_REGEX = /\b(hello+|heyy+|hey+|hi+|ok|okay)?\s*(skill\s*(exa|extra|exam|access|excel|ex|axa|alexa)|skillexa|skilleksha|skilexa|alexa)\b/i;
const STOP_PHRASE_REGEX = /\b(stop\s*skillexa|stop\s*listening|stop\s*speaking|shut\s*up|cancel|end\s*conversation|pause\s*assistant)\b/i;
const START_LISTENING_REGEX = /\b(start\s*listening|listen\s*to\s*me|i\s*have\s*a\s*question)\b/i;

export class VoiceAssistantEngine {
  private mode: AssistantMode = 'WAKE_WORD';
  private state: AssistantState = 'IDLE';
  private events: VoiceEngineEvents;

  private recognition: any = null;
  private isRecognitionActive: boolean = false;
  private hasMicPermission: boolean = false;
  private isSpeakingSelfAudio: boolean = false;
  private isSpeakingCooldown: boolean = false;
  private cooldownTimeout: any = null;
  private activeStream: MediaStream | null = null;
  private restartTimeout: any = null;
  private selectedVoice: SpeechSynthesisVoice | null = null;
  private audioContext: any = null;
  private wasAborted: boolean = false;

  // 5-6 Second Silence Timer & Transcript Buffer
  private silenceTimer: any = null;
  private silenceCountdownTimer: any = null;
  private secondsRemaining: number = 0;
  private accumulatedTranscript: string = '';

  constructor(events: VoiceEngineEvents) {
    this.events = events;
    this.initVoices();
  }

  // -------------------------------------------------------------
  // 1. INITIALIZATION & MICROPHONE AUDIO CAPTURE
  // -------------------------------------------------------------
  public async initializeMicrophone(): Promise<boolean> {
    this.log('Requesting microphone permissions and initializing audio stream...');
    this.setState('INITIALIZING');

    if (typeof window === 'undefined') {
      this.setState('ERROR');
      this.events.onError('Audio engine is only supported in browser/web environments.');
      return false;
    }

    // Step A: Request explicit user media stream (mic capture)
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({
          audio: {
            echoCancellation: true,
            noiseSuppression: true,
            autoGainControl: true,
          },
        });
        this.activeStream = stream;
        this.hasMicPermission = true;
        this.log('Microphone permission granted successfully.');
      } catch (err: any) {
        this.log('Microphone permission denied or failed:', err);
        this.hasMicPermission = false;
        this.setState('ERROR');
        this.events.onError(
          'Microphone permission was denied. Please click the camera/mic icon in your browser address bar to allow access.'
        );
        return false;
      }
    }

    // Step B: Initialize SpeechRecognition instance
    const SpeechRecognition =
      (window as any).SpeechRecognition || (window as any).webkitSpeechRecognition;

    if (!SpeechRecognition) {
      this.log('SpeechRecognition API not found in this browser.');
      this.setState('ERROR');
      this.events.onError(
        'Your browser does not support SpeechRecognition. Please use Google Chrome, Microsoft Edge, or Safari.'
      );
      return false;
    }

    try {
      if (!this.recognition) {
        this.recognition = new SpeechRecognition();
        this.recognition.continuous = true;
        this.recognition.interimResults = true;
        this.recognition.lang = 'en-IN'; // Indian English accent recognition
        this.recognition.maxAlternatives = 1;

        this.recognition.onstart = () => {
          this.isRecognitionActive = true;
          this.log(`Recognition stream started. Current mode: ${this.mode}`);
          if (this.mode === 'WAKE_WORD') {
            this.setState('WAKE_WORD_LISTENING');
          } else if (this.mode === 'PUSH_TO_TALK' || this.mode === 'CONTINUOUS') {
            this.setState('USER_LISTENING');
          }
        };

        this.recognition.onresult = (event: any) => {
          this.handleRecognitionResult(event);
        };

        this.recognition.onerror = (event: any) => {
          this.log('SpeechRecognition error event:', event.error);
          if (event.error === 'not-allowed' || event.error === 'service-not-allowed') {
            this.hasMicPermission = false;
            this.setState('ERROR');
            this.events.onError('Microphone permission was blocked. Please tap the mic button to allow access.');
          } else if (event.error === 'network') {
            this.scheduleRestart(1500);
          } else if (event.error === 'aborted') {
            this.isRecognitionActive = false;
            this.wasAborted = true;
            this.setState('IDLE');
          }
        };

        this.recognition.onend = () => {
          this.isRecognitionActive = false;
          this.log('Recognition stream ended.');

          if (this.wasAborted) {
            this.log('Stream was aborted, halting auto-restart loop.');
            this.wasAborted = false;
            return;
          }

          // If AI is currently speaking or in post-speech echo cooldown, DO NOT restart mic
          if (this.isSpeakingSelfAudio || this.isSpeakingCooldown || this.state === 'AI_SPEAKING') {
            this.log('Mic ended while AI speaking, skipping auto-restart until speech completes.');
            return;
          }

          // If in continuous or wake word mode and not paused or speaking, restart loop with safe debounce
          if (
            (this.mode === 'WAKE_WORD' || this.mode === 'CONTINUOUS') &&
            this.state !== 'PAUSED' &&
            this.state !== 'ERROR' &&
            this.state !== 'IDLE' &&
            this.state !== 'PROCESSING' &&
            !this.isSpeakingSelfAudio &&
            !this.isSpeakingCooldown
          ) {
            this.scheduleRestart(600);
          } else if (this.mode === 'PUSH_TO_TALK' && this.state === 'USER_LISTENING') {
            this.setState('IDLE');
          }
        };
      }

      return true;
    } catch (e: any) {
      this.log('Error creating SpeechRecognition:', e);
      this.setState('ERROR');
      this.events.onError(`Voice initialization error: ${e.message || e}`);
      return false;
    }
  }

  // -------------------------------------------------------------
  // 2. RECOGNITION PROCESSING & KEYWORD SPOTTING
  // -------------------------------------------------------------
  private handleRecognitionResult(event: any) {
    let interimTranscript = '';
    let finalTranscript = '';

    for (let i = event.resultIndex; i < event.results.length; ++i) {
      const text = event.results[i][0].transcript;
      if (event.results[i].isFinal) {
        finalTranscript += text + ' ';
      } else {
        interimTranscript += text;
      }
    }

    const currentText = (finalTranscript || interimTranscript).trim();
    if (!currentText) return;

    // STRICT ECHO & SELF-SPEECH SUPPRESSION:
    // If the assistant is speaking or cooling down after speech, completely discard all mic input!
    if (this.state === 'AI_SPEAKING' || this.isSpeakingSelfAudio || this.isSpeakingCooldown) {
      // Only allow an explicit "stop" command if student clearly commands it
      if (STOP_PHRASE_REGEX.test(currentText)) {
        this.log(`Stop command detected while speaking: "${currentText}"`);
        this.cancelSpeech();
        return;
      }
      // Drop all speaker audio / self-echo
      return;
    }

    // VOICE COMMAND: "Stop SkillExa" / "Stop speaking" / "End conversation"
    if (STOP_PHRASE_REGEX.test(currentText)) {
      this.log(`Stop command detected: "${currentText}"`);
      this.cancelSpeech();
      this.isSpeakingSelfAudio = false;
      this.setState('IDLE');
      this.events.onCommandDetected('STOP');
      this.speak("Stopping. I'm ready whenever you need me.");
      return;
    }

    // VOICE COMMAND: "Start listening"
    if (START_LISTENING_REGEX.test(currentText) && this.state !== 'USER_LISTENING') {
      this.log('Start listening command detected.');
      this.playChime();
      this.setState('USER_LISTENING');
      return;
    }

    // ---------------------------------------------------------
    // A. WAKE WORD DETECTION ("Hello SkillExa")
    // ---------------------------------------------------------
    if (this.state === 'WAKE_WORD_LISTENING') {
      if (WAKE_PHRASE_REGEX.test(currentText)) {
        this.log(`>>> Wake phrase detected in transcript: "${currentText}" <<<`);

        // Play pleasant acoustic chime
        this.playChime();

        // Switch to ACTIVATED state
        this.setState('ACTIVATED');

        // Check if student already spoke question after wake phrase (e.g. "heyy skillexa what is an array")
        const inlineQuestion = currentText
          .replace(WAKE_PHRASE_REGEX, '')
          .replace(/^[,\s?!.-]+/, '')
          .trim();

        const ack = VARIED_ACKS[Math.floor(Math.random() * VARIED_ACKS.length)];
        this.events.onWakeWordDetected(ack);

        if (inlineQuestion.length >= 3) {
          this.log(`Inline question detected with wake phrase: "${inlineQuestion}"`);
          this.speak("Hmm? Let me check that for you.", () => {
            this.setState('PROCESSING');
            this.events.onQuestionReady(inlineQuestion);
          });
        } else {
          // Standard wake-up: Speak "Hmm?", open chat modal, then start listening for question
          this.speak(ack, () => {
            this.log('Acknowledgment completed. Listening for student question...');
            this.setState('USER_LISTENING');
            // Clear any leftover transcript buffer
            this.events.onTranscriptChange('', false);
          });
        }
        return;
      }
      return;
    }

    // ---------------------------------------------------------
    // B. ACTIVE STUDENT QUESTION CAPTURE (USER_LISTENING)
    // ---------------------------------------------------------
    if (this.state === 'USER_LISTENING') {
      const fullText = (finalTranscript || interimTranscript).trim();
      if (!fullText) return;

      this.accumulatedTranscript = fullText;
      this.events.onTranscriptChange(fullText, Boolean(finalTranscript));

      // Reset any active silence countdown timers
      this.clearSilenceTimer();

      // Wait 6 seconds of silence so the student can complete their full thought
      const SILENCE_SECONDS = 6;
      this.secondsRemaining = SILENCE_SECONDS;
      if (this.events.onSilenceCountdown) {
        this.events.onSilenceCountdown(this.secondsRemaining, fullText);
      }

      this.silenceCountdownTimer = setInterval(() => {
        this.secondsRemaining -= 1;
        if (this.events.onSilenceCountdown) {
          this.events.onSilenceCountdown(Math.max(0, this.secondsRemaining), this.accumulatedTranscript);
        }
        if (this.secondsRemaining <= 0) {
          if (this.silenceCountdownTimer) {
            clearInterval(this.silenceCountdownTimer);
            this.silenceCountdownTimer = null;
          }
        }
      }, 1000);

      this.silenceTimer = setTimeout(() => {
        this.clearSilenceTimer();

        const question = this.accumulatedTranscript.trim();
        if (question.length >= 2) {
          this.log(`Silence period elapsed (6 seconds). Submitting student question: "${question}"`);
          this.setState('PROCESSING');
          this.events.onQuestionReady(question);
          this.accumulatedTranscript = '';
          if (this.mode === 'PUSH_TO_TALK') {
            this.stopListening();
          }
        }
      }, SILENCE_SECONDS * 1000);
    }
  }

  // -------------------------------------------------------------
  // 3. CONTROLS & STATE TRANSITIONS
  // -------------------------------------------------------------
  public async setMode(newMode: AssistantMode): Promise<boolean> {
    this.mode = newMode;
    this.log(`Mode changed to: ${newMode}`);

    if (newMode === 'WAKE_WORD') {
      return await this.startWakeWordListening();
    } else if (newMode === 'CONTINUOUS') {
      return await this.startContinuousListening();
    } else {
      // Push to talk: keep mic ready but idle
      if (this.state === 'WAKE_WORD_LISTENING' || this.state === 'USER_LISTENING') {
        this.stopListening();
      }
      this.setState('IDLE');
      return true;
    }
  }

  public getMode(): AssistantMode {
    return this.mode;
  }

  public getState(): AssistantState {
    return this.state;
  }

  public setState(state: AssistantState) {
    this.state = state;
    this.log(`State transition -> ${state}`);
    this.events.onStateChange(state);
  }

  public async startWakeWordListening(): Promise<boolean> {
    this.mode = 'WAKE_WORD';
    this.wasAborted = false;
    if (!this.hasMicPermission || !this.recognition) {
      const ok = await this.initializeMicrophone();
      if (!ok) return false;
    }

    try {
      if (!this.isRecognitionActive && this.recognition) {
        this.recognition.start();
      }
      this.setState('WAKE_WORD_LISTENING');
      return true;
    } catch (e) {
      this.setState('WAKE_WORD_LISTENING');
      return true;
    }
  }

  public async startContinuousListening(): Promise<boolean> {
    this.mode = 'CONTINUOUS';
    this.wasAborted = false;
    if (!this.hasMicPermission || !this.recognition) {
      const ok = await this.initializeMicrophone();
      if (!ok) return false;
    }

    try {
      if (!this.isRecognitionActive && this.recognition) {
        this.recognition.start();
      }
      this.setState('USER_LISTENING');
      return true;
    } catch (e) {
      this.setState('USER_LISTENING');
      return true;
    }
  }

  public async startPushToTalk(): Promise<boolean> {
    this.mode = 'PUSH_TO_TALK';
    this.wasAborted = false;
    if (!this.hasMicPermission || !this.recognition) {
      const ok = await this.initializeMicrophone();
      if (!ok) return false;
    }

    try {
      this.cancelSpeech();
      if (!this.isRecognitionActive && this.recognition) {
        this.recognition.start();
      }
      this.setState('USER_LISTENING');
      return true;
    } catch (e) {
      this.setState('USER_LISTENING');
      return true;
    }
  }

  public clearSilenceTimer(): void {
    if (this.silenceTimer) {
      clearTimeout(this.silenceTimer);
      this.silenceTimer = null;
    }
    if (this.silenceCountdownTimer) {
      clearInterval(this.silenceCountdownTimer);
      this.silenceCountdownTimer = null;
    }
    this.secondsRemaining = 0;
  }

  public stopListening() {
    this.log('Stopping microphone listening.');
    this.clearSilenceTimer();
    if (this.restartTimeout) {
      clearTimeout(this.restartTimeout);
      this.restartTimeout = null;
    }
    if (this.recognition && this.isRecognitionActive) {
      try {
        this.recognition.stop();
      } catch (e) {}
    }
    if (this.state === 'USER_LISTENING' || this.state === 'WAKE_WORD_LISTENING') {
      this.setState('IDLE');
    }
  }

  public pause() {
    this.log('Pausing voice assistant.');
    this.cancelSpeech();
    this.stopListening();
    this.setState('PAUSED');
  }

  public resume() {
    this.log('Resuming voice assistant.');
    if (this.mode === 'WAKE_WORD') {
      this.startWakeWordListening();
    } else if (this.mode === 'CONTINUOUS') {
      this.startContinuousListening();
    } else {
      this.setState('IDLE');
    }
  }

  private scheduleRestart(ms: number = 400) {
    if (this.restartTimeout) clearTimeout(this.restartTimeout);
    this.restartTimeout = setTimeout(() => {
      if (
        (this.mode === 'WAKE_WORD' || this.mode === 'CONTINUOUS') &&
        this.state !== 'PAUSED' &&
        this.state !== 'ERROR' &&
        !this.isSpeakingSelfAudio
      ) {
        try {
          if (this.recognition && !this.isRecognitionActive) {
            this.recognition.start();
          }
        } catch (e) {}
      }
    }, ms);
  }

  // -------------------------------------------------------------
  // 4. TEXT-TO-SPEECH (TTS) WITH INDIAN ENGLISH ACCENT
  // -------------------------------------------------------------
  private initVoices() {
    if (typeof window === 'undefined' || !window.speechSynthesis) return;

    const loadVoices = () => {
      const voices = window.speechSynthesis.getVoices();
      if (!voices || voices.length === 0) return;

      // Prefer Indian English voice (e.g. Google Indian English, Neerja, Rishi)
      const inVoice = voices.find(
        (v) =>
          v.lang === 'en-IN' ||
          v.name.includes('India') ||
          v.name.includes('Neerja') ||
          v.name.includes('Rishi')
      );
      const usVoice = voices.find(
        (v) =>
          v.lang.startsWith('en-US') &&
          (v.name.includes('Natural') || v.name.includes('Google') || v.name.includes('Samantha'))
      );
      const anyEnVoice = voices.find((v) => v.lang.startsWith('en'));

      this.selectedVoice = inVoice || usVoice || anyEnVoice || voices[0];
      this.log(`Loaded voice: ${this.selectedVoice?.name} (${this.selectedVoice?.lang})`);
    };

    loadVoices();
    if (window.speechSynthesis.onvoiceschanged !== undefined) {
      window.speechSynthesis.onvoiceschanged = loadVoices;
    }
  }

  public speak(text: string, onEndCallback?: () => void) {
    if (typeof window === 'undefined' || !window.speechSynthesis) {
      if (onEndCallback) onEndCallback();
      return;
    }

    window.speechSynthesis.cancel();

    const cleanText = text.trim();
    if (!cleanText) {
      if (onEndCallback) onEndCallback();
      return;
    }

    // Stop mic listening during TTS playback to prevent any speaker self-echo capture
    this.clearSilenceTimer();
    this.accumulatedTranscript = '';
    this.isSpeakingSelfAudio = true;
    this.isSpeakingCooldown = true;
    this.setState('AI_SPEAKING');

    if (this.recognition && this.isRecognitionActive) {
      try {
        this.recognition.stop();
      } catch (e) {}
      this.isRecognitionActive = false;
    }

    const utterance = new SpeechSynthesisUtterance(cleanText);
    if (this.selectedVoice) {
      utterance.voice = this.selectedVoice;
    }
    utterance.lang = 'en-IN';
    utterance.rate = 1.05; // Slightly brisk, natural cadence
    utterance.pitch = 1.0;

    utterance.onstart = () => {
      this.isSpeakingSelfAudio = true;
      this.isSpeakingCooldown = true;
      this.clearSilenceTimer();
      this.accumulatedTranscript = '';
      this.setState('AI_SPEAKING');
      this.log(`Started TTS playback: "${cleanText.substring(0, 60)}..."`);
    };

    utterance.onend = () => {
      this.log('TTS playback finished. Clearing echo buffer and cooling down...');
      this.clearSilenceTimer();
      this.accumulatedTranscript = '';
      this.events.onTranscriptChange('', false);

      // Acoustic echo cooldown: 800ms to allow room/speaker reverb to completely dissipate
      if (this.cooldownTimeout) clearTimeout(this.cooldownTimeout);
      this.cooldownTimeout = setTimeout(() => {
        this.isSpeakingSelfAudio = false;
        this.isSpeakingCooldown = false;
        this.log('Echo cooldown elapsed. Safely resuming microphone for human speech.');

        if (onEndCallback) {
          onEndCallback();
        } else {
          if (this.mode === 'CONTINUOUS') {
            // Resume listening for student follow-up
            this.setState('USER_LISTENING');
            this.scheduleRestart(150);
          } else if (this.mode === 'WAKE_WORD') {
            // Return to passive wake-word detection
            this.setState('WAKE_WORD_LISTENING');
            this.scheduleRestart(150);
          } else {
            this.setState('IDLE');
          }
        }
      }, 800);
    };

    utterance.onerror = (e) => {
      this.clearSilenceTimer();
      this.accumulatedTranscript = '';
      this.events.onTranscriptChange('', false);
      this.log('TTS playback notice/cancelled:', e);

      if (this.cooldownTimeout) clearTimeout(this.cooldownTimeout);
      this.cooldownTimeout = setTimeout(() => {
        this.isSpeakingSelfAudio = false;
        this.isSpeakingCooldown = false;
        if (onEndCallback) {
          onEndCallback();
        } else {
          this.setState(this.mode === 'WAKE_WORD' ? 'WAKE_WORD_LISTENING' : 'IDLE');
          this.scheduleRestart(150);
        }
      }, 300);
    };

    window.speechSynthesis.speak(utterance);
  }

  public cancelSpeech() {
    this.clearSilenceTimer();
    this.accumulatedTranscript = '';
    this.events.onTranscriptChange('', false);

    if (this.cooldownTimeout) {
      clearTimeout(this.cooldownTimeout);
      this.cooldownTimeout = null;
    }

    if (typeof window !== 'undefined' && window.speechSynthesis) {
      window.speechSynthesis.cancel();
    }
    this.isSpeakingSelfAudio = false;
    this.isSpeakingCooldown = false;

    if (this.state === 'AI_SPEAKING') {
      this.setState(this.mode === 'WAKE_WORD' ? 'WAKE_WORD_LISTENING' : 'IDLE');
      this.scheduleRestart(200);
    }
  }

  // -------------------------------------------------------------
  // 5. WEB AUDIO CHIME SYNTHESIZER
  // -------------------------------------------------------------
  public playChime() {
    if (typeof window === 'undefined') return;
    try {
      const AudioCtx = (window as any).AudioContext || (window as any).webkitAudioContext;
      if (!AudioCtx) return;

      if (!this.audioContext) {
        this.audioContext = new AudioCtx();
      }
      if (this.audioContext.state === 'suspended') {
        this.audioContext.resume();
      }

      const now = this.audioContext.currentTime;

      // Note 1: C5 (523 Hz)
      const osc1 = this.audioContext.createOscillator();
      const gain1 = this.audioContext.createGain();
      osc1.type = 'sine';
      osc1.frequency.setValueAtTime(523.25, now);
      gain1.gain.setValueAtTime(0.12, now);
      gain1.gain.exponentialRampToValueAtTime(0.001, now + 0.12);
      osc1.connect(gain1);
      gain1.connect(this.audioContext.destination);
      osc1.start(now);
      osc1.stop(now + 0.12);

      // Note 2: E5 (659 Hz) - pleasant confirmation
      const osc2 = this.audioContext.createOscillator();
      const gain2 = this.audioContext.createGain();
      osc2.type = 'sine';
      osc2.frequency.setValueAtTime(659.25, now + 0.08);
      gain2.gain.setValueAtTime(0.15, now + 0.08);
      gain2.gain.exponentialRampToValueAtTime(0.001, now + 0.22);
      osc2.connect(gain2);
      gain2.connect(this.audioContext.destination);
      osc2.start(now + 0.08);
      osc2.stop(now + 0.22);
    } catch (e) {
      // AudioContext failure or blocked
    }
  }

  // -------------------------------------------------------------
  // 6. LOGGING
  // -------------------------------------------------------------
  private log(...args: any[]) {
    console.log('[SkillExa Voice]', ...args);
  }
}
