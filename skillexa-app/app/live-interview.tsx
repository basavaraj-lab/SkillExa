import { Feather } from '@expo/vector-icons';
import { router, useLocalSearchParams } from 'expo-router';
import React, { useEffect, useState } from 'react';
import {
  ActivityIndicator,
  Alert,
  Modal,
  Platform,
  RefreshControl,
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  View,
} from 'react-native';
import { useAuth } from '../components/auth-context';
import { AppHeader } from '../components/common/AppHeader';
import { SkillExaLiveMeetingRoom } from '../components/interview/SkillExaLiveMeetingRoom';
import { Palette, Radii, Shadows } from '../constants/theme';
import { ApiClient } from '../services/api';

const CATEGORIES = [
  'Technical Interview',
  'HR Interview',
  'Python Interview',
  'C Interview',
  'C++ Interview',
  'Java Interview',
  'DSA Interview',
  'SQL and DBMS Interview',
  'Engineering Subjects',
  'Custom Interview',
];

const DURATIONS = [15, 30, 45, 60, 90];

const FALLBACK_STUDENTS = [
  {
    id: '753d5be3-55a1-4ef9-a1c7-46de21ac4b44',
    user_id: '753d5be3-55a1-4ef9-a1c7-46de21ac4b44',
    name: 'Ganesh Sharan',
    branch: 'ECE',
    academic_year: '3rd Year',
  },
  {
    id: 'ddf3c948-2798-4fa4-b1b4-db403b7ad4c5',
    user_id: 'ddf3c948-2798-4fa4-b1b4-db403b7ad4c5',
    name: 'Basavaraju R K',
    branch: 'ECE',
    academic_year: '4th Year',
  },
];

function parseInterviewDateTime(dateStr: string, timeStr: string): Date | null {
  const cleanDate = (dateStr || '').trim();
  const cleanTime = (timeStr || '').trim();
  if (!cleanDate) return null;

  // 12-hour AM/PM: e.g. "12:00 am", "12:00 AM", "02:30 pm", "9:15am", "9 am"
  const ampmMatch = cleanTime.match(/^(\d{1,2})(?::(\d{1,2}))?\s*(am|pm)$/i);
  let hours = 0;
  let minutes = 0;

  if (ampmMatch) {
    const rawHours = parseInt(ampmMatch[1], 10);
    minutes = ampmMatch[2] ? parseInt(ampmMatch[2], 10) : 0;
    const modifier = ampmMatch[3].toLowerCase();

    if (rawHours === 12) {
      hours = modifier === 'am' ? 0 : 12;
    } else {
      hours = modifier === 'pm' ? rawHours + 12 : rawHours;
    }
  } else {
    // 24-hour format: "14:30", "09:00", "11:00"
    const match24 = cleanTime.match(/^(\d{1,2}):(\d{1,2})$/);
    if (match24) {
      hours = parseInt(match24[1], 10);
      minutes = parseInt(match24[2], 10);
    } else {
      const attempt = new Date(`${cleanDate} ${cleanTime}`);
      if (!isNaN(attempt.getTime())) return attempt;
      return null;
    }
  }

  // Parse YYYY-MM-DD
  const dateMatch = cleanDate.match(/^(\d{4})-(\d{1,2})-(\d{1,2})$/);
  if (dateMatch) {
    const year = parseInt(dateMatch[1], 10);
    const month = parseInt(dateMatch[2], 10) - 1;
    const day = parseInt(dateMatch[3], 10);
    const parsedDate = new Date(year, month, day, hours, minutes, 0, 0);
    return isNaN(parsedDate.getTime()) ? null : parsedDate;
  }

  const fallback = new Date(
    `${cleanDate} ${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:00`
  );
  return isNaN(fallback.getTime()) ? null : fallback;
}

export default function SkillExaLiveInterviewScreen() {
  const { profile } = useAuth();
  const params = useLocalSearchParams<{
    bookingId?: string;
    roomId?: string;
    autoJoin?: string;
  }>();

  // Determine user role strictly from authenticated account
  const isTeacher = profile.role === 'FACULTY' || profile.role === 'ADMIN';

  // Navigation / View State: 'list' | 'schedule' | 'in-meeting'
  const [currentView, setCurrentView] = useState<'list' | 'schedule' | 'in-meeting'>('list');
  const [activeBooking, setActiveBooking] = useState<any | null>(null);
  const [activeRoomInfo, setActiveRoomInfo] = useState<any | null>(null);

  // Bookings list state
  const [bookings, setBookings] = useState<any[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [isRefreshing, setIsRefreshing] = useState(false);
  const [statusFilter, setStatusFilter] = useState<string>('ALL');

  // Student: Join by room code input
  const [roomCodeInput, setRoomCodeInput] = useState('');
  const [isValidatingCode, setIsValidatingCode] = useState(false);
  const [roomCodeError, setRoomCodeError] = useState<string | null>(null);

  // Schedule form state (Teacher only)
  const [students, setStudents] = useState<any[]>(FALLBACK_STUDENTS);
  const [selectedStudentId, setSelectedStudentId] = useState('753d5be3-55a1-4ef9-a1c7-46de21ac4b44');
  const [selectedCategory, setSelectedCategory] = useState('Technical Interview');
  const [subject, setSubject] = useState('Full Stack Web & Database Architecture');
  const [scheduledDateStr, setScheduledDateStr] = useState(
    new Date(Date.now() + 24 * 3600 * 1000).toISOString().slice(0, 10)
  );
  const [scheduledTimeStr, setScheduledTimeStr] = useState('11:00 AM');
  const [durationMinutes, setDurationMinutes] = useState(45);
  const [instructions, setInstructions] = useState(
    'Please review system architecture principles and be ready to explain trade-offs.'
  );
  const [prepMaterials, setPrepMaterials] = useState(
    'WebRTC protocols, REST API design, and SQL indexing.'
  );
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [formError, setFormError] = useState<string | null>(null);
  const [formSuccess, setFormSuccess] = useState<string | null>(null);

  // Reschedule Modal state (Teacher)
  const [rescheduleModalVisible, setRescheduleModalVisible] = useState(false);
  const [rescheduleBookingId, setRescheduleBookingId] = useState('');
  const [rescheduleDateStr, setRescheduleDateStr] = useState('');
  const [rescheduleTimeStr, setRescheduleTimeStr] = useState('');
  const [rescheduleDuration, setRescheduleDuration] = useState(45);
  const [isRescheduling, setIsRescheduling] = useState(false);

  // Cancel Modal state
  const [cancelModalVisible, setCancelModalVisible] = useState(false);
  const [cancelBookingId, setCancelBookingId] = useState('');
  const [isCancelling, setIsCancelling] = useState(false);

  // Feedback View Modal state
  const [feedbackModalVisible, setFeedbackModalVisible] = useState(false);
  const [feedbackData, setFeedbackData] = useState<any | null>(null);
  const [isLoadingFeedback, setIsLoadingFeedback] = useState(false);

  // Feedback Submit Modal state (Teacher)
  const [submitFeedbackModalVisible, setSubmitFeedbackModalVisible] = useState(false);
  const [evalBookingId, setEvalBookingId] = useState('');
  const [technicalScore, setTechnicalScore] = useState('85');
  const [commFeedback, setCommFeedback] = useState(
    'Clear, concise articulation with excellent technical vocabulary.'
  );
  const [problemSolvingFeedback, setProblemSolvingFeedback] = useState(
    'Methodical approach to edge cases and error handling.'
  );
  const [strengthsText, setStrengthsText] = useState(
    'Clean reasoning, strong fundamentals, confident delivery'
  );
  const [improvementText, setImprovementText] = useState(
    'Deep dive into distributed locking and cache invalidation'
  );
  const [teacherComments, setTeacherComments] = useState(
    'Ready for Tier-1 campus placement interviews.'
  );
  const [recommendedTopicsText, setRecommendedTopicsText] = useState(
    'System Design, Database Indexing, Concurrency'
  );

  // 1-click room code copy feedback
  const [copiedCodeId, setCopiedCodeId] = useState<string | null>(null);

  const handleCopyCardRoomCode = (code: string, id: string) => {
    if (typeof navigator !== 'undefined' && navigator.clipboard) {
      navigator.clipboard.writeText(code);
      setCopiedCodeId(id);
      setTimeout(() => setCopiedCodeId(null), 2500);
    }
  };

  // -------------------------------------------------------------
  // Load Bookings & Students
  // -------------------------------------------------------------
  const loadBookings = async () => {
    setIsLoading(true);
    try {
      if (isTeacher) {
        await ApiClient.ensureFacultyToken();
      } else {
        await ApiClient.ensureStudentToken();
      }
      const res = await ApiClient.getLiveInterviewBookings(
        statusFilter === 'ALL' ? undefined : statusFilter
      );
      if (res.success && res.data) {
        setBookings(res.data);
      }
    } catch (e) {
      console.warn('loadBookings error:', e);
    }
    setIsLoading(false);
    setIsRefreshing(false);
  };

  const loadStudents = async () => {
    if (!isTeacher) return;
    try {
      await ApiClient.ensureFacultyToken();
      const res = await ApiClient.getDepartmentStudents();
      if (res.success && res.data && res.data.length > 0) {
        setStudents(res.data);
        if (!selectedStudentId) {
          setSelectedStudentId(res.data[0].user_id || res.data[0].id);
        }
      }
    } catch (e) {
      console.warn('loadStudents notice:', e);
    }
  };

  useEffect(() => {
    loadBookings();
    loadStudents();
  }, [statusFilter, profile.role]);

  // Handle direct link / notification deep link
  useEffect(() => {
    if (params.roomId && params.autoJoin === 'true') {
      joinRoomById(params.roomId);
    }
  }, [params.roomId]);

  // -------------------------------------------------------------
  // Join Room
  // -------------------------------------------------------------
  const joinRoomById = async (roomIdentifier: string, booking?: any) => {
    setIsLoading(true);
    try {
      const res = await ApiClient.joinLiveInterviewRoom(roomIdentifier);
      setIsLoading(false);
      if (res.success && res.data) {
        setActiveRoomInfo(res.data);
        setActiveBooking(booking || res.data);
        setCurrentView('in-meeting');
      } else {
        Alert.alert('Unable to Join', res.message || 'Room could not be accessed.');
      }
    } catch (e: any) {
      setIsLoading(false);
      Alert.alert('Connection Notice', e.message || 'Failed to connect to the meeting room.');
    }
  };

  // -------------------------------------------------------------
  // Student: Join by Room Code
  // -------------------------------------------------------------
  const handleJoinByRoomCode = async () => {
    const code = roomCodeInput.trim();
    if (!code) {
      setRoomCodeError('Please enter a valid room code.');
      return;
    }
    setRoomCodeError(null);
    setIsValidatingCode(true);
    try {
      const res = await ApiClient.validateLiveInterviewRoom(code);
      setIsValidatingCode(false);
      if (res.success && res.data) {
        joinRoomById(res.data.secure_room_id);
      } else {
        setRoomCodeError(res.message || 'Room code could not be verified.');
      }
    } catch (e: any) {
      setIsValidatingCode(false);
      setRoomCodeError(e.message || 'Room code verification failed.');
    }
  };

  // -------------------------------------------------------------
  // Schedule Interview (Teacher Only)
  // -------------------------------------------------------------
  const handleScheduleSubmit = async () => {
    setFormError(null);
    setFormSuccess(null);

    const studentToUse =
      selectedStudentId ||
      students[0]?.user_id ||
      students[0]?.id ||
      '753d5be3-55a1-4ef9-a1c7-46de21ac4b44';

    if (!studentToUse) {
      const errMsg = 'Please select a student candidate for this interview.';
      setFormError(errMsg);
      return;
    }
    if (!subject.trim()) {
      const errMsg = 'Please specify the interview subject or role.';
      setFormError(errMsg);
      return;
    }

    const parsedDate = parseInterviewDateTime(scheduledDateStr, scheduledTimeStr);
    if (!parsedDate || isNaN(parsedDate.getTime())) {
      const errMsg =
        'Invalid date or time format. Please provide date as YYYY-MM-DD and time as HH:MM or 12:00 am/pm.';
      setFormError(errMsg);
      return;
    }

    const isoScheduled = parsedDate.toISOString();

    setIsSubmitting(true);
    try {
      await ApiClient.ensureFacultyToken();
      const res = await ApiClient.createLiveInterviewBooking({
        student_id: studentToUse,
        interview_category: selectedCategory,
        subject: subject.trim(),
        scheduled_at: isoScheduled,
        duration_minutes: durationMinutes,
        instructions: instructions.trim(),
        preparation_materials: prepMaterials.trim(),
      });

      setIsSubmitting(false);
      if (res.success && res.data) {
        setFormSuccess(
          `Live interview scheduled for ${res.data.student_name}! Room ID: ${res.data.secure_room_id}`
        );

        await loadBookings();
        setCurrentView('list');
      } else {
        const errMsg = res.message || 'Could not schedule interview.';
        setFormError(errMsg);
      }
    } catch (e: any) {
      setIsSubmitting(false);
      const errMsg = e.message || 'Could not complete interview booking.';
      setFormError(errMsg);
    }
  };

  // -------------------------------------------------------------
  // Reschedule Interview (Teacher Only)
  // -------------------------------------------------------------
  const handleOpenReschedule = (booking: any) => {
    setRescheduleBookingId(booking.id);
    const dt = new Date(booking.scheduled_at);
    setRescheduleDateStr(dt.toISOString().slice(0, 10));
    const hours = dt.getHours();
    const minutes = dt.getMinutes();
    const ampm = hours >= 12 ? 'PM' : 'AM';
    const h12 = hours % 12 || 12;
    setRescheduleTimeStr(`${h12}:${minutes.toString().padStart(2, '0')} ${ampm}`);
    setRescheduleDuration(booking.duration_minutes || 45);
    setRescheduleModalVisible(true);
  };

  const handleSaveReschedule = async () => {
    const parsedDate = parseInterviewDateTime(rescheduleDateStr, rescheduleTimeStr);
    if (!parsedDate || isNaN(parsedDate.getTime())) {
      Alert.alert(
        'Invalid Date/Time',
        'Please provide date as YYYY-MM-DD and time as HH:MM or 12:00 am/pm.'
      );
      return;
    }

    setIsRescheduling(true);
    try {
      const res = await ApiClient.rescheduleLiveInterviewBooking(rescheduleBookingId, {
        scheduled_at: parsedDate.toISOString(),
        duration_minutes: rescheduleDuration,
      });

      setIsRescheduling(false);
      if (res.success) {
        setRescheduleModalVisible(false);
        loadBookings();
      } else {
        Alert.alert('Reschedule Failed', res.message || 'Could not reschedule.');
      }
    } catch (e: any) {
      setIsRescheduling(false);
      Alert.alert('Reschedule Notice', e.message);
    }
  };

  // -------------------------------------------------------------
  // Confirm or Cancel Booking
  // -------------------------------------------------------------
  const handleConfirmBooking = async (bookingId: string) => {
    try {
      const res = await ApiClient.confirmLiveInterviewBooking(bookingId);
      if (res.success) {
        loadBookings();
      }
    } catch (e: any) {
      Alert.alert('Notice', e.message);
    }
  };

  const handleOpenCancel = (bookingId: string) => {
    setCancelBookingId(bookingId);
    setCancelModalVisible(true);
  };

  const handleConfirmCancel = async () => {
    setIsCancelling(true);
    try {
      const res = await ApiClient.cancelLiveInterviewBooking(cancelBookingId);
      setIsCancelling(false);
      if (res.success) {
        setCancelModalVisible(false);
        loadBookings();
      } else {
        Alert.alert('Cancel Error', res.message || 'Could not cancel booking.');
      }
    } catch (e: any) {
      setIsCancelling(false);
      Alert.alert('Cancel Notice', e.message);
    }
  };

  // -------------------------------------------------------------
  // View & Submit Feedback
  // -------------------------------------------------------------
  const handleViewFeedback = async (bookingId: string) => {
    setIsLoadingFeedback(true);
    setFeedbackModalVisible(true);
    try {
      const res = await ApiClient.getLiveInterviewFeedback(bookingId);
      setIsLoadingFeedback(false);
      if (res.success && res.data) {
        setFeedbackData(res.data);
      } else {
        setFeedbackData(null);
      }
    } catch (e) {
      setIsLoadingFeedback(false);
      setFeedbackData(null);
    }
  };

  const handleOpenSubmitFeedback = (bookingId: string) => {
    setEvalBookingId(bookingId);
    setSubmitFeedbackModalVisible(true);
  };

  const handleSaveEvaluation = async () => {
    const scoreNum = parseFloat(technicalScore);
    if (isNaN(scoreNum) || scoreNum < 0 || scoreNum > 100) {
      Alert.alert('Invalid Score', 'Please enter a technical score between 0 and 100.');
      return;
    }

    const strengths = strengthsText
      .split(',')
      .map((s) => s.trim())
      .filter(Boolean);
    const improvements = improvementText
      .split(',')
      .map((s) => s.trim())
      .filter(Boolean);
    const topics = recommendedTopicsText
      .split(',')
      .map((s) => s.trim())
      .filter(Boolean);

    setIsSubmitting(true);
    try {
      const res = await ApiClient.submitLiveInterviewFeedback(evalBookingId, {
        technical_score: scoreNum,
        communication_feedback: commFeedback.trim(),
        problem_solving_feedback: problemSolvingFeedback.trim(),
        strengths,
        areas_for_improvement: improvements,
        teacher_comments: teacherComments.trim(),
        recommended_topics: topics,
      });

      setIsSubmitting(false);
      if (res.success) {
        setSubmitFeedbackModalVisible(false);
        setActiveRoomInfo(null);
        if (isTeacher) {
          router.replace('/faculty-dashboard' as any);
        } else {
          router.replace('/home' as any);
        }
      } else {
        Alert.alert('Submission Error', res.message || 'Could not save feedback.');
      }
    } catch (e: any) {
      setIsSubmitting(false);
      Alert.alert('Error', e.message);
    }
  };

  // =============================================================
  // RENDER: IN-MEETING VIDEO CALL ROOM
  // =============================================================
  if (currentView === 'in-meeting' && activeRoomInfo) {
    const isTeacherRole = activeRoomInfo.current_user_role === 'teacher';
    const otherName = isTeacherRole ? activeRoomInfo.student_name : activeRoomInfo.teacher_name;
    const otherRole = isTeacherRole ? 'student' : 'teacher';

    return (
      <SafeAreaView style={{ flex: 1, backgroundColor: '#0F172A' }}>
        <StatusBar barStyle="light-content" backgroundColor="#0F172A" />
        <SkillExaLiveMeetingRoom
          roomId={activeRoomInfo.room_id}
          secureRoomId={activeRoomInfo.secure_room_id}
          bookingId={activeRoomInfo.booking_id}
          currentUserId={profile.id || 'usr-me'}
          currentUserName={profile.name || (isTeacherRole ? 'Faculty' : 'Student')}
          currentUserRole={isTeacherRole ? 'teacher' : 'student'}
          otherParticipantName={otherName || 'Participant'}
          otherParticipantRole={otherRole}
          interviewTitle={activeRoomInfo.subject}
          category={activeRoomInfo.interview_category}
          iceServers={activeRoomInfo.ice_servers}
          initialIsWaiting={activeRoomInfo.is_waiting}
          onLeaveMeeting={() => {
            if (isTeacher) {
              router.replace('/faculty-dashboard' as any);
            } else {
              router.replace('/home' as any);
            }
          }}
          onOpenFeedback={() => {
            setCurrentView('list');
            handleOpenSubmitFeedback(activeRoomInfo.booking_id);
          }}
        />
      </SafeAreaView>
    );
  }

  // =============================================================
  // RENDER: PORTAL (SCHEDULES & DASHBOARD)
  // =============================================================
  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader
        showBack
        title="SkillExa Live Interview"
        subtitle={
          isTeacher
            ? 'Faculty & Placement Interviewer Dashboard'
            : 'Candidate Video Panel Dashboard'
        }
        onBack={() => {
          if (isTeacher) {
            router.replace('/faculty-dashboard' as any);
          } else {
            router.replace('/home' as any);
          }
        }}
      />

      {/* Hero Welcome Banner */}
      <View style={styles.heroBanner}>
        <View style={styles.heroBadge}>
          <Feather name="video" size={24} color="#FFFFFF" />
        </View>
        <View style={{ flex: 1 }}>
          <Text style={styles.heroTitle}>
            {isTeacher ? 'Faculty Live Interview Console' : 'Placement Video Interviews'}
          </Text>
          <Text style={styles.heroSubtitle}>
            {isTeacher
              ? 'Schedule, manage, and conduct human-to-human video panels with real-time screen sharing and placement grading.'
              : 'Join live camera and microphone interviews with authorized faculty panels and view official evaluation results.'}
          </Text>
        </View>
      </View>

      {/* Student: Join by Room Code Card */}
      {!isTeacher && (
        <View style={styles.joinCodeCard}>
          <View style={styles.joinCodeHeaderRow}>
            <Feather name="log-in" size={16} color={Palette.primary} />
            <Text style={styles.joinCodeTitle}>Join with Room Code</Text>
          </View>
          <View style={styles.joinCodeInputRow}>
            <TextInput
              style={styles.joinCodeInput}
              placeholder="e.g. LIVE-TECH-94A2B"
              placeholderTextColor="#94A3B8"
              value={roomCodeInput}
              onChangeText={(text) => {
                setRoomCodeInput(text);
                setRoomCodeError(null);
              }}
              autoCapitalize="characters"
            />
            <TouchableOpacity
              style={[styles.joinCodeBtn, isValidatingCode && { opacity: 0.6 }]}
              onPress={handleJoinByRoomCode}
              disabled={isValidatingCode}
            >
              {isValidatingCode ? (
                <ActivityIndicator size="small" color="#FFFFFF" />
              ) : (
                <>
                  <Feather name="arrow-right" size={16} color="#FFFFFF" />
                  <Text style={styles.joinCodeBtnText}>Enter Room</Text>
                </>
              )}
            </TouchableOpacity>
          </View>
          {roomCodeError ? (
            <Text style={styles.joinCodeErrorText}>{roomCodeError}</Text>
          ) : null}
        </View>
      )}

      {/* Tab Switcher (Faculty has Schedule tab; Student only views assigned interviews) */}
      <View style={styles.tabBar}>
        <TouchableOpacity
          style={[styles.tabBtn, currentView === 'list' && styles.tabBtnActive]}
          onPress={() => {
            setCurrentView('list');
            loadBookings();
          }}
        >
          <Feather
            name="calendar"
            size={16}
            color={currentView === 'list' ? Palette.primary : '#64748B'}
          />
          <Text style={[styles.tabBtnText, currentView === 'list' && styles.tabBtnTextActive]}>
            {isTeacher ? `Interviews (${bookings.length})` : `My Assigned Interviews (${bookings.length})`}
          </Text>
        </TouchableOpacity>

        {isTeacher && (
          <TouchableOpacity
            style={[styles.tabBtn, currentView === 'schedule' && styles.tabBtnActive]}
            onPress={() => {
              setFormError(null);
              setFormSuccess(null);
              setCurrentView('schedule');
            }}
          >
            <Feather
              name="plus-circle"
              size={16}
              color={currentView === 'schedule' ? Palette.primary : '#64748B'}
            />
            <Text
              style={[
                styles.tabBtnText,
                currentView === 'schedule' && styles.tabBtnTextActive,
              ]}
            >
              Schedule Interview
            </Text>
          </TouchableOpacity>
        )}
      </View>

      {/* TAB CONTENT: MY INTERVIEWS */}
      {currentView === 'list' ? (
        <ScrollView
          style={styles.contentScroll}
          contentContainerStyle={{ padding: 16 }}
          refreshControl={
            <RefreshControl
              refreshing={isRefreshing}
              onRefresh={() => {
                setIsRefreshing(true);
                loadBookings();
              }}
            />
          }
        >
          {/* Status Filter Chips */}
          <ScrollView horizontal showsHorizontalScrollIndicator={false} style={styles.filterScroll}>
            {['ALL', 'Scheduled', 'Confirmed', 'In Progress', 'Completed', 'Cancelled'].map((st) => (
              <TouchableOpacity
                key={st}
                style={[styles.filterChip, statusFilter === st && styles.filterChipActive]}
                onPress={() => setStatusFilter(st)}
              >
                <Text
                  style={[
                    styles.filterChipText,
                    statusFilter === st && styles.filterChipTextActive,
                  ]}
                >
                  {st}
                </Text>
              </TouchableOpacity>
            ))}
          </ScrollView>

          {formSuccess ? (
            <View style={styles.successBannerList}>
              <View style={{ flexDirection: 'row', alignItems: 'center', gap: 8, flex: 1 }}>
                <Feather name="check-circle" size={16} color="#16A34A" />
                <Text style={styles.successBannerListText}>{formSuccess}</Text>
              </View>
              <TouchableOpacity onPress={() => setFormSuccess(null)}>
                <Feather name="x" size={16} color="#16A34A" />
              </TouchableOpacity>
            </View>
          ) : null}

          {isLoading ? (
            <View style={styles.centerBox}>
              <ActivityIndicator size="large" color={Palette.primary} />
              <Text style={styles.loadingText}>Loading interview schedule...</Text>
            </View>
          ) : bookings.length === 0 ? (
            <View style={styles.emptyCard}>
              <Feather name="video-off" size={42} color="#CBD5E1" />
              <Text style={styles.emptyTitle}>No Interviews Scheduled</Text>
              <Text style={styles.emptyDesc}>
                {isTeacher
                  ? 'You have not scheduled any live interviews yet. Click "Schedule Interview" to book a candidate.'
                  : 'You have no scheduled live interviews. Your faculty or placement coordinator will invite you when an interview is booked.'}
              </Text>
              {isTeacher && (
                <TouchableOpacity
                  style={styles.primaryActionBtn}
                  onPress={() => setCurrentView('schedule')}
                >
                  <Feather name="plus" size={16} color="#FFFFFF" />
                  <Text style={styles.primaryActionBtnText}>Schedule Candidate</Text>
                </TouchableOpacity>
              )}
            </View>
          ) : (
            bookings.map((b) => {
              const otherPerson = isTeacher ? b.student_name : b.teacher_name;
              const isScheduledOrConfirmed =
                b.booking_status === 'Scheduled' ||
                b.booking_status === 'Confirmed' ||
                b.booking_status === 'In Progress';

              return (
                <View key={b.id} style={styles.bookingCard}>
                  {/* Card Header */}
                  <View style={styles.bookingCardHeader}>
                    <View style={styles.categoryPill}>
                      <Text style={styles.categoryPillText}>{b.interview_category}</Text>
                    </View>

                    <View
                      style={[
                        styles.statusBadge,
                        b.booking_status === 'Scheduled' && { backgroundColor: '#FEF3C7', borderColor: '#FDE68A' },
                        b.booking_status === 'Confirmed' && styles.statusBadgeConfirmed,
                        b.booking_status === 'In Progress' && styles.statusBadgeActive,
                        b.booking_status === 'Completed' && styles.statusBadgeCompleted,
                        b.booking_status === 'Cancelled' && styles.statusBadgeCancelled,
                      ]}
                    >
                      <Text
                        style={[
                          styles.statusBadgeText,
                          b.booking_status === 'Scheduled' && { color: '#B45309' },
                          b.booking_status === 'Confirmed' && styles.statusTextConfirmed,
                          b.booking_status === 'In Progress' && styles.statusTextActive,
                          b.booking_status === 'Completed' && styles.statusTextCompleted,
                          b.booking_status === 'Cancelled' && styles.statusTextCancelled,
                        ]}
                      >
                        {b.booking_status === 'Scheduled' && !isTeacher ? 'Pending Confirmation' : b.booking_status}
                      </Text>
                    </View>
                  </View>

                  {/* Subject Title */}
                  <Text style={styles.bookingSubject}>{b.subject}</Text>

                  {/* Room Code Display with 1-click Copy */}
                  <View style={styles.roomCodeCardRow}>
                    <View style={styles.roomCodeBadge}>
                      <Feather name="key" size={12} color="#4F46E5" />
                      <Text style={styles.roomCodeLabel}>ROOM CODE:</Text>
                      <Text style={styles.roomCodeValue}>{b.secure_room_id}</Text>
                    </View>
                    <TouchableOpacity
                      style={styles.copyCodeBtn}
                      onPress={() => handleCopyCardRoomCode(b.secure_room_id, b.id)}
                    >
                      <Feather
                        name={copiedCodeId === b.id ? 'check' : 'copy'}
                        size={13}
                        color={copiedCodeId === b.id ? '#16A34A' : '#4F46E5'}
                      />
                      <Text
                        style={[
                          styles.copyCodeBtnText,
                          copiedCodeId === b.id && { color: '#16A34A' },
                        ]}
                      >
                        {copiedCodeId === b.id ? 'Copied!' : 'Copy Code'}
                      </Text>
                    </TouchableOpacity>
                  </View>

                  {/* Meta Details */}
                  <View style={styles.bookingMetaRow}>
                    <View style={styles.metaItem}>
                      <Feather name="calendar" size={13} color="#64748B" />
                      <Text style={styles.metaText}>
                        {new Date(b.scheduled_at).toLocaleDateString('en-US', {
                          weekday: 'short',
                          month: 'short',
                          day: 'numeric',
                        })}
                      </Text>
                    </View>

                    <View style={styles.metaItem}>
                      <Feather name="clock" size={13} color="#64748B" />
                      <Text style={styles.metaText}>
                        {new Date(b.scheduled_at).toLocaleTimeString('en-US', {
                          hour: '2-digit',
                          minute: '2-digit',
                        })}{' '}
                        ({b.duration_minutes} mins)
                      </Text>
                    </View>

                    <View style={styles.metaItem}>
                      <Feather name="user" size={13} color="#64748B" />
                      <Text style={styles.metaText}>
                        {isTeacher ? 'Candidate: ' : 'Faculty Interviewer: '}
                        <Text style={{ fontWeight: '700', color: '#0F172A' }}>{otherPerson}</Text>
                        {!isTeacher && b.teacher_email ? (
                          <Text style={{ color: '#64748B', fontSize: 11 }}> ({b.teacher_email})</Text>
                        ) : null}
                      </Text>
                    </View>
                  </View>

                  {/* Instructions if available */}
                  {b.instructions ? (
                    <View style={styles.instructionsBox}>
                      <Feather name="info" size={12} color="#3B82F6" style={{ marginTop: 2 }} />
                      <Text style={styles.instructionsText} numberOfLines={2}>
                        {b.instructions}
                      </Text>
                    </View>
                  ) : null}

                  {/* Preparation materials if available */}
                  {b.preparation_materials ? (
                    <View style={[styles.instructionsBox, { backgroundColor: '#EEF2FF', borderColor: '#C7D2FE', marginTop: 6 }]}>
                      <Feather name="book-open" size={12} color="#4F46E5" style={{ marginTop: 2 }} />
                      <Text style={[styles.instructionsText, { color: '#3730A3' }]} numberOfLines={2}>
                        <Text style={{ fontWeight: '700' }}>Preparation Topics: </Text>
                        {b.preparation_materials}
                      </Text>
                    </View>
                  ) : null}

                  {/* Card Actions */}
                  <View style={styles.cardActionsRow}>
                    {isScheduledOrConfirmed && (
                      <TouchableOpacity
                        style={styles.joinBtn}
                        onPress={() => joinRoomById(b.secure_room_id, b)}
                      >
                        <Feather name="video" size={15} color="#FFFFFF" />
                        <Text style={styles.joinBtnText}>
                          {isTeacher ? 'Start Live Room' : 'Join Interview'}
                        </Text>
                      </TouchableOpacity>
                    )}

                    {!isTeacher && b.booking_status === 'Scheduled' && (
                      <TouchableOpacity
                        style={styles.confirmBtn}
                        onPress={() => handleConfirmBooking(b.id)}
                      >
                        <Feather name="check" size={14} color="#16A34A" />
                        <Text style={styles.confirmBtnText}>Confirm Interview</Text>
                      </TouchableOpacity>
                    )}

                    {b.has_feedback && (
                      <TouchableOpacity
                        style={styles.feedbackBtn}
                        onPress={() => handleViewFeedback(b.id)}
                      >
                        <Feather name="award" size={14} color="#4F46E5" />
                        <Text style={styles.feedbackBtnText}>View Feedback</Text>
                      </TouchableOpacity>
                    )}

                    {isTeacher &&
                      (b.booking_status === 'Completed' || b.booking_status === 'In Progress') && (
                        <TouchableOpacity
                          style={styles.gradeBtn}
                          onPress={() => handleOpenSubmitFeedback(b.id)}
                        >
                          <Feather name="edit-3" size={14} color="#EA580C" />
                          <Text style={styles.gradeBtnText}>
                            {b.has_feedback ? 'Edit Grade' : 'Submit Feedback'}
                          </Text>
                        </TouchableOpacity>
                      )}

                    {isTeacher && isScheduledOrConfirmed && (
                      <TouchableOpacity
                        style={styles.rescheduleBtn}
                        onPress={() => handleOpenReschedule(b)}
                      >
                        <Feather name="calendar" size={14} color="#475569" />
                        <Text style={styles.rescheduleBtnText}>Reschedule</Text>
                      </TouchableOpacity>
                    )}

                    {isScheduledOrConfirmed && (
                      <TouchableOpacity
                        style={styles.cancelActionBtn}
                        onPress={() => handleOpenCancel(b.id)}
                      >
                        <Feather name="x" size={14} color="#EF4444" />
                      </TouchableOpacity>
                    )}
                  </View>
                </View>
              );
            })
          )}
        </ScrollView>
      ) : (
        /* TAB CONTENT: SCHEDULE INTERVIEW (TEACHER ONLY) */
        <ScrollView style={styles.contentScroll} contentContainerStyle={{ padding: 16 }}>
          <View style={styles.formCard}>
            <Text style={styles.formSectionTitle}>1. Candidate Selection</Text>
            <Text style={styles.formFieldLabel}>SELECT STUDENT</Text>
            {students.length > 0 ? (
              <ScrollView
                horizontal
                showsHorizontalScrollIndicator={false}
                style={styles.candidateSelectScroll}
              >
                {students.map((s) => {
                  const uid = s.user_id || s.id;
                  const active = selectedStudentId === uid;
                  return (
                    <TouchableOpacity
                      key={uid}
                      style={[styles.candidateChip, active && styles.candidateChipActive]}
                      onPress={() => setSelectedStudentId(uid)}
                    >
                      <View
                        style={[
                          styles.candidateAvatarCircle,
                          active && { backgroundColor: Palette.primary },
                        ]}
                      >
                        <Text
                          style={[
                            styles.candidateAvatarLetter,
                            active && { color: '#FFFFFF' },
                          ]}
                        >
                          {s.name.charAt(0)}
                        </Text>
                      </View>
                      <View>
                        <Text
                          style={[
                            styles.candidateNameText,
                            active && styles.candidateNameActive,
                          ]}
                        >
                          {s.name}
                        </Text>
                        <Text style={styles.candidateBranchText}>
                          {s.branch} • {s.academic_year}
                        </Text>
                      </View>
                    </TouchableOpacity>
                  );
                })}
              </ScrollView>
            ) : (
              <TextInput
                style={styles.formInput}
                placeholder="Enter Student ID (e.g. 753d5be3-55a1-4ef9-a1c7-46de21ac4b44)"
                placeholderTextColor="#94A3B8"
                value={selectedStudentId}
                onChangeText={setSelectedStudentId}
              />
            )}

            <Text style={[styles.formSectionTitle, { marginTop: 20 }]}>
              2. Category & Subject Focus
            </Text>
            <Text style={styles.formFieldLabel}>INTERVIEW CATEGORY</Text>
            <ScrollView
              horizontal
              showsHorizontalScrollIndicator={false}
              style={styles.candidateSelectScroll}
            >
              {CATEGORIES.map((cat) => {
                const active = selectedCategory === cat;
                return (
                  <TouchableOpacity
                    key={cat}
                    style={[styles.catChip, active && styles.catChipActive]}
                    onPress={() => setSelectedCategory(cat)}
                  >
                    <Text style={[styles.catChipText, active && styles.catChipTextActive]}>
                      {cat}
                    </Text>
                  </TouchableOpacity>
                );
              })}
            </ScrollView>

            <Text style={[styles.formFieldLabel, { marginTop: 12 }]}>SUBJECT / ROLE FOCUS</Text>
            <TextInput
              style={styles.formInput}
              placeholder="e.g. Full Stack React & FastAPI, Embedded C, DSA"
              placeholderTextColor="#94A3B8"
              value={subject}
              onChangeText={setSubject}
            />

            <Text style={[styles.formSectionTitle, { marginTop: 20 }]}>
              3. Date, Time & Duration
            </Text>
            <View style={styles.formRow}>
              <View style={{ flex: 1 }}>
                <Text style={styles.formFieldLabel}>DATE (YYYY-MM-DD)</Text>
                <TextInput
                  style={styles.formInput}
                  value={scheduledDateStr}
                  onChangeText={setScheduledDateStr}
                  placeholder="2026-10-27"
                />
              </View>
              <View style={{ flex: 1 }}>
                <Text style={styles.formFieldLabel}>START TIME (HH:MM)</Text>
                <TextInput
                  style={styles.formInput}
                  value={scheduledTimeStr}
                  onChangeText={setScheduledTimeStr}
                  placeholder="11:00 AM"
                />
              </View>
            </View>

            <Text style={[styles.formFieldLabel, { marginTop: 12 }]}>DURATION</Text>
            <View style={styles.durationRow}>
              {DURATIONS.map((dur) => {
                const active = durationMinutes === dur;
                return (
                  <TouchableOpacity
                    key={dur}
                    style={[styles.durBtn, active && styles.durBtnActive]}
                    onPress={() => setDurationMinutes(dur)}
                  >
                    <Text style={[styles.durBtnText, active && styles.durBtnTextActive]}>
                      {dur} mins
                    </Text>
                  </TouchableOpacity>
                );
              })}
            </View>

            <Text style={[styles.formSectionTitle, { marginTop: 20 }]}>
              4. Instructions & Preparation
            </Text>
            <Text style={styles.formFieldLabel}>INTERVIEW INSTRUCTIONS (OPTIONAL)</Text>
            <TextInput
              style={[styles.formInput, styles.formTextArea]}
              multiline
              numberOfLines={3}
              placeholder="Specific instructions or expectations for the student..."
              placeholderTextColor="#94A3B8"
              value={instructions}
              onChangeText={setInstructions}
            />

            <Text style={[styles.formFieldLabel, { marginTop: 12 }]}>
              PREPARATION MATERIALS (OPTIONAL)
            </Text>
            <TextInput
              style={[styles.formInput, styles.formTextArea]}
              multiline
              numberOfLines={2}
              placeholder="Recommended reading, chapters, or repository references..."
              placeholderTextColor="#94A3B8"
              value={prepMaterials}
              onChangeText={setPrepMaterials}
            />

            {formError ? (
              <View style={styles.formAlertError}>
                <Feather name="alert-circle" size={16} color="#DC2626" />
                <Text style={styles.formAlertErrorText}>{formError}</Text>
              </View>
            ) : null}

            {formSuccess ? (
              <View style={styles.formAlertSuccess}>
                <Feather name="check-circle" size={16} color="#16A34A" />
                <Text style={styles.formAlertSuccessText}>{formSuccess}</Text>
              </View>
            ) : null}

            <TouchableOpacity
              style={[styles.scheduleSubmitBtn, isSubmitting && { opacity: 0.6 }]}
              onPress={handleScheduleSubmit}
              disabled={isSubmitting}
            >
              {isSubmitting ? (
                <ActivityIndicator color="#FFFFFF" />
              ) : (
                <>
                  <Feather name="calendar" size={18} color="#FFFFFF" />
                  <Text style={styles.scheduleSubmitBtnText}>Schedule & Send Invitation</Text>
                </>
              )}
            </TouchableOpacity>
          </View>
        </ScrollView>
      )}

      {/* MODAL: RESCHEDULE INTERVIEW */}
      <Modal visible={rescheduleModalVisible} animationType="fade" transparent>
        <View style={styles.confirmModalOverlay}>
          <View style={styles.confirmModalCard}>
            <View style={styles.confirmModalHeader}>
              <Feather name="calendar" size={22} color={Palette.primary} />
              <Text style={styles.confirmModalTitle}>Reschedule Interview</Text>
            </View>

            <View style={{ gap: 12, marginVertical: 14 }}>
              <View>
                <Text style={styles.formFieldLabel}>NEW DATE (YYYY-MM-DD)</Text>
                <TextInput
                  style={styles.formInput}
                  value={rescheduleDateStr}
                  onChangeText={setRescheduleDateStr}
                  placeholder="2026-10-28"
                />
              </View>
              <View>
                <Text style={styles.formFieldLabel}>NEW TIME (HH:MM or AM/PM)</Text>
                <TextInput
                  style={styles.formInput}
                  value={rescheduleTimeStr}
                  onChangeText={setRescheduleTimeStr}
                  placeholder="02:30 PM"
                />
              </View>
              <View>
                <Text style={styles.formFieldLabel}>DURATION</Text>
                <View style={styles.durationRow}>
                  {DURATIONS.map((dur) => (
                    <TouchableOpacity
                      key={dur}
                      style={[
                        styles.durBtn,
                        rescheduleDuration === dur && styles.durBtnActive,
                      ]}
                      onPress={() => setRescheduleDuration(dur)}
                    >
                      <Text
                        style={[
                          styles.durBtnText,
                          rescheduleDuration === dur && styles.durBtnTextActive,
                        ]}
                      >
                        {dur}m
                      </Text>
                    </TouchableOpacity>
                  ))}
                </View>
              </View>
            </View>

            <View style={styles.confirmModalActionsRow}>
              <TouchableOpacity
                style={styles.confirmModalCancelBtn}
                onPress={() => setRescheduleModalVisible(false)}
                disabled={isRescheduling}
              >
                <Text style={styles.confirmModalCancelText}>Cancel</Text>
              </TouchableOpacity>
              <TouchableOpacity
                style={styles.primaryActionModalBtn}
                onPress={handleSaveReschedule}
                disabled={isRescheduling}
              >
                {isRescheduling ? (
                  <ActivityIndicator size="small" color="#FFFFFF" />
                ) : (
                  <Text style={styles.primaryActionModalBtnText}>Update Schedule</Text>
                )}
              </TouchableOpacity>
            </View>
          </View>
        </View>
      </Modal>

      {/* MODAL: CANCEL INTERVIEW CONFIRMATION */}
      <Modal visible={cancelModalVisible} animationType="fade" transparent>
        <View style={styles.confirmModalOverlay}>
          <View style={styles.confirmModalCard}>
            <View style={styles.confirmModalHeader}>
              <Feather name="alert-triangle" size={24} color="#EF4444" />
              <Text style={styles.confirmModalTitle}>Cancel Interview Booking?</Text>
            </View>
            <Text style={styles.confirmModalDesc}>
              Are you sure you want to cancel this live interview? Both the host and candidate will no longer be able to join this room.
            </Text>
            <View style={styles.confirmModalActionsRow}>
              <TouchableOpacity
                style={styles.confirmModalCancelBtn}
                onPress={() => setCancelModalVisible(false)}
                disabled={isCancelling}
              >
                <Text style={styles.confirmModalCancelText}>Keep</Text>
              </TouchableOpacity>
              <TouchableOpacity
                style={styles.confirmModalDangerBtn}
                onPress={handleConfirmCancel}
                disabled={isCancelling}
              >
                {isCancelling ? (
                  <ActivityIndicator size="small" color="#FFFFFF" />
                ) : (
                  <Text style={styles.confirmModalDangerText}>Yes, Cancel</Text>
                )}
              </TouchableOpacity>
            </View>
          </View>
        </View>
      </Modal>

      {/* MODAL: VIEW EVALUATION REPORT */}
      <Modal visible={feedbackModalVisible} animationType="slide" transparent>
        <View style={styles.modalOverlay}>
          <View style={styles.feedbackReportModal}>
            <View style={styles.modalHeader}>
              <View style={{ flexDirection: 'row', alignItems: 'center', gap: 8 }}>
                <Feather name="award" size={20} color="#F59E0B" />
                <Text style={styles.modalTitle}>Official Interview Evaluation</Text>
              </View>
              <TouchableOpacity onPress={() => setFeedbackModalVisible(false)}>
                <Feather name="x" size={20} color="#64748B" />
              </TouchableOpacity>
            </View>

            <ScrollView style={{ flex: 1 }} contentContainerStyle={{ padding: 20 }}>
              {isLoadingFeedback ? (
                <ActivityIndicator size="large" color={Palette.primary} />
              ) : !feedbackData ? (
                <View style={styles.emptyCard}>
                  <Text style={styles.emptyTitle}>Feedback Pending</Text>
                  <Text style={styles.emptyDesc}>
                    The evaluator has not submitted feedback for this interview yet.
                  </Text>
                </View>
              ) : (
                <>
                  {/* Score Hero */}
                  <View style={styles.scoreHeroCard}>
                    <View style={styles.scoreCircle}>
                      <Text style={styles.scoreBigText}>
                        {Math.round(feedbackData.technical_score)}%
                      </Text>
                      <Text style={styles.scoreCircleLabel}>Technical Score</Text>
                    </View>
                    <View style={{ flex: 1, gap: 4 }}>
                      <Text style={styles.scoreVerdictTitle}>
                        {feedbackData.technical_score >= 80
                          ? 'Placement Ready'
                          : feedbackData.technical_score >= 60
                          ? 'Proficient with Gaps'
                          : 'Needs Further Preparation'}
                      </Text>
                      <Text style={styles.scoreEvaluatorText}>
                        Evaluated by {feedbackData.teacher_name}
                      </Text>
                      <Text style={styles.scoreDateText}>
                        {new Date(feedbackData.submitted_at).toLocaleDateString()}
                      </Text>
                    </View>
                  </View>

                  {/* Communication Feedback */}
                  <View style={styles.feedbackSection}>
                    <Text style={styles.feedbackSectionHeading}>
                      <Feather name="message-square" size={14} color={Palette.primary} /> Communication
                      Skills
                    </Text>
                    <Text style={styles.feedbackSectionBody}>
                      {feedbackData.communication_feedback}
                    </Text>
                  </View>

                  {/* Problem Solving Feedback */}
                  <View style={styles.feedbackSection}>
                    <Text style={styles.feedbackSectionHeading}>
                      <Feather name="cpu" size={14} color={Palette.aiPurple} /> Problem Solving &
                      Reasoning
                    </Text>
                    <Text style={styles.feedbackSectionBody}>
                      {feedbackData.problem_solving_feedback}
                    </Text>
                  </View>

                  {/* Strengths */}
                  {feedbackData.strengths && feedbackData.strengths.length > 0 && (
                    <View style={styles.feedbackSection}>
                      <Text style={styles.feedbackSectionHeading}>
                        <Feather name="check-circle" size={14} color="#16A34A" /> Identified Strengths
                      </Text>
                      <View style={styles.chipsWrap}>
                        {feedbackData.strengths.map((str: string, idx: number) => (
                          <View key={idx} style={styles.strengthChip}>
                            <Text style={styles.strengthChipText}>{str}</Text>
                          </View>
                        ))}
                      </View>
                    </View>
                  )}

                  {/* Areas for Improvement */}
                  {feedbackData.areas_for_improvement &&
                    feedbackData.areas_for_improvement.length > 0 && (
                      <View style={styles.feedbackSection}>
                        <Text style={styles.feedbackSectionHeading}>
                          <Feather name="target" size={14} color="#DC2626" /> Recommended Focus Areas
                        </Text>
                        <View style={styles.chipsWrap}>
                          {feedbackData.areas_for_improvement.map((item: string, idx: number) => (
                            <View key={idx} style={styles.improveChip}>
                              <Text style={styles.improveChipText}>{item}</Text>
                            </View>
                          ))}
                        </View>
                      </View>
                    )}

                  {/* Recommended Topics */}
                  {feedbackData.recommended_topics &&
                    feedbackData.recommended_topics.length > 0 && (
                      <View style={styles.feedbackSection}>
                        <Text style={styles.feedbackSectionHeading}>
                          <Feather name="book-open" size={14} color="#2563EB" /> Recommended Practice
                          Topics
                        </Text>
                        <View style={styles.chipsWrap}>
                          {feedbackData.recommended_topics.map((t: string, idx: number) => (
                            <View key={idx} style={styles.topicChip}>
                              <Text style={styles.topicChipText}>{t}</Text>
                            </View>
                          ))}
                        </View>
                      </View>
                    )}

                  {/* Comments */}
                  {feedbackData.teacher_comments ? (
                    <View style={styles.feedbackSection}>
                      <Text style={styles.feedbackSectionHeading}>
                        <Feather name="file-text" size={14} color="#64748B" /> Evaluator Final Notes
                      </Text>
                      <Text style={styles.feedbackSectionBody}>
                        {feedbackData.teacher_comments}
                      </Text>
                    </View>
                  ) : null}
                </>
              )}
            </ScrollView>
          </View>
        </View>
      </Modal>

      {/* MODAL: TEACHER SUBMIT EVALUATION */}
      <Modal visible={submitFeedbackModalVisible} animationType="slide" transparent>
        <View style={styles.modalOverlay}>
          <View style={styles.feedbackReportModal}>
            <View style={styles.modalHeader}>
              <View style={{ flexDirection: 'row', alignItems: 'center', gap: 8 }}>
                <Feather name="edit" size={20} color={Palette.primary} />
                <Text style={styles.modalTitle}>Grade Interview Session</Text>
              </View>
              <TouchableOpacity onPress={() => {
                setSubmitFeedbackModalVisible(false);
                if (isTeacher && activeRoomInfo) {
                  setActiveRoomInfo(null);
                  router.replace('/faculty-dashboard' as any);
                }
              }}>
                <Feather name="x" size={20} color="#64748B" />
              </TouchableOpacity>
            </View>

            <ScrollView style={{ flex: 1 }} contentContainerStyle={{ padding: 20 }}>
              <Text style={styles.formFieldLabel}>TECHNICAL KNOWLEDGE SCORE (0 - 100)</Text>
              <TextInput
                style={styles.formInput}
                keyboardType="numeric"
                value={technicalScore}
                onChangeText={setTechnicalScore}
                placeholder="85"
              />

              <Text style={[styles.formFieldLabel, { marginTop: 14 }]}>COMMUNICATION ASSESSMENT</Text>
              <TextInput
                style={[styles.formInput, styles.formTextArea]}
                multiline
                numberOfLines={3}
                value={commFeedback}
                onChangeText={setCommFeedback}
                placeholder="Candidate clarity, vocabulary, pacing..."
              />

              <Text style={[styles.formFieldLabel, { marginTop: 14 }]}>
                PROBLEM SOLVING ASSESSMENT
              </Text>
              <TextInput
                style={[styles.formInput, styles.formTextArea]}
                multiline
                numberOfLines={3}
                value={problemSolvingFeedback}
                onChangeText={setProblemSolvingFeedback}
                placeholder="Reasoning, debugging approach, edge cases..."
              />

              <Text style={[styles.formFieldLabel, { marginTop: 14 }]}>
                CANDIDATE STRENGTHS (COMMA-SEPARATED)
              </Text>
              <TextInput
                style={styles.formInput}
                value={strengthsText}
                onChangeText={setStrengthsText}
                placeholder="Clear communication, Strong algorithms, Confident"
              />

              <Text style={[styles.formFieldLabel, { marginTop: 14 }]}>
                AREAS FOR IMPROVEMENT (COMMA-SEPARATED)
              </Text>
              <TextInput
                style={styles.formInput}
                value={improvementText}
                onChangeText={setImprovementText}
                placeholder="Database indexing, Concurrency, Caching"
              />

              <Text style={[styles.formFieldLabel, { marginTop: 14 }]}>
                RECOMMENDED PRACTICE TOPICS
              </Text>
              <TextInput
                style={styles.formInput}
                value={recommendedTopicsText}
                onChangeText={setRecommendedTopicsText}
                placeholder="B-Tree Indexing, Distributed Systems"
              />

              <Text style={[styles.formFieldLabel, { marginTop: 14 }]}>
                FINAL COMMENTS & PLACEMENT RECOMMENDATION
              </Text>
              <TextInput
                style={[styles.formInput, styles.formTextArea]}
                multiline
                numberOfLines={2}
                value={teacherComments}
                onChangeText={setTeacherComments}
                placeholder="Overall recommendations or hiring notes..."
              />

              <TouchableOpacity
                style={[styles.scheduleSubmitBtn, isSubmitting && { opacity: 0.6 }]}
                onPress={handleSaveEvaluation}
                disabled={isSubmitting}
              >
                {isSubmitting ? (
                  <ActivityIndicator color="#FFFFFF" />
                ) : (
                  <>
                    <Feather name="check-circle" size={18} color="#FFFFFF" />
                    <Text style={styles.scheduleSubmitBtnText}>Submit Official Evaluation</Text>
                  </>
                )}
              </TouchableOpacity>
            </ScrollView>
          </View>
        </View>
      </Modal>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: '#F8FAFC' },
  heroBanner: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 14,
    backgroundColor: '#1E293B',
    padding: 16,
    marginHorizontal: 16,
    marginTop: 12,
    borderRadius: Radii.lg,
    ...Shadows.md,
  },
  heroBadge: {
    width: 48,
    height: 48,
    borderRadius: 24,
    backgroundColor: Palette.primary,
    justifyContent: 'center',
    alignItems: 'center',
  },
  heroTitle: {
    fontSize: 16,
    fontWeight: '800',
    color: '#FFFFFF',
  },
  heroSubtitle: {
    fontSize: 12,
    color: '#94A3B8',
    marginTop: 3,
    lineHeight: 17,
  },
  joinCodeCard: {
    backgroundColor: '#FFFFFF',
    marginHorizontal: 16,
    marginTop: 12,
    borderRadius: Radii.lg,
    padding: 14,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    ...Shadows.sm,
  },
  joinCodeHeaderRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    marginBottom: 8,
  },
  joinCodeTitle: {
    fontSize: 13,
    fontWeight: '700',
    color: '#0F172A',
  },
  joinCodeInputRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 10,
  },
  joinCodeInput: {
    flex: 1,
    backgroundColor: '#F8FAFC',
    borderWidth: 1,
    borderColor: '#CBD5E1',
    borderRadius: Radii.md,
    paddingHorizontal: 14,
    paddingVertical: 10,
    fontSize: 14,
    fontFamily: Platform.OS === 'ios' ? 'Menlo' : 'monospace',
    fontWeight: '700',
    color: '#0F172A',
  },
  joinCodeBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    backgroundColor: Palette.primary,
    paddingHorizontal: 16,
    paddingVertical: 12,
    borderRadius: Radii.md,
  },
  joinCodeBtnText: {
    fontSize: 13,
    fontWeight: '700',
    color: '#FFFFFF',
  },
  joinCodeErrorText: {
    fontSize: 12,
    color: '#DC2626',
    fontWeight: '600',
    marginTop: 6,
  },
  tabBar: {
    flexDirection: 'row',
    backgroundColor: '#FFFFFF',
    marginHorizontal: 16,
    marginTop: 14,
    borderRadius: Radii.md,
    padding: 4,
    borderWidth: 1,
    borderColor: '#E2E8F0',
  },
  tabBtn: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
    paddingVertical: 10,
    borderRadius: Radii.sm,
  },
  tabBtnActive: {
    backgroundColor: '#EEF2FF',
  },
  tabBtnText: {
    fontSize: 13,
    fontWeight: '600',
    color: '#64748B',
  },
  tabBtnTextActive: {
    color: Palette.primary,
    fontWeight: '700',
  },
  contentScroll: {
    flex: 1,
  },
  filterScroll: {
    flexDirection: 'row',
    marginBottom: 14,
  },
  filterChip: {
    backgroundColor: '#FFFFFF',
    borderWidth: 1,
    borderColor: '#E2E8F0',
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: Radii.full,
    marginRight: 8,
  },
  filterChipActive: {
    backgroundColor: Palette.primary,
    borderColor: Palette.primary,
  },
  filterChipText: {
    fontSize: 12,
    fontWeight: '600',
    color: '#64748B',
  },
  filterChipTextActive: {
    color: '#FFFFFF',
  },
  centerBox: {
    paddingVertical: 60,
    alignItems: 'center',
    gap: 12,
  },
  loadingText: {
    fontSize: 14,
    color: '#64748B',
  },
  emptyCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.lg,
    padding: 30,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: '#E2E8F0',
    marginTop: 20,
    gap: 8,
  },
  emptyTitle: {
    fontSize: 17,
    fontWeight: '800',
    color: '#0F172A',
    marginTop: 10,
  },
  emptyDesc: {
    fontSize: 13,
    color: '#64748B',
    textAlign: 'center',
    lineHeight: 19,
    maxWidth: 300,
  },
  primaryActionBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    backgroundColor: Palette.primary,
    paddingHorizontal: 18,
    paddingVertical: 10,
    borderRadius: Radii.md,
    marginTop: 14,
  },
  primaryActionBtnText: {
    color: '#FFFFFF',
    fontSize: 13,
    fontWeight: '700',
  },
  bookingCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.lg,
    padding: 16,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    marginBottom: 14,
    ...Shadows.sm,
  },
  bookingCardHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 10,
  },
  categoryPill: {
    backgroundColor: '#F1F5F9',
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 4,
  },
  categoryPillText: {
    fontSize: 11,
    fontWeight: '700',
    color: '#475569',
    textTransform: 'uppercase',
  },
  statusBadge: {
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: Radii.full,
    backgroundColor: '#FEF3C7',
  },
  statusBadgeConfirmed: {
    backgroundColor: '#DBEAFE',
  },
  statusBadgeActive: {
    backgroundColor: '#FAF5FF',
    borderWidth: 1,
    borderColor: '#E9D5FF',
  },
  statusBadgeCompleted: {
    backgroundColor: '#DCFCE7',
  },
  statusBadgeCancelled: {
    backgroundColor: '#FEE2E2',
  },
  statusBadgeText: {
    fontSize: 11,
    fontWeight: '700',
    color: '#B45309',
  },
  statusTextConfirmed: {
    color: '#1D4ED8',
  },
  statusTextActive: {
    color: '#7E22CE',
  },
  statusTextCompleted: {
    color: '#15803D',
  },
  statusTextCancelled: {
    color: '#B91C1C',
  },
  bookingSubject: {
    fontSize: 16,
    fontWeight: '800',
    color: '#0F172A',
    marginBottom: 8,
  },
  roomCodeCardRow: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    backgroundColor: '#F1F5F9',
    paddingHorizontal: 10,
    paddingVertical: 6,
    borderRadius: Radii.sm,
    marginBottom: 10,
  },
  roomCodeBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
  },
  roomCodeLabel: {
    fontSize: 10,
    fontWeight: '800',
    color: '#4F46E5',
  },
  roomCodeValue: {
    fontSize: 12,
    fontFamily: Platform.OS === 'ios' ? 'Menlo' : 'monospace',
    fontWeight: '700',
    color: '#0F172A',
  },
  copyCodeBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
    paddingHorizontal: 6,
    paddingVertical: 2,
  },
  copyCodeBtnText: {
    fontSize: 11,
    fontWeight: '700',
    color: '#4F46E5',
  },
  bookingMetaRow: {
    gap: 6,
    marginBottom: 12,
  },
  metaItem: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  metaText: {
    fontSize: 12.5,
    color: '#64748B',
  },
  instructionsBox: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    gap: 8,
    backgroundColor: '#F8FAFC',
    borderRadius: Radii.sm,
    padding: 10,
    marginBottom: 12,
    borderLeftWidth: 3,
    borderLeftColor: '#3B82F6',
  },
  instructionsText: {
    fontSize: 12,
    color: '#334155',
    lineHeight: 17,
    flex: 1,
  },
  cardActionsRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    borderTopWidth: 1,
    borderTopColor: '#F1F5F9',
    paddingTop: 12,
    flexWrap: 'wrap',
  },
  joinBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    backgroundColor: '#16A34A',
    paddingHorizontal: 14,
    paddingVertical: 8,
    borderRadius: Radii.sm,
  },
  joinBtnText: {
    fontSize: 12.5,
    fontWeight: '700',
    color: '#FFFFFF',
  },
  confirmBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
    backgroundColor: '#F0FDF4',
    borderWidth: 1,
    borderColor: '#BBF7D0',
    paddingHorizontal: 10,
    paddingVertical: 7,
    borderRadius: Radii.sm,
  },
  confirmBtnText: {
    fontSize: 12,
    fontWeight: '700',
    color: '#16A34A',
  },
  feedbackBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
    backgroundColor: '#EEF2FF',
    borderWidth: 1,
    borderColor: '#C7D2FE',
    paddingHorizontal: 10,
    paddingVertical: 7,
    borderRadius: Radii.sm,
  },
  feedbackBtnText: {
    fontSize: 12,
    fontWeight: '700',
    color: '#4F46E5',
  },
  gradeBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
    backgroundColor: '#FFF7ED',
    borderWidth: 1,
    borderColor: '#FFEDD5',
    paddingHorizontal: 10,
    paddingVertical: 7,
    borderRadius: Radii.sm,
  },
  gradeBtnText: {
    fontSize: 12,
    fontWeight: '700',
    color: '#EA580C',
  },
  rescheduleBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
    backgroundColor: '#F8FAFC',
    borderWidth: 1,
    borderColor: '#E2E8F0',
    paddingHorizontal: 10,
    paddingVertical: 7,
    borderRadius: Radii.sm,
  },
  rescheduleBtnText: {
    fontSize: 12,
    fontWeight: '700',
    color: '#475569',
  },
  cancelActionBtn: {
    marginLeft: 'auto',
    padding: 6,
    borderRadius: Radii.sm,
    backgroundColor: '#FEF2F2',
  },
  formCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.lg,
    padding: 20,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    ...Shadows.sm,
  },
  formSectionTitle: {
    fontSize: 15,
    fontWeight: '800',
    color: '#0F172A',
    marginBottom: 12,
  },
  formFieldLabel: {
    fontSize: 11,
    fontWeight: '700',
    color: '#64748B',
    marginBottom: 6,
    textTransform: 'uppercase',
  },
  formInput: {
    backgroundColor: '#F8FAFC',
    borderWidth: 1,
    borderColor: '#CBD5E1',
    borderRadius: Radii.md,
    paddingHorizontal: 12,
    paddingVertical: 10,
    fontSize: 14,
    color: '#0F172A',
  },
  formTextArea: {
    minHeight: 70,
    textAlignVertical: 'top',
  },
  formRow: {
    flexDirection: 'row',
    gap: 10,
  },
  candidateSelectScroll: {
    flexDirection: 'row',
    marginBottom: 8,
  },
  candidateChip: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    backgroundColor: '#F8FAFC',
    borderWidth: 1.5,
    borderColor: '#E2E8F0',
    paddingHorizontal: 12,
    paddingVertical: 8,
    borderRadius: Radii.md,
    marginRight: 10,
  },
  candidateChipActive: {
    borderColor: Palette.primary,
    backgroundColor: '#EEF2FF',
  },
  candidateAvatarCircle: {
    width: 30,
    height: 30,
    borderRadius: 15,
    backgroundColor: '#CBD5E1',
    justifyContent: 'center',
    alignItems: 'center',
  },
  candidateAvatarLetter: {
    fontSize: 13,
    fontWeight: '800',
    color: '#334155',
  },
  candidateNameText: {
    fontSize: 13,
    fontWeight: '700',
    color: '#0F172A',
  },
  candidateNameActive: {
    color: Palette.primary,
  },
  candidateBranchText: {
    fontSize: 11,
    color: '#64748B',
  },
  catChip: {
    backgroundColor: '#F8FAFC',
    borderWidth: 1,
    borderColor: '#CBD5E1',
    paddingHorizontal: 12,
    paddingVertical: 7,
    borderRadius: Radii.full,
    marginRight: 8,
  },
  catChipActive: {
    backgroundColor: Palette.primary,
    borderColor: Palette.primary,
  },
  catChipText: {
    fontSize: 12,
    fontWeight: '600',
    color: '#475569',
  },
  catChipTextActive: {
    color: '#FFFFFF',
    fontWeight: '700',
  },
  durationRow: {
    flexDirection: 'row',
    gap: 8,
    marginBottom: 8,
  },
  durBtn: {
    flex: 1,
    alignItems: 'center',
    paddingVertical: 8,
    backgroundColor: '#F8FAFC',
    borderWidth: 1,
    borderColor: '#CBD5E1',
    borderRadius: Radii.sm,
  },
  durBtnActive: {
    backgroundColor: Palette.primary,
    borderColor: Palette.primary,
  },
  durBtnText: {
    fontSize: 12,
    fontWeight: '600',
    color: '#475569',
  },
  durBtnTextActive: {
    color: '#FFFFFF',
    fontWeight: '700',
  },
  scheduleSubmitBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
    backgroundColor: Palette.primary,
    borderRadius: Radii.md,
    paddingVertical: 14,
    marginTop: 22,
    ...Shadows.md,
  },
  scheduleSubmitBtnText: {
    fontSize: 15,
    fontWeight: '800',
    color: '#FFFFFF',
  },
  modalOverlay: {
    flex: 1,
    backgroundColor: 'rgba(0, 0, 0, 0.6)',
    justifyContent: 'center',
    padding: 16,
  },
  feedbackReportModal: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.lg,
    maxHeight: '85%',
    ...Shadows.floating,
    overflow: 'hidden',
  },
  modalHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: 20,
    paddingVertical: 16,
    borderBottomWidth: 1,
    borderBottomColor: '#F1F5F9',
  },
  modalTitle: {
    fontSize: 16,
    fontWeight: '800',
    color: '#0F172A',
  },
  scoreHeroCard: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 16,
    backgroundColor: '#F8FAFC',
    borderRadius: Radii.md,
    padding: 16,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    marginBottom: 16,
  },
  scoreCircle: {
    width: 80,
    height: 80,
    borderRadius: 40,
    backgroundColor: '#EFF6FF',
    borderWidth: 3,
    borderColor: Palette.primary,
    justifyContent: 'center',
    alignItems: 'center',
  },
  scoreBigText: {
    fontSize: 22,
    fontWeight: '900',
    color: Palette.primary,
  },
  scoreCircleLabel: {
    fontSize: 9,
    fontWeight: '700',
    color: '#64748B',
    textTransform: 'uppercase',
  },
  scoreVerdictTitle: {
    fontSize: 16,
    fontWeight: '800',
    color: '#0F172A',
  },
  scoreEvaluatorText: {
    fontSize: 13,
    color: '#475569',
  },
  scoreDateText: {
    fontSize: 11,
    color: '#94A3B8',
  },
  feedbackSection: {
    marginBottom: 14,
    backgroundColor: '#F8FAFC',
    padding: 12,
    borderRadius: Radii.md,
    borderWidth: 1,
    borderColor: '#F1F5F9',
  },
  feedbackSectionHeading: {
    fontSize: 13,
    fontWeight: '700',
    color: '#0F172A',
    marginBottom: 6,
  },
  feedbackSectionBody: {
    fontSize: 13,
    color: '#334155',
    lineHeight: 19,
  },
  chipsWrap: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 6,
    marginTop: 4,
  },
  strengthChip: {
    backgroundColor: '#DCFCE7',
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: 4,
  },
  strengthChipText: {
    fontSize: 12,
    fontWeight: '600',
    color: '#15803D',
  },
  improveChip: {
    backgroundColor: '#FEE2E2',
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: 4,
  },
  improveChipText: {
    fontSize: 12,
    fontWeight: '600',
    color: '#DC2626',
  },
  topicChip: {
    backgroundColor: '#DBEAFE',
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: 4,
  },
  topicChipText: {
    fontSize: 12,
    fontWeight: '600',
    color: '#1D4ED8',
  },
  formAlertError: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    backgroundColor: '#FEF2F2',
    borderWidth: 1,
    borderColor: '#FCA5A5',
    borderRadius: Radii.sm,
    padding: 12,
    marginTop: 14,
  },
  formAlertErrorText: {
    color: '#B91C1C',
    fontSize: 13,
    fontWeight: '600',
    flex: 1,
  },
  formAlertSuccess: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    backgroundColor: '#F0FDF4',
    borderWidth: 1,
    borderColor: '#86EFAC',
    borderRadius: Radii.sm,
    padding: 12,
    marginTop: 14,
  },
  formAlertSuccessText: {
    color: '#15803D',
    fontSize: 13,
    fontWeight: '600',
    flex: 1,
  },
  successBannerList: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    backgroundColor: '#F0FDF4',
    borderWidth: 1,
    borderColor: '#86EFAC',
    borderRadius: Radii.md,
    padding: 12,
    marginBottom: 12,
  },
  successBannerListText: {
    color: '#15803D',
    fontSize: 13,
    fontWeight: '700',
    flex: 1,
    marginRight: 8,
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
  primaryActionModalBtn: {
    paddingHorizontal: 18,
    paddingVertical: 10,
    borderRadius: Radii.sm,
    backgroundColor: Palette.primary,
    minWidth: 120,
    alignItems: 'center',
  },
  primaryActionModalBtnText: {
    fontSize: 13,
    fontWeight: '800',
    color: '#FFFFFF',
  },
});
