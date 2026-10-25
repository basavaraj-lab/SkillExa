import { Feather } from '@expo/vector-icons';
import React, { useEffect, useRef, useState } from 'react';
import {
  ActivityIndicator,
  Modal,
  Platform,
  ScrollView,
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  View,
} from 'react-native';
import { Palette, Radii, Shadows } from '../../constants/theme';
import { ApiClient, getApiBaseUrl, getAuthToken } from '../../services/api';

export interface SkillExaLiveMeetingRoomProps {
  roomId: string;
  secureRoomId: string;
  bookingId: string;
  currentUserId: string;
  currentUserName: string;
  currentUserRole: 'teacher' | 'student' | 'admin';
  otherParticipantName: string;
  otherParticipantRole: 'teacher' | 'student';
  interviewTitle: string;
  category: string;
  iceServers?: any[];
  initialIsWaiting?: boolean;
  onLeaveMeeting: () => void;
  onOpenFeedback?: () => void;
}

interface ChatMessage {
  id?: string;
  sender_id: string;
  sender_name: string;
  sender_role: string;
  message: string;
  timestamp: string;
}

export const SkillExaLiveMeetingRoom: React.FC<SkillExaLiveMeetingRoomProps> = ({
  roomId,
  secureRoomId,
  bookingId,
  currentUserId,
  currentUserName,
  currentUserRole,
  otherParticipantName,
  otherParticipantRole,
  interviewTitle,
  category,
  iceServers = [
    { urls: 'stun:stun.l.google.com:19302' },
    { urls: 'stun:stun1.l.google.com:19302' },
  ],
  initialIsWaiting = false,
  onLeaveMeeting,
  onOpenFeedback,
}) => {
  // State
  const [micOn, setMicOn] = useState(true);
  const [camOn, setCamOn] = useState(true);
  const [isScreenSharing, setIsScreenSharing] = useState(false);
  const [connectionStatus, setConnectionStatus] = useState<
    'connecting' | 'connected' | 'reconnecting' | 'disconnected'
  >('connecting');
  const [isPeerConnected, setIsPeerConnected] = useState(false);
  const [meetingSeconds, setMeetingSeconds] = useState(0);

  // Waiting Room state (Student)
  const isTeacher = currentUserRole === 'teacher' || currentUserRole === 'admin';
  const [isWaiting, setIsWaiting] = useState(!isTeacher && initialIsWaiting);
  const [studentInWaitingRoom, setStudentInWaitingRoom] = useState(false);

  // Modals for confirmation
  const [showEndModal, setShowEndModal] = useState(false);
  const [showLeaveModal, setShowLeaveModal] = useState(false);
  const [showHostEndedModal, setShowHostEndedModal] = useState(false);
  const [copiedCodeNotice, setCopiedCodeNotice] = useState(false);
  const [isEndingCall, setIsEndingCall] = useState(false);

  // In-call drawers
  const [chatOpen, setChatOpen] = useState(false);
  const [participantsOpen, setParticipantsOpen] = useState(false);
  const [chatMessages, setChatMessages] = useState<ChatMessage[]>([]);
  const [chatInput, setChatInput] = useState('');
  const [unreadCount, setUnreadCount] = useState(0);

  // Peer presence
  const [peerMicOn, setPeerMicOn] = useState(true);
  const [peerCamOn, setPeerCamOn] = useState(true);
  const [peerIsSharingScreen, setPeerIsSharingScreen] = useState(false);

  // WebRTC & Stream Refs
  const localStreamRef = useRef<MediaStream | null>(null);
  const remoteStreamRef = useRef<MediaStream | null>(null);
  const peerConnectionRef = useRef<RTCPeerConnection | null>(null);
  const screenTrackRef = useRef<MediaStreamTrack | null>(null);
  const webSocketRef = useRef<WebSocket | null>(null);

  // Video element DOM container refs (web)
  const localVideoContainerRef = useRef<any>(null);
  const waitingVideoContainerRef = useRef<any>(null);
  const remoteVideoContainerRef = useRef<any>(null);

  // Meeting duration timer
  useEffect(() => {
    if (isWaiting) return;
    const timer = setInterval(() => {
      setMeetingSeconds((prev) => prev + 1);
    }, 1000);
    return () => clearInterval(timer);
  }, [isWaiting]);

  const formatTimer = (sec: number) => {
    const m = Math.floor(sec / 60);
    const s = sec % 60;
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  };

  const copyRoomCode = () => {
    if (typeof navigator !== 'undefined' && navigator.clipboard) {
      navigator.clipboard.writeText(secureRoomId);
      setCopiedCodeNotice(true);
      setTimeout(() => setCopiedCodeNotice(false), 2500);
    }
  };

  // -------------------------------------------------------------
  // Clean Stop Media Hardware Tracks
  // -------------------------------------------------------------
  const stopAllMediaTracks = () => {
    try {
      if (localStreamRef.current) {
        localStreamRef.current.getTracks().forEach((track) => {
          track.stop();
        });
        localStreamRef.current = null;
      }
      if (screenTrackRef.current) {
        screenTrackRef.current.stop();
        screenTrackRef.current = null;
      }
    } catch (e) {}
  };

  // -------------------------------------------------------------
  // Attach Local Video to DOM Container
  // -------------------------------------------------------------
  const attachLocalStreamToDom = (container: any, stream: MediaStream) => {
    if (!container) return;
    let videoEl = container.querySelector('video');
    if (!videoEl) {
      videoEl = document.createElement('video');
      videoEl.autoplay = true;
      videoEl.muted = true; // Mute local preview to prevent feedback loop
      videoEl.playsInline = true;
      videoEl.style.width = '100%';
      videoEl.style.height = '100%';
      videoEl.style.objectFit = 'cover';
      videoEl.style.borderRadius = '12px';
      videoEl.style.transform = 'scaleX(-1)'; // Mirror local camera
      container.appendChild(videoEl);
    }
    videoEl.srcObject = stream;
  };

  // -------------------------------------------------------------
  // Initialize Local Media Stream
  // -------------------------------------------------------------
  const initLocalMedia = async (): Promise<MediaStream | null> => {
    if (Platform.OS !== 'web' || typeof navigator === 'undefined' || !navigator.mediaDevices) {
      return null;
    }
    try {
      const stream = await navigator.mediaDevices.getUserMedia({
        video: { width: { ideal: 1280 }, height: { ideal: 720 }, frameRate: { ideal: 30 } },
        audio: { echoCancellation: true, noiseSuppression: true, autoGainControl: true },
      });
      localStreamRef.current = stream;

      // Attach to active video element
      if (localVideoContainerRef.current) {
        attachLocalStreamToDom(localVideoContainerRef.current, stream);
      }
      if (waitingVideoContainerRef.current) {
        attachLocalStreamToDom(waitingVideoContainerRef.current, stream);
      }
      return stream;
    } catch (err: any) {
      console.warn('Camera/Mic permission denied or not found:', err);
      return null;
    }
  };

  // -------------------------------------------------------------
  // Attach Remote Stream to Video DOM Element
  // -------------------------------------------------------------
  const attachRemoteStream = (stream: MediaStream) => {
    remoteStreamRef.current = stream;
    setIsPeerConnected(true);
    setConnectionStatus('connected');

    if (Platform.OS === 'web' && remoteVideoContainerRef.current) {
      let videoEl = remoteVideoContainerRef.current.querySelector('video');
      if (!videoEl) {
        videoEl = document.createElement('video');
        videoEl.autoplay = true;
        videoEl.playsInline = true;
        videoEl.style.width = '100%';
        videoEl.style.height = '100%';
        videoEl.style.objectFit = 'cover';
        videoEl.style.borderRadius = '12px';
        remoteVideoContainerRef.current.appendChild(videoEl);
      }
      videoEl.srcObject = stream;
    }
  };

  // -------------------------------------------------------------
  // WebRTC Peer Connection & Signaling Setup
  // -------------------------------------------------------------
  useEffect(() => {
    let isMounted = true;

    const setupCall = async () => {
      // 1. Fetch initial chat history
      try {
        const msgRes = await ApiClient.getLiveMeetingMessages(secureRoomId);
        if (isMounted && msgRes.success && msgRes.data) {
          const formatted: ChatMessage[] = msgRes.data.map((m: any) => ({
            id: m.id,
            sender_id: m.sender_id,
            sender_name: m.sender_name,
            sender_role: m.sender_role,
            message: m.message_content,
            timestamp: m.created_at,
          }));
          setChatMessages(formatted);
        }
      } catch (e) {}

      // 2. Start local camera/mic
      const localStream = await initLocalMedia();

      // 3. Create RTCPeerConnection
      if (Platform.OS === 'web' && typeof RTCPeerConnection !== 'undefined') {
        const pc = new RTCPeerConnection({ iceServers });
        peerConnectionRef.current = pc;

        // Add local tracks to peer connection
        if (localStream) {
          localStream.getTracks().forEach((track) => {
            pc.addTrack(track, localStream);
          });
        }

        // On remote track received
        pc.ontrack = (event) => {
          if (event.streams && event.streams[0]) {
            attachRemoteStream(event.streams[0]);
          }
        };

        // On ICE Candidate generated
        pc.onicecandidate = (event) => {
          if (
            event.candidate &&
            webSocketRef.current &&
            webSocketRef.current.readyState === WebSocket.OPEN
          ) {
            webSocketRef.current.send(
              JSON.stringify({
                type: 'ice-candidate',
                candidate: event.candidate,
              })
            );
          }
        };

        // ICE Connection state changes
        pc.oniceconnectionstatechange = () => {
          const state = pc.iceConnectionState;
          if (state === 'connected' || state === 'completed') {
            setConnectionStatus('connected');
            setIsPeerConnected(true);
          } else if (state === 'failed' || state === 'disconnected') {
            setConnectionStatus('reconnecting');
          } else if (state === 'closed') {
            setConnectionStatus('disconnected');
          }
        };

        // 4. Connect WebSocket Signaling
        const token = getAuthToken();
        const base = getApiBaseUrl();
        const wsProtocol = base.startsWith('https') ? 'wss:' : 'ws:';
        const wsHost = base.replace(/^https?:\/\//, '').replace(/\/api$/, '');
        const wsUrl = `${wsProtocol}//${wsHost}/api/live-interview/ws/${secureRoomId}?token=${encodeURIComponent(
          token || ''
        )}`;

        const ws = new WebSocket(wsUrl);
        webSocketRef.current = ws;

        ws.onopen = () => {
          setConnectionStatus('connecting');
        };

        ws.onmessage = async (event) => {
          try {
            const data = JSON.parse(event.data);

            if (data.type === 'room-joined') {
              if (data.peers && data.peers.length > 0) {
                // If not in waiting room, initiate WebRTC offer
                if (!isWaiting) {
                  setIsPeerConnected(true);
                  const offer = await pc.createOffer();
                  await pc.setLocalDescription(offer);
                  ws.send(JSON.stringify({ type: 'offer', sdp: offer }));
                }
              }
            } else if (data.type === 'peer-joined') {
              setIsPeerConnected(true);
              if (isTeacher && data.role === 'student') {
                // Inform faculty that student is present
                setStudentInWaitingRoom(true);
              }
            } else if (data.type === 'student-admitted') {
              // Student admitted by faculty!
              setIsWaiting(false);
              setStudentInWaitingRoom(false);
              // Initiate offer now that session is active
              try {
                const offer = await pc.createOffer();
                await pc.setLocalDescription(offer);
                ws.send(JSON.stringify({ type: 'offer', sdp: offer }));
              } catch (e) {}
            } else if (data.type === 'interview-ended') {
              // Faculty ended interview for everyone
              stopAllMediaTracks();
              setShowHostEndedModal(true);
            } else if (data.type === 'offer') {
              await pc.setRemoteDescription(new RTCSessionDescription(data.sdp));
              const answer = await pc.createAnswer();
              await pc.setLocalDescription(answer);
              ws.send(JSON.stringify({ type: 'answer', sdp: answer }));
            } else if (data.type === 'answer') {
              await pc.setRemoteDescription(new RTCSessionDescription(data.sdp));
            } else if (data.type === 'ice-candidate') {
              if (data.candidate) {
                try {
                  await pc.addIceCandidate(new RTCIceCandidate(data.candidate));
                } catch (e) {}
              }
            } else if (data.type === 'chat-message') {
              setChatMessages((prev) => [
                ...prev,
                {
                  id: data.id,
                  sender_id: data.sender_id,
                  sender_name: data.sender_name,
                  sender_role: data.sender_role,
                  message: data.message,
                  timestamp: data.timestamp || new Date().toISOString(),
                },
              ]);
              if (!chatOpen) {
                setUnreadCount((prev) => prev + 1);
              }
            } else if (data.type === 'media-state') {
              setPeerMicOn(data.mic_on);
              setPeerCamOn(data.cam_on);
            } else if (data.type === 'screen-share-status') {
              setPeerIsSharingScreen(data.is_sharing);
            } else if (data.type === 'peer-left') {
              setIsPeerConnected(false);
              setConnectionStatus('connecting');
            }
          } catch (e) {}
        };

        ws.onclose = () => {
          setConnectionStatus('disconnected');
        };
      }
    };

    setupCall();

    return () => {
      isMounted = false;
      stopAllMediaTracks();
      if (peerConnectionRef.current) {
        peerConnectionRef.current.close();
        peerConnectionRef.current = null;
      }
      if (webSocketRef.current) {
        webSocketRef.current.close();
        webSocketRef.current = null;
      }
      ApiClient.leaveLiveInterviewRoom(secureRoomId).catch(() => {});
    };
  }, [secureRoomId]);

  // Keep local video attached when leaving waiting room
  useEffect(() => {
    if (!isWaiting && localStreamRef.current && localVideoContainerRef.current) {
      setTimeout(() => {
        attachLocalStreamToDom(localVideoContainerRef.current, localStreamRef.current!);
      }, 100);
    }
  }, [isWaiting]);

  // -------------------------------------------------------------
  // Toggle Microphone
  // -------------------------------------------------------------
  const toggleMicrophone = () => {
    const nextMic = !micOn;
    setMicOn(nextMic);
    if (localStreamRef.current) {
      localStreamRef.current.getAudioTracks().forEach((track) => {
        track.enabled = nextMic;
      });
    }
    if (webSocketRef.current && webSocketRef.current.readyState === WebSocket.OPEN) {
      webSocketRef.current.send(
        JSON.stringify({
          type: 'media-state',
          mic_on: nextMic,
          cam_on: camOn,
        })
      );
    }
  };

  // -------------------------------------------------------------
  // Toggle Camera
  // -------------------------------------------------------------
  const toggleCamera = () => {
    const nextCam = !camOn;
    setCamOn(nextCam);
    if (localStreamRef.current) {
      localStreamRef.current.getVideoTracks().forEach((track) => {
        track.enabled = nextCam;
      });
    }
    if (webSocketRef.current && webSocketRef.current.readyState === WebSocket.OPEN) {
      webSocketRef.current.send(
        JSON.stringify({
          type: 'media-state',
          mic_on: micOn,
          cam_on: nextCam,
        })
      );
    }
  };

  // -------------------------------------------------------------
  // Screen Sharing
  // -------------------------------------------------------------
  const toggleScreenSharing = async () => {
    if (Platform.OS !== 'web' || !navigator.mediaDevices?.getDisplayMedia) {
      return;
    }

    if (isScreenSharing) {
      // Stop screen sharing and revert back to webcam track
      if (screenTrackRef.current) {
        screenTrackRef.current.stop();
        screenTrackRef.current = null;
      }
      if (localStreamRef.current && peerConnectionRef.current) {
        const camTrack = localStreamRef.current.getVideoTracks()[0];
        const senders = peerConnectionRef.current.getSenders();
        const videoSender = senders.find((s) => s.track && s.track.kind === 'video');
        if (videoSender && camTrack) {
          videoSender.replaceTrack(camTrack);
        }
      }
      setIsScreenSharing(false);
      if (webSocketRef.current && webSocketRef.current.readyState === WebSocket.OPEN) {
        webSocketRef.current.send(JSON.stringify({ type: 'screen-share-status', is_sharing: false }));
      }
    } else {
      // Start screen sharing
      try {
        const screenStream = await navigator.mediaDevices.getDisplayMedia({
          video: true,
          audio: false,
        });
        const screenTrack = screenStream.getVideoTracks()[0];
        screenTrackRef.current = screenTrack;

        screenTrack.onended = () => {
          toggleScreenSharing();
        };

        if (peerConnectionRef.current) {
          const senders = peerConnectionRef.current.getSenders();
          const videoSender = senders.find((s) => s.track && s.track.kind === 'video');
          if (videoSender) {
            videoSender.replaceTrack(screenTrack);
          }
        }
        setIsScreenSharing(true);
        if (webSocketRef.current && webSocketRef.current.readyState === WebSocket.OPEN) {
          webSocketRef.current.send(JSON.stringify({ type: 'screen-share-status', is_sharing: true }));
        }
      } catch (err) {
        console.warn('Screen sharing cancelled or denied:', err);
      }
    }
  };

  // -------------------------------------------------------------
  // Send Meeting Chat Message
  // -------------------------------------------------------------
  const handleSendMessage = () => {
    if (!chatInput.trim()) return;
    const text = chatInput.trim();
    setChatInput('');

    if (webSocketRef.current && webSocketRef.current.readyState === WebSocket.OPEN) {
      webSocketRef.current.send(
        JSON.stringify({
          type: 'chat-message',
          message: text,
        })
      );
    } else {
      ApiClient.sendLiveMeetingMessage(secureRoomId, text).catch(() => {});
    }
  };

  // -------------------------------------------------------------
  // Admit Waiting Student (Faculty Host Action)
  // -------------------------------------------------------------
  const handleAdmitStudent = async () => {
    try {
      await ApiClient.admitStudentToLiveInterview(secureRoomId);
      setStudentInWaitingRoom(false);
      if (webSocketRef.current && webSocketRef.current.readyState === WebSocket.OPEN) {
        webSocketRef.current.send(JSON.stringify({ type: 'admit-student' }));
      }
    } catch (e) {
      console.warn('Admit error:', e);
    }
  };

  // -------------------------------------------------------------
  // Faculty: End Interview for Everyone
  // -------------------------------------------------------------
  const handleConfirmEndForEveryone = async () => {
    setIsEndingCall(true);
    try {
      await ApiClient.endLiveInterviewRoomForAll(secureRoomId);
      if (webSocketRef.current && webSocketRef.current.readyState === WebSocket.OPEN) {
        webSocketRef.current.send(JSON.stringify({ type: 'end-interview' }));
      }
    } catch (e) {}

    stopAllMediaTracks();
    setShowEndModal(false);
    setIsEndingCall(false);
    onLeaveMeeting();
    if (onOpenFeedback) {
      onOpenFeedback();
    }
  };

  // -------------------------------------------------------------
  // Student: Leave Call (Without ending host session)
  // -------------------------------------------------------------
  const handleConfirmStudentLeave = async () => {
    try {
      await ApiClient.leaveLiveInterviewRoom(secureRoomId);
    } catch (e) {}

    stopAllMediaTracks();
    setShowLeaveModal(false);
    onLeaveMeeting();
  };

  // =============================================================
  // RENDER: CANDIDATE WAITING ROOM VIEW
  // =============================================================
  if (isWaiting) {
    return (
      <View style={styles.waitingScreenContainer}>
        {/* Top Header */}
        <View style={styles.topBar}>
          <View style={styles.topBarLeft}>
            <View style={styles.liveBadgeWaiting}>
              <Feather name="clock" size={12} color="#F59E0B" />
              <Text style={styles.liveBadgeWaitingText}>WAITING ROOM</Text>
            </View>
            <TouchableOpacity style={styles.roomCodePill} onPress={copyRoomCode}>
              <Feather name="copy" size={11} color="#94A3B8" />
              <Text style={styles.roomCodePillText}>{secureRoomId}</Text>
              {copiedCodeNotice && <Text style={styles.copiedBadgeText}>Copied!</Text>}
            </TouchableOpacity>
          </View>
          <View style={styles.topBarCenter}>
            <Text style={styles.interviewTitleText} numberOfLines={1}>
              {interviewTitle}
            </Text>
          </View>
          <View style={styles.topBarRight}>
            <TouchableOpacity
              style={styles.leaveWaitingBtn}
              onPress={() => setShowLeaveModal(true)}
            >
              <Feather name="log-out" size={14} color="#EF4444" />
              <Text style={styles.leaveWaitingText}>Exit</Text>
            </TouchableOpacity>
          </View>
        </View>

        {/* Waiting Room Body */}
        <View style={styles.waitingBodyWrap}>
          {/* Camera Preview Card */}
          <View style={styles.waitingPreviewCard}>
            {Platform.OS === 'web' && (
              <div
                ref={(el) => {
                  if (el) waitingVideoContainerRef.current = el;
                  if (el && localStreamRef.current) {
                    attachLocalStreamToDom(el, localStreamRef.current);
                  }
                }}
                style={{
                  width: '100%',
                  height: '100%',
                  display: camOn ? 'block' : 'none',
                }}
              />
            )}

            {!camOn && (
              <View style={styles.avatarBigCircle}>
                <Text style={styles.avatarBigLetter}>
                  {currentUserName.charAt(0).toUpperCase()}
                </Text>
              </View>
            )}

            {/* In-Preview Hardware Testing Controls */}
            <View style={styles.waitingPreviewControlsRow}>
              <TouchableOpacity
                style={[styles.mediaActionBtnSmall, !micOn && styles.mediaActionBtnOff]}
                onPress={toggleMicrophone}
              >
                <Feather name={micOn ? 'mic' : 'mic-off'} size={16} color="#FFFFFF" />
              </TouchableOpacity>
              <TouchableOpacity
                style={[styles.mediaActionBtnSmall, !camOn && styles.mediaActionBtnOff]}
                onPress={toggleCamera}
              >
                <Feather name={camOn ? 'video' : 'video-off'} size={16} color="#FFFFFF" />
              </TouchableOpacity>
            </View>

            <View style={styles.pipNameTag}>
              <Text style={styles.pipNameText}>{currentUserName} (Camera Preview)</Text>
              <Feather
                name={micOn ? 'mic' : 'mic-off'}
                size={11}
                color={micOn ? '#10B981' : '#EF4444'}
              />
            </View>
          </View>

          {/* Polite Waiting Banner */}
          <View style={styles.waitingNoticeBox}>
            <ActivityIndicator size="large" color={Palette.primary} />
            <Text style={styles.waitingNoticeTitle}>Waiting for Faculty to Admit You</Text>
            <Text style={styles.waitingNoticeDesc}>
              Interviewer <Text style={{ fontWeight: '700', color: '#0F172A' }}>{otherParticipantName}</Text> has
              been notified that you are ready. You will automatically join the live video session as soon as they admit you.
            </Text>
            <View style={styles.waitingCheckRow}>
              <Feather name="check" size={14} color="#16A34A" />
              <Text style={styles.waitingCheckText}>Camera & microphone preview verified</Text>
            </View>
          </View>
        </View>

        {/* Leave Waiting Room Confirmation Modal */}
        <Modal visible={showLeaveModal} animationType="fade" transparent>
          <View style={styles.confirmModalOverlay}>
            <View style={styles.confirmModalCard}>
              <View style={styles.confirmModalHeader}>
                <Feather name="log-out" size={24} color="#EF4444" />
                <Text style={styles.confirmModalTitle}>Leave Waiting Room?</Text>
              </View>
              <Text style={styles.confirmModalDesc}>
                Are you sure you want to disconnect? You can re-enter this interview room anytime before it concludes.
              </Text>
              <View style={styles.confirmModalActionsRow}>
                <TouchableOpacity
                  style={styles.confirmModalCancelBtn}
                  onPress={() => setShowLeaveModal(false)}
                >
                  <Text style={styles.confirmModalCancelText}>Stay in Lobby</Text>
                </TouchableOpacity>
                <TouchableOpacity
                  style={styles.confirmModalDangerBtn}
                  onPress={handleConfirmStudentLeave}
                >
                  <Text style={styles.confirmModalDangerText}>Leave Room</Text>
                </TouchableOpacity>
              </View>
            </View>
          </View>
        </Modal>
      </View>
    );
  }

  // =============================================================
  // RENDER: LIVE 2-WAY MEETING ROOM
  // =============================================================
  return (
    <View style={styles.container}>
      {/* 1. Google Meet Top App Bar */}
      <View style={styles.topBar}>
        <View style={styles.topBarLeft}>
          <View style={styles.liveBadge}>
            <View style={styles.livePulseDot} />
            <Text style={styles.liveBadgeText}>LIVE INTERVIEW</Text>
          </View>
          <View style={styles.timerBadge}>
            <Feather name="clock" size={12} color="#94A3B8" />
            <Text style={styles.timerText}>{formatTimer(meetingSeconds)}</Text>
          </View>
          <TouchableOpacity style={styles.roomCodePill} onPress={copyRoomCode}>
            <Feather name="copy" size={11} color="#94A3B8" />
            <Text style={styles.roomCodePillText}>{secureRoomId}</Text>
            {copiedCodeNotice && <Text style={styles.copiedBadgeText}>Copied!</Text>}
          </TouchableOpacity>
        </View>

        <View style={styles.topBarCenter}>
          <Text style={styles.interviewTitleText} numberOfLines={1}>
            {interviewTitle}
          </Text>
          <Text style={styles.interviewCategoryText}>{category}</Text>
        </View>

        <View style={styles.topBarRight}>
          <TouchableOpacity
            style={styles.headerIconBtn}
            onPress={() => setParticipantsOpen(true)}
          >
            <Feather name="users" size={18} color="#FFFFFF" />
            <View style={styles.userCountBadge}>
              <Text style={styles.userCountText}>{isPeerConnected ? 2 : 1}</Text>
            </View>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.headerIconBtn}
            onPress={() => {
              setChatOpen(true);
              setUnreadCount(0);
            }}
          >
            <Feather name="message-square" size={18} color="#FFFFFF" />
            {unreadCount > 0 && (
              <View style={styles.unreadBadge}>
                <Text style={styles.unreadText}>{unreadCount}</Text>
              </View>
            )}
          </TouchableOpacity>
        </View>
      </View>

      {/* Host Banner: Student Waiting Notification (Faculty Only) */}
      {isTeacher && studentInWaitingRoom && (
        <View style={styles.admitBannerRow}>
          <View style={{ flexDirection: 'row', alignItems: 'center', gap: 8, flex: 1 }}>
            <Feather name="user-check" size={18} color="#F59E0B" />
            <Text style={styles.admitBannerText}>
              Candidate <Text style={{ fontWeight: '800' }}>{otherParticipantName}</Text> is waiting to enter the interview.
            </Text>
          </View>
          <TouchableOpacity style={styles.admitActionBtn} onPress={handleAdmitStudent}>
            <Feather name="check" size={14} color="#FFFFFF" />
            <Text style={styles.admitActionBtnText}>Admit Candidate</Text>
          </TouchableOpacity>
        </View>
      )}

      {/* 2. Video Stage (Google Meet Layout) */}
      <View style={styles.videoStage}>
        {/* Remote Video Container */}
        <View style={styles.remoteVideoCard}>
          {Platform.OS === 'web' && (
            <div
              ref={(el) => {
                if (el) remoteVideoContainerRef.current = el;
              }}
              style={{
                width: '100%',
                height: '100%',
                display: isPeerConnected && peerCamOn ? 'block' : 'none',
              }}
            />
          )}

          {/* Fallback / Waiting state if remote camera is off or not connected */}
          {(!isPeerConnected || !peerCamOn) && (
            <View style={styles.avatarPlaceholderContainer}>
              <View style={styles.avatarBigCircle}>
                <Text style={styles.avatarBigLetter}>
                  {otherParticipantName.charAt(0).toUpperCase()}
                </Text>
              </View>
              <Text style={styles.avatarNameText}>{otherParticipantName}</Text>
              <Text style={styles.avatarRoleText}>
                {otherParticipantRole === 'teacher' ? 'Interviewer' : 'Candidate'}
              </Text>
              {!isPeerConnected ? (
                <View style={styles.waitingNoticeRow}>
                  <View style={styles.waitingDot} />
                  <Text style={styles.waitingNoticeText}>
                    Waiting for {otherParticipantName} to join room...
                  </Text>
                </View>
              ) : (
                <Text style={styles.camOffNoticeText}>Camera is turned off</Text>
              )}
            </View>
          )}

          {/* Remote Participant Label Badge */}
          <View style={styles.videoInfoTag}>
            <View style={styles.roleBadgePill}>
              <Text style={styles.roleBadgePillText}>
                {otherParticipantRole === 'teacher' ? 'Interviewer' : 'Student Candidate'}
              </Text>
            </View>
            <Text style={styles.participantNameBadge}>{otherParticipantName}</Text>
            <View style={[styles.micStatePill, !peerMicOn && styles.micStatePillMuted]}>
              <Feather
                name={peerMicOn ? 'mic' : 'mic-off'}
                size={12}
                color={peerMicOn ? '#10B981' : '#EF4444'}
              />
            </View>
          </View>

          {peerIsSharingScreen && (
            <View style={styles.screenShareActiveBadge}>
              <Feather name="airplay" size={13} color="#FFFFFF" />
              <Text style={styles.screenShareActiveText}>Presenting Screen</Text>
            </View>
          )}
        </View>

        {/* Local Stream (Picture-in-Picture) */}
        <View style={styles.localPipCard}>
          {Platform.OS === 'web' && (
            <div
              ref={(el) => {
                if (el) localVideoContainerRef.current = el;
                if (el && localStreamRef.current) {
                  attachLocalStreamToDom(el, localStreamRef.current);
                }
              }}
              style={{
                width: '100%',
                height: '100%',
                display: camOn ? 'block' : 'none',
              }}
            />
          )}

          {!camOn && (
            <View style={styles.pipAvatarFallback}>
              <View style={styles.pipAvatarCircle}>
                <Text style={styles.pipAvatarLetter}>
                  {currentUserName.charAt(0).toUpperCase()}
                </Text>
              </View>
              <Text style={styles.pipCamOffText}>Cam Off</Text>
            </View>
          )}

          <View style={styles.pipNameTag}>
            <Text style={styles.pipNameText}>
              You ({isTeacher ? 'Interviewer' : 'Candidate'})
            </Text>
            <Feather
              name={micOn ? 'mic' : 'mic-off'}
              size={11}
              color={micOn ? '#10B981' : '#EF4444'}
            />
          </View>
        </View>
      </View>

      {/* 3. Bottom Control Toolbar (Google Meet inspired) */}
      <View style={styles.bottomToolbar}>
        {/* Mic Toggle */}
        <TouchableOpacity
          style={[styles.mediaActionBtn, !micOn && styles.mediaActionBtnOff]}
          onPress={toggleMicrophone}
        >
          <Feather name={micOn ? 'mic' : 'mic-off'} size={20} color="#FFFFFF" />
        </TouchableOpacity>

        {/* Camera Toggle */}
        <TouchableOpacity
          style={[styles.mediaActionBtn, !camOn && styles.mediaActionBtnOff]}
          onPress={toggleCamera}
        >
          <Feather name={camOn ? 'video' : 'video-off'} size={20} color="#FFFFFF" />
        </TouchableOpacity>

        {/* Screen Sharing Toggle */}
        <TouchableOpacity
          style={[styles.mediaActionBtn, isScreenSharing && styles.mediaActionBtnActive]}
          onPress={toggleScreenSharing}
        >
          <Feather name="airplay" size={20} color="#FFFFFF" />
        </TouchableOpacity>

        {/* Chat Toggle */}
        <TouchableOpacity
          style={[styles.mediaActionBtn, chatOpen && styles.mediaActionBtnActive]}
          onPress={() => {
            setChatOpen(!chatOpen);
            setUnreadCount(0);
          }}
        >
          <Feather name="message-square" size={20} color="#FFFFFF" />
          {unreadCount > 0 && <View style={styles.controlUnreadDot} />}
        </TouchableOpacity>

        {/* Leave / End Call */}
        {isTeacher ? (
          <TouchableOpacity
            style={styles.endCallPillBtn}
            onPress={() => setShowEndModal(true)}
          >
            <Feather name="phone-off" size={18} color="#FFFFFF" />
            <Text style={styles.endCallText}>End Interview for All</Text>
          </TouchableOpacity>
        ) : (
          <TouchableOpacity
            style={styles.leaveCallPillBtn}
            onPress={() => setShowLeaveModal(true)}
          >
            <Feather name="phone-off" size={18} color="#FFFFFF" />
            <Text style={styles.endCallText}>Leave Call</Text>
          </TouchableOpacity>
        )}
      </View>

      {/* 4. Real-Time In-Meeting Chat Drawer Modal */}
      <Modal visible={chatOpen} animationType="slide" transparent>
        <View style={styles.modalOverlay}>
          <View style={styles.chatDrawerCard}>
            <View style={styles.drawerHeaderRow}>
              <View style={{ flexDirection: 'row', alignItems: 'center', gap: 8 }}>
                <Feather name="message-square" size={18} color={Palette.primary} />
                <Text style={styles.drawerTitleText}>In-Call Messages</Text>
              </View>
              <TouchableOpacity onPress={() => setChatOpen(false)} style={styles.closeBtn}>
                <Feather name="x" size={20} color="#64748B" />
              </TouchableOpacity>
            </View>

            <ScrollView style={styles.chatScroll} contentContainerStyle={{ padding: 16 }}>
              {chatMessages.length === 0 ? (
                <View style={styles.emptyChatBox}>
                  <Feather name="message-circle" size={32} color="#CBD5E1" />
                  <Text style={styles.emptyChatText}>
                    Messages sent here are visible to interview participants and stored for review.
                  </Text>
                </View>
              ) : (
                chatMessages.map((msg, idx) => {
                  const isMe = msg.sender_id === currentUserId;
                  return (
                    <View
                      key={msg.id || idx}
                      style={[
                        styles.chatBubbleWrap,
                        isMe ? styles.chatBubbleMe : styles.chatBubbleOther,
                      ]}
                    >
                      <View style={styles.chatMetaRow}>
                        <Text style={styles.chatSenderName}>
                          {isMe ? 'You' : msg.sender_name}
                        </Text>
                        <Text style={styles.chatRoleTag}>
                          {msg.sender_role === 'teacher' ? 'Faculty' : 'Candidate'}
                        </Text>
                      </View>
                      <Text style={styles.chatMessageText}>{msg.message}</Text>
                    </View>
                  );
                })
              )}
            </ScrollView>

            <View style={styles.chatInputRow}>
              <TextInput
                style={styles.chatTextInput}
                placeholder="Send a message to everyone..."
                placeholderTextColor="#94A3B8"
                value={chatInput}
                onChangeText={setChatInput}
                onSubmitEditing={handleSendMessage}
              />
              <TouchableOpacity
                style={[styles.chatSendBtn, !chatInput.trim() && { opacity: 0.5 }]}
                onPress={handleSendMessage}
                disabled={!chatInput.trim()}
              >
                <Feather name="send" size={16} color="#FFFFFF" />
              </TouchableOpacity>
            </View>
          </View>
        </View>
      </Modal>

      {/* 5. Participants Drawer Modal */}
      <Modal visible={participantsOpen} animationType="slide" transparent>
        <View style={styles.modalOverlay}>
          <View style={styles.chatDrawerCard}>
            <View style={styles.drawerHeaderRow}>
              <View style={{ flexDirection: 'row', alignItems: 'center', gap: 8 }}>
                <Feather name="users" size={18} color={Palette.primary} />
                <Text style={styles.drawerTitleText}>
                  Participants ({isPeerConnected ? 2 : 1})
                </Text>
              </View>
              <TouchableOpacity onPress={() => setParticipantsOpen(false)} style={styles.closeBtn}>
                <Feather name="x" size={20} color="#64748B" />
              </TouchableOpacity>
            </View>

            <View style={{ padding: 16, gap: 12 }}>
              {/* You */}
              <View style={styles.participantItemRow}>
                <View style={styles.partAvatarCircle}>
                  <Text style={styles.partAvatarText}>
                    {currentUserName.charAt(0).toUpperCase()}
                  </Text>
                </View>
                <View style={{ flex: 1 }}>
                  <Text style={styles.partItemName}>{currentUserName} (You)</Text>
                  <Text style={styles.partItemRole}>
                    {isTeacher ? 'Interviewer / Faculty' : 'Candidate'}
                  </Text>
                </View>
                <Feather
                  name={micOn ? 'mic' : 'mic-off'}
                  size={16}
                  color={micOn ? '#10B981' : '#EF4444'}
                />
              </View>

              {/* Other */}
              <View style={styles.participantItemRow}>
                <View style={[styles.partAvatarCircle, { backgroundColor: '#EEF2FF' }]}>
                  <Text style={[styles.partAvatarText, { color: '#4F46E5' }]}>
                    {otherParticipantName.charAt(0).toUpperCase()}
                  </Text>
                </View>
                <View style={{ flex: 1 }}>
                  <Text style={styles.partItemName}>{otherParticipantName}</Text>
                  <Text style={styles.partItemRole}>
                    {otherParticipantRole === 'teacher' ? 'Interviewer / Faculty' : 'Candidate'} •{' '}
                    <Text style={{ color: isPeerConnected ? '#10B981' : '#F59E0B' }}>
                      {isPeerConnected ? 'In Meeting' : 'Waiting in Room'}
                    </Text>
                  </Text>
                </View>
                {isPeerConnected && (
                  <Feather
                    name={peerMicOn ? 'mic' : 'mic-off'}
                    size={16}
                    color={peerMicOn ? '#10B981' : '#EF4444'}
                  />
                )}
              </View>
            </View>
          </View>
        </View>
      </Modal>

      {/* MODAL: Faculty End Interview for Everyone Confirmation */}
      <Modal visible={showEndModal} animationType="fade" transparent>
        <View style={styles.confirmModalOverlay}>
          <View style={styles.confirmModalCard}>
            <View style={styles.confirmModalHeader}>
              <Feather name="alert-triangle" size={24} color="#EF4444" />
              <Text style={styles.confirmModalTitle}>End Interview for Everyone?</Text>
            </View>
            <Text style={styles.confirmModalDesc}>
              This will conclude the live interview for all participants, mark the session as completed in the database, and prompt you to submit final evaluation feedback.
            </Text>
            <View style={styles.confirmModalActionsRow}>
              <TouchableOpacity
                style={styles.confirmModalCancelBtn}
                onPress={() => setShowEndModal(false)}
                disabled={isEndingCall}
              >
                <Text style={styles.confirmModalCancelText}>Keep Calling</Text>
              </TouchableOpacity>
              <TouchableOpacity
                style={styles.confirmModalDangerBtn}
                onPress={handleConfirmEndForEveryone}
                disabled={isEndingCall}
              >
                {isEndingCall ? (
                  <ActivityIndicator size="small" color="#FFFFFF" />
                ) : (
                  <Text style={styles.confirmModalDangerText}>End & Grade</Text>
                )}
              </TouchableOpacity>
            </View>
          </View>
        </View>
      </Modal>

      {/* MODAL: Student Leave Meeting Confirmation */}
      <Modal visible={showLeaveModal} animationType="fade" transparent>
        <View style={styles.confirmModalOverlay}>
          <View style={styles.confirmModalCard}>
            <View style={styles.confirmModalHeader}>
              <Feather name="log-out" size={24} color="#EF4444" />
              <Text style={styles.confirmModalTitle}>Leave Interview Room?</Text>
            </View>
            <Text style={styles.confirmModalDesc}>
              Are you sure you want to disconnect from this interview call? The faculty session will remain open so you can reconnect if needed.
            </Text>
            <View style={styles.confirmModalActionsRow}>
              <TouchableOpacity
                style={styles.confirmModalCancelBtn}
                onPress={() => setShowLeaveModal(false)}
              >
                <Text style={styles.confirmModalCancelText}>Stay in Call</Text>
              </TouchableOpacity>
              <TouchableOpacity
                style={styles.confirmModalDangerBtn}
                onPress={handleConfirmStudentLeave}
              >
                <Text style={styles.confirmModalDangerText}>Disconnect</Text>
              </TouchableOpacity>
            </View>
          </View>
        </View>
      </Modal>

      {/* MODAL: Interview Concluded by Faculty (Student Notification) */}
      <Modal visible={showHostEndedModal} animationType="fade" transparent>
        <View style={styles.confirmModalOverlay}>
          <View style={styles.confirmModalCard}>
            <View style={styles.confirmModalHeader}>
              <Feather name="award" size={24} color={Palette.primary} />
              <Text style={styles.confirmModalTitle}>Interview Concluded</Text>
            </View>
            <Text style={styles.confirmModalDesc}>
              The faculty interviewer has ended this live interview session. Your participation has been recorded. Once your evaluation feedback is published, you can view your official score and report.
            </Text>
            <TouchableOpacity
              style={styles.returnDashboardBtn}
              onPress={() => {
                setShowHostEndedModal(false);
                onLeaveMeeting();
              }}
            >
              <Text style={styles.returnDashboardBtnText}>Return to Dashboard</Text>
            </TouchableOpacity>
          </View>
        </View>
      </Modal>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0F172A',
  },
  waitingScreenContainer: {
    flex: 1,
    backgroundColor: '#0F172A',
  },
  topBar: {
    height: 60,
    backgroundColor: '#1E293B',
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: 16,
    borderBottomWidth: 1,
    borderBottomColor: 'rgba(255, 255, 255, 0.08)',
  },
  topBarLeft: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 10,
  },
  liveBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    backgroundColor: 'rgba(239, 68, 68, 0.2)',
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: Radii.full,
  },
  liveBadgeWaiting: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    backgroundColor: 'rgba(245, 158, 11, 0.2)',
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: Radii.full,
  },
  liveBadgeWaitingText: {
    fontSize: 10,
    fontWeight: '800',
    color: '#F59E0B',
  },
  livePulseDot: {
    width: 7,
    height: 7,
    borderRadius: 3.5,
    backgroundColor: '#EF4444',
  },
  liveBadgeText: {
    fontSize: 10,
    fontWeight: '800',
    color: '#EF4444',
  },
  timerBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
    backgroundColor: 'rgba(255, 255, 255, 0.05)',
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: Radii.sm,
  },
  timerText: {
    fontSize: 12,
    fontWeight: '700',
    color: '#F8FAFC',
    fontVariant: ['tabular-nums'],
  },
  roomCodePill: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 5,
    backgroundColor: 'rgba(255, 255, 255, 0.08)',
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: Radii.sm,
  },
  roomCodePillText: {
    fontSize: 11,
    fontFamily: Platform.OS === 'ios' ? 'Menlo' : 'monospace',
    color: '#CBD5E1',
    fontWeight: '600',
  },
  copiedBadgeText: {
    fontSize: 10,
    color: '#10B981',
    fontWeight: '700',
    marginLeft: 4,
  },
  leaveWaitingBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    backgroundColor: 'rgba(239, 68, 68, 0.15)',
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: Radii.sm,
  },
  leaveWaitingText: {
    fontSize: 12,
    fontWeight: '700',
    color: '#EF4444',
  },
  topBarCenter: {
    flex: 1,
    alignItems: 'center',
    paddingHorizontal: 12,
  },
  interviewTitleText: {
    fontSize: 14,
    fontWeight: '800',
    color: '#FFFFFF',
  },
  interviewCategoryText: {
    fontSize: 11,
    color: '#94A3B8',
    marginTop: 1,
  },
  topBarRight: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  headerIconBtn: {
    width: 38,
    height: 38,
    borderRadius: 19,
    backgroundColor: 'rgba(255, 255, 255, 0.08)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  userCountBadge: {
    position: 'absolute',
    top: -2,
    right: -2,
    backgroundColor: Palette.primary,
    borderRadius: 8,
    width: 16,
    height: 16,
    justifyContent: 'center',
    alignItems: 'center',
  },
  userCountText: {
    fontSize: 9,
    fontWeight: '800',
    color: '#FFFFFF',
  },
  unreadBadge: {
    position: 'absolute',
    top: -2,
    right: -2,
    backgroundColor: Palette.danger,
    borderRadius: 8,
    width: 16,
    height: 16,
    justifyContent: 'center',
    alignItems: 'center',
  },
  unreadText: {
    fontSize: 9,
    fontWeight: '800',
    color: '#FFFFFF',
  },
  admitBannerRow: {
    backgroundColor: '#FEF3C7',
    borderBottomWidth: 1,
    borderBottomColor: '#FDE68A',
    paddingHorizontal: 16,
    paddingVertical: 10,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    gap: 12,
  },
  admitBannerText: {
    fontSize: 13,
    color: '#92400E',
  },
  admitActionBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    backgroundColor: '#16A34A',
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: Radii.sm,
  },
  admitActionBtnText: {
    fontSize: 12,
    fontWeight: '700',
    color: '#FFFFFF',
  },
  waitingBodyWrap: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    padding: 24,
    gap: 24,
  },
  waitingPreviewCard: {
    width: '100%',
    maxWidth: 480,
    height: 280,
    backgroundColor: '#1E293B',
    borderRadius: Radii.lg,
    overflow: 'hidden',
    position: 'relative',
    borderWidth: 2,
    borderColor: 'rgba(255, 255, 255, 0.1)',
    justifyContent: 'center',
    alignItems: 'center',
    ...Shadows.floating,
  },
  waitingPreviewControlsRow: {
    position: 'absolute',
    bottom: 12,
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
    backgroundColor: 'rgba(0, 0, 0, 0.6)',
    paddingHorizontal: 14,
    paddingVertical: 8,
    borderRadius: Radii.full,
  },
  mediaActionBtnSmall: {
    width: 36,
    height: 36,
    borderRadius: 18,
    backgroundColor: '#334155',
    justifyContent: 'center',
    alignItems: 'center',
  },
  waitingNoticeBox: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.lg,
    padding: 24,
    alignItems: 'center',
    maxWidth: 480,
    width: '100%',
    gap: 10,
    ...Shadows.md,
  },
  waitingNoticeTitle: {
    fontSize: 18,
    fontWeight: '800',
    color: '#0F172A',
    marginTop: 8,
  },
  waitingNoticeDesc: {
    fontSize: 13,
    color: '#64748B',
    textAlign: 'center',
    lineHeight: 19,
  },
  waitingCheckRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    backgroundColor: '#F0FDF4',
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: Radii.full,
    marginTop: 6,
  },
  waitingCheckText: {
    fontSize: 12,
    fontWeight: '600',
    color: '#16A34A',
  },
  videoStage: {
    flex: 1,
    padding: 16,
    position: 'relative',
    justifyContent: 'center',
    alignItems: 'center',
  },
  remoteVideoCard: {
    width: '100%',
    height: '100%',
    backgroundColor: '#1E293B',
    borderRadius: Radii.lg,
    overflow: 'hidden',
    borderWidth: 1.5,
    borderColor: 'rgba(255, 255, 255, 0.1)',
    justifyContent: 'center',
    alignItems: 'center',
    position: 'relative',
  },
  avatarPlaceholderContainer: {
    alignItems: 'center',
    gap: 8,
  },
  avatarBigCircle: {
    width: 90,
    height: 90,
    borderRadius: 45,
    backgroundColor: Palette.primary,
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 4,
    ...Shadows.md,
  },
  avatarBigLetter: {
    fontSize: 36,
    fontWeight: '900',
    color: '#FFFFFF',
  },
  avatarNameText: {
    fontSize: 18,
    fontWeight: '800',
    color: '#FFFFFF',
  },
  avatarRoleText: {
    fontSize: 13,
    color: '#94A3B8',
  },
  waitingNoticeRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    backgroundColor: 'rgba(245, 158, 11, 0.15)',
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: Radii.full,
    marginTop: 10,
  },
  waitingDot: {
    width: 8,
    height: 8,
    borderRadius: 4,
    backgroundColor: '#F59E0B',
  },
  waitingNoticeText: {
    fontSize: 12,
    color: '#FCD34D',
    fontWeight: '600',
  },
  camOffNoticeText: {
    fontSize: 12,
    color: '#64748B',
    fontStyle: 'italic',
    marginTop: 4,
  },
  videoInfoTag: {
    position: 'absolute',
    bottom: 16,
    left: 16,
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    backgroundColor: 'rgba(15, 23, 42, 0.85)',
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: Radii.full,
    borderWidth: 1,
    borderColor: 'rgba(255, 255, 255, 0.1)',
  },
  roleBadgePill: {
    backgroundColor: Palette.primary,
    paddingHorizontal: 6,
    paddingVertical: 2,
    borderRadius: 4,
  },
  roleBadgePillText: {
    fontSize: 10,
    fontWeight: '800',
    color: '#FFFFFF',
    textTransform: 'uppercase',
  },
  participantNameBadge: {
    fontSize: 13,
    fontWeight: '700',
    color: '#FFFFFF',
  },
  micStatePill: {
    width: 20,
    height: 20,
    borderRadius: 10,
    backgroundColor: 'rgba(16, 185, 129, 0.15)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  micStatePillMuted: {
    backgroundColor: 'rgba(239, 68, 68, 0.15)',
  },
  screenShareActiveBadge: {
    position: 'absolute',
    top: 16,
    left: 16,
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    backgroundColor: '#2563EB',
    paddingHorizontal: 10,
    paddingVertical: 5,
    borderRadius: Radii.full,
  },
  screenShareActiveText: {
    fontSize: 11,
    fontWeight: '700',
    color: '#FFFFFF',
  },
  localPipCard: {
    position: 'absolute',
    bottom: 30,
    right: 30,
    width: 180,
    height: 120,
    backgroundColor: '#0F172A',
    borderRadius: Radii.md,
    overflow: 'hidden',
    borderWidth: 2,
    borderColor: 'rgba(255, 255, 255, 0.25)',
    ...Shadows.floating,
    justifyContent: 'center',
    alignItems: 'center',
  },
  pipAvatarFallback: {
    alignItems: 'center',
    gap: 4,
  },
  pipAvatarCircle: {
    width: 44,
    height: 44,
    borderRadius: 22,
    backgroundColor: '#334155',
    justifyContent: 'center',
    alignItems: 'center',
  },
  pipAvatarLetter: {
    fontSize: 18,
    fontWeight: '800',
    color: '#FFFFFF',
  },
  pipCamOffText: {
    fontSize: 10,
    color: '#94A3B8',
  },
  pipNameTag: {
    position: 'absolute',
    bottom: 6,
    left: 6,
    right: 6,
    backgroundColor: 'rgba(0, 0, 0, 0.75)',
    paddingHorizontal: 6,
    paddingVertical: 3,
    borderRadius: 4,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
  },
  pipNameText: {
    fontSize: 10,
    fontWeight: '700',
    color: '#FFFFFF',
  },
  bottomToolbar: {
    height: 80,
    backgroundColor: '#1E293B',
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 14,
    paddingHorizontal: 20,
    borderTopWidth: 1,
    borderTopColor: 'rgba(255, 255, 255, 0.08)',
  },
  mediaActionBtn: {
    width: 50,
    height: 50,
    borderRadius: 25,
    backgroundColor: '#334155',
    justifyContent: 'center',
    alignItems: 'center',
    ...Shadows.sm,
  },
  mediaActionBtnOff: {
    backgroundColor: '#DC2626',
  },
  mediaActionBtnActive: {
    backgroundColor: '#2563EB',
  },
  controlUnreadDot: {
    position: 'absolute',
    top: 10,
    right: 10,
    width: 10,
    height: 10,
    borderRadius: 5,
    backgroundColor: '#EF4444',
  },
  endCallPillBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    backgroundColor: '#DC2626',
    paddingHorizontal: 18,
    paddingVertical: 13,
    borderRadius: Radii.full,
    marginLeft: 6,
    ...Shadows.md,
  },
  leaveCallPillBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    backgroundColor: '#475569',
    paddingHorizontal: 18,
    paddingVertical: 13,
    borderRadius: Radii.full,
    marginLeft: 6,
    ...Shadows.md,
  },
  endCallText: {
    fontSize: 13,
    fontWeight: '800',
    color: '#FFFFFF',
  },
  modalOverlay: {
    flex: 1,
    backgroundColor: 'rgba(0, 0, 0, 0.65)',
    justifyContent: 'flex-end',
  },
  chatDrawerCard: {
    backgroundColor: '#FFFFFF',
    borderTopLeftRadius: Radii.cardLarge,
    borderTopRightRadius: Radii.cardLarge,
    height: '65%',
    ...Shadows.floating,
  },
  drawerHeaderRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: 20,
    paddingVertical: 16,
    borderBottomWidth: 1,
    borderBottomColor: '#F1F5F9',
  },
  drawerTitleText: {
    fontSize: 16,
    fontWeight: '800',
    color: '#0F172A',
  },
  closeBtn: {
    padding: 6,
  },
  chatScroll: {
    flex: 1,
  },
  emptyChatBox: {
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 40,
    gap: 12,
  },
  emptyChatText: {
    fontSize: 13,
    color: '#94A3B8',
    textAlign: 'center',
    maxWidth: 260,
    lineHeight: 18,
  },
  chatBubbleWrap: {
    borderRadius: Radii.md,
    padding: 12,
    marginBottom: 10,
    maxWidth: '85%',
  },
  chatBubbleMe: {
    alignSelf: 'flex-end',
    backgroundColor: '#EEF2FF',
    borderBottomRightRadius: 2,
  },
  chatBubbleOther: {
    alignSelf: 'flex-start',
    backgroundColor: '#F8FAFC',
    borderWidth: 1,
    borderColor: '#E2E8F0',
    borderBottomLeftRadius: 2,
  },
  chatMetaRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    marginBottom: 4,
  },
  chatSenderName: {
    fontSize: 12,
    fontWeight: '700',
    color: '#334155',
  },
  chatRoleTag: {
    fontSize: 10,
    fontWeight: '600',
    color: '#64748B',
    backgroundColor: '#E2E8F0',
    paddingHorizontal: 5,
    paddingVertical: 1,
    borderRadius: 4,
  },
  chatMessageText: {
    fontSize: 13.5,
    color: '#0F172A',
    lineHeight: 19,
  },
  chatInputRow: {
    flexDirection: 'row',
    alignItems: 'center',
    padding: 12,
    borderTopWidth: 1,
    borderTopColor: '#F1F5F9',
    gap: 10,
  },
  chatTextInput: {
    flex: 1,
    backgroundColor: '#F8FAFC',
    borderRadius: Radii.full,
    paddingHorizontal: 16,
    paddingVertical: 10,
    fontSize: 14,
    color: '#0F172A',
    borderWidth: 1,
    borderColor: '#E2E8F0',
  },
  chatSendBtn: {
    width: 40,
    height: 40,
    borderRadius: 20,
    backgroundColor: Palette.primary,
    justifyContent: 'center',
    alignItems: 'center',
  },
  participantItemRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
    padding: 10,
    backgroundColor: '#F8FAFC',
    borderRadius: Radii.md,
    borderWidth: 1,
    borderColor: '#E2E8F0',
  },
  partAvatarCircle: {
    width: 38,
    height: 38,
    borderRadius: 19,
    backgroundColor: Palette.primary,
    justifyContent: 'center',
    alignItems: 'center',
  },
  partAvatarText: {
    fontSize: 16,
    fontWeight: '800',
    color: '#FFFFFF',
  },
  partItemName: {
    fontSize: 14,
    fontWeight: '700',
    color: '#0F172A',
  },
  partItemRole: {
    fontSize: 12,
    color: '#64748B',
    marginTop: 2,
  },
  confirmModalOverlay: {
    flex: 1,
    backgroundColor: 'rgba(0, 0, 0, 0.7)',
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  confirmModalCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.lg,
    padding: 24,
    width: '100%',
    maxWidth: 440,
    ...Shadows.floating,
  },
  confirmModalHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 10,
    marginBottom: 12,
  },
  confirmModalTitle: {
    fontSize: 17,
    fontWeight: '800',
    color: '#0F172A',
  },
  confirmModalDesc: {
    fontSize: 13.5,
    color: '#64748B',
    lineHeight: 20,
    marginBottom: 20,
  },
  confirmModalActionsRow: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'flex-end',
    gap: 10,
  },
  confirmModalCancelBtn: {
    paddingHorizontal: 16,
    paddingVertical: 10,
    borderRadius: Radii.sm,
    backgroundColor: '#F1F5F9',
  },
  confirmModalCancelText: {
    fontSize: 13,
    fontWeight: '700',
    color: '#475569',
  },
  confirmModalDangerBtn: {
    paddingHorizontal: 18,
    paddingVertical: 10,
    borderRadius: Radii.sm,
    backgroundColor: '#DC2626',
    minWidth: 100,
    alignItems: 'center',
  },
  confirmModalDangerText: {
    fontSize: 13,
    fontWeight: '800',
    color: '#FFFFFF',
  },
  returnDashboardBtn: {
    backgroundColor: Palette.primary,
    borderRadius: Radii.sm,
    paddingVertical: 12,
    alignItems: 'center',
    marginTop: 8,
  },
  returnDashboardBtnText: {
    fontSize: 14,
    fontWeight: '800',
    color: '#FFFFFF',
  },
});
