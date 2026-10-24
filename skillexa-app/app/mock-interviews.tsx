import { Feather } from '@expo/vector-icons';
import { router } from 'expo-router';
import React, { useEffect, useRef, useState } from 'react';
import {
  ActivityIndicator,
  Alert,
  Platform,
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  View,
} from 'react-native';
import { AppHeader } from '../components/common/AppHeader';
import { ProgressBar } from '../components/common/EducationalCards';
import { Palette, Radii, Shadows } from '../constants/theme';
import { ApiClient, getApiBaseUrl } from '../services/api';

// Supported Categories
const CATEGORIES = [
  { id: 'Technical', label: 'Technical', icon: 'code', desc: 'Coding, core CS & system design' },
  { id: 'HR', label: 'HR Interview', icon: 'user-check', desc: 'Strengths, company fit & vision' },
  { id: 'Behavioral', label: 'Behavioral', icon: 'users', desc: 'Teamwork, STAR & conflict resolution' },
];

// Technical Subjects
const TECHNICAL_SUBJECTS = [
  'Python',
  'C',
  'C++',
  'Java',
  'Data Structures and Algorithms',
  'SQL and DBMS',
  'Operating Systems',
  'Computer Networks',
  'Object-Oriented Programming',
  'Software Engineering',
  'Artificial Intelligence',
  'Machine Learning',
  'Web Development',
  'Electronics and Communication Engineering fundamentals',
];

const TARGET_ROLES = [
  'Software Developer',
  'Frontend Engineer',
  'Backend Engineer',
  'Full Stack Developer',
  'Embedded & IoT Engineer',
  'AI/ML Engineer',
  'Data Engineer',
];

const DIFFICULTIES = ['Beginner', 'Intermediate', 'Advanced'];
const EXPERIENCE_LEVELS = ['Student', 'Fresher', 'Experienced'];
const QUESTION_COUNTS = [3, 5, 8];

/**
 * Safely merge existing base transcript with newly recognized speech
 * to prevent duplicates, repetition of interim hypotheses, or echo.
 */
function mergeTranscripts(base: string, spoken: string): string {
  const b = base.trim();
  const s = spoken.trim();
  if (!b) return s;
  if (!s) return b;

  // If the spoken text already starts with the base text, avoid repeating it
  if (s.toLowerCase().startsWith(b.toLowerCase())) {
    return s;
  }

  const bWords = b.split(/\s+/);
  const sWords = s.split(/\s+/);

  // Check up to 5 words of overlap at the boundary
  const maxOverlap = Math.min(bWords.length, sWords.length, 5);
  for (let len = maxOverlap; len > 0; len--) {
    const bTail = bWords.slice(-len).map((w) => w.toLowerCase()).join(' ');
    const sHead = sWords.slice(0, len).map((w) => w.toLowerCase()).join(' ');
    if (bTail === sHead) {
      return `${b} ${sWords.slice(len).join(' ')}`.trim();
    }
  }

  return `${b} ${s}`.trim();
}

export default function MockInterviewsPage() {
  // Navigation / View State: 'setup' | 'interview' | 'feedback' | 'report' | 'history'
  const [currentView, setCurrentView] = useState<'setup' | 'interview' | 'feedback' | 'report' | 'history'>('setup');

  // Setup Form State
  const [selectedCategory, setSelectedCategory] = useState<string>('Technical');
  const [selectedRole, setSelectedRole] = useState<string>('Software Developer');
  const [selectedSubject, setSelectedSubject] = useState<string>('Python');
  const [selectedDifficulty, setSelectedDifficulty] = useState<string>('Intermediate');
  const [selectedExperience, setSelectedExperience] = useState<string>('Student');
  const [selectedQuestionCount, setSelectedQuestionCount] = useState<number>(3);
  const [selectedMode, setSelectedMode] = useState<'text' | 'voice'>('text');

  // Active Session State
  const [activeSession, setActiveSession] = useState<any>(null);
  const [currentQuestion, setCurrentQuestion] = useState<any>(null);
  const [answerText, setAnswerText] = useState<string>('');
  const [isSubmitting, setIsSubmitting] = useState<boolean>(false);
  const [lastEvaluation, setLastEvaluation] = useState<any>(null);
  const [finalReport, setFinalReport] = useState<any>(null);

  // History State
  const [historyItems, setHistoryItems] = useState<any[]>([]);
  const [isLoadingHistory, setIsLoadingHistory] = useState<boolean>(false);

  // Voice & Speech State
  const [isSpeakingQuestion, setIsSpeakingQuestion] = useState<boolean>(false);
  const [autoAskQuestion, setAutoAskQuestion] = useState<boolean>(true);
  const [selectedVoicePersona, setSelectedVoicePersona] = useState<string>('Aria (Clear Studio)');
  const [speechRate, setSpeechRate] = useState<number>(0.95);
  const audioElementRef = useRef<any>(null);
  const [isRecording, setIsRecording] = useState<boolean>(false);
  const [speechRecognitionSupported, setSpeechRecognitionSupported] = useState<boolean>(false);
  const recognitionRef = useRef<any>(null);
  const isRecordingRef = useRef<boolean>(false);
  const baseAnswerRef = useRef<string>('');
  const answerTextRef = useRef<string>('');

  // Keep answerTextRef synchronized for recognition callbacks
  useEffect(() => {
    answerTextRef.current = answerText;
  }, [answerText]);

  // Timer State
  const [elapsedSeconds, setElapsedSeconds] = useState<number>(0);

  useEffect(() => {
    let interval: any = null;
    if (currentView === 'interview') {
      interval = setInterval(() => {
        setElapsedSeconds((prev) => prev + 1);
      }, 1000);
    }
    return () => {
      if (interval) clearInterval(interval);
    };
  }, [currentView]);

  // Proactively verify and ensure authentication session on mount
  useEffect(() => {
    ApiClient.ensureAuthToken().catch((err) => {
      console.warn('Initial authentication check:', err);
    });
  }, []);

  // Initialize Speech Recognition on Web / Supported Browsers
  useEffect(() => {
    if (Platform.OS === 'web' && typeof window !== 'undefined') {
      const SpeechRecognition =
        (window as any).SpeechRecognition || (window as any).webkitSpeechRecognition;
      if (SpeechRecognition) {
        setSpeechRecognitionSupported(true);
        const recog = new SpeechRecognition();
        recog.continuous = true;
        recog.interimResults = true;
        recog.lang = 'en-US';

        recog.onresult = (event: any) => {
          let finalTranscript = '';
          let interimTranscript = '';

          for (let i = 0; i < event.results.length; ++i) {
            const res = event.results[i];
            if (res.isFinal) {
              finalTranscript += res[0].transcript + ' ';
            } else {
              interimTranscript += res[0].transcript;
            }
          }

          const currentSessionSpoken = `${finalTranscript} ${interimTranscript}`.replace(/\s+/g, ' ').trim();
          const merged = mergeTranscripts(baseAnswerRef.current, currentSessionSpoken);
          setAnswerText(merged);
        };

        recog.onerror = (e: any) => {
          console.warn('Speech recognition error:', e.error);
          if (e.error === 'not-allowed') {
            setIsRecording(false);
            isRecordingRef.current = false;
          }
        };

        recog.onend = () => {
          // If the user hasn't explicitly clicked stop, keep recording active across browser silence pauses
          if (isRecordingRef.current) {
            try {
              baseAnswerRef.current = answerTextRef.current.trim();
              recog.start();
            } catch (e) {
              setIsRecording(false);
              isRecordingRef.current = false;
            }
          } else {
            setIsRecording(false);
            baseAnswerRef.current = answerTextRef.current.trim();
          }
        };

        recognitionRef.current = recog;
      }
    }
  }, []);

  // -------------------------------------------------------------
  // Text-To-Speech (TTS) Voice Converter for Asking Questions
  // Crystal Clear Studio Neural Audio (Edge-TTS Aria, Guy, Jenny, Neerja)
  // -------------------------------------------------------------
  const fallbackWebSpeech = (text: string) => {
    if (Platform.OS === 'web' && typeof window !== 'undefined' && window.speechSynthesis) {
      try {
        window.speechSynthesis.cancel();
        const utterance = new SpeechSynthesisUtterance(text);
        utterance.rate = speechRate;
        utterance.lang = 'en-US';

        const voices = window.speechSynthesis.getVoices();
        if (voices && voices.length > 0) {
          const isFemale =
            selectedVoicePersona.includes('Aria') ||
            selectedVoicePersona.includes('Jenny') ||
            selectedVoicePersona.includes('Neerja');
          const preferredKeywords = isFemale
            ? ['Natural', 'Neural', 'Google', 'Samantha', 'Victoria', 'Zira']
            : ['Natural', 'Neural', 'Daniel', 'Alex', 'David'];

          const matchedVoice =
            voices.find((v) => preferredKeywords.some((pk) => v.name.includes(pk)) && !v.name.includes('Bad')) ||
            voices.find((v) => v.lang.startsWith('en') && !v.name.includes('Bad') && !v.name.includes('Albert'));

          if (matchedVoice) {
            utterance.voice = matchedVoice;
          }
        }

        utterance.onstart = () => setIsSpeakingQuestion(true);
        utterance.onend = () => setIsSpeakingQuestion(false);
        utterance.onerror = () => setIsSpeakingQuestion(false);

        setIsSpeakingQuestion(true);
        window.speechSynthesis.speak(utterance);
      } catch (e) {
        setIsSpeakingQuestion(false);
      }
    } else {
      setIsSpeakingQuestion(false);
    }
  };

  const playQuestionSpeech = (questionText?: string, questionNumber?: number, forceReplay: boolean = false) => {
    const textToSpeak = questionText || currentQuestion?.question_text;
    if (!textToSpeak) return;

    // Toggle stop if already playing and not an explicit replay command
    if (isSpeakingQuestion && !forceReplay) {
      if (Platform.OS === 'web' && typeof window !== 'undefined' && window.speechSynthesis) {
        window.speechSynthesis.cancel();
      }
      if (audioElementRef.current) {
        try {
          audioElementRef.current.pause();
          audioElementRef.current.currentTime = 0;
        } catch (e) {}
      }
      setIsSpeakingQuestion(false);
      return;
    }

    const qNum = questionNumber ?? currentQuestion?.question_number;
    const spokenPrefix = qNum ? `Question ${qNum}. ` : '';
    const fullSpokenText = `${spokenPrefix}${textToSpeak}`;

    // Clean up any previously playing speech/audio
    if (Platform.OS === 'web' && typeof window !== 'undefined' && window.speechSynthesis) {
      window.speechSynthesis.cancel();
    }
    if (audioElementRef.current) {
      try {
        audioElementRef.current.pause();
        audioElementRef.current.currentTime = 0;
      } catch (e) {}
    }

    setIsSpeakingQuestion(true);

    // Map voice persona to backend neural voice key
    let voiceCode = 'aria';
    if (selectedVoicePersona.includes('Guy')) {
      voiceCode = 'guy';
    } else if (selectedVoicePersona.includes('Jenny')) {
      voiceCode = 'jenny';
    } else if (selectedVoicePersona.includes('Neerja')) {
      voiceCode = 'neerja';
    }

    // High-Fidelity Python Edge Neural Voice Synthesis (Real human clarity)
    ApiClient.synthesizeTTS(fullSpokenText, voiceCode)
      .then((res) => {
        if (res.data?.audio_url && typeof Audio !== 'undefined') {
          const rawUrl = res.data.audio_url;
          const baseUrl = getApiBaseUrl().replace(/\/api\/?$/, '');
          const fullAudioUrl = rawUrl.startsWith('http')
            ? rawUrl
            : `${baseUrl}${rawUrl.startsWith('/') ? '' : '/'}${rawUrl}`;

          const audio = new Audio(fullAudioUrl);
          audio.playbackRate = speechRate;
          audioElementRef.current = audio;

          audio.onplay = () => setIsSpeakingQuestion(true);
          audio.onended = () => setIsSpeakingQuestion(false);
          audio.onerror = (e) => {
            console.warn('Neural audio playback failed, falling back to browser synthesis:', e);
            fallbackWebSpeech(fullSpokenText);
          };

          const playPromise = audio.play();
          if (playPromise !== undefined) {
            playPromise.catch((err) => {
              console.warn('Audio play() rejected:', err);
              fallbackWebSpeech(fullSpokenText);
            });
          }
        } else {
          fallbackWebSpeech(fullSpokenText);
        }
      })
      .catch((err) => {
        console.warn('Backend neural TTS call failed, using client fallback:', err);
        fallbackWebSpeech(fullSpokenText);
      });
  };

  // Automatically ask the question using the voice converter when displayed
  useEffect(() => {
    if (currentView === 'interview' && currentQuestion?.question_text && autoAskQuestion) {
      const timer = setTimeout(() => {
        playQuestionSpeech(currentQuestion.question_text, currentQuestion.question_number, true);
      }, 450);
      return () => {
        clearTimeout(timer);
        if (Platform.OS === 'web' && typeof window !== 'undefined' && window.speechSynthesis) {
          window.speechSynthesis.cancel();
        }
        if (audioElementRef.current) {
          try {
            audioElementRef.current.pause();
          } catch (e) {}
        }
      };
    }
  }, [currentQuestion?.id, currentView, autoAskQuestion]);

  // -------------------------------------------------------------
  // Speech-To-Text (STT) Recording Toggle
  // -------------------------------------------------------------
  const toggleRecording = () => {
    if (isRecording) {
      isRecordingRef.current = false;
      if (recognitionRef.current) {
        try {
          recognitionRef.current.stop();
        } catch (e) {}
      }
      setIsRecording(false);
      baseAnswerRef.current = answerTextRef.current.trim();
    } else {
      baseAnswerRef.current = answerTextRef.current.trim();
      isRecordingRef.current = true;
      if (recognitionRef.current) {
        try {
          recognitionRef.current.start();
          setIsRecording(true);
        } catch (e) {
          isRecordingRef.current = false;
          setIsRecording(false);
          Alert.alert('Microphone Access', 'Please ensure microphone permissions are granted in your browser settings.');
        }
      } else {
        // Fallback simulation / prompt
        setIsRecording(true);
        setTimeout(() => {
          setIsRecording(false);
          isRecordingRef.current = false;
          setAnswerText((prev) =>
            prev ? `${prev} Transcribed voice response confirmed.` : 'I approach this technical problem by analyzing memory constraints and data structures.'
          );
        }, 3000);
      }
    }
  };

  // -------------------------------------------------------------
  // Start Interview API Workflow
  // -------------------------------------------------------------
  const handleStartInterview = async () => {
    setIsSubmitting(true);
    const subject = selectedCategory === 'Technical' ? selectedSubject : selectedCategory;
    try {
      await ApiClient.ensureAuthToken();
      const res = await ApiClient.startAIInterview({
        interview_category: selectedCategory,
        job_role: selectedRole,
        subject,
        difficulty: selectedDifficulty,
        experience_level: selectedExperience,
        total_questions: selectedQuestionCount,
        interview_mode: selectedMode,
        preferred_language: 'English',
        duration_minutes: selectedQuestionCount * 5,
      });

      setIsSubmitting(false);
      if (res.success && res.data) {
        setActiveSession(res.data);
        setCurrentQuestion(res.data.current_question);
        setAnswerText('');
        baseAnswerRef.current = '';
        answerTextRef.current = '';
        setElapsedSeconds(0);
        setCurrentView('interview');
      } else {
        Alert.alert('Interview Setup Failed', res.message || 'Could not initiate AI session. Please log in.');
      }
    } catch (err: any) {
      setIsSubmitting(false);
      Alert.alert('Connection Error', err.message || 'Cannot reach FastAPI server.');
    }
  };

  // -------------------------------------------------------------
  // Submit Answer & Evaluate API Workflow
  // -------------------------------------------------------------
  const handleSubmitAnswer = async () => {
    if (!answerText.trim() || !activeSession || !currentQuestion) {
      Alert.alert('Answer Required', 'Please provide or record your answer before submitting.');
      return;
    }

    if (isRecording && recognitionRef.current) {
      isRecordingRef.current = false;
      try {
        recognitionRef.current.stop();
      } catch (e) {}
      setIsRecording(false);
    }
    if (isSpeakingQuestion && Platform.OS === 'web' && window.speechSynthesis) {
      window.speechSynthesis.cancel();
      setIsSpeakingQuestion(false);
    }

    setIsSubmitting(true);
    try {
      const res = await ApiClient.submitAIAnswer(activeSession.id, {
        question_id: currentQuestion.id,
        answer_text: answerText.trim(),
        answer_mode: selectedMode,
        speech_metrics: selectedMode === 'voice' ? { duration_seconds: elapsedSeconds } : undefined,
      });

      setIsSubmitting(false);
      if (res.success && res.data) {
        setLastEvaluation(res.data);
        setCurrentView('feedback');
      } else {
        Alert.alert('Submission Error', res.message || 'Could not evaluate answer.');
      }
    } catch (err: any) {
      setIsSubmitting(false);
      Alert.alert('Error', err.message || 'An error occurred during evaluation.');
    }
  };

  // -------------------------------------------------------------
  // Next Question / Finish Transition
  // -------------------------------------------------------------
  const handleProceedFromFeedback = async () => {
    if (lastEvaluation?.is_interview_complete) {
      // Fetch Final Report
      setIsSubmitting(true);
      try {
        const repRes = await ApiClient.getAIInterviewReport(activeSession.id);
        setIsSubmitting(false);
        if (repRes.success && repRes.data) {
          setFinalReport(repRes.data);
          setCurrentView('report');
        } else {
          Alert.alert('Report Notice', 'Generating report summary...');
          setCurrentView('setup');
        }
      } catch (e: any) {
        setIsSubmitting(false);
        setCurrentView('setup');
      }
    } else {
      // Fetch next unanswered question
      setIsSubmitting(true);
      try {
        const stateRes = await ApiClient.getAIInterviewState(activeSession.id);
        setIsSubmitting(false);
        if (stateRes.success && stateRes.data?.current_question) {
          setCurrentQuestion(stateRes.data.current_question);
          setAnswerText('');
          baseAnswerRef.current = '';
          answerTextRef.current = '';
          setCurrentView('interview');
        } else {
          Alert.alert('Notice', 'Interview complete!');
          setCurrentView('setup');
        }
      } catch (e: any) {
        setIsSubmitting(false);
        Alert.alert('Error', 'Could not load next question.');
      }
    }
  };

  // -------------------------------------------------------------
  // End Interview Early
  // -------------------------------------------------------------
  const handleEndInterviewEarly = () => {
    Alert.alert('End Interview?', 'Are you sure you want to conclude this interview session early?', [
      { text: 'Resume', style: 'cancel' },
      {
        text: 'End & View Report',
        style: 'destructive',
        onPress: async () => {
          if (activeSession) {
            setIsSubmitting(true);
            try {
              const res = await ApiClient.finishAIInterview(activeSession.id);
              setIsSubmitting(false);
              if (res.success && res.data) {
                setFinalReport(res.data);
                setCurrentView('report');
                return;
              }
            } catch (e) {}
            setIsSubmitting(false);
          }
          setCurrentView('setup');
        },
      },
    ]);
  };

  // -------------------------------------------------------------
  // Load History
  // -------------------------------------------------------------
  const loadHistory = async () => {
    setIsLoadingHistory(true);
    setCurrentView('history');
    try {
      const res = await ApiClient.getAIInterviewHistory(1, 20);
      setIsLoadingHistory(false);
      if (res.success && res.data?.items) {
        setHistoryItems(res.data.items);
      }
    } catch (e) {
      setIsLoadingHistory(false);
    }
  };

  const viewPastReport = async (interviewId: string) => {
    setIsSubmitting(true);
    try {
      const res = await ApiClient.getAIInterviewReport(interviewId);
      setIsSubmitting(false);
      if (res.success && res.data) {
        setFinalReport(res.data);
        setCurrentView('report');
      } else {
        Alert.alert('Incomplete Session', 'This session does not have a completed report.');
      }
    } catch (e: any) {
      setIsSubmitting(false);
      Alert.alert('Report Notice', 'Session report is pending or unavailable.');
    }
  };

  const formatTimer = (sec: number) => {
    const mins = Math.floor(sec / 60);
    const secs = sec % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  // =============================================================
  // RENDER: SETUP VIEW
  // =============================================================
  if (currentView === 'setup') {
    return (
      <SafeAreaView style={styles.safeArea}>
        <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
        <AppHeader
          showBack
          title="AI Mock Interview"
          subtitle="Campus Placement & Technical Preparation"
          rightAction={
            <TouchableOpacity style={styles.headerHistoryBtn} onPress={loadHistory}>
              <Feather name="clock" size={16} color={Palette.aiPurple} />
              <Text style={styles.headerHistoryText}>History</Text>
            </TouchableOpacity>
          }
        />

        <ScrollView style={styles.content} contentContainerStyle={styles.scrollContent}>
          {/* Hero Banner */}
          <View style={styles.heroBanner}>
            <View style={styles.heroIconBadge}>
              <Feather name="cpu" size={28} color="#FFFFFF" />
            </View>
            <View style={styles.heroTextContainer}>
              <Text style={styles.heroTitle}>SkillExa AI Interview Engine</Text>
              <Text style={styles.heroSubtitle}>
                Simulate real campus placement, technical, HR, and behavioral interviews with real-time feedback & multi-criteria evaluation.
              </Text>
            </View>
          </View>

          {/* 1. Category Selection */}
          <Text style={styles.sectionTitle}>1. Interview Category</Text>
          <View style={styles.categoriesRow}>
            {CATEGORIES.map((cat) => {
              const active = selectedCategory === cat.id;
              return (
                <TouchableOpacity
                  key={cat.id}
                  style={[styles.categoryCard, active && styles.categoryCardActive]}
                  onPress={() => setSelectedCategory(cat.id)}
                >
                  <View style={[styles.categoryIconCircle, active && styles.categoryIconCircleActive]}>
                    <Feather name={cat.icon as any} size={20} color={active ? '#FFFFFF' : Palette.aiPurple} />
                  </View>
                  <Text style={[styles.categoryLabel, active && styles.categoryLabelActive]}>{cat.label}</Text>
                  <Text style={styles.categoryDesc}>{cat.desc}</Text>
                </TouchableOpacity>
              );
            })}
          </View>

          {/* 2. Target Job Role */}
          <Text style={styles.sectionTitle}>2. Target Job Role</Text>
          <ScrollView horizontal showsHorizontalScrollIndicator={false} style={styles.horizontalScroll}>
            {TARGET_ROLES.map((role) => {
              const active = selectedRole === role;
              return (
                <TouchableOpacity
                  key={role}
                  style={[styles.chip, active && styles.chipActive]}
                  onPress={() => setSelectedRole(role)}
                >
                  <Text style={[styles.chipText, active && styles.chipTextActive]}>{role}</Text>
                </TouchableOpacity>
              );
            })}
          </ScrollView>

          {/* 3. Subject Selection (Only for Technical) */}
          {selectedCategory === 'Technical' && (
            <>
              <Text style={styles.sectionTitle}>3. Core Subject or Language</Text>
              <View style={styles.subjectsGrid}>
                {TECHNICAL_SUBJECTS.map((sub) => {
                  const active = selectedSubject === sub;
                  return (
                    <TouchableOpacity
                      key={sub}
                      style={[styles.subjectChip, active && styles.subjectChipActive]}
                      onPress={() => setSelectedSubject(sub)}
                    >
                      <Feather name="book-open" size={14} color={active ? '#FFFFFF' : Palette.textBody} style={{ marginRight: 6 }} />
                      <Text style={[styles.subjectChipText, active && styles.subjectChipTextActive]} numberOfLines={1}>
                        {sub}
                      </Text>
                    </TouchableOpacity>
                  );
                })}
              </View>
            </>
          )}

          {/* 4. Difficulty & Experience */}
          <View style={styles.twoColumnRow}>
            <View style={styles.columnHalf}>
              <Text style={styles.sectionTitle}>Difficulty</Text>
              <View style={styles.segmentedControl}>
                {DIFFICULTIES.map((diff) => {
                  const active = selectedDifficulty === diff;
                  return (
                    <TouchableOpacity
                      key={diff}
                      style={[styles.segmentBtn, active && styles.segmentBtnActive]}
                      onPress={() => setSelectedDifficulty(diff)}
                    >
                      <Text style={[styles.segmentText, active && styles.segmentTextActive]}>{diff}</Text>
                    </TouchableOpacity>
                  );
                })}
              </View>
            </View>

            <View style={styles.columnHalf}>
              <Text style={styles.sectionTitle}>Experience</Text>
              <View style={styles.segmentedControl}>
                {EXPERIENCE_LEVELS.map((exp) => {
                  const active = selectedExperience === exp;
                  return (
                    <TouchableOpacity
                      key={exp}
                      style={[styles.segmentBtn, active && styles.segmentBtnActive]}
                      onPress={() => setSelectedExperience(exp)}
                    >
                      <Text style={[styles.segmentText, active && styles.segmentTextActive]}>{exp}</Text>
                    </TouchableOpacity>
                  );
                })}
              </View>
            </View>
          </View>

          {/* 5. Questions Count & Mode */}
          <View style={styles.twoColumnRow}>
            <View style={styles.columnHalf}>
              <Text style={styles.sectionTitle}>Questions Count</Text>
              <View style={styles.segmentedControl}>
                {QUESTION_COUNTS.map((cnt) => {
                  const active = selectedQuestionCount === cnt;
                  return (
                    <TouchableOpacity
                      key={cnt}
                      style={[styles.segmentBtn, active && styles.segmentBtnActive]}
                      onPress={() => setSelectedQuestionCount(cnt)}
                    >
                      <Text style={[styles.segmentText, active && styles.segmentTextActive]}>{cnt} Qs</Text>
                    </TouchableOpacity>
                  );
                })}
              </View>
            </View>

            <View style={styles.columnHalf}>
              <Text style={styles.sectionTitle}>Interview Mode</Text>
              <View style={styles.segmentedControl}>
                {(['text', 'voice'] as const).map((m) => {
                  const active = selectedMode === m;
                  return (
                    <TouchableOpacity
                      key={m}
                      style={[styles.segmentBtn, active && styles.segmentBtnActive]}
                      onPress={() => setSelectedMode(m)}
                    >
                      <Feather
                        name={m === 'text' ? 'file-text' : 'mic'}
                        size={14}
                        color={active ? '#FFFFFF' : Palette.textBody}
                        style={{ marginRight: 4 }}
                      />
                      <Text style={[styles.segmentText, active && styles.segmentTextActive]}>
                        {m === 'text' ? 'Text' : 'Voice'}
                      </Text>
                    </TouchableOpacity>
                  );
                })}
              </View>
            </View>
          </View>

          {/* Start Button */}
          <TouchableOpacity
            style={[styles.startBtn, isSubmitting && styles.startBtnDisabled]}
            disabled={isSubmitting}
            onPress={handleStartInterview}
          >
            {isSubmitting ? (
              <ActivityIndicator color="#FFFFFF" />
            ) : (
              <>
                <Text style={styles.startBtnText}>Start AI Mock Interview</Text>
                <Feather name="arrow-right" size={20} color="#FFFFFF" style={{ marginLeft: 8 }} />
              </>
            )}
          </TouchableOpacity>
        </ScrollView>
      </SafeAreaView>
    );
  }

  // =============================================================
  // RENDER: LIVE INTERVIEW SCREEN
  // =============================================================
  if (currentView === 'interview') {
    const qNum = currentQuestion?.question_number || 1;
    const totalQ = activeSession?.total_questions || 3;
    const progress = qNum / totalQ;

    return (
      <SafeAreaView style={styles.safeArea}>
        <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
        <AppHeader
          showBack
          onBack={handleEndInterviewEarly}
          title={`Question ${qNum} of ${totalQ}`}
          subtitle={`${activeSession?.subject || 'Interview'} · ${activeSession?.difficulty || 'Intermediate'}`}
          rightAction={
            <View style={styles.timerBadge}>
              <Feather name="clock" size={14} color={Palette.textTitle} style={{ marginRight: 4 }} />
              <Text style={styles.timerText}>{formatTimer(elapsedSeconds)}</Text>
            </View>
          }
        />

        <ScrollView style={styles.content} contentContainerStyle={styles.scrollContent}>
          {/* Progress Indicator */}
          <View style={styles.progressContainer}>
            <ProgressBar progress={progress} color={Palette.aiPurple} />
          </View>

          {/* Question Card with Voice Converter */}
          <View style={styles.questionCard}>
            <View style={styles.questionHeader}>
              <View style={{ flexDirection: 'row', alignItems: 'center', flexWrap: 'wrap', gap: 6 }}>
                <View style={styles.topicBadge}>
                  <Text style={styles.topicBadgeText}>{currentQuestion?.topic || activeSession?.subject}</Text>
                </View>
                {currentQuestion?.difficulty && (
                  <View style={[styles.topicBadge, { backgroundColor: '#F1F5F9' }]}>
                    <Text style={[styles.topicBadgeText, { color: Palette.textSecondary }]}>{currentQuestion.difficulty}</Text>
                  </View>
                )}
                {currentQuestion?.generated_follow_up && (
                  <View style={styles.followUpBadge}>
                    <Text style={styles.followUpBadgeText}>Adaptive Follow-Up</Text>
                  </View>
                )}
              </View>

              {/* Live Voice Converter Indicator */}
              <View style={[styles.voiceIndicatorBadge, isSpeakingQuestion && styles.voiceIndicatorBadgeSpeaking]}>
                <View style={[styles.voiceIndicatorDot, isSpeakingQuestion && styles.voiceIndicatorDotSpeaking]} />
                <Text style={[styles.voiceIndicatorText, isSpeakingQuestion && styles.voiceIndicatorTextSpeaking]}>
                  {isSpeakingQuestion ? 'Interviewer Asking...' : 'Voice Ready'}
                </Text>
              </View>
            </View>

            <Text style={styles.questionText}>{currentQuestion?.question_text}</Text>

            {/* AI Voice Converter Interactive Section */}
            <View style={styles.voiceConverterBox}>
              <View style={styles.voiceMainControlsRow}>
                {/* Ask Aloud / Pause Button */}
                <TouchableOpacity
                  style={[styles.voiceAskBtn, isSpeakingQuestion && styles.voiceAskBtnSpeaking]}
                  onPress={() => playQuestionSpeech()}
                >
                  <Feather
                    name={isSpeakingQuestion ? 'pause' : 'volume-2'}
                    size={16}
                    color="#FFFFFF"
                    style={{ marginRight: 6 }}
                  />
                  <Text style={styles.voiceAskBtnText}>
                    {isSpeakingQuestion ? 'Pause Voice' : 'Ask Question Aloud'}
                  </Text>
                </TouchableOpacity>

                {/* Re-Ask Button */}
                <TouchableOpacity
                  style={styles.voiceReaskBtn}
                  onPress={() => playQuestionSpeech(currentQuestion?.question_text, currentQuestion?.question_number, true)}
                >
                  <Feather name="rotate-ccw" size={14} color={Palette.aiPurple} style={{ marginRight: 4 }} />
                  <Text style={styles.voiceReaskBtnText}>Re-Ask</Text>
                </TouchableOpacity>

                {/* Auto-Ask Toggle */}
                <TouchableOpacity
                  style={[styles.autoAskPill, autoAskQuestion && styles.autoAskPillActive]}
                  onPress={() => setAutoAskQuestion(!autoAskQuestion)}
                >
                  <Feather
                    name={autoAskQuestion ? 'check-circle' : 'circle'}
                    size={13}
                    color={autoAskQuestion ? '#FFFFFF' : Palette.textMuted}
                    style={{ marginRight: 4 }}
                  />
                  <Text style={[styles.autoAskPillText, autoAskQuestion && styles.autoAskPillTextActive]}>
                    Auto-Ask: {autoAskQuestion ? 'ON' : 'OFF'}
                  </Text>
                </TouchableOpacity>
              </View>

              {/* Voice Converter Preferences (Voice Persona & Speaking Rate) */}
              <View style={styles.voiceCustomizationRow}>
                <View style={styles.voiceSubGroup}>
                  <Text style={styles.voiceSubLabel}>Voice:</Text>
                  <View style={styles.voiceOptionGroup}>
                    {(['Aria (Clear Studio)', 'Guy (Executive Lead)', 'Jenny (Warm Natural)', 'Neerja (Indian English)'] as const).map((persona) => {
                      const active = selectedVoicePersona === persona;
                      const shortName = persona.split(' ')[0];
                      return (
                        <TouchableOpacity
                          key={persona}
                          style={[styles.voiceChip, active && styles.voiceChipActive]}
                          onPress={() => setSelectedVoicePersona(persona)}
                          accessibilityLabel={persona}
                        >
                          <Text style={[styles.voiceChipText, active && styles.voiceChipTextActive]}>
                            {shortName}
                          </Text>
                        </TouchableOpacity>
                      );
                    })}
                  </View>
                </View>

                <View style={styles.voiceSubGroup}>
                  <Text style={styles.voiceSubLabel}>Speed:</Text>
                  <View style={styles.voiceOptionGroup}>
                    {([0.85, 0.95, 1.15] as const).map((rate) => {
                      const active = speechRate === rate;
                      const label = rate === 0.85 ? '0.8x' : rate === 0.95 ? '1.0x' : '1.2x';
                      return (
                        <TouchableOpacity
                          key={rate}
                          style={[styles.voiceChip, active && styles.voiceChipActive]}
                          onPress={() => setSpeechRate(rate)}
                        >
                          <Text style={[styles.voiceChipText, active && styles.voiceChipTextActive]}>
                            {label}
                          </Text>
                        </TouchableOpacity>
                      );
                    })}
                  </View>
                </View>

                {/* Wikipedia Grounding & Citation */}
                {currentQuestion?.source_reference && (
                  <View style={styles.wikiGroundingBadge}>
                    <Feather name="book-open" size={12} color="#2563EB" style={{ marginRight: 4 }} />
                    <Text style={styles.wikiGroundingText} numberOfLines={1}>
                      Theory: {decodeURIComponent(currentQuestion.source_reference.replace('https://en.wikipedia.org/wiki/', '').replace(/_/g, ' '))}
                    </Text>
                  </View>
                )}
              </View>
            </View>
          </View>

          {/* Mode Switcher Banner */}
          <View style={styles.modeToggleRow}>
            <Text style={styles.answerSectionTitle}>Your Response</Text>
            <View style={styles.modePillContainer}>
              <TouchableOpacity
                style={[styles.modePill, selectedMode === 'text' && styles.modePillActive]}
                onPress={() => setSelectedMode('text')}
              >
                <Feather name="edit-3" size={13} color={selectedMode === 'text' ? '#FFFFFF' : Palette.textBody} />
                <Text style={[styles.modePillText, selectedMode === 'text' && styles.modePillTextActive]}>Text</Text>
              </TouchableOpacity>
              <TouchableOpacity
                style={[styles.modePill, selectedMode === 'voice' && styles.modePillActive]}
                onPress={() => setSelectedMode('voice')}
              >
                <Feather name="mic" size={13} color={selectedMode === 'voice' ? '#FFFFFF' : Palette.textBody} />
                <Text style={[styles.modePillText, selectedMode === 'voice' && styles.modePillTextActive]}>Voice</Text>
              </TouchableOpacity>
            </View>
          </View>

          {/* Voice Input Section */}
          {selectedMode === 'voice' && (
            <View style={styles.voiceSection}>
              <TouchableOpacity
                style={[styles.micBigBtn, isRecording && styles.micBigBtnRecording]}
                onPress={toggleRecording}
              >
                <Feather name={isRecording ? 'square' : 'mic'} size={28} color="#FFFFFF" />
              </TouchableOpacity>
              <Text style={styles.voiceStatusText}>
                {isRecording ? 'Listening... Speak clearly into your microphone' : 'Tap microphone to speak your response'}
              </Text>
            </View>
          )}

          {/* Editable Transcript / Text Input Area */}
          <View style={styles.inputCard}>
            <TextInput
              style={styles.textInput}
              multiline
              numberOfLines={8}
              placeholder={
                selectedMode === 'voice'
                  ? 'Your speech transcript appears here. You can review, expand, or edit it freely before submitting.'
                  : 'Type your comprehensive answer here (supports full, in-depth responses up to 1,000+ words with code snippets, trade-offs, and architecture)...'
              }
              placeholderTextColor={Palette.textMuted}
              value={answerText}
              onChangeText={setAnswerText}
              textAlignVertical="top"
            />
            <View style={styles.wordCountRow}>
              {(() => {
                const words = answerText.trim() ? answerText.trim().split(/\s+/).length : 0;
                let badge = '';
                if (words >= 500) badge = ' • Comprehensive Master Answer';
                else if (words >= 200) badge = ' • In-Depth Explanation';
                else if (words >= 75) badge = ' • Detailed Response';
                return (
                  <Text style={styles.wordCountText}>
                    {words} words{badge}
                  </Text>
                );
              })()}
              {answerText.trim().length > 0 && (
                <TouchableOpacity
                  onPress={() => {
                    setAnswerText('');
                    baseAnswerRef.current = '';
                    answerTextRef.current = '';
                  }}
                  style={styles.clearTextBtn}
                >
                  <Feather name="trash-2" size={12} color={Palette.textMuted} style={{ marginRight: 4 }} />
                  <Text style={styles.clearTextBtnText}>Clear Answer</Text>
                </TouchableOpacity>
              )}
            </View>
          </View>

          {/* Submit Button */}
          <TouchableOpacity
            style={[styles.submitBtn, (isSubmitting || !answerText.trim()) && styles.startBtnDisabled]}
            disabled={isSubmitting || !answerText.trim()}
            onPress={handleSubmitAnswer}
          >
            {isSubmitting ? (
              <ActivityIndicator color="#FFFFFF" />
            ) : (
              <>
                <Text style={styles.submitBtnText}>Submit Answer for AI Evaluation</Text>
                <Feather name="check-circle" size={18} color="#FFFFFF" style={{ marginLeft: 8 }} />
              </>
            )}
          </TouchableOpacity>

          <TouchableOpacity style={styles.endEarlyBtn} onPress={handleEndInterviewEarly}>
            <Text style={styles.endEarlyBtnText}>End Interview Early</Text>
          </TouchableOpacity>
        </ScrollView>
      </SafeAreaView>
    );
  }

  // =============================================================
  // RENDER: ANSWER FEEDBACK SCREEN
  // =============================================================
  if (currentView === 'feedback' && lastEvaluation) {
    const isComplete = lastEvaluation.is_interview_complete;

    return (
      <SafeAreaView style={styles.safeArea}>
        <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
        <AppHeader title="Evaluation Feedback" subtitle="AI Multi-Criteria Scoring" />

        <ScrollView style={styles.content} contentContainerStyle={styles.scrollContent}>
          {/* Score Header Card */}
          <View style={styles.feedbackScoreCard}>
            <Text style={styles.feedbackScoreLabel}>Answer Score</Text>
            <Text style={styles.feedbackScoreBig}>{Math.round(lastEvaluation.overall_score)}%</Text>
            <Text style={styles.feedbackScoreSummary}>{lastEvaluation.feedback}</Text>

            {/* Criteria Grid */}
            <View style={styles.criteriaGrid}>
              <View style={styles.criteriaItem}>
                <Text style={styles.criteriaValue}>{lastEvaluation.technical_score}/10</Text>
                <Text style={styles.criteriaName}>Technical</Text>
              </View>
              <View style={styles.criteriaItem}>
                <Text style={styles.criteriaValue}>{lastEvaluation.completeness_score}/10</Text>
                <Text style={styles.criteriaName}>Completeness</Text>
              </View>
              <View style={styles.criteriaItem}>
                <Text style={styles.criteriaValue}>{lastEvaluation.clarity_score}/10</Text>
                <Text style={styles.criteriaName}>Clarity</Text>
              </View>
              <View style={styles.criteriaItem}>
                <Text style={styles.criteriaValue}>{lastEvaluation.communication_score}/10</Text>
                <Text style={styles.criteriaName}>Communication</Text>
              </View>
            </View>
          </View>

          {/* Strengths */}
          {lastEvaluation.strengths && lastEvaluation.strengths.length > 0 && (
            <View style={styles.cardSection}>
              <Text style={styles.sectionSubtitle}>
                <Feather name="check" size={16} color={Palette.success} /> Key Strengths
              </Text>
              {lastEvaluation.strengths.map((str: string, i: number) => (
                <View key={i} style={styles.bulletRow}>
                  <Feather name="check-circle" size={15} color={Palette.success} style={{ marginTop: 2, marginRight: 8 }} />
                  <Text style={styles.bulletText}>{str}</Text>
                </View>
              ))}
            </View>
          )}

          {/* Improvement Areas */}
          {lastEvaluation.improvement_areas && lastEvaluation.improvement_areas.length > 0 && (
            <View style={styles.cardSection}>
              <Text style={styles.sectionSubtitle}>
                <Feather name="trending-up" size={16} color={Palette.amber} /> Actionable Improvements
              </Text>
              {lastEvaluation.improvement_areas.map((imp: string, i: number) => (
                <View key={i} style={styles.bulletRow}>
                  <Feather name="arrow-up-right" size={15} color={Palette.amber} style={{ marginTop: 2, marginRight: 8 }} />
                  <Text style={styles.bulletText}>{imp}</Text>
                </View>
              ))}
            </View>
          )}

          {/* Model Answer Card */}
          {lastEvaluation.model_answer && (
            <View style={styles.modelAnswerCard}>
              <Text style={styles.modelAnswerHeader}>
                <Feather name="book" size={15} color={Palette.primary} /> Expert Model Answer
              </Text>
              <Text style={styles.modelAnswerText}>{lastEvaluation.model_answer}</Text>
            </View>
          )}

          {/* Action Button */}
          <TouchableOpacity
            style={styles.continueBtn}
            disabled={isSubmitting}
            onPress={handleProceedFromFeedback}
          >
            {isSubmitting ? (
              <ActivityIndicator color="#FFFFFF" />
            ) : (
              <>
                <Text style={styles.continueBtnText}>
                  {isComplete ? 'View Comprehensive Interview Report' : 'Proceed to Next Question'}
                </Text>
                <Feather name="arrow-right" size={18} color="#FFFFFF" style={{ marginLeft: 8 }} />
              </>
            )}
          </TouchableOpacity>
        </ScrollView>
      </SafeAreaView>
    );
  }

  // =============================================================
  // RENDER: FINAL REPORT SCREEN
  // =============================================================
  if (currentView === 'report' && finalReport) {
    return (
      <SafeAreaView style={styles.safeArea}>
        <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
        <AppHeader
          showBack
          onBack={() => setCurrentView('setup')}
          title="Interview Performance Report"
          subtitle="Final Evaluation & Placement Readiness"
        />

        <ScrollView style={styles.content} contentContainerStyle={styles.scrollContent}>
          {/* Main Score Hero */}
          <View style={styles.reportScoreCard}>
            <View style={styles.scoreCircle}>
              <Text style={styles.scoreCircleText}>{Math.round(finalReport.overall_score)}%</Text>
              <Text style={styles.scoreCircleLabel}>Overall</Text>
            </View>
            <Text style={styles.reportFeedbackText}>{finalReport.final_feedback}</Text>
          </View>

          {/* Summary Sections */}
          <View style={styles.cardSection}>
            <Text style={styles.sectionSubtitle}>
              <Feather name="cpu" size={16} color={Palette.primary} /> Technical Performance
            </Text>
            <Text style={styles.bodyText}>{finalReport.technical_summary}</Text>
          </View>

          <View style={styles.cardSection}>
            <Text style={styles.sectionSubtitle}>
              <Feather name="message-square" size={16} color={Palette.aiPurple} /> Communication Skills
            </Text>
            <Text style={styles.bodyText}>{finalReport.communication_summary}</Text>
          </View>

          {/* Recommended Topics */}
          {finalReport.recommended_topics && finalReport.recommended_topics.length > 0 && (
            <View style={styles.cardSection}>
              <Text style={styles.sectionSubtitle}>
                <Feather name="target" size={16} color={Palette.danger} /> Recommended Practice Topics
              </Text>
              <View style={styles.recommendedTopicsWrap}>
                {finalReport.recommended_topics.map((top: string, i: number) => (
                  <View key={i} style={styles.recommendedChip}>
                    <Feather name="bookmark" size={12} color={Palette.primary} style={{ marginRight: 6 }} />
                    <Text style={styles.recommendedChipText}>{top}</Text>
                  </View>
                ))}
              </View>
            </View>
          )}

          {/* Question Breakdown Review */}
          {finalReport.questions_breakdown && finalReport.questions_breakdown.length > 0 && (
            <View style={styles.cardSection}>
              <Text style={styles.sectionSubtitle}>
                <Feather name="list" size={16} color={Palette.textTitle} /> Answer Review Breakdown
              </Text>
              {finalReport.questions_breakdown.map((q: any, i: number) => (
                <View key={i} style={styles.breakdownItem}>
                  <Text style={styles.breakdownQNum}>Q{q.question_number}: {q.question_text}</Text>
                  <Text style={styles.breakdownAnsText}>Your Answer: {q.student_answer || 'No answer submitted'}</Text>
                  {q.feedback && <Text style={styles.breakdownFeedback}>Feedback: {q.feedback}</Text>}
                </View>
              ))}
            </View>
          )}

          {/* Action Buttons */}
          <TouchableOpacity style={styles.startBtn} onPress={() => setCurrentView('setup')}>
            <Text style={styles.startBtnText}>Start Another Mock Interview</Text>
          </TouchableOpacity>
        </ScrollView>
      </SafeAreaView>
    );
  }

  // =============================================================
  // RENDER: HISTORY SCREEN
  // =============================================================
  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader
        showBack
        onBack={() => setCurrentView('setup')}
        title="My Interview History"
        subtitle="Review past AI interviews & performance reports"
      />

      <ScrollView style={styles.content} contentContainerStyle={styles.scrollContent}>
        {isLoadingHistory ? (
          <ActivityIndicator size="large" color={Palette.aiPurple} style={{ marginTop: 40 }} />
        ) : historyItems.length === 0 ? (
          <View style={styles.emptyContainer}>
            <Feather name="inbox" size={48} color={Palette.textMuted} />
            <Text style={styles.emptyTitle}>No Interview History Yet</Text>
            <Text style={styles.emptyDesc}>Take your first AI Mock Interview to start tracking your progress.</Text>
            <TouchableOpacity style={styles.startBtn} onPress={() => setCurrentView('setup')}>
              <Text style={styles.startBtnText}>Start New Interview</Text>
            </TouchableOpacity>
          </View>
        ) : (
          historyItems.map((item) => (
            <TouchableOpacity
              key={item.id}
              style={styles.historyCard}
              onPress={() => viewPastReport(item.id)}
            >
              <View style={styles.historyCardTop}>
                <View>
                  <Text style={styles.historyCategory}>{item.interview_category} Interview</Text>
                  <Text style={styles.historySubject}>{item.subject} · {item.difficulty}</Text>
                </View>
                <View style={styles.historyScoreBadge}>
                  <Text style={styles.historyScoreText}>{Math.round(item.total_score)}%</Text>
                </View>
              </View>

              <View style={styles.historyCardBottom}>
                <Text style={styles.historyDate}>
                  {item.started_at ? new Date(item.started_at).toLocaleDateString() : 'Recent'} · {item.questions_answered}/{item.total_questions} Questions
                </Text>
                <View style={styles.viewReportRow}>
                  <Text style={styles.viewReportText}>View Report</Text>
                  <Feather name="chevron-right" size={16} color={Palette.primary} />
                </View>
              </View>
            </TouchableOpacity>
          ))
        )}
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: Palette.background,
  },
  content: {
    flex: 1,
  },
  scrollContent: {
    padding: 16,
    paddingBottom: 40,
  },
  headerHistoryBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: Palette.aiPurpleLight,
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: Radii.full,
    borderWidth: 1,
    borderColor: Palette.aiPurpleBorder,
  },
  headerHistoryText: {
    fontSize: 13,
    fontWeight: '600',
    color: Palette.aiPurple,
    marginLeft: 6,
  },
  heroBanner: {
    backgroundColor: Palette.aiPurple,
    borderRadius: Radii.lg,
    padding: 18,
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 20,
    ...Shadows.sm,
  },
  heroIconBadge: {
    width: 48,
    height: 48,
    borderRadius: 24,
    backgroundColor: 'rgba(255, 255, 255, 0.2)',
    justifyContent: 'center',
    alignItems: 'center',
    marginRight: 14,
  },
  heroTextContainer: {
    flex: 1,
  },
  heroTitle: {
    fontSize: 17,
    fontWeight: '700',
    color: '#FFFFFF',
    marginBottom: 4,
  },
  heroSubtitle: {
    fontSize: 12,
    color: 'rgba(255, 255, 255, 0.9)',
    lineHeight: 18,
  },
  sectionTitle: {
    fontSize: 14,
    fontWeight: '700',
    color: Palette.textTitle,
    marginBottom: 10,
    marginTop: 6,
    textTransform: 'uppercase',
    letterSpacing: 0.5,
  },
  categoriesRow: {
    flexDirection: 'row',
    gap: 10,
    marginBottom: 16,
  },
  categoryCard: {
    flex: 1,
    backgroundColor: Palette.card,
    borderRadius: Radii.md,
    padding: 12,
    borderWidth: 1.5,
    borderColor: Palette.border,
    alignItems: 'center',
    ...Shadows.sm,
  },
  categoryCardActive: {
    borderColor: Palette.aiPurple,
    backgroundColor: Palette.aiPurpleLight,
  },
  categoryIconCircle: {
    width: 40,
    height: 40,
    borderRadius: 20,
    backgroundColor: Palette.aiPurpleLight,
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 8,
  },
  categoryIconCircleActive: {
    backgroundColor: Palette.aiPurple,
  },
  categoryLabel: {
    fontSize: 13,
    fontWeight: '700',
    color: Palette.textTitle,
    marginBottom: 4,
    textAlign: 'center',
  },
  categoryLabelActive: {
    color: Palette.aiPurple,
  },
  categoryDesc: {
    fontSize: 10,
    color: Palette.textMuted,
    textAlign: 'center',
    lineHeight: 14,
  },
  horizontalScroll: {
    flexDirection: 'row',
    marginBottom: 16,
  },
  chip: {
    backgroundColor: Palette.card,
    paddingHorizontal: 14,
    paddingVertical: 8,
    borderRadius: Radii.full,
    borderWidth: 1,
    borderColor: Palette.border,
    marginRight: 8,
  },
  chipActive: {
    backgroundColor: Palette.aiPurple,
    borderColor: Palette.aiPurple,
  },
  chipText: {
    fontSize: 13,
    fontWeight: '600',
    color: Palette.textBody,
  },
  chipTextActive: {
    color: '#FFFFFF',
  },
  subjectsGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 8,
    marginBottom: 16,
  },
  subjectChip: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: Palette.card,
    paddingHorizontal: 12,
    paddingVertical: 7,
    borderRadius: Radii.sm,
    borderWidth: 1,
    borderColor: Palette.border,
  },
  subjectChipActive: {
    backgroundColor: Palette.aiPurple,
    borderColor: Palette.aiPurple,
  },
  subjectChipText: {
    fontSize: 12,
    fontWeight: '600',
    color: Palette.textBody,
  },
  subjectChipTextActive: {
    color: '#FFFFFF',
  },
  twoColumnRow: {
    flexDirection: 'row',
    gap: 12,
    marginBottom: 16,
  },
  columnHalf: {
    flex: 1,
  },
  segmentedControl: {
    flexDirection: 'row',
    backgroundColor: Palette.card,
    borderRadius: Radii.md,
    borderWidth: 1,
    borderColor: Palette.border,
    padding: 3,
  },
  segmentBtn: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 7,
    borderRadius: Radii.sm,
  },
  segmentBtnActive: {
    backgroundColor: Palette.aiPurple,
  },
  segmentText: {
    fontSize: 12,
    fontWeight: '600',
    color: Palette.textBody,
  },
  segmentTextActive: {
    color: '#FFFFFF',
  },
  startBtn: {
    backgroundColor: Palette.aiPurple,
    borderRadius: Radii.md,
    paddingVertical: 14,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    marginTop: 10,
    ...Shadows.md,
  },
  startBtnDisabled: {
    opacity: 0.6,
  },
  startBtnText: {
    color: '#FFFFFF',
    fontSize: 15,
    fontWeight: '700',
  },
  // Interview Screen
  timerBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: Palette.backgroundSecondary,
    paddingHorizontal: 10,
    paddingVertical: 5,
    borderRadius: Radii.full,
    borderWidth: 1,
    borderColor: Palette.border,
  },
  timerText: {
    fontSize: 13,
    fontWeight: '700',
    color: Palette.textTitle,
  },
  progressContainer: {
    marginBottom: 16,
  },
  questionCard: {
    backgroundColor: Palette.card,
    borderRadius: Radii.lg,
    padding: 18,
    borderWidth: 1,
    borderColor: Palette.border,
    marginBottom: 16,
    ...Shadows.sm,
  },
  questionHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 12,
    gap: 8,
  },
  topicBadge: {
    backgroundColor: Palette.aiPurpleLight,
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: Radii.full,
  },
  topicBadgeText: {
    fontSize: 11,
    fontWeight: '700',
    color: Palette.aiPurple,
  },
  followUpBadge: {
    backgroundColor: Palette.amberLight,
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: Radii.full,
  },
  followUpBadgeText: {
    fontSize: 11,
    fontWeight: '700',
    color: Palette.amber,
  },
  questionText: {
    fontSize: 16,
    fontWeight: '600',
    color: Palette.textTitle,
    lineHeight: 24,
    marginBottom: 14,
  },
  ttsButton: {
    flexDirection: 'row',
    alignItems: 'center',
    alignSelf: 'flex-start',
    backgroundColor: Palette.aiPurpleLight,
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: Radii.full,
    borderWidth: 1,
    borderColor: Palette.aiPurpleBorder,
  },
  ttsButtonText: {
    fontSize: 12,
    fontWeight: '600',
    color: Palette.aiPurple,
  },
  voiceIndicatorBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#F8FAFC',
    borderWidth: 1,
    borderColor: '#E2E8F0',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: Radii.full,
  },
  voiceIndicatorBadgeSpeaking: {
    backgroundColor: '#F3E8FF',
    borderColor: Palette.aiPurpleBorder,
  },
  voiceIndicatorDot: {
    width: 8,
    height: 8,
    borderRadius: 4,
    backgroundColor: '#94A3B8',
    marginRight: 6,
  },
  voiceIndicatorDotSpeaking: {
    backgroundColor: Palette.aiPurple,
  },
  voiceIndicatorText: {
    fontSize: 11,
    fontWeight: '700',
    color: Palette.textSecondary,
  },
  voiceIndicatorTextSpeaking: {
    color: Palette.aiPurple,
  },
  voiceConverterBox: {
    marginTop: 14,
    paddingTop: 12,
    borderTopWidth: 1,
    borderTopColor: '#F1F5F9',
    gap: 10,
  },
  voiceMainControlsRow: {
    flexDirection: 'row',
    alignItems: 'center',
    flexWrap: 'wrap',
    gap: 8,
  },
  voiceAskBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: Palette.aiPurple,
    paddingHorizontal: 14,
    paddingVertical: 8,
    borderRadius: Radii.full,
    ...Shadows.sm,
  },
  voiceAskBtnSpeaking: {
    backgroundColor: '#D946EF',
  },
  voiceAskBtnText: {
    fontSize: 13,
    fontWeight: '700',
    color: '#FFFFFF',
  },
  voiceReaskBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: Palette.aiPurpleLight,
    borderWidth: 1,
    borderColor: Palette.aiPurpleBorder,
    paddingHorizontal: 12,
    paddingVertical: 7,
    borderRadius: Radii.full,
  },
  voiceReaskBtnText: {
    fontSize: 12,
    fontWeight: '700',
    color: Palette.aiPurple,
  },
  autoAskPill: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#F1F5F9',
    borderWidth: 1,
    borderColor: '#E2E8F0',
    paddingHorizontal: 10,
    paddingVertical: 7,
    borderRadius: Radii.full,
  },
  autoAskPillActive: {
    backgroundColor: '#10B981',
    borderColor: '#059669',
  },
  autoAskPillText: {
    fontSize: 11,
    fontWeight: '700',
    color: Palette.textSecondary,
  },
  autoAskPillTextActive: {
    color: '#FFFFFF',
  },
  voiceCustomizationRow: {
    flexDirection: 'row',
    alignItems: 'center',
    flexWrap: 'wrap',
    gap: 12,
  },
  voiceSubGroup: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
  },
  voiceSubLabel: {
    fontSize: 11,
    fontWeight: '700',
    color: Palette.textMuted,
  },
  voiceOptionGroup: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
  },
  voiceChip: {
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 6,
    backgroundColor: '#F8FAFC',
    borderWidth: 1,
    borderColor: '#E2E8F0',
  },
  voiceChipActive: {
    backgroundColor: Palette.aiPurple,
    borderColor: Palette.aiPurple,
  },
  voiceChipText: {
    fontSize: 11,
    fontWeight: '600',
    color: Palette.textSecondary,
  },
  voiceChipTextActive: {
    color: '#FFFFFF',
  },
  wikiGroundingBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#EFF6FF',
    borderWidth: 1,
    borderColor: '#BFDBFE',
    borderRadius: Radii.full,
    paddingHorizontal: 10,
    paddingVertical: 5,
  },
  wikiGroundingText: {
    fontSize: 12,
    color: '#1E40AF',
    fontWeight: '600',
    maxWidth: 240,
  },
  modeToggleRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 10,
  },
  answerSectionTitle: {
    fontSize: 14,
    fontWeight: '700',
    color: Palette.textTitle,
  },
  modePillContainer: {
    flexDirection: 'row',
    backgroundColor: Palette.card,
    borderRadius: Radii.full,
    borderWidth: 1,
    borderColor: Palette.border,
    padding: 2,
  },
  modePill: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: Radii.full,
  },
  modePillActive: {
    backgroundColor: Palette.aiPurple,
  },
  modePillText: {
    fontSize: 11,
    fontWeight: '600',
    color: Palette.textBody,
    marginLeft: 4,
  },
  modePillTextActive: {
    color: '#FFFFFF',
  },
  voiceSection: {
    backgroundColor: Palette.card,
    borderRadius: Radii.md,
    padding: 16,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: Palette.border,
    marginBottom: 12,
  },
  micBigBtn: {
    width: 60,
    height: 60,
    borderRadius: 30,
    backgroundColor: Palette.aiPurple,
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 8,
    ...Shadows.md,
  },
  micBigBtnRecording: {
    backgroundColor: Palette.danger,
  },
  voiceStatusText: {
    fontSize: 12,
    fontWeight: '500',
    color: Palette.textMuted,
    textAlign: 'center',
  },
  inputCard: {
    backgroundColor: Palette.card,
    borderRadius: Radii.md,
    borderWidth: 1,
    borderColor: Palette.border,
    padding: 12,
    marginBottom: 16,
  },
  textInput: {
    fontSize: 14,
    color: Palette.textTitle,
    lineHeight: 22,
    minHeight: 180,
    maxHeight: 450,
  },
  wordCountRow: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginTop: 6,
  },
  wordCountText: {
    fontSize: 11,
    color: Palette.textMuted,
  },
  clearTextBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingHorizontal: 8,
    paddingVertical: 3,
    backgroundColor: '#F1F5F9',
    borderRadius: 6,
  },
  clearTextBtnText: {
    fontSize: 11,
    color: Palette.textSecondary,
    fontWeight: '600',
  },
  submitBtn: {
    backgroundColor: Palette.aiPurple,
    borderRadius: Radii.md,
    paddingVertical: 14,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: 12,
    ...Shadows.md,
  },
  submitBtnText: {
    color: '#FFFFFF',
    fontSize: 15,
    fontWeight: '700',
  },
  endEarlyBtn: {
    alignItems: 'center',
    paddingVertical: 8,
  },
  endEarlyBtnText: {
    fontSize: 13,
    color: Palette.textMuted,
    fontWeight: '600',
  },
  // Feedback Screen
  feedbackScoreCard: {
    backgroundColor: Palette.card,
    borderRadius: Radii.lg,
    padding: 20,
    borderWidth: 1,
    borderColor: Palette.border,
    alignItems: 'center',
    marginBottom: 16,
    ...Shadows.sm,
  },
  feedbackScoreLabel: {
    fontSize: 12,
    fontWeight: '700',
    color: Palette.textMuted,
    textTransform: 'uppercase',
  },
  feedbackScoreBig: {
    fontSize: 44,
    fontWeight: '800',
    color: Palette.aiPurple,
    marginVertical: 4,
  },
  feedbackScoreSummary: {
    fontSize: 14,
    color: Palette.textBody,
    textAlign: 'center',
    lineHeight: 20,
    marginBottom: 16,
  },
  criteriaGrid: {
    flexDirection: 'row',
    width: '100%',
    borderTopWidth: 1,
    borderColor: Palette.border,
    paddingTop: 12,
  },
  criteriaItem: {
    flex: 1,
    alignItems: 'center',
  },
  criteriaValue: {
    fontSize: 15,
    fontWeight: '700',
    color: Palette.textTitle,
  },
  criteriaName: {
    fontSize: 10,
    color: Palette.textMuted,
    marginTop: 2,
  },
  cardSection: {
    backgroundColor: Palette.card,
    borderRadius: Radii.md,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.border,
    marginBottom: 14,
  },
  sectionSubtitle: {
    fontSize: 14,
    fontWeight: '700',
    color: Palette.textTitle,
    marginBottom: 10,
  },
  bodyText: {
    fontSize: 13,
    color: Palette.textBody,
    lineHeight: 20,
  },
  bulletRow: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    marginBottom: 6,
  },
  bulletText: {
    flex: 1,
    fontSize: 13,
    color: Palette.textBody,
    lineHeight: 19,
  },
  modelAnswerCard: {
    backgroundColor: Palette.primaryLight,
    borderRadius: Radii.md,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.primaryBorder,
    marginBottom: 16,
  },
  modelAnswerHeader: {
    fontSize: 13,
    fontWeight: '700',
    color: Palette.primary,
    marginBottom: 6,
  },
  modelAnswerText: {
    fontSize: 13,
    color: Palette.textBody,
    lineHeight: 20,
  },
  continueBtn: {
    backgroundColor: Palette.aiPurple,
    borderRadius: Radii.md,
    paddingVertical: 14,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: 20,
  },
  continueBtnText: {
    color: '#FFFFFF',
    fontSize: 15,
    fontWeight: '700',
  },
  // Report Screen
  reportScoreCard: {
    backgroundColor: Palette.card,
    borderRadius: Radii.lg,
    padding: 20,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: Palette.border,
    marginBottom: 16,
  },
  scoreCircle: {
    width: 110,
    height: 110,
    borderRadius: 55,
    backgroundColor: Palette.aiPurpleLight,
    borderWidth: 4,
    borderColor: Palette.aiPurple,
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 12,
  },
  scoreCircleText: {
    fontSize: 32,
    fontWeight: '800',
    color: Palette.aiPurple,
  },
  scoreCircleLabel: {
    fontSize: 10,
    fontWeight: '700',
    color: Palette.textMuted,
    textTransform: 'uppercase',
  },
  reportFeedbackText: {
    fontSize: 14,
    fontWeight: '500',
    color: Palette.textBody,
    textAlign: 'center',
    lineHeight: 21,
  },
  recommendedTopicsWrap: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 8,
  },
  recommendedChip: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: Palette.primaryLight,
    paddingHorizontal: 10,
    paddingVertical: 6,
    borderRadius: Radii.sm,
  },
  recommendedChipText: {
    fontSize: 12,
    fontWeight: '600',
    color: Palette.primary,
  },
  breakdownItem: {
    paddingVertical: 10,
    borderBottomWidth: 1,
    borderColor: Palette.border,
  },
  breakdownQNum: {
    fontSize: 13,
    fontWeight: '700',
    color: Palette.textTitle,
    marginBottom: 4,
  },
  breakdownAnsText: {
    fontSize: 12,
    color: Palette.textBody,
    marginBottom: 3,
  },
  breakdownFeedback: {
    fontSize: 11,
    color: Palette.aiPurple,
    fontStyle: 'italic',
  },
  // History Screen
  historyCard: {
    backgroundColor: Palette.card,
    borderRadius: Radii.md,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.border,
    marginBottom: 12,
    ...Shadows.sm,
  },
  historyCardTop: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 10,
  },
  historyCategory: {
    fontSize: 15,
    fontWeight: '700',
    color: Palette.textTitle,
  },
  historySubject: {
    fontSize: 12,
    color: Palette.textMuted,
    marginTop: 2,
  },
  historyScoreBadge: {
    backgroundColor: Palette.aiPurpleLight,
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: Radii.full,
  },
  historyScoreText: {
    fontSize: 14,
    fontWeight: '800',
    color: Palette.aiPurple,
  },
  historyCardBottom: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    borderTopWidth: 1,
    borderColor: Palette.border,
    paddingTop: 10,
  },
  historyDate: {
    fontSize: 11,
    color: Palette.textMuted,
  },
  viewReportRow: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  viewReportText: {
    fontSize: 12,
    fontWeight: '600',
    color: Palette.primary,
    marginRight: 4,
  },
  emptyContainer: {
    alignItems: 'center',
    paddingVertical: 60,
  },
  emptyTitle: {
    fontSize: 17,
    fontWeight: '700',
    color: Palette.textTitle,
    marginTop: 16,
    marginBottom: 6,
  },
  emptyDesc: {
    fontSize: 13,
    color: Palette.textMuted,
    textAlign: 'center',
    maxWidth: 280,
    marginBottom: 20,
    lineHeight: 18,
  },
});
