import React, { useCallback, useEffect, useRef, useState } from 'react';
import {
  ActivityIndicator,
  Alert,
  Modal,
  Platform,
  ScrollView,
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  View,
} from 'react-native';
import { Feather } from '@expo/vector-icons';
import { Palette, Radii, Shadows } from '../../constants/theme';
import { ApiClient } from '../../services/api';

interface GoogleMeetRoomProps {
  session: any;
  currentQuestion: any;
  elapsedSeconds: number;
  isSpeakingQuestion: boolean;
  isRecording: boolean;
  answerText: string;
  isSubmitting: boolean;
  selectedVoicePersona: string;
  speechRate: number;
  autoAskQuestion: boolean;
  cameraPreference: boolean;
  inCallFeedback?: {
    qNum: number;
    score: number;
    verdict: string;
    cumulativeAccuracy?: number;
  } | null;
  onDismissInCallFeedback?: () => void;
  onToggleRecording: () => void;
  onPlayQuestionSpeech: (forceReplay?: boolean) => void;
  onSelectVoicePersona: (persona: string) => void;
  onSetSpeechRate: (rate: number) => void;
  onToggleAutoAsk: () => void;
  onChangeAnswerText: (text: string) => void;
  onSubmitAnswer: () => void;
  onEndInterview: () => void;
}

export const GoogleMeetRoom: React.FC<GoogleMeetRoomProps> = ({
  session,
  currentQuestion,
  elapsedSeconds,
  isSpeakingQuestion,
  isRecording,
  answerText,
  isSubmitting,
  selectedVoicePersona,
  speechRate,
  autoAskQuestion,
  cameraPreference,
  inCallFeedback,
  onDismissInCallFeedback,
  onToggleRecording,
  onPlayQuestionSpeech,
  onSelectVoicePersona,
  onSetSpeechRate,
  onToggleAutoAsk,
  onChangeAnswerText,
  onSubmitAnswer,
  onEndInterview,
}) => {
  // Media Devices & WebRTC Video State
  const [isCameraOn, setIsCameraOn] = useState<boolean>(cameraPreference);
  const [mediaStream, setMediaStream] = useState<any>(null);
  const [cameraError, setCameraError] = useState<string | null>(null);
  const [isRequestingMedia, setIsRequestingMedia] = useState<boolean>(false);
  const videoElementRef = useRef<any>(null);
  const mediaStreamRef = useRef<any>(null);

  // UI Panels State
  const [isCaptionsOn, setIsCaptionsOn] = useState<boolean>(true);
  const [isCodeWorkspaceOpen, setIsCodeWorkspaceOpen] = useState<boolean>(false);
  const [isTextAnswerOpen, setIsTextAnswerOpen] = useState<boolean>(false);
  const [isSettingsOpen, setIsSettingsOpen] = useState<boolean>(false);
  const [showEndConfirm, setShowEndConfirm] = useState<boolean>(false);

  // Coding Workspace State
  const [codeLanguage, setCodeLanguage] = useState<string>('python');
  const [codeSnippet, setCodeSnippet] = useState<string>(
    '# Write your solution or code explanation here\ndef solution():\n    pass\n\n# Call solution\nprint(solution())'
  );
  const [isRunningCode, setIsRunningCode] = useState<boolean>(false);
  const [codeOutput, setCodeOutput] = useState<string | null>(null);
  const [codeStatus, setCodeStatus] = useState<string | null>(null);

  // Animated Speaking Visualizer wave bar simulation
  const [waveHeights, setWaveHeights] = useState<number[]>([12, 18, 24, 16, 10]);

  // Guaranteed hardware camera and microphone shutdown
  const stopAllMediaTracks = useCallback(() => {
    if (mediaStreamRef.current) {
      try {
        const tracks = mediaStreamRef.current.getTracks();
        tracks.forEach((track: any) => {
          track.enabled = false;
          track.stop();
        });
      } catch (err) {
        console.warn('Error stopping media tracks:', err);
      }
      mediaStreamRef.current = null;
    }
    if (videoElementRef.current) {
      try {
        videoElementRef.current.srcObject = null;
      } catch (e) {}
    }
    setMediaStream(null);
  }, []);

  // Component Unmount Cleanup: Stop camera & mic hardware unconditionally
  useEffect(() => {
    return () => {
      stopAllMediaTracks();
    };
  }, [stopAllMediaTracks]);

  useEffect(() => {
    let animTimer: any = null;
    if (isSpeakingQuestion) {
      animTimer = setInterval(() => {
        setWaveHeights([
          Math.floor(Math.random() * 22) + 8,
          Math.floor(Math.random() * 28) + 12,
          Math.floor(Math.random() * 34) + 16,
          Math.floor(Math.random() * 26) + 10,
          Math.floor(Math.random() * 18) + 6,
        ]);
      }, 140);
    } else {
      setWaveHeights([8, 12, 14, 10, 6]);
    }
    return () => {
      if (animTimer) clearInterval(animTimer);
    };
  }, [isSpeakingQuestion]);

  // Request & Mount User Media (Webcam & Microphone)
  useEffect(() => {
    let mounted = true;

    const startMedia = async () => {
      if (Platform.OS !== 'web' || typeof navigator === 'undefined' || !navigator.mediaDevices?.getUserMedia) {
        return;
      }
      if (!isCameraOn) {
        // Audio only or camera disabled: ensure active tracks are stopped
        stopAllMediaTracks();
        return;
      }

      setIsRequestingMedia(true);
      setCameraError(null);

      try {
        const stream = await navigator.mediaDevices.getUserMedia({
          video: {
            width: { ideal: 1280 },
            height: { ideal: 720 },
            facingMode: 'user',
          },
          audio: true,
        });

        if (!mounted) {
          stream.getTracks().forEach((track) => track.stop());
          return;
        }

        mediaStreamRef.current = stream;
        setMediaStream(stream);
        setIsRequestingMedia(false);

        // Attach stream to video DOM element
        if (videoElementRef.current) {
          videoElementRef.current.srcObject = stream;
          videoElementRef.current.play().catch((err: any) => {
            console.warn('Video preview autoplay prevented:', err);
          });
        }
      } catch (err: any) {
        if (!mounted) return;
        setIsRequestingMedia(false);
        const errMsg =
          err.name === 'NotAllowedError' || err.name === 'PermissionDeniedError'
            ? 'Camera access permission was denied. Practicing in Audio-Only mode.'
            : err.name === 'NotFoundError' || err.name === 'DevicesNotFoundError'
            ? 'No hardware camera detected. Running in Audio-Only mode.'
            : `Camera unavailable: ${err.message || 'Media stream error'}`;
        setCameraError(errMsg);
        setIsCameraOn(false);
      }
    };

    startMedia();

    return () => {
      mounted = false;
      stopAllMediaTracks();
    };
  }, [isCameraOn, stopAllMediaTracks]);

  // Handle Video Element Re-attachment when view re-renders
  useEffect(() => {
    if (Platform.OS === 'web' && videoElementRef.current && mediaStream && isCameraOn) {
      if (videoElementRef.current.srcObject !== mediaStream) {
        videoElementRef.current.srcObject = mediaStream;
        videoElementRef.current.play().catch(() => {});
      }
    }
  }, [mediaStream, isCameraOn]);

  // Toggle Camera
  const toggleCamera = () => {
    if (isCameraOn) {
      if (mediaStreamRef.current) {
        try {
          mediaStreamRef.current.getVideoTracks().forEach((track: any) => {
            track.enabled = false;
            track.stop();
          });
        } catch (e) {}
      }
      setIsCameraOn(false);
    } else {
      setIsCameraOn(true);
    }
  };

  // Explicit End Call Handler: Guarantee camera & mic tracks are stopped immediately
  const handleEndCall = () => {
    stopAllMediaTracks();
    setShowEndConfirm(false);
    onEndInterview();
  };

  // Format Elapsed Timer
  const formatTimer = (totalSeconds: number) => {
    const mins = Math.floor(totalSeconds / 60);
    const secs = totalSeconds % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  // Sandboxed Code Execution
  const handleRunCode = async () => {
    if (!codeSnippet.trim()) return;
    setIsRunningCode(true);
    setCodeOutput(null);
    setCodeStatus(null);

    try {
      const res = await ApiClient.executeDsaCode(codeLanguage, codeSnippet);
      setIsRunningCode(false);
      if (res.success && res.data) {
        const out = res.data.stdout || res.data.stderr || res.data.error_message || 'Execution completed with no output.';
        setCodeOutput(out);
        setCodeStatus(res.data.status || 'PASSED');
      } else {
        setCodeOutput(res.message || 'Execution encountered an unexpected issue.');
        setCodeStatus('ERROR');
      }
    } catch (err: any) {
      setIsRunningCode(false);
      setCodeOutput(err.message || 'Sandbox runner unreachable.');
      setCodeStatus('NETWORK_ERROR');
    }
  };

  // Insert code into student answer
  const handleAttachCodeToAnswer = () => {
    const codeBlock = `\n\`\`\`${codeLanguage}\n${codeSnippet}\n\`\`\`\n`;
    onChangeAnswerText(answerText ? `${answerText.trim()}${codeBlock}` : codeBlock.trim());
    setIsCodeWorkspaceOpen(false);
    setIsTextAnswerOpen(true);
  };

  const qNum = currentQuestion?.question_number || 1;
  const totalQ = session?.total_questions || 3;
  const subjectName = session?.subject || 'Interview';

  return (
    <View style={styles.meetContainer}>
      {/* 1. GOOGLE MEET TOP BAR */}
      <View style={styles.topBar}>
        <View style={styles.topBarLeft}>
          <View style={styles.brandingPill}>
            <View style={styles.meetLogoDot} />
            <Text style={styles.brandingText}>SkillExa Meet</Text>
          </View>
          <Text style={styles.sessionTitleText} numberOfLines={1}>
            {subjectName} · {session?.difficulty || 'Intermediate'}
          </Text>
        </View>

        <View style={styles.topBarCenter}>
          <View style={styles.timerBadge}>
            <View style={styles.recDot} />
            <Text style={styles.recText}>REC</Text>
            <Text style={styles.timerDivider}>|</Text>
            <Feather name="clock" size={13} color="#E8EAED" style={{ marginRight: 4 }} />
            <Text style={styles.timerText}>{formatTimer(elapsedSeconds)}</Text>
          </View>
        </View>

        <View style={styles.topBarRight}>
          <View style={styles.qualityBadge}>
            <Feather name="shield" size={12} color="#10B981" style={{ marginRight: 4 }} />
            <Text style={styles.qualityText}>HD 1080p · Encrypted</Text>
          </View>

          <View style={styles.questionCounterPill}>
            <Text style={styles.questionCounterText}>
              Q {qNum} / {totalQ}
            </Text>
          </View>
        </View>
      </View>

      {/* 2. CAMERA PERMISSION / STATUS BANNER */}
      {cameraError && (
        <View style={styles.cameraBanner}>
          <Feather name="info" size={14} color="#F59E0B" style={{ marginRight: 6 }} />
          <Text style={styles.cameraBannerText}>{cameraError}</Text>
          <TouchableOpacity
            style={styles.retryPermBtn}
            onPress={() => {
              setCameraError(null);
              setIsCameraOn(true);
            }}
          >
            <Text style={styles.retryPermBtnText}>Enable Camera</Text>
          </TouchableOpacity>
        </View>
      )}

      {/* 2.5 IN-CALL EVALUATION NOTIFICATION TOAST */}
      {inCallFeedback && (
        <View style={styles.inCallFeedbackBanner}>
          <View style={styles.inCallFeedbackLeft}>
            <View style={styles.inCallCheckCircle}>
              <Feather name="check-circle" size={16} color="#10B981" />
            </View>
            <View style={{ flex: 1 }}>
              <Text style={styles.inCallFeedbackTitle}>
                Question {inCallFeedback.qNum} of {totalQ} Evaluated: {Math.round(inCallFeedback.score)}% Accuracy ({inCallFeedback.verdict})
              </Text>
              <Text style={styles.inCallFeedbackSubtitle}>
                {inCallFeedback.cumulativeAccuracy !== undefined
                  ? `Performance Accuracy so far: ${Math.round(inCallFeedback.cumulativeAccuracy)}% · Now asking Question ${qNum} of ${totalQ}`
                  : `Now asking Question ${qNum} of ${totalQ}...`}
              </Text>
            </View>
          </View>
          {onDismissInCallFeedback && (
            <TouchableOpacity style={styles.inCallDismissBtn} onPress={onDismissInCallFeedback}>
              <Feather name="x" size={14} color="#9AA0A6" />
            </TouchableOpacity>
          )}
        </View>
      )}

      {/* 3. MAIN VIDEO STAGE (2-TIER RESPONSIVE GRID) */}
      <View style={styles.videoStage}>
        {/* TILE 1: AI INTERVIEWER */}
        <View style={[styles.videoTile, styles.aiTile]}>
          <View style={styles.tileHeader}>
            <View style={styles.roleBadge}>
              <Feather name="cpu" size={12} color="#A78BFA" style={{ marginRight: 4 }} />
              <Text style={styles.roleBadgeText}>AI Senior Interviewer (Host)</Text>
            </View>

            <TouchableOpacity
              style={styles.voiceConfigBtn}
              onPress={() => setIsSettingsOpen(true)}
              accessibilityLabel="Voice settings"
            >
              <Feather name="sliders" size={13} color="#9AA0A6" style={{ marginRight: 4 }} />
              <Text style={styles.voiceConfigText}>{selectedVoicePersona.split(' ')[0]}</Text>
            </TouchableOpacity>
          </View>

          {/* AI Avatar & Animated Waveform */}
          <View style={styles.aiCenterContainer}>
            <View style={[styles.aiAvatarHalo, isSpeakingQuestion && styles.aiAvatarHaloSpeaking]}>
              <View style={styles.aiAvatarCircle}>
                <Feather name="user" size={48} color="#FFFFFF" />
              </View>
            </View>

            {/* Speaking Wave Bars */}
            <View style={styles.soundWaveRow}>
              {waveHeights.map((h, i) => (
                <View
                  key={i}
                  style={[
                    styles.soundWaveBar,
                    { height: h },
                    isSpeakingQuestion && styles.soundWaveBarActive,
                  ]}
                />
              ))}
            </View>

            <View style={[styles.aiSpeakingBadge, isSpeakingQuestion && styles.aiSpeakingBadgeActive]}>
              <Feather
                name={isSpeakingQuestion ? 'volume-2' : 'mic'}
                size={12}
                color={isSpeakingQuestion ? '#10B981' : '#9AA0A6'}
                style={{ marginRight: 4 }}
              />
              <Text
                style={[styles.aiSpeakingBadgeText, isSpeakingQuestion && styles.aiSpeakingBadgeTextActive]}
              >
                {isSpeakingQuestion ? 'AI Speaking Question...' : 'AI Listening to You'}
              </Text>
            </View>
          </View>

          {/* AI Tile Footer */}
          <View style={styles.tileFooter}>
            <Text style={styles.tileName}>SkillExa AI Recruiter</Text>
            <View style={styles.aiSubStatus}>
              <View style={[styles.statusDot, isSpeakingQuestion ? styles.dotGreen : styles.dotBlue]} />
              <Text style={styles.statusDotText}>{isSpeakingQuestion ? 'Speaking' : 'Active'}</Text>
            </View>
          </View>
        </View>

        {/* TILE 2: STUDENT WEBCAM */}
        <View style={[styles.videoTile, styles.userTile]}>
          <View style={styles.tileHeader}>
            <View style={styles.roleBadge}>
              <Feather name="user" size={12} color="#60A5FA" style={{ marginRight: 4 }} />
              <Text style={styles.roleBadgeText}>You (Candidate)</Text>
            </View>

            <View style={styles.userStatusBadges}>
              <View style={[styles.devicePill, !isCameraOn && styles.devicePillOff]}>
                <Feather name={isCameraOn ? 'video' : 'video-off'} size={12} color={isCameraOn ? '#10B981' : '#EF4444'} />
              </View>
              <View style={[styles.devicePill, isRecording ? styles.devicePillActive : styles.devicePillMuted]}>
                <Feather name={isRecording ? 'mic' : 'mic-off'} size={12} color={isRecording ? '#10B981' : '#EF4444'} />
              </View>
            </View>
          </View>

          {/* Web Video Feed vs Camera-Off Avatar */}
          <View style={styles.userVideoWrapper}>
            {isCameraOn && Platform.OS === 'web' ? (
              <video
                ref={videoElementRef}
                autoPlay
                playsInline
                muted
                style={{
                  width: '100%',
                  height: '100%',
                  objectFit: 'cover',
                  transform: 'scaleX(-1)', // Mirror effect
                  borderRadius: 12,
                  backgroundColor: '#1E1F22',
                }}
              />
            ) : (
              <View style={styles.cameraOffPlaceholder}>
                <View style={styles.userAvatarCircle}>
                  <Text style={styles.userAvatarInitials}>
                    {session?.job_role ? session.job_role.slice(0, 2).toUpperCase() : 'ME'}
                  </Text>
                </View>
                <Text style={styles.cameraOffText}>
                  {isRequestingMedia ? 'Initializing Camera Feed...' : 'Camera is Turned Off (Audio Only)'}
                </Text>
                {!isCameraOn && (
                  <TouchableOpacity style={styles.enableCamSmallBtn} onPress={toggleCamera}>
                    <Feather name="video" size={12} color="#FFFFFF" style={{ marginRight: 4 }} />
                    <Text style={styles.enableCamSmallBtnText}>Turn On Camera</Text>
                  </TouchableOpacity>
                )}
              </View>
            )}

            {/* Speaking audio ripple overlay if recording */}
            {isRecording && (
              <View style={styles.candidateRecordingPulse}>
                <View style={styles.recPulseDot} />
                <Text style={styles.candidateRecordingPulseText}>Microphone Active · Listening</Text>
              </View>
            )}
          </View>

          {/* User Tile Footer */}
          <View style={styles.tileFooter}>
            <Text style={styles.tileName}>You (Candidate)</Text>
            <View style={styles.aiSubStatus}>
              <View style={[styles.statusDot, isRecording ? styles.dotGreen : styles.dotGray]} />
              <Text style={styles.statusDotText}>{isRecording ? 'Mic Live' : 'Mic Muted'}</Text>
            </View>
          </View>
        </View>
      </View>

      {/* 4. PINNED ACTIVE QUESTION BANNER */}
      <View style={styles.pinnedQuestionBanner}>
        <View style={styles.pinnedQuestionHeader}>
          <View style={styles.questionTopicPill}>
            <Text style={styles.questionTopicText}>{currentQuestion?.topic || subjectName}</Text>
          </View>
          {currentQuestion?.difficulty && (
            <View style={styles.questionDifficultyPill}>
              <Text style={styles.questionDifficultyText}>{currentQuestion.difficulty}</Text>
            </View>
          )}
          {currentQuestion?.generated_follow_up && (
            <View style={styles.followUpBadge}>
              <Feather name="corner-down-right" size={11} color="#A78BFA" style={{ marginRight: 3 }} />
              <Text style={styles.followUpBadgeText}>Adaptive Follow-Up</Text>
            </View>
          )}

          <View style={{ flex: 1 }} />

          {/* Re-Ask Question Button */}
          <TouchableOpacity
            style={styles.reaskQuestionBtn}
            onPress={() => onPlayQuestionSpeech(true)}
            accessibilityLabel="Repeat question aloud"
          >
            <Feather name="rotate-ccw" size={12} color="#A78BFA" style={{ marginRight: 4 }} />
            <Text style={styles.reaskQuestionBtnText}>Repeat Question</Text>
          </TouchableOpacity>

          {/* Auto-Ask Toggle */}
          <TouchableOpacity style={styles.autoAskToggle} onPress={onToggleAutoAsk}>
            <Feather
              name={autoAskQuestion ? 'check-circle' : 'circle'}
              size={12}
              color={autoAskQuestion ? '#10B981' : '#9AA0A6'}
              style={{ marginRight: 4 }}
            />
            <Text style={[styles.autoAskToggleText, autoAskQuestion && styles.autoAskToggleTextActive]}>
              Auto-Voice: {autoAskQuestion ? 'ON' : 'OFF'}
            </Text>
          </TouchableOpacity>
        </View>

        <Text style={styles.pinnedQuestionText}>
          {currentQuestion?.question_text || 'Waiting for interviewer question...'}
        </Text>
      </View>

      {/* 5. LIVE CLOSED CAPTIONS (CC) STRIP */}
      {isCaptionsOn && (
        <View style={styles.captionsStrip}>
          <View style={styles.captionSpeakerHeader}>
            <View style={styles.captionLiveDot} />
            <Text style={styles.captionSpeakerLabel}>
              {isSpeakingQuestion
                ? 'AI Interviewer'
                : isRecording
                ? 'You (Transcribing...)'
                : answerText.trim()
                ? 'Your Recorded Answer'
                : 'Live Closed Captions'}
            </Text>
          </View>

          <Text style={styles.captionBodyText} numberOfLines={2}>
            {isSpeakingQuestion
              ? currentQuestion?.question_text || 'Asking question...'
              : answerText.trim()
              ? answerText
              : isRecording
              ? 'Listening... Speak your answer aloud into your microphone.'
              : 'Click the Microphone button below to speak, or open the Text editor to write your response.'}
          </Text>
        </View>
      )}

      {/* 6. GOOGLE MEET BOTTOM CONTROL BAR */}
      <View style={styles.bottomControlBar}>
        <View style={styles.controlsPill}>
          {/* 1. Microphone Toggle */}
          <TouchableOpacity
            style={[styles.controlBtn, isRecording ? styles.controlBtnActiveGreen : styles.controlBtnMuted]}
            onPress={onToggleRecording}
            accessibilityLabel={isRecording ? 'Mute microphone' : 'Unmute microphone'}
          >
            <Feather name={isRecording ? 'mic' : 'mic-off'} size={18} color="#FFFFFF" />
            <Text style={styles.controlBtnSubText}>{isRecording ? 'Speaking' : 'Mic Off'}</Text>
          </TouchableOpacity>

          {/* 2. Camera Toggle */}
          <TouchableOpacity
            style={[styles.controlBtn, isCameraOn ? styles.controlBtnGray : styles.controlBtnMutedRed]}
            onPress={toggleCamera}
            accessibilityLabel={isCameraOn ? 'Turn camera off' : 'Turn camera on'}
          >
            <Feather name={isCameraOn ? 'video' : 'video-off'} size={18} color="#FFFFFF" />
            <Text style={styles.controlBtnSubText}>{isCameraOn ? 'Camera On' : 'Camera Off'}</Text>
          </TouchableOpacity>

          {/* 3. Closed Captions (CC) Toggle */}
          <TouchableOpacity
            style={[styles.controlBtn, isCaptionsOn ? styles.controlBtnActiveBlue : styles.controlBtnGray]}
            onPress={() => setIsCaptionsOn(!isCaptionsOn)}
            accessibilityLabel="Toggle closed captions"
          >
            <Feather name="message-square" size={18} color="#FFFFFF" />
            <Text style={styles.controlBtnSubText}>CC</Text>
          </TouchableOpacity>

          {/* 4. Coding Workspace Toggle */}
          <TouchableOpacity
            style={[styles.controlBtn, isCodeWorkspaceOpen ? styles.controlBtnActivePurple : styles.controlBtnGray]}
            onPress={() => setIsCodeWorkspaceOpen(!isCodeWorkspaceOpen)}
            accessibilityLabel="Toggle coding IDE"
          >
            <Feather name="code" size={18} color="#FFFFFF" />
            <Text style={styles.controlBtnSubText}>Code IDE</Text>
          </TouchableOpacity>

          {/* 5. Review / Text Answer Fallback */}
          <TouchableOpacity
            style={[styles.controlBtn, isTextAnswerOpen ? styles.controlBtnActiveBlue : styles.controlBtnGray]}
            onPress={() => setIsTextAnswerOpen(!isTextAnswerOpen)}
            accessibilityLabel="Edit or review text response"
          >
            <Feather name="edit-3" size={18} color="#FFFFFF" />
            <Text style={styles.controlBtnSubText}>Edit Text</Text>
          </TouchableOpacity>

          {/* 6. Submit Answer for Evaluation */}
          <TouchableOpacity
            style={[
              styles.controlBtn,
              styles.controlBtnSubmit,
              (!answerText.trim() || isSubmitting) && styles.controlBtnDisabled,
            ]}
            disabled={!answerText.trim() || isSubmitting}
            onPress={onSubmitAnswer}
            accessibilityLabel="Submit answer for AI evaluation"
          >
            {isSubmitting ? (
              <ActivityIndicator size="small" color="#FFFFFF" />
            ) : (
              <>
                <Feather name="check" size={18} color="#FFFFFF" />
                <Text style={styles.controlBtnSubText}>Submit</Text>
              </>
            )}
          </TouchableOpacity>

          {/* 7. End Call Button (Classic Google Meet Red Pill) */}
          <TouchableOpacity
            style={styles.endCallBtn}
            onPress={() => setShowEndConfirm(true)}
            accessibilityLabel="End interview call"
          >
            <Feather name="phone-off" size={20} color="#FFFFFF" />
            <Text style={styles.endCallBtnText}>End Call</Text>
          </TouchableOpacity>
        </View>
      </View>

      {/* 7. TECHNICAL CODING WORKSPACE MODAL / DRAWER */}
      <Modal visible={isCodeWorkspaceOpen} transparent animationType="slide">
        <View style={styles.modalBackdrop}>
          <View style={styles.codeWorkspaceContainer}>
            <View style={styles.codeWorkspaceHeader}>
              <View style={{ flexDirection: 'row', alignItems: 'center', gap: 8 }}>
                <Feather name="terminal" size={18} color="#A78BFA" />
                <Text style={styles.codeWorkspaceTitle}>Coding Workspace & Sandboxed Runner</Text>
              </View>

              <View style={{ flexDirection: 'row', alignItems: 'center', gap: 8 }}>
                {/* Language Selectors */}
                {(['python', 'javascript', 'c', 'cpp', 'java'] as const).map((lang) => (
                  <TouchableOpacity
                    key={lang}
                    style={[styles.langChip, codeLanguage === lang && styles.langChipActive]}
                    onPress={() => setCodeLanguage(lang)}
                  >
                    <Text style={[styles.langChipText, codeLanguage === lang && styles.langChipTextActive]}>
                      {lang === 'cpp' ? 'C++' : lang.toUpperCase()}
                    </Text>
                  </TouchableOpacity>
                ))}

                <TouchableOpacity
                  style={styles.modalCloseBtn}
                  onPress={() => setIsCodeWorkspaceOpen(false)}
                >
                  <Feather name="x" size={18} color="#FFFFFF" />
                </TouchableOpacity>
              </View>
            </View>

            {/* Code Input Area */}
            <View style={styles.codeEditorWrapper}>
              <TextInput
                style={styles.codeTextInput}
                multiline
                value={codeSnippet}
                onChangeText={setCodeSnippet}
                placeholder="Write your solution here..."
                placeholderTextColor="#64748B"
                textAlignVertical="top"
                autoCapitalize="none"
                autoCorrect={false}
              />
            </View>

            {/* Execution Output Console */}
            {codeOutput && (
              <View style={styles.codeOutputBox}>
                <View style={styles.codeOutputHeader}>
                  <Text style={styles.codeOutputTitle}>Output Console</Text>
                  <View
                    style={[
                      styles.codeStatusBadge,
                      codeStatus === 'PASSED' ? styles.statusPassed : styles.statusFailed,
                    ]}
                  >
                    <Text style={styles.codeStatusBadgeText}>{codeStatus}</Text>
                  </View>
                </View>
                <ScrollView style={styles.outputScroll}>
                  <Text style={styles.codeOutputText}>{codeOutput}</Text>
                </ScrollView>
              </View>
            )}

            {/* Action Buttons */}
            <View style={styles.codeActionsRow}>
              <TouchableOpacity
                style={[styles.runCodeBtn, isRunningCode && styles.controlBtnDisabled]}
                disabled={isRunningCode}
                onPress={handleRunCode}
              >
                {isRunningCode ? (
                  <ActivityIndicator size="small" color="#FFFFFF" />
                ) : (
                  <>
                    <Feather name="play" size={14} color="#FFFFFF" style={{ marginRight: 6 }} />
                    <Text style={styles.runCodeBtnText}>Run Code (Sandbox)</Text>
                  </>
                )}
              </TouchableOpacity>

              <TouchableOpacity style={styles.attachCodeBtn} onPress={handleAttachCodeToAnswer}>
                <Feather name="plus-circle" size={14} color="#FFFFFF" style={{ marginRight: 6 }} />
                <Text style={styles.attachCodeBtnText}>Add Code to Answer</Text>
              </TouchableOpacity>

              <TouchableOpacity
                style={styles.cancelCodeBtn}
                onPress={() => setIsCodeWorkspaceOpen(false)}
              >
                <Text style={styles.cancelCodeBtnText}>Close Editor</Text>
              </TouchableOpacity>
            </View>
          </View>
        </View>
      </Modal>

      {/* 8. EDITABLE TEXT ANSWER & TRANSCRIPT MODAL */}
      <Modal visible={isTextAnswerOpen} transparent animationType="slide">
        <View style={styles.modalBackdrop}>
          <View style={styles.textAnswerContainer}>
            <View style={styles.codeWorkspaceHeader}>
              <View style={{ flexDirection: 'row', alignItems: 'center', gap: 8 }}>
                <Feather name="file-text" size={18} color="#60A5FA" />
                <Text style={styles.codeWorkspaceTitle}>Review & Edit Your Answer</Text>
              </View>
              <TouchableOpacity
                style={styles.modalCloseBtn}
                onPress={() => setIsTextAnswerOpen(false)}
              >
                <Feather name="x" size={18} color="#FFFFFF" />
              </TouchableOpacity>
            </View>

            <Text style={styles.textModalSubtext}>
              Review the live speech transcript, fix technical terminology, or type your response in full before submitting to the AI interviewer.
            </Text>

            <TextInput
              style={styles.textAnswerInput}
              multiline
              numberOfLines={9}
              value={answerText}
              onChangeText={onChangeAnswerText}
              placeholder="Your answer transcript appears here. You can refine, format, or type your complete explanation..."
              placeholderTextColor="#64748B"
              textAlignVertical="top"
            />

            <View style={styles.textModalFooter}>
              <Text style={styles.wordCountLabel}>
                {answerText.trim() ? answerText.trim().split(/\s+/).length : 0} words
              </Text>

              <View style={{ flexDirection: 'row', gap: 10 }}>
                <TouchableOpacity
                  style={styles.cancelCodeBtn}
                  onPress={() => setIsTextAnswerOpen(false)}
                >
                  <Text style={styles.cancelCodeBtnText}>Done</Text>
                </TouchableOpacity>

                <TouchableOpacity
                  style={[styles.runCodeBtn, (!answerText.trim() || isSubmitting) && styles.controlBtnDisabled]}
                  disabled={!answerText.trim() || isSubmitting}
                  onPress={() => {
                    setIsTextAnswerOpen(false);
                    onSubmitAnswer();
                  }}
                >
                  {isSubmitting ? (
                    <ActivityIndicator size="small" color="#FFFFFF" />
                  ) : (
                    <>
                      <Feather name="check" size={14} color="#FFFFFF" style={{ marginRight: 6 }} />
                      <Text style={styles.runCodeBtnText}>Submit Answer</Text>
                    </>
                  )}
                </TouchableOpacity>
              </View>
            </View>
          </View>
        </View>
      </Modal>

      {/* 9. SETTINGS & VOICE CUSTOMIZATION MODAL */}
      <Modal visible={isSettingsOpen} transparent animationType="fade">
        <View style={styles.modalBackdrop}>
          <View style={styles.settingsContainer}>
            <View style={styles.codeWorkspaceHeader}>
              <Text style={styles.codeWorkspaceTitle}>Interview Voice & Audio Settings</Text>
              <TouchableOpacity style={styles.modalCloseBtn} onPress={() => setIsSettingsOpen(false)}>
                <Feather name="x" size={18} color="#FFFFFF" />
              </TouchableOpacity>
            </View>

            {/* Voice Personas */}
            <Text style={styles.settingsSectionTitle}>Interviewer Voice Persona</Text>
            <View style={styles.settingsGrid}>
              {[
                { id: 'Aria (Clear Studio)', label: 'Aria', desc: 'Studio female interviewer' },
                { id: 'Guy (Executive Lead)', label: 'Guy', desc: 'Crisp male technical lead' },
                { id: 'Jenny (Warm Natural)', label: 'Jenny', desc: 'Natural, conversational recruiter' },
                { id: 'Neerja (Indian English)', label: 'Neerja', desc: 'Indian English recruiter' },
              ].map((v) => {
                const active = selectedVoicePersona === v.id;
                return (
                  <TouchableOpacity
                    key={v.id}
                    style={[styles.personaCard, active && styles.personaCardActive]}
                    onPress={() => onSelectVoicePersona(v.id)}
                  >
                    <View style={{ flexDirection: 'row', alignItems: 'center', justifyContent: 'space-between' }}>
                      <Text style={[styles.personaLabel, active && styles.personaLabelActive]}>{v.label}</Text>
                      {active && <Feather name="check-circle" size={14} color="#A78BFA" />}
                    </View>
                    <Text style={styles.personaDesc}>{v.desc}</Text>
                  </TouchableOpacity>
                );
              })}
            </View>

            {/* Speaking Rate */}
            <Text style={styles.settingsSectionTitle}>Speaking Speed</Text>
            <View style={styles.speedRow}>
              {[0.85, 0.95, 1.15].map((rate) => {
                const active = speechRate === rate;
                const label = rate === 0.85 ? '0.85x (Deliberate)' : rate === 0.95 ? '1.0x (Standard)' : '1.15x (Brisk)';
                return (
                  <TouchableOpacity
                    key={rate}
                    style={[styles.speedPill, active && styles.speedPillActive]}
                    onPress={() => onSetSpeechRate(rate)}
                  >
                    <Text style={[styles.speedPillText, active && styles.speedPillTextActive]}>{label}</Text>
                  </TouchableOpacity>
                );
              })}
            </View>

            <TouchableOpacity style={styles.settingsCloseBtn} onPress={() => setIsSettingsOpen(false)}>
              <Text style={styles.settingsCloseBtnText}>Save & Return to Call</Text>
            </TouchableOpacity>
          </View>
        </View>
      </Modal>

      {/* 10. END CALL CONFIRMATION DIALOG */}
      <Modal visible={showEndConfirm} transparent animationType="fade">
        <View style={styles.modalBackdrop}>
          <View style={styles.confirmBox}>
            <View style={styles.confirmIconCircle}>
              <Feather name="phone-off" size={24} color="#EF4444" />
            </View>
            <Text style={styles.confirmTitle}>End Mock Interview?</Text>
            <Text style={styles.confirmDesc}>
              Your completed questions and evaluations will be finalized into a comprehensive performance report.
            </Text>

            <View style={styles.confirmActionsRow}>
              <TouchableOpacity
                style={styles.confirmCancelBtn}
                onPress={() => setShowEndConfirm(false)}
              >
                <Text style={styles.confirmCancelBtnText}>Return to Interview</Text>
              </TouchableOpacity>

              <TouchableOpacity
                style={styles.confirmEndBtn}
                onPress={handleEndCall}
              >
                <Text style={styles.confirmEndBtnText}>End Call & View Report</Text>
              </TouchableOpacity>
            </View>
          </View>
        </View>
      </Modal>
    </View>
  );
};

const styles = StyleSheet.create({
  meetContainer: {
    flex: 1,
    backgroundColor: '#202124', // Google Meet Authentic Dark Background
  },

  // 1. TOP BAR
  topBar: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: 20,
    paddingVertical: 12,
    borderBottomWidth: 1,
    borderBottomColor: '#3C4043',
    backgroundColor: '#1E1F22',
  },
  topBarLeft: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
    flex: 1,
  },
  brandingPill: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: 'rgba(139, 92, 246, 0.15)',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 20,
    borderWidth: 1,
    borderColor: 'rgba(139, 92, 246, 0.3)',
  },
  meetLogoDot: {
    width: 8,
    height: 8,
    borderRadius: 4,
    backgroundColor: '#A78BFA',
    marginRight: 6,
  },
  brandingText: {
    color: '#E8EAED',
    fontSize: 13,
    fontWeight: '700',
    letterSpacing: 0.3,
  },
  sessionTitleText: {
    color: '#9AA0A6',
    fontSize: 13,
    fontWeight: '500',
    maxWidth: 240,
  },
  topBarCenter: {
    alignItems: 'center',
  },
  timerBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#2D2E30',
    paddingHorizontal: 12,
    paddingVertical: 5,
    borderRadius: 20,
    borderWidth: 1,
    borderColor: '#3C4043',
  },
  recDot: {
    width: 8,
    height: 8,
    borderRadius: 4,
    backgroundColor: '#EF4444',
    marginRight: 5,
  },
  recText: {
    color: '#EF4444',
    fontSize: 11,
    fontWeight: '800',
    letterSpacing: 0.5,
  },
  timerDivider: {
    color: '#5F6368',
    marginHorizontal: 8,
  },
  timerText: {
    color: '#FFFFFF',
    fontSize: 13,
    fontWeight: '700',
    fontVariant: ['tabular-nums'],
  },
  topBarRight: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 10,
    flex: 1,
    justifyContent: 'flex-end',
  },
  qualityBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: 'rgba(16, 185, 129, 0.12)',
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: 16,
  },
  qualityText: {
    color: '#34D399',
    fontSize: 11,
    fontWeight: '600',
  },
  questionCounterPill: {
    backgroundColor: '#8B5CF6',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 16,
  },
  questionCounterText: {
    color: '#FFFFFF',
    fontSize: 12,
    fontWeight: '700',
  },

  // 2. CAMERA BANNER
  cameraBanner: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: 'rgba(245, 158, 11, 0.12)',
    paddingHorizontal: 16,
    paddingVertical: 8,
    borderBottomWidth: 1,
    borderBottomColor: 'rgba(245, 158, 11, 0.25)',
  },
  cameraBannerText: {
    color: '#FDE68A',
    fontSize: 12,
    flex: 1,
  },
  retryPermBtn: {
    backgroundColor: '#F59E0B',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 12,
  },
  retryPermBtnText: {
    color: '#000000',
    fontSize: 11,
    fontWeight: '700',
  },

  // IN-CALL FEEDBACK TOAST BANNER
  inCallFeedbackBanner: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    backgroundColor: '#064E3B',
    paddingHorizontal: 16,
    paddingVertical: 10,
    borderBottomWidth: 1,
    borderBottomColor: '#059669',
  },
  inCallFeedbackLeft: {
    flexDirection: 'row',
    alignItems: 'center',
    flex: 1,
    gap: 10,
  },
  inCallCheckCircle: {
    width: 28,
    height: 28,
    borderRadius: 14,
    backgroundColor: 'rgba(16, 185, 129, 0.2)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  inCallFeedbackTitle: {
    color: '#A7F3D0',
    fontSize: 13,
    fontWeight: '700',
  },
  inCallFeedbackSubtitle: {
    color: '#D1FAE5',
    fontSize: 11,
    fontWeight: '500',
    marginTop: 2,
  },
  inCallDismissBtn: {
    padding: 6,
    borderRadius: 12,
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
  },

  // 3. VIDEO STAGE (2 TILES)
  videoStage: {
    flex: 1,
    flexDirection: 'row',
    padding: 16,
    gap: 16,
    minHeight: 340,
  },
  videoTile: {
    flex: 1,
    backgroundColor: '#2D2E30',
    borderRadius: 16,
    borderWidth: 1,
    borderColor: '#3C4043',
    overflow: 'hidden',
    position: 'relative',
    justifyContent: 'space-between',
  },
  aiTile: {
    backgroundColor: '#1E1F22',
  },
  userTile: {
    backgroundColor: '#1E1F22',
  },
  tileHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: 12,
    zIndex: 10,
  },
  roleBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: 'rgba(0, 0, 0, 0.6)',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 12,
  },
  roleBadgeText: {
    color: '#E8EAED',
    fontSize: 11,
    fontWeight: '600',
  },
  voiceConfigBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: 'rgba(0, 0, 0, 0.6)',
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: 12,
  },
  voiceConfigText: {
    color: '#E8EAED',
    fontSize: 11,
    fontWeight: '500',
  },
  userStatusBadges: {
    flexDirection: 'row',
    gap: 6,
  },
  devicePill: {
    width: 26,
    height: 26,
    borderRadius: 13,
    backgroundColor: 'rgba(0,0,0,0.6)',
    alignItems: 'center',
    justifyContent: 'center',
  },
  devicePillOff: {
    backgroundColor: 'rgba(239, 68, 68, 0.25)',
  },
  devicePillActive: {
    backgroundColor: 'rgba(16, 185, 129, 0.25)',
  },
  devicePillMuted: {
    backgroundColor: 'rgba(239, 68, 68, 0.25)',
  },

  // AI Avatar & Waveform
  aiCenterContainer: {
    alignItems: 'center',
    justifyContent: 'center',
    flex: 1,
  },
  aiAvatarHalo: {
    width: 108,
    height: 108,
    borderRadius: 54,
    borderWidth: 2,
    borderColor: '#4A4D51',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: 'rgba(139, 92, 246, 0.08)',
  },
  aiAvatarHaloSpeaking: {
    borderColor: '#8B5CF6',
    backgroundColor: 'rgba(139, 92, 246, 0.2)',
    shadowColor: '#8B5CF6',
    shadowOpacity: 0.8,
    shadowRadius: 18,
    elevation: 8,
  },
  aiAvatarCircle: {
    width: 86,
    height: 86,
    borderRadius: 43,
    backgroundColor: '#8B5CF6',
    alignItems: 'center',
    justifyContent: 'center',
  },
  soundWaveRow: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 5,
    height: 36,
    marginTop: 16,
  },
  soundWaveBar: {
    width: 4,
    borderRadius: 2,
    backgroundColor: '#5F6368',
  },
  soundWaveBarActive: {
    backgroundColor: '#A78BFA',
  },
  aiSpeakingBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: 'rgba(255, 255, 255, 0.06)',
    paddingHorizontal: 12,
    paddingVertical: 5,
    borderRadius: 16,
    marginTop: 12,
  },
  aiSpeakingBadgeActive: {
    backgroundColor: 'rgba(16, 185, 129, 0.15)',
  },
  aiSpeakingBadgeText: {
    color: '#9AA0A6',
    fontSize: 12,
    fontWeight: '500',
  },
  aiSpeakingBadgeTextActive: {
    color: '#34D399',
    fontWeight: '700',
  },

  // User Video Feed / Camera-Off Tile
  userVideoWrapper: {
    flex: 1,
    width: '100%',
    height: '100%',
    position: 'relative',
    alignItems: 'center',
    justifyContent: 'center',
  },
  cameraOffPlaceholder: {
    alignItems: 'center',
    justifyContent: 'center',
  },
  userAvatarCircle: {
    width: 96,
    height: 96,
    borderRadius: 48,
    backgroundColor: '#2563EB',
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: 12,
  },
  userAvatarInitials: {
    color: '#FFFFFF',
    fontSize: 32,
    fontWeight: '700',
  },
  cameraOffText: {
    color: '#9AA0A6',
    fontSize: 12,
    fontWeight: '500',
    marginBottom: 10,
  },
  enableCamSmallBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#3C4043',
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 16,
  },
  enableCamSmallBtnText: {
    color: '#FFFFFF',
    fontSize: 11,
    fontWeight: '600',
  },
  candidateRecordingPulse: {
    position: 'absolute',
    top: 10,
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: 'rgba(16, 185, 129, 0.9)',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 14,
    zIndex: 10,
  },
  recPulseDot: {
    width: 6,
    height: 6,
    borderRadius: 3,
    backgroundColor: '#FFFFFF',
    marginRight: 6,
  },
  candidateRecordingPulseText: {
    color: '#FFFFFF',
    fontSize: 11,
    fontWeight: '700',
  },

  // Tile Footer
  tileFooter: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: 12,
    backgroundColor: 'rgba(0,0,0,0.4)',
    zIndex: 10,
  },
  tileName: {
    color: '#E8EAED',
    fontSize: 12,
    fontWeight: '600',
  },
  aiSubStatus: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 5,
  },
  statusDot: {
    width: 6,
    height: 6,
    borderRadius: 3,
  },
  dotGreen: {
    backgroundColor: '#10B981',
  },
  dotBlue: {
    backgroundColor: '#60A5FA',
  },
  dotGray: {
    backgroundColor: '#64748B',
  },
  statusDotText: {
    color: '#9AA0A6',
    fontSize: 11,
  },

  // 4. PINNED QUESTION BANNER
  pinnedQuestionBanner: {
    backgroundColor: '#2D2E30',
    marginHorizontal: 16,
    marginBottom: 10,
    padding: 14,
    borderRadius: 14,
    borderWidth: 1,
    borderColor: '#3C4043',
  },
  pinnedQuestionHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    marginBottom: 8,
    flexWrap: 'wrap',
  },
  questionTopicPill: {
    backgroundColor: 'rgba(139, 92, 246, 0.2)',
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 10,
  },
  questionTopicText: {
    color: '#C4B5FD',
    fontSize: 11,
    fontWeight: '700',
  },
  questionDifficultyPill: {
    backgroundColor: '#3C4043',
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 10,
  },
  questionDifficultyText: {
    color: '#E8EAED',
    fontSize: 11,
    fontWeight: '600',
  },
  followUpBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: 'rgba(139, 92, 246, 0.15)',
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 10,
  },
  followUpBadgeText: {
    color: '#C4B5FD',
    fontSize: 11,
    fontWeight: '600',
  },
  reaskQuestionBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: 'rgba(139, 92, 246, 0.15)',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 14,
    borderWidth: 1,
    borderColor: 'rgba(139, 92, 246, 0.3)',
  },
  reaskQuestionBtnText: {
    color: '#C4B5FD',
    fontSize: 11,
    fontWeight: '600',
  },
  autoAskToggle: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#3C4043',
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: 14,
  },
  autoAskToggleText: {
    color: '#9AA0A6',
    fontSize: 11,
    fontWeight: '500',
  },
  autoAskToggleTextActive: {
    color: '#10B981',
    fontWeight: '700',
  },
  pinnedQuestionText: {
    color: '#FFFFFF',
    fontSize: 15,
    fontWeight: '600',
    lineHeight: 22,
  },

  // 5. LIVE CLOSED CAPTIONS STRIP
  captionsStrip: {
    backgroundColor: 'rgba(32, 33, 36, 0.95)',
    marginHorizontal: 16,
    marginBottom: 10,
    padding: 12,
    borderRadius: 12,
    borderWidth: 1,
    borderColor: '#3C4043',
  },
  captionSpeakerHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 4,
  },
  captionLiveDot: {
    width: 6,
    height: 6,
    borderRadius: 3,
    backgroundColor: '#60A5FA',
    marginRight: 6,
  },
  captionSpeakerLabel: {
    color: '#9AA0A6',
    fontSize: 11,
    fontWeight: '700',
    textTransform: 'uppercase',
    letterSpacing: 0.5,
  },
  captionBodyText: {
    color: '#E8EAED',
    fontSize: 13,
    lineHeight: 18,
  },

  // 6. GOOGLE MEET BOTTOM CONTROL BAR
  bottomControlBar: {
    alignItems: 'center',
    justifyContent: 'center',
    paddingBottom: 16,
    paddingTop: 4,
  },
  controlsPill: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#1E1F22',
    paddingHorizontal: 16,
    paddingVertical: 10,
    borderRadius: 36,
    borderWidth: 1,
    borderColor: '#3C4043',
    gap: 12,
  },
  controlBtn: {
    alignItems: 'center',
    justifyContent: 'center',
    width: 54,
    height: 54,
    borderRadius: 27,
  },
  controlBtnSubText: {
    color: '#9AA0A6',
    fontSize: 9,
    fontWeight: '600',
    marginTop: 2,
  },
  controlBtnGray: {
    backgroundColor: '#3C4043',
  },
  controlBtnActiveGreen: {
    backgroundColor: '#10B981',
    shadowColor: '#10B981',
    shadowOpacity: 0.6,
    shadowRadius: 10,
    elevation: 6,
  },
  controlBtnMuted: {
    backgroundColor: '#EA4335',
  },
  controlBtnMutedRed: {
    backgroundColor: '#EA4335',
  },
  controlBtnActiveBlue: {
    backgroundColor: '#2563EB',
  },
  controlBtnActivePurple: {
    backgroundColor: '#8B5CF6',
  },
  controlBtnSubmit: {
    backgroundColor: '#10B981',
  },
  controlBtnDisabled: {
    opacity: 0.4,
  },
  endCallBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#EA4335',
    paddingHorizontal: 18,
    height: 48,
    borderRadius: 24,
    gap: 8,
  },
  endCallBtnText: {
    color: '#FFFFFF',
    fontSize: 13,
    fontWeight: '700',
  },

  // 7. MODALS & WORKSPACES
  modalBackdrop: {
    flex: 1,
    backgroundColor: 'rgba(0, 0, 0, 0.75)',
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  codeWorkspaceContainer: {
    width: '100%',
    maxWidth: 900,
    backgroundColor: '#1E1F22',
    borderRadius: 16,
    borderWidth: 1,
    borderColor: '#3C4043',
    padding: 20,
    maxHeight: '85%',
  },
  codeWorkspaceHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: 14,
    flexWrap: 'wrap',
    gap: 10,
  },
  codeWorkspaceTitle: {
    color: '#FFFFFF',
    fontSize: 16,
    fontWeight: '700',
  },
  langChip: {
    backgroundColor: '#2D2E30',
    paddingHorizontal: 10,
    paddingVertical: 5,
    borderRadius: 10,
    borderWidth: 1,
    borderColor: '#3C4043',
  },
  langChipActive: {
    backgroundColor: '#8B5CF6',
    borderColor: '#8B5CF6',
  },
  langChipText: {
    color: '#9AA0A6',
    fontSize: 11,
    fontWeight: '600',
  },
  langChipTextActive: {
    color: '#FFFFFF',
    fontWeight: '700',
  },
  modalCloseBtn: {
    width: 32,
    height: 32,
    borderRadius: 16,
    backgroundColor: '#3C4043',
    alignItems: 'center',
    justifyContent: 'center',
  },
  codeEditorWrapper: {
    backgroundColor: '#0F172A',
    borderRadius: 12,
    borderWidth: 1,
    borderColor: '#334155',
    minHeight: 180,
    maxHeight: 280,
    padding: 12,
  },
  codeTextInput: {
    color: '#38BDF8',
    fontFamily: Platform.OS === 'ios' ? 'Courier' : 'monospace',
    fontSize: 13,
    lineHeight: 20,
  },
  codeOutputBox: {
    backgroundColor: '#0A0F1D',
    borderRadius: 10,
    borderWidth: 1,
    borderColor: '#1E293B',
    marginTop: 12,
    padding: 12,
    maxHeight: 140,
  },
  codeOutputHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 6,
  },
  codeOutputTitle: {
    color: '#94A3B8',
    fontSize: 11,
    fontWeight: '700',
    textTransform: 'uppercase',
  },
  codeStatusBadge: {
    paddingHorizontal: 8,
    paddingVertical: 2,
    borderRadius: 6,
  },
  statusPassed: {
    backgroundColor: 'rgba(16, 185, 129, 0.2)',
  },
  statusFailed: {
    backgroundColor: 'rgba(239, 68, 68, 0.2)',
  },
  codeStatusBadgeText: {
    color: '#FFFFFF',
    fontSize: 10,
    fontWeight: '700',
  },
  outputScroll: {
    maxHeight: 90,
  },
  codeOutputText: {
    color: '#CBD5E1',
    fontFamily: Platform.OS === 'ios' ? 'Courier' : 'monospace',
    fontSize: 12,
  },
  codeActionsRow: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'flex-end',
    gap: 10,
    marginTop: 16,
  },
  runCodeBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#10B981',
    paddingHorizontal: 14,
    paddingVertical: 10,
    borderRadius: 10,
  },
  runCodeBtnText: {
    color: '#FFFFFF',
    fontSize: 13,
    fontWeight: '700',
  },
  attachCodeBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#8B5CF6',
    paddingHorizontal: 14,
    paddingVertical: 10,
    borderRadius: 10,
  },
  attachCodeBtnText: {
    color: '#FFFFFF',
    fontSize: 13,
    fontWeight: '700',
  },
  cancelCodeBtn: {
    paddingHorizontal: 14,
    paddingVertical: 10,
    borderRadius: 10,
    backgroundColor: '#3C4043',
  },
  cancelCodeBtnText: {
    color: '#E8EAED',
    fontSize: 13,
    fontWeight: '600',
  },

  // 8. TEXT ANSWER DRAWER
  textAnswerContainer: {
    width: '100%',
    maxWidth: 720,
    backgroundColor: '#1E1F22',
    borderRadius: 16,
    borderWidth: 1,
    borderColor: '#3C4043',
    padding: 20,
  },
  textModalSubtext: {
    color: '#9AA0A6',
    fontSize: 12,
    marginBottom: 12,
    lineHeight: 18,
  },
  textAnswerInput: {
    backgroundColor: '#2D2E30',
    color: '#FFFFFF',
    borderRadius: 12,
    borderWidth: 1,
    borderColor: '#3C4043',
    padding: 14,
    fontSize: 14,
    lineHeight: 22,
    minHeight: 160,
  },
  textModalFooter: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginTop: 14,
  },
  wordCountLabel: {
    color: '#9AA0A6',
    fontSize: 12,
    fontWeight: '600',
  },

  // 9. SETTINGS MODAL
  settingsContainer: {
    width: '100%',
    maxWidth: 580,
    backgroundColor: '#1E1F22',
    borderRadius: 16,
    borderWidth: 1,
    borderColor: '#3C4043',
    padding: 20,
  },
  settingsSectionTitle: {
    color: '#E8EAED',
    fontSize: 13,
    fontWeight: '700',
    marginTop: 14,
    marginBottom: 8,
  },
  settingsGrid: {
    gap: 8,
  },
  personaCard: {
    backgroundColor: '#2D2E30',
    padding: 12,
    borderRadius: 10,
    borderWidth: 1,
    borderColor: '#3C4043',
  },
  personaCardActive: {
    borderColor: '#8B5CF6',
    backgroundColor: 'rgba(139, 92, 246, 0.15)',
  },
  personaLabel: {
    color: '#FFFFFF',
    fontSize: 13,
    fontWeight: '700',
  },
  personaLabelActive: {
    color: '#C4B5FD',
  },
  personaDesc: {
    color: '#9AA0A6',
    fontSize: 11,
    marginTop: 2,
  },
  speedRow: {
    flexDirection: 'row',
    gap: 10,
  },
  speedPill: {
    flex: 1,
    backgroundColor: '#2D2E30',
    paddingVertical: 10,
    alignItems: 'center',
    borderRadius: 10,
    borderWidth: 1,
    borderColor: '#3C4043',
  },
  speedPillActive: {
    borderColor: '#8B5CF6',
    backgroundColor: 'rgba(139, 92, 246, 0.2)',
  },
  speedPillText: {
    color: '#9AA0A6',
    fontSize: 12,
    fontWeight: '600',
  },
  speedPillTextActive: {
    color: '#FFFFFF',
    fontWeight: '700',
  },
  settingsCloseBtn: {
    backgroundColor: '#8B5CF6',
    paddingVertical: 12,
    borderRadius: 12,
    alignItems: 'center',
    marginTop: 20,
  },
  settingsCloseBtnText: {
    color: '#FFFFFF',
    fontSize: 13,
    fontWeight: '700',
  },

  // 10. END CALL CONFIRM
  confirmBox: {
    width: '100%',
    maxWidth: 420,
    backgroundColor: '#1E1F22',
    borderRadius: 16,
    borderWidth: 1,
    borderColor: '#3C4043',
    padding: 24,
    alignItems: 'center',
  },
  confirmIconCircle: {
    width: 56,
    height: 56,
    borderRadius: 28,
    backgroundColor: 'rgba(239, 68, 68, 0.15)',
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: 14,
  },
  confirmTitle: {
    color: '#FFFFFF',
    fontSize: 18,
    fontWeight: '700',
    marginBottom: 8,
  },
  confirmDesc: {
    color: '#9AA0A6',
    fontSize: 13,
    textAlign: 'center',
    lineHeight: 18,
    marginBottom: 20,
  },
  confirmActionsRow: {
    flexDirection: 'row',
    gap: 12,
    width: '100%',
  },
  confirmCancelBtn: {
    flex: 1,
    backgroundColor: '#3C4043',
    paddingVertical: 12,
    borderRadius: 10,
    alignItems: 'center',
  },
  confirmCancelBtnText: {
    color: '#FFFFFF',
    fontSize: 13,
    fontWeight: '600',
  },
  confirmEndBtn: {
    flex: 1,
    backgroundColor: '#EA4335',
    paddingVertical: 12,
    borderRadius: 10,
    alignItems: 'center',
  },
  confirmEndBtnText: {
    color: '#FFFFFF',
    fontSize: 13,
    fontWeight: '700',
  },
});
