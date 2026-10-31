import React, { useState, useEffect, useRef, useMemo } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  TextInput,
  ScrollView,
  Platform,
  Animated,
  ActivityIndicator,
  Modal,
  Linking,
  Image,
} from 'react-native';
import { Feather, Ionicons, MaterialCommunityIcons } from '@expo/vector-icons';
import { LinearGradient } from 'expo-linear-gradient';
import { useAuth } from './auth-context';
import { getApiBaseUrl } from '../services/api';
import {
  VoiceAssistantEngine,
  AssistantMode,
  AssistantState,
} from '../services/voiceAssistantEngine';
import { MarkdownRenderer } from './MarkdownRenderer';

interface Project {
  id: string;
  student_id: string;
  name: string;
  description?: string;
  icon: string;
  conversation_count: number;
}

interface AttachedFile {
  name: string;
  mimeType: string;
  data: string;
  size: number;
}

interface Message {
  id: string;
  conversation_id: string;
  sender_type: 'user' | 'assistant' | 'system';
  message_text: string;
  input_type: 'text' | 'voice';
  file_data?: string;
  file_name?: string;
  search_sources?: Array<{
    title: string;
    url: string;
    snippet: string;
    source?: string;
  }>;
  created_at: string;
}

class FloatingAIErrorBoundary extends React.Component<{ children: React.ReactNode }, { hasError: boolean }> {
  constructor(props: { children: React.ReactNode }) {
    super(props);
    this.state = { hasError: false };
  }
  static getDerivedStateFromError() {
    return { hasError: true };
  }
  componentDidCatch(error: any, errorInfo: any) {
    console.warn('[SkillExa AI] Error safely caught by boundary:', error, errorInfo);
  }
  render() {
    if (this.state.hasError) {
      return null;
    }
    return this.props.children;
  }
}

export function FloatingSkillExaAI() {
  return (
    <FloatingAIErrorBoundary>
      <FloatingSkillExaAIInner />
    </FloatingAIErrorBoundary>
  );
}

function FloatingSkillExaAIInner() {
  const { profile } = useAuth();
  const studentEmail = profile?.email || 'guest-session';

  // Assistant & Voice Engine State
  const [isOpen, setIsOpen] = useState(false);
  const [assistantState, setAssistantState] = useState<AssistantState>('IDLE');
  const [assistantMode, setAssistantMode] = useState<AssistantMode>('WAKE_WORD');
  const [interimSpeech, setInterimSpeech] = useState('');
  const [silenceCountdown, setSilenceCountdown] = useState<number>(0);
  const [statusNotice, setStatusNotice] = useState<string | null>(null);

  // Projects & Conversations
  const [projects, setProjects] = useState<Project[]>([]);
  const [activeProjectId, setActiveProjectId] = useState<string>('');
  const [activeConversationId, setActiveConversationId] = useState<string>('');
  const [messages, setMessages] = useState<Message[]>([]);
  const [projectMemory, setProjectMemory] = useState<string>('');
  const [showMemoryBanner, setShowMemoryBanner] = useState(false);

  // New Project Dialog
  const [showNewProjectModal, setShowNewProjectModal] = useState(false);
  const [newProjectName, setNewProjectName] = useState('');
  const [newProjectDesc, setNewProjectDesc] = useState('');

  // UI & Input
  const [inputText, setInputText] = useState('');
  const [attachedFile, setAttachedFile] = useState<AttachedFile | null>(null);
  const [searchEnabled, setSearchEnabled] = useState(false);
  const [isSending, setIsSending] = useState(false);
  const [showProjectDropdown, setShowProjectDropdown] = useState(false);
  const [showModeDropdown, setShowModeDropdown] = useState(false);

  // Animations
  const pulseAnim = useRef(new Animated.Value(1)).current;
  const waveAnim1 = useRef(new Animated.Value(0.4)).current;
  const waveAnim2 = useRef(new Animated.Value(0.7)).current;
  const waveAnim3 = useRef(new Animated.Value(0.3)).current;
  const scrollViewRef = useRef<ScrollView>(null);

  // Voice Engine Instance
  const engineRef = useRef<VoiceAssistantEngine | null>(null);

  // Current active project object
  const activeProject = useMemo(() => {
    return projects.find((p) => p.id === activeProjectId) || projects[0] || null;
  }, [projects, activeProjectId]);

  // Pulse animation when listening or speaking
  useEffect(() => {
    if (
      assistantState === 'WAKE_WORD_LISTENING' ||
      assistantState === 'USER_LISTENING' ||
      assistantState === 'AI_SPEAKING' ||
      assistantState === 'ACTIVATED'
    ) {
      const pulseLoop = Animated.loop(
        Animated.sequence([
          Animated.timing(pulseAnim, { toValue: 1.15, duration: 600, useNativeDriver: true }),
          Animated.timing(pulseAnim, { toValue: 1, duration: 600, useNativeDriver: true }),
        ])
      );
      pulseLoop.start();
      return () => pulseLoop.stop();
    } else {
      pulseAnim.setValue(1);
    }
  }, [assistantState]);

  // Waveform animation when speaking
  useEffect(() => {
    if (assistantState === 'AI_SPEAKING') {
      const createWave = (val: Animated.Value, dur: number) =>
        Animated.loop(
          Animated.sequence([
            Animated.timing(val, { toValue: 1, duration: dur, useNativeDriver: true }),
            Animated.timing(val, { toValue: 0.2, duration: dur, useNativeDriver: true }),
          ])
        );

      const a1 = createWave(waveAnim1, 350);
      const a2 = createWave(waveAnim2, 250);
      const a3 = createWave(waveAnim3, 400);

      a1.start();
      a2.start();
      a3.start();

      return () => {
        a1.stop();
        a2.stop();
        a3.stop();
      };
    }
  }, [assistantState]);

  // Initialize Voice Assistant Engine
  useEffect(() => {
    const engine = new VoiceAssistantEngine({
      onStateChange: (newState) => {
        setAssistantState(newState);
      },
      onTranscriptChange: (text) => {
        setInterimSpeech(text);
        if (text) {
          setInputText(text);
        }
      },
      onSilenceCountdown: (secondsLeft, text) => {
        setSilenceCountdown(secondsLeft);
        if (text) {
          setInputText(text);
        }
      },
      onWakeWordDetected: (ack) => {
        setStatusNotice(ack);
        setInterimSpeech('');
        setSilenceCountdown(0);
        // Automatically open assistant UI when wake word triggers
        setIsOpen(true);
      },
      onCommandDetected: (cmd) => {
        if (cmd === 'STOP') {
          setStatusNotice('SkillExa AI stopped.');
          setInterimSpeech('');
          setSilenceCountdown(0);
        }
      },
      onQuestionReady: (question) => {
        setInterimSpeech('');
        setSilenceCountdown(0);
        setInputText('');
        sendChatMessage(question, 'voice');
      },
      onError: (msg) => {
        setStatusNotice(msg);
      },
    });

    engineRef.current = engine;

    return () => {
      engine.stopListening();
      engine.cancelSpeech();
    };
  }, []);

  // Activate voice engine silently in background
  const activateVoiceAssistant = async (shouldOpenPanel: boolean = false) => {
    if (!engineRef.current) return;
    const ok = await engineRef.current.startWakeWordListening();
    if (ok) {
      setStatusNotice('Listening for "Hey SkillExa"...');
      if (shouldOpenPanel) setIsOpen(true);
    } else {
      if (shouldOpenPanel) setIsOpen(true);
    }
  };

  // Silently initialize wake-word listening on first user interaction anywhere (Web only)
  useEffect(() => {
    if (
      Platform.OS !== 'web' ||
      typeof window === 'undefined' ||
      typeof window.addEventListener !== 'function'
    ) {
      return;
    }

    const handleFirstUserInteraction = () => {
      if (
        engineRef.current &&
        (engineRef.current.getState() === 'IDLE' || engineRef.current.getState() === 'INITIALIZING')
      ) {
        engineRef.current.startWakeWordListening();
      }
      if (typeof window !== 'undefined' && typeof window.removeEventListener === 'function') {
        window.removeEventListener('click', handleFirstUserInteraction);
        window.removeEventListener('keydown', handleFirstUserInteraction);
        window.removeEventListener('touchstart', handleFirstUserInteraction);
      }
    };

    window.addEventListener('click', handleFirstUserInteraction, { once: true });
    window.addEventListener('keydown', handleFirstUserInteraction, { once: true });
    window.addEventListener('touchstart', handleFirstUserInteraction, { once: true });

    return () => {
      if (typeof window !== 'undefined' && typeof window.removeEventListener === 'function') {
        window.removeEventListener('click', handleFirstUserInteraction);
        window.removeEventListener('keydown', handleFirstUserInteraction);
        window.removeEventListener('touchstart', handleFirstUserInteraction);
      }
    };
  }, []);

  // Always scroll to the last chat whenever panel opens or messages change
  useEffect(() => {
    if (isOpen) {
      setTimeout(() => {
        scrollViewRef.current?.scrollToEnd({ animated: false });
      }, 50);
      setTimeout(() => {
        scrollViewRef.current?.scrollToEnd({ animated: true });
      }, 200);
    }
  }, [isOpen, messages.length]);

  // Sync mode changes to engine
  const handleModeChange = async (mode: AssistantMode) => {
    setAssistantMode(mode);
    setShowModeDropdown(false);
    if (engineRef.current) {
      const ok = await engineRef.current.setMode(mode);
      if (mode === 'WAKE_WORD') {
        setStatusNotice(ok ? 'Listening for "Hey SkillExa"...' : 'Please tap the mic to allow microphone access.');
      } else if (mode === 'CONTINUOUS') {
        setStatusNotice(ok ? 'Continuous Conversation Mode active.' : 'Please allow microphone access.');
      } else {
        setStatusNotice('Push-to-Talk Mode: Tap the mic button to speak.');
      }
    }
  };

  // Load projects from backend
  const loadProjects = async () => {
    try {
      const baseUrl = getApiBaseUrl();
      const res = await fetch(`${baseUrl}/ai/projects?email=${encodeURIComponent(studentEmail)}`);
      if (res.ok) {
        const data = await res.json();
        setProjects(data);
        if (data.length > 0 && !activeProjectId) {
          setActiveProjectId(data[0].id);
          loadProjectMemory(data[0].id);
        }
      }
    } catch (e) {
      console.warn('Could not load AI projects:', e);
    }
  };

  // Load project memory
  const loadProjectMemory = async (projectId: string) => {
    try {
      const baseUrl = getApiBaseUrl();
      const res = await fetch(`${baseUrl}/ai/projects/${projectId}/memory?email=${encodeURIComponent(studentEmail)}`);
      if (res.ok) {
        const data = await res.json();
        setProjectMemory(data.memory_summary || '');
      }
    } catch (e) {}
  };

  // Load conversations when project changes
  useEffect(() => {
    loadProjects();
  }, [studentEmail]);

  useEffect(() => {
    if (activeProjectId) {
      loadProjectMemory(activeProjectId);
      loadConversationsForProject(activeProjectId);
    }
  }, [activeProjectId]);

  const loadConversationsForProject = async (projectId: string) => {
    try {
      const baseUrl = getApiBaseUrl();
      const res = await fetch(`${baseUrl}/ai/conversations?project_id=${projectId}&email=${encodeURIComponent(studentEmail)}`);
      if (res.ok) {
        const convs = await res.json();
        if (convs.length > 0) {
          // Load most recent conversation
          setActiveConversationId(convs[0].id);
          loadConversationMessages(convs[0].id);
        } else {
          setActiveConversationId('');
          setMessages([]);
        }
      }
    } catch (e) {}
  };

  const loadConversationMessages = async (conversationId: string) => {
    try {
      const baseUrl = getApiBaseUrl();
      const res = await fetch(`${baseUrl}/ai/conversations/${conversationId}?email=${encodeURIComponent(studentEmail)}`);
      if (res.ok) {
        const detail = await res.json();
        setMessages(detail.messages || []);
        setTimeout(() => scrollViewRef.current?.scrollToEnd({ animated: true }), 150);
      }
    } catch (e) {}
  };

  // Create Project
  const handleCreateProject = async () => {
    if (!newProjectName.trim()) return;
    try {
      const baseUrl = getApiBaseUrl();
      const res = await fetch(`${baseUrl}/ai/projects?email=${encodeURIComponent(studentEmail)}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          name: newProjectName.trim(),
          description: newProjectDesc.trim() || undefined,
          icon: 'folder',
        }),
      });
      if (res.ok) {
        const created = await res.json();
        setProjects((prev) => [created, ...prev]);
        setActiveProjectId(created.id);
        setShowNewProjectModal(false);
        setNewProjectName('');
        setNewProjectDesc('');
        setStatusNotice(`Switched to project: ${created.name}`);
      }
    } catch (e) {
      console.warn('Failed to create project:', e);
    }
  };

  // Send Chat Message (Voice, Typed, or with Image/Document Attachment)
  const sendChatMessage = async (text: string, inputType: 'text' | 'voice' = 'text') => {
    const cleanText = text.trim();
    if ((!cleanText && !attachedFile) || isSending) return;

    const currentAttachment = attachedFile;
    setAttachedFile(null);

    const messageText = cleanText || (currentAttachment ? `Please analyze this attached ${currentAttachment.mimeType.startsWith('image/') ? 'image' : 'file'}: ${currentAttachment.name}` : '');

    if (engineRef.current) {
      engineRef.current.clearSilenceTimer();
    }
    setSilenceCountdown(0);
    setInputText('');
    setIsSending(true);

    // Optimistically add user message to UI
    const tempUserMsg: Message = {
      id: `temp-${Date.now()}`,
      conversation_id: activeConversationId,
      sender_type: 'user',
      message_text: messageText,
      input_type: inputType,
      file_data: currentAttachment?.data,
      file_name: currentAttachment?.name,
      created_at: new Date().toISOString(),
    };
    setMessages((prev) => [...prev, tempUserMsg]);
    setTimeout(() => scrollViewRef.current?.scrollToEnd({ animated: true }), 100);

    try {
      const baseUrl = getApiBaseUrl();
      const res = await fetch(`${baseUrl}/ai/chat?email=${encodeURIComponent(studentEmail)}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          message: messageText,
          project_id: activeProjectId || undefined,
          conversation_id: activeConversationId || undefined,
          input_type: inputType,
          search_enabled: searchEnabled,
          file_data: currentAttachment?.data,
          file_name: currentAttachment?.name,
          file_mime_type: currentAttachment?.mimeType,
        }),
      });

      if (res.ok) {
        const data = await res.json();
        setActiveConversationId(data.conversation_id);
        if (data.project_id && data.project_id !== activeProjectId) {
          setActiveProjectId(data.project_id);
        }

        const newAssistantMsg: Message = {
          id: `asst-${Date.now()}`,
          conversation_id: data.conversation_id,
          sender_type: 'assistant',
          message_text: data.reply,
          input_type: 'text',
          search_sources: data.search_sources || [],
          created_at: new Date().toISOString(),
        };

        setMessages((prev) => [...prev, newAssistantMsg]);
        setTimeout(() => scrollViewRef.current?.scrollToEnd({ animated: true }), 100);

        // Update project memory summary if returned
        if (data.memory_summary) {
          setProjectMemory(data.memory_summary);
        }

        // Play speech response if user interacted with voice or continuous mode
        if (inputType === 'voice' || assistantMode === 'CONTINUOUS' || assistantMode === 'WAKE_WORD') {
          if (engineRef.current && data.speech_text) {
            engineRef.current.speak(data.speech_text);
          }
        }
      } else {
        const errorMsg: Message = {
          id: `err-${Date.now()}`,
          conversation_id: activeConversationId,
          sender_type: 'assistant',
          message_text: 'I encountered an issue connecting to SkillExa AI servers. Please try again.',
          input_type: 'text',
          created_at: new Date().toISOString(),
        };
        setMessages((prev) => [...prev, errorMsg]);
      }
    } catch (e: any) {
      console.warn('AI Chat Error:', e);
    } finally {
      setIsSending(false);
    }
  };

  // Mic Button Action (Push to talk or toggle)
  const handleMicClick = async () => {
    if (!engineRef.current) return;

    if (
      assistantState === 'WAKE_WORD_LISTENING' ||
      assistantState === 'USER_LISTENING'
    ) {
      engineRef.current.stopListening();
    } else if (assistantState === 'AI_SPEAKING') {
      engineRef.current.cancelSpeech();
    } else {
      if (assistantMode === 'WAKE_WORD') {
        await engineRef.current.startWakeWordListening();
      } else if (assistantMode === 'CONTINUOUS') {
        await engineRef.current.startContinuousListening();
      } else {
        await engineRef.current.startPushToTalk();
      }
    }
  };

  // Attach image or code/document file
  const handlePickFile = () => {
    if (Platform.OS === 'web' && typeof document !== 'undefined') {
      const input = document.createElement('input');
      input.type = 'file';
      input.accept = 'image/*,application/pdf,.py,.c,.cpp,.java,.js,.ts,.html,.css,.json,.txt,.sql';
      input.onchange = (e: any) => {
        const file = e.target.files?.[0];
        if (!file) return;
        if (file.size > 15 * 1024 * 1024) {
          setStatusNotice('File exceeds 15MB size limit.');
          return;
        }
        const reader = new FileReader();
        reader.onload = (loadEvt: any) => {
          const base64Data = loadEvt.target.result as string;
          setAttachedFile({
            name: file.name,
            mimeType: file.type || 'application/octet-stream',
            data: base64Data,
            size: file.size,
          });
          setStatusNotice(`Attached: ${file.name}`);
        };
        reader.readAsDataURL(file);
      };
      input.click();
    } else {
      setStatusNotice('File upload ready.');
    }
  };

  // Re-listen / speak an assistant message
  const handleReplayMessage = (text: string) => {
    if (engineRef.current) {
      engineRef.current.speak(text);
    }
  };

  // Start a new chat session
  const handleNewChat = () => {
    if (engineRef.current) {
      engineRef.current.cancelSpeech();
    }
    setActiveConversationId('');
    setMessages([]);
    setInputText('');
    setStatusNotice('Started a new conversation');
  };

  // Stop assistant completely
  const handleStopAll = () => {
    if (engineRef.current) {
      engineRef.current.cancelSpeech();
      engineRef.current.stopListening();
    }
    setStatusNotice('SkillExa AI stopped.');
  };

  return (
    <>
      {/* ------------------------------------------------------------- */}
      {/* FLOATING ACTION BUTTON (Always in Bottom-Right Corner)         */}
      {/* ------------------------------------------------------------- */}
      <View style={styles.floatingContainer} pointerEvents="box-none">
        <Animated.View style={[{ transform: [{ scale: pulseAnim }] }]}>
          <TouchableOpacity
            style={[
              styles.floatingButton,
              (assistantState === 'WAKE_WORD_LISTENING' || assistantState === 'USER_LISTENING') && styles.floatingButtonListening,
              (assistantState === 'AI_SPEAKING' || assistantState === 'ACTIVATED') && styles.floatingButtonSpeaking,
              assistantState === 'ERROR' && styles.floatingButtonError,
            ]}
            onPress={() => {
              if (!isOpen) {
                if (assistantState === 'IDLE' || assistantState === 'ERROR') {
                  activateVoiceAssistant(true);
                } else {
                  setIsOpen(true);
                }
              } else {
                setIsOpen(false);
              }
            }}
            activeOpacity={0.85}
          >
            <LinearGradient
              colors={
                assistantState === 'WAKE_WORD_LISTENING' || assistantState === 'USER_LISTENING'
                  ? ['#10B981', '#059669']
                  : assistantState === 'AI_SPEAKING' || assistantState === 'ACTIVATED'
                  ? ['#8B5CF6', '#6D28D9']
                  : assistantState === 'ERROR'
                  ? ['#EF4444', '#DC2626']
                  : ['#4F46E5', '#3730A3']
              }
              style={styles.floatingGradient}
            >
              {assistantState === 'WAKE_WORD_LISTENING' || assistantState === 'USER_LISTENING' ? (
                <Feather name="mic" size={26} color="#FFFFFF" />
              ) : assistantState === 'AI_SPEAKING' || assistantState === 'ACTIVATED' ? (
                <View style={styles.waveRow}>
                  <Animated.View style={[styles.waveBar, { transform: [{ scaleY: waveAnim1 }] }]} />
                  <Animated.View style={[styles.waveBar, { transform: [{ scaleY: waveAnim2 }] }]} />
                  <Animated.View style={[styles.waveBar, { transform: [{ scaleY: waveAnim3 }] }]} />
                </View>
              ) : assistantState === 'PROCESSING' || assistantState === 'INITIALIZING' ? (
                <ActivityIndicator size="small" color="#FFFFFF" />
              ) : (
                <MaterialCommunityIcons name="creation" size={26} color="#FFFFFF" />
              )}
            </LinearGradient>
          </TouchableOpacity>
        </Animated.View>
      </View>

      {/* ------------------------------------------------------------- */}
      {/* EXPANDABLE CHATGPT-STYLE AI PROJECTS & CONVERSATION PANEL     */}
      {/* ------------------------------------------------------------- */}
      {isOpen && (
        <View style={styles.panelContainer}>
          {/* Header */}
          <LinearGradient colors={['#1E293B', '#0F172A']} style={styles.panelHeader}>
            <View style={styles.headerLeft}>
              <View style={styles.brandIconWrap}>
                <MaterialCommunityIcons name="creation" size={20} color="#8B5CF6" />
              </View>
              <View>
                <Text style={styles.brandTitle}>SkillExa AI</Text>
                <View style={styles.statusRow}>
                  <View
                    style={[
                      styles.statusDot,
                      {
                        backgroundColor:
                          assistantState === 'WAKE_WORD_LISTENING' || assistantState === 'USER_LISTENING'
                            ? '#10B981'
                            : assistantState === 'AI_SPEAKING' || assistantState === 'ACTIVATED'
                            ? '#8B5CF6'
                            : assistantState === 'ERROR'
                            ? '#EF4444'
                            : '#64748B',
                      },
                    ]}
                  />
                  <Text style={styles.statusSubtitle}>
                    {assistantState === 'WAKE_WORD_LISTENING'
                      ? 'Listening for "Heyy SkillExa"...'
                      : assistantState === 'ACTIVATED'
                      ? "Hmm? I'm listening."
                      : assistantState === 'USER_LISTENING'
                      ? "I'm listening..."
                      : assistantState === 'PROCESSING'
                      ? 'Thinking...'
                      : assistantState === 'AI_SPEAKING'
                      ? 'Speaking...'
                      : assistantState === 'INITIALIZING'
                      ? 'Initializing microphone...'
                      : assistantState === 'PAUSED'
                      ? 'Voice assistant paused.'
                      : assistantState === 'ERROR'
                      ? 'Microphone blocked (tap to allow)'
                      : 'Ready'}
                  </Text>
                </View>
              </View>
            </View>

            <View style={styles.headerRight}>
              {/* New Chat button */}
              <TouchableOpacity
                style={styles.newChatHeaderBtn}
                onPress={handleNewChat}
                accessibilityLabel="New Chat"
              >
                <Feather name="plus" size={15} color="#A78BFA" />
                <Text style={styles.newChatHeaderText}>New</Text>
              </TouchableOpacity>

              {/* Stop button if active */}
              {(assistantState === 'AI_SPEAKING' ||
                assistantState === 'USER_LISTENING' ||
                assistantState === 'WAKE_WORD_LISTENING') && (
                <TouchableOpacity
                  style={styles.stopIconBtn}
                  onPress={handleStopAll}
                  accessibilityLabel="Stop SkillExa"
                >
                  <Feather name="square" size={14} color="#EF4444" />
                </TouchableOpacity>
              )}

              {/* Minimize/Close */}
              <TouchableOpacity style={styles.closeBtn} onPress={() => setIsOpen(false)}>
                <Feather name="x" size={20} color="#94A3B8" />
              </TouchableOpacity>
            </View>
          </LinearGradient>

          {/* Project & Mode Control Bar */}
          <View style={styles.controlBar}>
            {/* Project Selector Dropdown Button */}
            <TouchableOpacity
              style={styles.projectPill}
              onPress={() => {
                setShowProjectDropdown(!showProjectDropdown);
                setShowModeDropdown(false);
              }}
            >
              <Feather name="folder" size={13} color="#4F46E5" />
              <Text style={styles.projectPillText} numberOfLines={1}>
                {activeProject?.name || 'General Chats'}
              </Text>
              <Feather name="chevron-down" size={13} color="#64748B" />
            </TouchableOpacity>

            {/* Mode Selector Pill */}
            <TouchableOpacity
              style={styles.modePill}
              onPress={() => {
                setShowModeDropdown(!showModeDropdown);
                setShowProjectDropdown(false);
              }}
            >
              <Feather
                name={
                  assistantMode === 'WAKE_WORD'
                    ? 'radio'
                    : assistantMode === 'CONTINUOUS'
                    ? 'repeat'
                    : 'mic'
                }
                size={12}
                color="#059669"
              />
              <Text style={styles.modePillText}>
                {assistantMode === 'WAKE_WORD'
                  ? 'Wake Word'
                  : assistantMode === 'CONTINUOUS'
                  ? 'Continuous'
                  : 'Push-to-Talk'}
              </Text>
              <Feather name="chevron-down" size={12} color="#64748B" />
            </TouchableOpacity>

            {/* Memory toggle */}
            <TouchableOpacity
              style={[styles.iconPill, showMemoryBanner && styles.iconPillActive]}
              onPress={() => setShowMemoryBanner(!showMemoryBanner)}
              accessibilityLabel="Project Memory"
            >
              <Feather name="cpu" size={13} color={showMemoryBanner ? '#4F46E5' : '#64748B'} />
            </TouchableOpacity>
          </View>

          {/* PROJECT SELECTION DROPDOWN MENU */}
          {showProjectDropdown && (
            <View style={styles.dropdownMenu}>
              <View style={styles.dropdownHeader}>
                <Text style={styles.dropdownTitle}>SkillExa AI Projects</Text>
                <TouchableOpacity
                  style={styles.newProjectBtn}
                  onPress={() => {
                    setShowProjectDropdown(false);
                    setShowNewProjectModal(true);
                  }}
                >
                  <Feather name="plus" size={14} color="#4F46E5" />
                  <Text style={styles.newProjectText}>New Project</Text>
                </TouchableOpacity>
              </View>

              <ScrollView style={styles.dropdownScroll}>
                {projects.map((proj) => (
                  <TouchableOpacity
                    key={proj.id}
                    style={[
                      styles.dropdownItem,
                      proj.id === activeProjectId && styles.dropdownItemActive,
                    ]}
                    onPress={() => {
                      setActiveProjectId(proj.id);
                      setShowProjectDropdown(false);
                      setStatusNotice(`Switched to project: ${proj.name}`);
                    }}
                  >
                    <Feather
                      name={proj.id === activeProjectId ? 'check-circle' : 'folder'}
                      size={14}
                      color={proj.id === activeProjectId ? '#4F46E5' : '#64748B'}
                    />
                    <View style={styles.itemTextCol}>
                      <Text
                        style={[
                          styles.itemName,
                          proj.id === activeProjectId && styles.itemNameActive,
                        ]}
                      >
                        {proj.name}
                      </Text>
                      {proj.description ? (
                        <Text style={styles.itemDesc} numberOfLines={1}>
                          {proj.description}
                        </Text>
                      ) : null}
                    </View>
                    <Text style={styles.itemBadge}>{proj.conversation_count || 0}</Text>
                  </TouchableOpacity>
                ))}
              </ScrollView>
            </View>
          )}

          {/* MODE SELECTION DROPDOWN MENU */}
          {showModeDropdown && (
            <View style={styles.dropdownMenu}>
              <Text style={styles.dropdownTitle}>Listening & Speaking Mode</Text>

              <TouchableOpacity
                style={[
                  styles.dropdownItem,
                  assistantMode === 'WAKE_WORD' && styles.dropdownItemActive,
                ]}
                onPress={() => handleModeChange('WAKE_WORD')}
              >
                <Feather name="radio" size={16} color="#4F46E5" />
                <View style={styles.itemTextCol}>
                  <Text style={styles.itemName}>A. Wake Word Mode ("Hello SkillExa")</Text>
                  <Text style={styles.itemDesc}>
                    Listens on-device for "Hello SkillExa", acknowledges, then answers.
                  </Text>
                </View>
              </TouchableOpacity>

              <TouchableOpacity
                style={[
                  styles.dropdownItem,
                  assistantMode === 'PUSH_TO_TALK' && styles.dropdownItemActive,
                ]}
                onPress={() => handleModeChange('PUSH_TO_TALK')}
              >
                <Feather name="mic" size={16} color="#059669" />
                <View style={styles.itemTextCol}>
                  <Text style={styles.itemName}>B. Push-to-Talk Mode</Text>
                  <Text style={styles.itemDesc}>
                    Click mic to record your question, click stop to process & answer.
                  </Text>
                </View>
              </TouchableOpacity>

              <TouchableOpacity
                style={[
                  styles.dropdownItem,
                  assistantMode === 'CONTINUOUS' && styles.dropdownItemActive,
                ]}
                onPress={() => handleModeChange('CONTINUOUS')}
              >
                <Feather name="repeat" size={16} color="#8B5CF6" />
                <View style={styles.itemTextCol}>
                  <Text style={styles.itemName}>C. Continuous Conversation Mode</Text>
                  <Text style={styles.itemDesc}>
                    Natural back-and-forth dialogue without clicking mic each time. Supports
                    barge-in interruption.
                  </Text>
                </View>
              </TouchableOpacity>
            </View>
          )}

          {/* Project Memory Summary Banner */}
          {showMemoryBanner && (
            <View style={styles.memoryBanner}>
              <View style={styles.memoryHeader}>
                <Feather name="cpu" size={14} color="#4F46E5" />
                <Text style={styles.memoryTitle}>
                  Project Memory: {activeProject?.name}
                </Text>
              </View>
              <Text style={styles.memoryText}>
                {projectMemory ||
                  'No previous memory recorded yet for this project. As you discuss topics, key concepts are preserved here.'}
              </Text>
            </View>
          )}

          {/* Status / Ack Toast */}
          {statusNotice && (
            <View style={styles.noticeBar}>
              <Feather name="info" size={12} color="#4F46E5" />
              <Text style={styles.noticeText} numberOfLines={1}>
                {statusNotice}
              </Text>
              <TouchableOpacity onPress={() => setStatusNotice(null)}>
                <Feather name="x" size={12} color="#64748B" />
              </TouchableOpacity>
            </View>
          )}

          {/* Wake Word Start / Mic Permission Trigger Card */}
          {assistantMode === 'WAKE_WORD' && assistantState === 'IDLE' && (
            <View style={styles.wakeActivationBanner}>
              <View style={styles.wakeActivationIconWrap}>
                <Feather name="mic" size={16} color="#4F46E5" />
              </View>
              <View style={{ flex: 1 }}>
                <Text style={styles.wakeActivationTitle}>Voice Assistant Ready</Text>
                <Text style={styles.wakeActivationSubtitle}>
                  Tap below to allow microphone and start listening for "Hey SkillExa" or "Hello SkillExa".
                </Text>
              </View>
              <TouchableOpacity
                style={styles.wakeActivationBtn}
                onPress={() => activateVoiceAssistant(false)}
              >
                <Text style={styles.wakeActivationBtnText}>Start Listening</Text>
              </TouchableOpacity>
            </View>
          )}

          {/* Message List */}
          <ScrollView
            ref={scrollViewRef}
            style={styles.messageScroll}
            contentContainerStyle={styles.messageContainer}
            onContentSizeChange={() => {
              scrollViewRef.current?.scrollToEnd({ animated: false });
            }}
            onLayout={() => {
              scrollViewRef.current?.scrollToEnd({ animated: false });
            }}
          >
            {messages.length === 0 ? (
              <View style={styles.emptyContainer}>
                <LinearGradient
                  colors={['#EEF2FF', '#E0E7FF']}
                  style={styles.emptyIconCircle}
                >
                  <MaterialCommunityIcons name="brain" size={36} color="#4F46E5" />
                </LinearGradient>
                <Text style={styles.emptyTitle}>
                  SkillExa AI Learning Companion
                </Text>
                <Text style={styles.emptySubtitle}>
                  Ask anything in {activeProject?.name || 'General Chats'}: Programming (Python, C,
                  DSA), ECE Engineering, Placement Aptitude, or Govt Exams (GATE, SSC, UPSC).
                </Text>

                <View style={styles.suggestChips}>
                  <TouchableOpacity
                    style={styles.chip}
                    onPress={() => sendChatMessage('Explain pointers in C')}
                  >
                    <Text style={styles.chipText}>Explain pointers in C</Text>
                  </TouchableOpacity>
                  <TouchableOpacity
                    style={styles.chip}
                    onPress={() => sendChatMessage('Explain Python inheritance')}
                  >
                    <Text style={styles.chipText}>Python inheritance</Text>
                  </TouchableOpacity>
                  <TouchableOpacity
                    style={styles.chip}
                    onPress={() => sendChatMessage('What did we discuss last time?')}
                  >
                    <Text style={styles.chipText}>What did we learn last time?</Text>
                  </TouchableOpacity>
                  <TouchableOpacity
                    style={styles.chip}
                    onPress={() => {
                      setSearchEnabled(true);
                      sendChatMessage('Find the latest GATE ECE updates');
                    }}
                  >
                    <Text style={styles.chipText}>Find latest GATE ECE updates</Text>
                  </TouchableOpacity>
                </View>
              </View>
            ) : (
              messages.map((msg) => (
                <View
                  key={msg.id}
                  style={[
                    styles.messageRow,
                    msg.sender_type === 'user' ? styles.userRow : styles.asstRow,
                  ]}
                >
                  <View
                    style={[
                      styles.messageBubble,
                      msg.sender_type === 'user' ? styles.userBubble : styles.asstBubble,
                    ]}
                  >
                    {/* Header info */}
                    <View style={styles.msgHeaderRow}>
                      <Text style={styles.msgAuthor}>
                        {msg.sender_type === 'user' ? 'You' : 'SkillExa AI'}
                      </Text>
                      {msg.input_type === 'voice' && (
                        <View style={styles.voiceBadge}>
                          <Feather name="mic" size={10} color="#059669" />
                          <Text style={styles.voiceBadgeText}>Voice</Text>
                        </View>
                      )}
                    </View>

                    {/* Attached image preview */}
                    {msg.file_data && msg.file_data.startsWith('data:image') && (
                      <Image
                        source={{ uri: msg.file_data }}
                        style={styles.messageImageThumbnail}
                        resizeMode="cover"
                      />
                    )}

                    {/* Attached document badge */}
                    {msg.file_name && !msg.file_data?.startsWith('data:image') && (
                      <View style={styles.messageFileChip}>
                        <Feather name="file-text" size={13} color="#8B5CF6" />
                        <Text style={styles.messageFileName} numberOfLines={1}>
                          {msg.file_name}
                        </Text>
                      </View>
                    )}

                    {/* Content with Markdown Rendering */}
                    <MarkdownRenderer
                      content={msg.message_text}
                      isUser={msg.sender_type === 'user'}
                    />

                    {/* Educational Citations if present */}
                    {msg.search_sources && msg.search_sources.length > 0 && (
                      <View style={styles.sourcesContainer}>
                        <Text style={styles.sourcesTitle}>Verified Educational Sources:</Text>
                        {msg.search_sources.map((src, idx) => (
                          <TouchableOpacity
                            key={idx}
                            style={styles.sourceItem}
                            onPress={() => Linking.openURL(src.url)}
                          >
                            <Feather name="external-link" size={12} color="#4F46E5" />
                            <Text style={styles.sourceText} numberOfLines={1}>
                              {src.title} ({src.source || 'Official'})
                            </Text>
                          </TouchableOpacity>
                        ))}
                      </View>
                    )}

                    {/* Replay audio button for assistant message */}
                    {msg.sender_type === 'assistant' && (
                      <TouchableOpacity
                        style={styles.replayBtn}
                        onPress={() => handleReplayMessage(msg.message_text)}
                      >
                        <Feather name="volume-2" size={12} color="#64748B" />
                        <Text style={styles.replayText}>Listen</Text>
                      </TouchableOpacity>
                    )}
                  </View>
                </View>
              ))
            )}

            {/* Live Interim Transcript */}
            {interimSpeech ? (
              <View style={styles.interimBubble}>
                <Feather name="mic" size={12} color="#10B981" />
                <Text style={styles.interimText}>Listening: "{interimSpeech}"</Text>
              </View>
            ) : null}

            {/* Speaking Waveform Indicator */}
            {assistantState === 'AI_SPEAKING' && (
              <View style={styles.speakingIndicator}>
                <View style={styles.waveRowSmall}>
                  <Animated.View style={[styles.waveBarSmall, { transform: [{ scaleY: waveAnim1 }] }]} />
                  <Animated.View style={[styles.waveBarSmall, { transform: [{ scaleY: waveAnim2 }] }]} />
                  <Animated.View style={[styles.waveBarSmall, { transform: [{ scaleY: waveAnim3 }] }]} />
                </View>
                <Text style={styles.speakingText}>SkillExa AI is speaking...</Text>
              </View>
            )}

            {assistantState === 'WAKE_WORD_LISTENING' && !interimSpeech && (
              <View style={styles.listeningNoticeRow}>
                <View style={styles.liveListeningDot} />
                <Text style={styles.listeningNoticeText}>
                  Listening for "Hey SkillExa"...
                </Text>
              </View>
            )}

            {assistantState === 'USER_LISTENING' && (
              <View style={styles.listeningNoticeRow}>
                <View style={[styles.liveListeningDot, { backgroundColor: '#10B981' }]} />
                <Text style={[styles.listeningNoticeText, { color: '#065F46' }]}>
                  {silenceCountdown > 0
                    ? `I'm listening... auto-sending in ${silenceCountdown}s (or tap send)`
                    : "I'm listening... Speak your question."}
                </Text>
              </View>
            )}

            {isSending && (
              <View style={styles.typingRow}>
                <ActivityIndicator size="small" color="#4F46E5" />
                <Text style={styles.typingText}>SkillExa AI is thinking...</Text>
              </View>
            )}
          </ScrollView>

          {/* Bottom Control & Input Bar */}
          <View style={styles.inputArea}>
            {/* Search Grounding Toggle & Silence Countdown Badge */}
            <View style={styles.toolBar}>
              <TouchableOpacity
                style={[styles.searchToggle, searchEnabled && styles.searchToggleActive]}
                onPress={() => setSearchEnabled(!searchEnabled)}
              >
                <Feather
                  name="globe"
                  size={12}
                  color={searchEnabled ? '#FFFFFF' : '#4F46E5'}
                />
                <Text
                  style={[
                    styles.searchToggleText,
                    searchEnabled && styles.searchToggleTextActive,
                  ]}
                >
                  {searchEnabled ? 'Web Search: ON' : 'Web Search: OFF'}
                </Text>
              </TouchableOpacity>

              {assistantState === 'USER_LISTENING' && silenceCountdown > 0 && (
                <View style={styles.countdownBadge}>
                  <Feather name="clock" size={11} color="#065F46" />
                  <Text style={styles.countdownBadgeText}>
                    Sending in {silenceCountdown}s
                  </Text>
                </View>
              )}

              {assistantState === 'AI_SPEAKING' && (
                <TouchableOpacity style={styles.stopTextBtn} onPress={handleStopAll}>
                  <Feather name="square" size={11} color="#EF4444" />
                  <Text style={styles.stopText}>Stop Speaking</Text>
                </TouchableOpacity>
              )}
            </View>

            {/* Attachment Preview Bar if file selected */}
            {attachedFile && (
              <View style={styles.attachmentBar}>
                <View style={styles.attachmentLeft}>
                  <Feather
                    name={attachedFile.mimeType.startsWith('image/') ? 'image' : 'file-text'}
                    size={14}
                    color="#8B5CF6"
                  />
                  <Text style={styles.attachmentText} numberOfLines={1}>
                    {attachedFile.name} ({(attachedFile.size / 1024).toFixed(1)} KB)
                  </Text>
                </View>
                <TouchableOpacity onPress={() => setAttachedFile(null)} style={styles.attachmentRemoveBtn}>
                  <Feather name="x" size={14} color="#EF4444" />
                </TouchableOpacity>
              </View>
            )}

            {/* Input Row with Paperclip, Mic & Send */}
            <View style={styles.inputRow}>
              {/* Paperclip File Upload Button */}
              <TouchableOpacity
                style={styles.attachBtn}
                onPress={handlePickFile}
                activeOpacity={0.8}
                accessibilityLabel="Attach Image or Code File"
              >
                <Feather name="paperclip" size={18} color="#64748B" />
              </TouchableOpacity>

              {/* Mic Action Button */}
              <TouchableOpacity
                style={[
                  styles.micBtn,
                  (assistantState === 'WAKE_WORD_LISTENING' || assistantState === 'USER_LISTENING') &&
                    styles.micBtnListening,
                  assistantState === 'AI_SPEAKING' && styles.micBtnSpeaking,
                ]}
                onPress={handleMicClick}
                activeOpacity={0.8}
              >
                <Feather
                  name={
                    assistantState === 'WAKE_WORD_LISTENING' || assistantState === 'USER_LISTENING'
                      ? 'mic-off'
                      : assistantState === 'AI_SPEAKING'
                      ? 'volume-x'
                      : 'mic'
                  }
                  size={18}
                  color="#FFFFFF"
                />
              </TouchableOpacity>

              {/* Text Input */}
              <TextInput
                style={styles.textInput}
                placeholder={
                  attachedFile
                    ? `Ask about ${attachedFile.name}...`
                    : assistantMode === 'WAKE_WORD'
                    ? 'Ask anything or say "Hey SkillExa"...'
                    : 'Ask anything in this project...'
                }
                placeholderTextColor="#94A3B8"
                value={inputText}
                onChangeText={setInputText}
                onSubmitEditing={() => sendChatMessage(inputText, 'text')}
                returnKeyType="send"
              />

              {/* Send Button */}
              <TouchableOpacity
                style={[
                  styles.sendBtn,
                  ((!inputText.trim() && !attachedFile) || isSending) && styles.sendBtnDisabled,
                ]}
                disabled={(!inputText.trim() && !attachedFile) || isSending}
                onPress={() => sendChatMessage(inputText, 'text')}
              >
                <Feather name="send" size={16} color="#FFFFFF" />
              </TouchableOpacity>
            </View>
          </View>
        </View>
      )}

      {/* ------------------------------------------------------------- */}
      {/* NEW PROJECT CREATION MODAL                                    */}
      {/* ------------------------------------------------------------- */}
      <Modal visible={showNewProjectModal} transparent animationType="fade">
        <View style={styles.modalOverlay}>
          <View style={styles.modalCard}>
            <View style={styles.modalHeader}>
              <Text style={styles.modalTitle}>Create New AI Project</Text>
              <TouchableOpacity onPress={() => setShowNewProjectModal(false)}>
                <Feather name="x" size={18} color="#64748B" />
              </TouchableOpacity>
            </View>

            <Text style={styles.inputLabel}>Project Name *</Text>
            <TextInput
              style={styles.modalInput}
              placeholder="e.g. Python Learning, Final Year Project, GATE ECE"
              placeholderTextColor="#94A3B8"
              value={newProjectName}
              onChangeText={setNewProjectName}
            />

            <Text style={styles.inputLabel}>Description (Optional)</Text>
            <TextInput
              style={[styles.modalInput, { height: 70 }]}
              placeholder="e.g. Focused preparation for algorithms, coding rounds, and viva"
              placeholderTextColor="#94A3B8"
              value={newProjectDesc}
              onChangeText={setNewProjectDesc}
              multiline
            />

            <View style={styles.modalActions}>
              <TouchableOpacity
                style={styles.modalCancelBtn}
                onPress={() => setShowNewProjectModal(false)}
              >
                <Text style={styles.modalCancelText}>Cancel</Text>
              </TouchableOpacity>
              <TouchableOpacity
                style={[
                  styles.modalConfirmBtn,
                  !newProjectName.trim() && styles.modalBtnDisabled,
                ]}
                disabled={!newProjectName.trim()}
                onPress={handleCreateProject}
              >
                <Text style={styles.modalConfirmText}>Create Project</Text>
              </TouchableOpacity>
            </View>
          </View>
        </View>
      </Modal>
    </>
  );
}

const styles = StyleSheet.create({
  // Floating Action Button
  floatingContainer: {
    position: (Platform.OS === 'web' ? 'fixed' : 'absolute') as any,
    bottom: 24,
    right: 24,
    zIndex: 99999,
    flexDirection: 'row',
    alignItems: 'center',
    gap: 10,
  },
  floatingButton: {
    width: 58,
    height: 58,
    borderRadius: 29,
    overflow: 'hidden',
    shadowColor: '#4F46E5',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.35,
    shadowRadius: 10,
    elevation: 8,
  },
  floatingButtonListening: {
    shadowColor: '#10B981',
    shadowOpacity: 0.5,
  },
  floatingButtonSpeaking: {
    shadowColor: '#8B5CF6',
    shadowOpacity: 0.5,
  },
  floatingButtonError: {
    shadowColor: '#EF4444',
  },
  floatingGradient: {
    width: '100%',
    height: '100%',
    justifyContent: 'center',
    alignItems: 'center',
  },
  wakePill: {
    backgroundColor: '#FFFFFF',
    paddingHorizontal: 12,
    paddingVertical: 7,
    borderRadius: 20,
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.08,
    shadowRadius: 5,
    elevation: 3,
  },
  wakePillText: {
    fontSize: 12,
    fontWeight: '600',
    color: '#1E293B',
  },

  // Floating Chat Panel
  panelContainer: {
    position: (Platform.OS === 'web' ? 'fixed' : 'absolute') as any,
    bottom: 92,
    right: 24,
    width: Platform.OS === 'web' ? 440 : '92%',
    height: 600,
    maxHeight: '80%',
    backgroundColor: '#FFFFFF',
    borderRadius: 18,
    overflow: 'hidden',
    zIndex: 99998,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 10 },
    shadowOpacity: 0.18,
    shadowRadius: 24,
    elevation: 12,
    display: 'flex',
    flexDirection: 'column',
  },
  panelHeader: {
    paddingHorizontal: 16,
    paddingVertical: 14,
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  headerLeft: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 10,
  },
  brandIconWrap: {
    width: 32,
    height: 32,
    borderRadius: 16,
    backgroundColor: 'rgba(139, 92, 246, 0.18)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  brandTitle: {
    fontSize: 15,
    fontWeight: '700',
    color: '#FFFFFF',
  },
  statusRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 5,
    marginTop: 1,
  },
  statusDot: {
    width: 6,
    height: 6,
    borderRadius: 3,
  },
  statusSubtitle: {
    fontSize: 11,
    color: '#94A3B8',
  },
  headerRight: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  newChatHeaderBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: 'rgba(139, 92, 246, 0.2)',
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: 6,
    gap: 4,
  },
  newChatHeaderText: {
    color: '#DDD6FE',
    fontSize: 12,
    fontWeight: '600',
  },
  stopIconBtn: {
    backgroundColor: 'rgba(239, 68, 68, 0.15)',
    padding: 6,
    borderRadius: 8,
  },
  closeBtn: {
    padding: 4,
  },

  // Control Bar
  controlBar: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingHorizontal: 12,
    paddingVertical: 8,
    backgroundColor: '#F8FAFC',
    borderBottomWidth: 1,
    borderBottomColor: '#E2E8F0',
    gap: 8,
  },
  projectPill: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    backgroundColor: '#FFFFFF',
    borderWidth: 1,
    borderColor: '#CBD5E1',
    borderRadius: 8,
    paddingHorizontal: 10,
    paddingVertical: 6,
  },
  projectPillText: {
    flex: 1,
    fontSize: 12,
    fontWeight: '600',
    color: '#1E293B',
  },
  modePill: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
    backgroundColor: '#ECFDF5',
    borderWidth: 1,
    borderColor: '#A7F3D0',
    borderRadius: 8,
    paddingHorizontal: 8,
    paddingVertical: 6,
  },
  modePillText: {
    fontSize: 11,
    fontWeight: '600',
    color: '#065F46',
  },
  iconPill: {
    backgroundColor: '#FFFFFF',
    borderWidth: 1,
    borderColor: '#CBD5E1',
    borderRadius: 8,
    padding: 6,
  },
  iconPillActive: {
    backgroundColor: '#EEF2FF',
    borderColor: '#4F46E5',
  },

  // Dropdown Menus
  dropdownMenu: {
    backgroundColor: '#FFFFFF',
    borderBottomWidth: 1,
    borderBottomColor: '#E2E8F0',
    padding: 12,
    maxHeight: 250,
  },
  dropdownHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 8,
  },
  dropdownTitle: {
    fontSize: 12,
    fontWeight: '700',
    color: '#64748B',
    textTransform: 'uppercase',
  },
  newProjectBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
  },
  newProjectText: {
    fontSize: 12,
    fontWeight: '600',
    color: '#4F46E5',
  },
  dropdownScroll: {
    maxHeight: 180,
  },
  dropdownItem: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 10,
    paddingVertical: 8,
    paddingHorizontal: 8,
    borderRadius: 8,
    marginBottom: 4,
  },
  dropdownItemActive: {
    backgroundColor: '#EEF2FF',
  },
  itemTextCol: {
    flex: 1,
  },
  itemName: {
    fontSize: 13,
    fontWeight: '600',
    color: '#1E293B',
  },
  itemNameActive: {
    color: '#4F46E5',
  },
  itemDesc: {
    fontSize: 11,
    color: '#64748B',
  },
  itemBadge: {
    fontSize: 11,
    fontWeight: '600',
    color: '#64748B',
    backgroundColor: '#F1F5F9',
    paddingHorizontal: 6,
    paddingVertical: 2,
    borderRadius: 6,
  },

  // Memory Banner
  memoryBanner: {
    backgroundColor: '#F0FDF4',
    borderBottomWidth: 1,
    borderBottomColor: '#DCFCE7',
    padding: 10,
  },
  memoryHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    marginBottom: 4,
  },
  memoryTitle: {
    fontSize: 11,
    fontWeight: '700',
    color: '#166534',
    textTransform: 'uppercase',
  },
  memoryText: {
    fontSize: 12,
    color: '#14532D',
    lineHeight: 16,
  },

  // Notice Bar
  noticeBar: {
    backgroundColor: '#EFF6FF',
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderBottomWidth: 1,
    borderBottomColor: '#DBEAFE',
  },
  noticeText: {
    flex: 1,
    fontSize: 11,
    color: '#1E40AF',
  },

  // Message Area
  messageScroll: {
    flex: 1,
    backgroundColor: '#F8FAFC',
  },
  messageContainer: {
    padding: 14,
    gap: 12,
  },
  emptyContainer: {
    alignItems: 'center',
    paddingVertical: 32,
    paddingHorizontal: 16,
  },
  emptyIconCircle: {
    width: 64,
    height: 64,
    borderRadius: 32,
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 12,
  },
  emptyTitle: {
    fontSize: 16,
    fontWeight: '700',
    color: '#1E293B',
    marginBottom: 6,
    textAlign: 'center',
  },
  emptySubtitle: {
    fontSize: 12,
    color: '#64748B',
    textAlign: 'center',
    lineHeight: 18,
    marginBottom: 16,
  },
  suggestChips: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 8,
    justifyContent: 'center',
  },
  chip: {
    backgroundColor: '#FFFFFF',
    borderWidth: 1,
    borderColor: '#CBD5E1',
    borderRadius: 16,
    paddingHorizontal: 12,
    paddingVertical: 7,
  },
  chipText: {
    fontSize: 11,
    fontWeight: '600',
    color: '#4F46E5',
  },

  // Messages
  messageRow: {
    flexDirection: 'row',
    marginBottom: 8,
  },
  userRow: {
    justifyContent: 'flex-end',
  },
  asstRow: {
    justifyContent: 'flex-start',
  },
  messageBubble: {
    maxWidth: '85%',
    borderRadius: 14,
    padding: 12,
  },
  userBubble: {
    backgroundColor: '#4F46E5',
    borderBottomRightRadius: 4,
  },
  asstBubble: {
    backgroundColor: '#FFFFFF',
    borderBottomLeftRadius: 4,
    borderWidth: 1,
    borderColor: '#E2E8F0',
  },
  msgHeaderRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 4,
  },
  msgAuthor: {
    fontSize: 11,
    fontWeight: '700',
    color: '#94A3B8',
  },
  voiceBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 3,
    backgroundColor: '#ECFDF5',
    paddingHorizontal: 5,
    paddingVertical: 1,
    borderRadius: 6,
  },
  voiceBadgeText: {
    fontSize: 9,
    color: '#059669',
    fontWeight: '700',
  },
  msgText: {
    fontSize: 13,
    lineHeight: 19,
  },
  userText: {
    color: '#FFFFFF',
  },
  asText: {
    color: '#1E293B',
  },

  // Sources
  sourcesContainer: {
    marginTop: 8,
    paddingTop: 8,
    borderTopWidth: 1,
    borderTopColor: '#F1F5F9',
    gap: 4,
  },
  sourcesTitle: {
    fontSize: 11,
    fontWeight: '700',
    color: '#64748B',
    marginBottom: 2,
  },
  sourceItem: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    backgroundColor: '#F8FAFC',
    padding: 5,
    borderRadius: 6,
    borderWidth: 1,
    borderColor: '#E2E8F0',
  },
  sourceText: {
    fontSize: 11,
    color: '#4F46E5',
    fontWeight: '600',
    flex: 1,
  },
  replayBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
    marginTop: 8,
    alignSelf: 'flex-start',
  },
  replayText: {
    fontSize: 11,
    color: '#64748B',
    fontWeight: '600',
  },

  // Live Speech & Typing
  interimBubble: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    backgroundColor: '#ECFDF5',
    borderWidth: 1,
    borderColor: '#A7F3D0',
    borderRadius: 12,
    padding: 8,
    alignSelf: 'flex-start',
  },
  interimText: {
    fontSize: 12,
    color: '#065F46',
    fontStyle: 'italic',
  },
  speakingIndicator: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    backgroundColor: '#F5F3FF',
    borderWidth: 1,
    borderColor: '#DDD6FE',
    borderRadius: 12,
    padding: 8,
    alignSelf: 'flex-start',
  },
  speakingText: {
    fontSize: 11,
    color: '#6D28D9',
    fontWeight: '600',
  },
  listeningNoticeRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    backgroundColor: '#ECFDF5',
    borderWidth: 1,
    borderColor: '#A7F3D0',
    borderRadius: 10,
    paddingHorizontal: 10,
    paddingVertical: 6,
    alignSelf: 'flex-start',
  },
  listeningNoticeText: {
    fontSize: 11,
    fontWeight: '600',
    color: '#065F46',
  },
  liveListeningDot: {
    width: 8,
    height: 8,
    borderRadius: 4,
    backgroundColor: '#10B981',
  },
  wakeActivationBanner: {
    backgroundColor: '#EEF2FF',
    borderBottomWidth: 1,
    borderBottomColor: '#C7D2FE',
    padding: 12,
    flexDirection: 'row',
    alignItems: 'center',
    gap: 10,
  },
  wakeActivationIconWrap: {
    width: 32,
    height: 32,
    borderRadius: 16,
    backgroundColor: '#E0E7FF',
    justifyContent: 'center',
    alignItems: 'center',
  },
  wakeActivationTitle: {
    fontSize: 13,
    fontWeight: '700',
    color: '#312E81',
  },
  wakeActivationSubtitle: {
    fontSize: 11,
    color: '#4338CA',
    marginTop: 1,
  },
  wakeActivationBtn: {
    backgroundColor: '#4F46E5',
    paddingHorizontal: 12,
    paddingVertical: 7,
    borderRadius: 8,
  },
  wakeActivationBtnText: {
    fontSize: 11,
    fontWeight: '700',
    color: '#FFFFFF',
  },
  typingRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    padding: 8,
  },
  typingText: {
    fontSize: 12,
    color: '#64748B',
  },

  // Audio Waveform
  waveRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 3,
    height: 20,
  },
  waveBar: {
    width: 3.5,
    height: 18,
    backgroundColor: '#FFFFFF',
    borderRadius: 2,
  },
  waveRowSmall: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 2,
    height: 14,
  },
  waveBarSmall: {
    width: 2.5,
    height: 12,
    backgroundColor: '#8B5CF6',
    borderRadius: 2,
  },

  // Bottom Input Area
  inputArea: {
    backgroundColor: '#FFFFFF',
    borderTopWidth: 1,
    borderTopColor: '#E2E8F0',
    padding: 10,
  },
  toolBar: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 8,
  },
  searchToggle: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
    backgroundColor: '#EEF2FF',
    borderWidth: 1,
    borderColor: '#C7D2FE',
    borderRadius: 12,
    paddingHorizontal: 8,
    paddingVertical: 3,
  },
  searchToggleActive: {
    backgroundColor: '#4F46E5',
    borderColor: '#4F46E5',
  },
  searchToggleText: {
    fontSize: 10,
    fontWeight: '700',
    color: '#4F46E5',
  },
  searchToggleTextActive: {
    color: '#FFFFFF',
  },
  countdownBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
    backgroundColor: '#ECFDF5',
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 12,
    borderWidth: 1,
    borderColor: '#A7F3D0',
  },
  countdownBadgeText: {
    fontSize: 11,
    fontWeight: '700',
    color: '#065F46',
  },
  stopTextBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
  },
  stopText: {
    fontSize: 11,
    fontWeight: '600',
    color: '#EF4444',
  },
  inputRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  attachmentBar: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    backgroundColor: '#F3E8FF',
    borderRadius: 8,
    paddingHorizontal: 10,
    paddingVertical: 6,
    marginBottom: 8,
    borderWidth: 1,
    borderColor: '#DDD6FE',
  },
  attachmentLeft: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    flex: 1,
  },
  attachmentText: {
    fontSize: 12,
    color: '#6B21A8',
    fontWeight: '600',
    flex: 1,
  },
  attachmentRemoveBtn: {
    padding: 2,
    marginLeft: 6,
  },
  attachBtn: {
    width: 36,
    height: 38,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F1F5F9',
    borderRadius: 18,
    borderWidth: 1,
    borderColor: '#E2E8F0',
  },
  messageImageThumbnail: {
    width: '100%',
    height: 160,
    borderRadius: 8,
    marginTop: 6,
    marginBottom: 6,
  },
  messageFileChip: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    backgroundColor: 'rgba(255, 255, 255, 0.2)',
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: 6,
    marginTop: 4,
    marginBottom: 4,
  },
  messageFileName: {
    fontSize: 11,
    color: '#FFFFFF',
    fontWeight: '600',
    flex: 1,
  },
  micBtn: {
    width: 38,
    height: 38,
    borderRadius: 19,
    backgroundColor: '#4F46E5',
    justifyContent: 'center',
    alignItems: 'center',
  },
  micBtnListening: {
    backgroundColor: '#10B981',
  },
  micBtnSpeaking: {
    backgroundColor: '#8B5CF6',
  },
  textInput: {
    flex: 1,
    height: 38,
    backgroundColor: '#F8FAFC',
    borderRadius: 19,
    paddingHorizontal: 14,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    fontSize: 13,
    color: '#1E293B',
  },
  sendBtn: {
    width: 38,
    height: 38,
    borderRadius: 19,
    backgroundColor: '#4F46E5',
    justifyContent: 'center',
    alignItems: 'center',
  },
  sendBtnDisabled: {
    backgroundColor: '#CBD5E1',
  },

  // Modal
  modalOverlay: {
    flex: 1,
    backgroundColor: 'rgba(0, 0, 0, 0.5)',
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  modalCard: {
    width: '100%',
    maxWidth: 400,
    backgroundColor: '#FFFFFF',
    borderRadius: 16,
    padding: 20,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 6 },
    shadowOpacity: 0.15,
    shadowRadius: 16,
    elevation: 10,
  },
  modalHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 16,
  },
  modalTitle: {
    fontSize: 16,
    fontWeight: '700',
    color: '#1E293B',
  },
  inputLabel: {
    fontSize: 12,
    fontWeight: '600',
    color: '#475569',
    marginBottom: 6,
  },
  modalInput: {
    backgroundColor: '#F8FAFC',
    borderWidth: 1,
    borderColor: '#CBD5E1',
    borderRadius: 8,
    paddingHorizontal: 12,
    paddingVertical: 10,
    fontSize: 13,
    color: '#1E293B',
    marginBottom: 14,
  },
  modalActions: {
    flexDirection: 'row',
    justifyContent: 'flex-end',
    gap: 10,
    marginTop: 6,
  },
  modalCancelBtn: {
    paddingHorizontal: 14,
    paddingVertical: 8,
    borderRadius: 8,
    borderWidth: 1,
    borderColor: '#CBD5E1',
  },
  modalCancelText: {
    fontSize: 13,
    color: '#64748B',
    fontWeight: '600',
  },
  modalConfirmBtn: {
    backgroundColor: '#4F46E5',
    paddingHorizontal: 16,
    paddingVertical: 8,
    borderRadius: 8,
  },
  modalConfirmText: {
    fontSize: 13,
    color: '#FFFFFF',
    fontWeight: '600',
  },
  modalBtnDisabled: {
    backgroundColor: '#A5B4FC',
  },
});
