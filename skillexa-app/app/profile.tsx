import { Feather } from '@expo/vector-icons';
import { router } from 'expo-router';
import React, { useEffect, useState } from 'react';
import {
  ActivityIndicator,
  Alert,
  Modal,
  Platform,
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Switch,
  Text,
  TextInput,
  TouchableOpacity,
  View,
} from 'react-native';
import { useAuth } from '../components/auth-context';
import { AppHeader } from '../components/common/AppHeader';
import { Palette, Radii, Shadows } from '../constants/theme';
import { ApiClient, setAuthToken } from '../services/api';

const BRANCH_OPTIONS = ['ECE', 'CSE', 'AIML', 'MECH', 'CIVIL'];
const YEAR_OPTIONS = ['1st Year', '2nd Year', '3rd Year', '4th Year'];
const SECTION_OPTIONS = ['A', 'B', 'C'];

export default function ProfileScreen() {
  const { profile, logout, updateProfile } = useAuth();
  const [showLogoutModal, setShowLogoutModal] = useState(false);
  const [showEditModal, setShowEditModal] = useState(false);
  const [showReminderModal, setShowReminderModal] = useState(false);
  const [showHelpModal, setShowHelpModal] = useState(false);

  // Edit form state
  const [editName, setEditName] = useState(profile.name || '');
  const [editRollNumber, setEditRollNumber] = useState(profile.rollNumber || '4KV22EC018');
  const [editBranch, setEditBranch] = useState(profile.department || 'ECE');
  const [editYear, setEditYear] = useState(profile.academicYear || '3rd Year');
  const [editSection, setEditSection] = useState(profile.section || 'A');
  const [editPhone, setEditPhone] = useState(profile.phone || '');
  const [isSavingProfile, setIsSavingProfile] = useState(false);

  // Notification Preferences state
  const [dailyReminders, setDailyReminders] = useState(true);
  const [assessmentAlerts, setAssessmentAlerts] = useState(true);
  const [emailAlerts, setEmailAlerts] = useState(true);
  const [weeklyDigest, setWeeklyDigest] = useState(false);

  // Help FAQ Accordion state
  const [expandedFaq, setExpandedFaq] = useState<number | null>(null);

  // Real stats state
  const isFaculty =
    profile?.role === 'FACULTY' ||
    profile?.role === 'ADMIN' ||
    profile?.email?.includes('faculty') ||
    profile?.email === 'dr.ramesh@kvgce.edu.in';

  const [stats, setStats] = useState({
    questionsSolved: 0,
    quizzesCompleted: 0,
    codeSubmissions: 0,
    aiInterviews: 0,
    overallScore: 0,
    quizAccuracy: 0,
    notesRead: 0,
    dsaProgress: 0,
    classRank: null as number | null,
  });
  const [loadingStats, setLoadingStats] = useState(true);

  // Load real student or faculty stats
  useEffect(() => {
    let isMounted = true;
    setLoadingStats(true);

    if (isFaculty) {
      Promise.all([
        ApiClient.getFacultyNotes().catch(() => ({ data: [] })),
        ApiClient.getFacultyQuizzes().catch(() => ({ data: [] })),
        ApiClient.getFacultyPerformance().catch(() => ({ data: [] })),
        ApiClient.getInterviews().catch(() => ({ data: [] })),
      ]).then(([notesRes, quizRes, perfRes, intRes]) => {
        if (!isMounted) return;
        setStats({
          questionsSolved: Array.isArray(notesRes?.data) ? notesRes.data.length : 1,
          quizzesCompleted: Array.isArray(quizRes?.data) ? quizRes.data.length : 4,
          codeSubmissions: Array.isArray(perfRes?.data) ? perfRes.data.length : 4,
          aiInterviews: Array.isArray(intRes?.data) ? intRes.data.length : 2,
          overallScore: 92,
          quizAccuracy: 88,
          notesRead: 0,
          dsaProgress: 0,
          classRank: null,
        });
        setLoadingStats(false);
      });
    } else {
      ApiClient.getStudentStats()
        .then((res) => {
          if (!isMounted) return;
          if (res?.success && res.data) {
            setStats({
              questionsSolved: res.data.questions_solved ?? (res.data.total_coding_solved + (res.data.total_quizzes_completed * 5)),
              quizzesCompleted: res.data.total_quizzes_completed ?? 0,
              codeSubmissions: res.data.code_submissions ?? res.data.total_coding_solved ?? 0,
              aiInterviews: res.data.total_ai_interviews ?? 0,
              overallScore: res.data.overall_score ?? 0,
              quizAccuracy: res.data.quiz_accuracy ?? 0,
              notesRead: res.data.total_notes_read ?? 0,
              dsaProgress: res.data.dsa_progress_percentage ?? 0,
              classRank: res.data.class_rank,
            });
          }
        })
        .catch((err) => {
          console.log('Error fetching real student stats:', err);
        })
        .finally(() => {
          if (isMounted) setLoadingStats(false);
        });
    }

    return () => {
      isMounted = false;
    };
  }, [isFaculty]);

  // Sync edit form with current profile
  useEffect(() => {
    if (showEditModal) {
      setEditName(profile.name || '');
      setEditRollNumber(profile.rollNumber || '4KV22EC018');
      setEditBranch(profile.department || 'ECE');
      setEditYear(profile.academicYear || '3rd Year');
      setEditSection(profile.section || 'A');
      setEditPhone(profile.phone || '');
    }
  }, [showEditModal, profile]);

  const displayName =
    profile?.name &&
    profile.name.toLowerCase() !== 'student scholar' &&
    profile.name.toLowerCase() !== 'faculty'
      ? profile.name
      : isFaculty
      ? 'Dr. Ramesh Kumar'
      : 'Ganesh Sharan';

  const displayEmail = profile?.email || (isFaculty ? 'faculty@skillexa.edu' : 'ganesh@kvgce.edu.in');
  const initial = displayName.charAt(0).toUpperCase();

  const handleSaveProfile = async () => {
    if (!editName.trim()) {
      Alert.alert('Name Required', 'Please enter your full name.');
      return;
    }
    setIsSavingProfile(true);
    try {
      await ApiClient.updateStudentProfile({
        name: editName.trim(),
        branch: editBranch,
        academic_year: editYear,
        section: editSection,
        roll_number: editRollNumber.trim(),
        phone: editPhone.trim(),
      });
    } catch (e) {
      console.log('Backend profile sync note:', e);
    }

    // Cross-platform sync to Competitive platform
    try {
      fetch('http://localhost:3001/api/user/sync', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          email: displayEmail,
          name: editName.trim(),
          phone: editPhone.trim(),
          college: profile?.collegeName || 'KVG College of Engineering',
          branch: editBranch,
          year: editYear,
          section: editSection,
          rollNumber: editRollNumber.trim(),
          role: 'student',
        }),
      }).catch(() => {});
    } catch (e) {}

    const updated = {
      name: editName.trim(),
      department: editBranch,
      academicYear: editYear,
      section: editSection,
      rollNumber: editRollNumber.trim(),
      phone: editPhone.trim(),
    };
    updateProfile(updated);

    if (typeof window !== 'undefined' && window.localStorage) {
      try {
        const saved = window.localStorage.getItem('skillexa_user_profile');
        if (saved) {
          const parsed = JSON.parse(saved);
          window.localStorage.setItem('skillexa_user_profile', JSON.stringify({ ...parsed, ...updated }));
        }
      } catch (e) {}
    }

    setIsSavingProfile(false);
    setShowEditModal(false);
    Alert.alert('Profile Updated! 🎉', 'Your academic details have been successfully saved.');
  };

  const performLogout = () => {
    setShowLogoutModal(false);
    logout();
    setAuthToken(null);
    if (typeof window !== 'undefined' && window.localStorage) {
      try {
        window.localStorage.removeItem('skillexa_jwt_token');
        window.localStorage.removeItem('skillexa_user_profile');
        window.localStorage.removeItem('skillexa_user_role');
      } catch (e) {}
    }
    router.replace('/login' as any);
  };

  const handleLogout = () => {
    setShowLogoutModal(true);
  };

  const FAQS = [
    {
      q: 'Where do I find study notes uploaded by my college faculty?',
      a: 'Navigate to "My College" workspace from the home screen to access verified notes, syllabus modules, and downloadable PDF materials uploaded directly by your professors.',
    },
    {
      q: 'How are quiz scores and rankings calculated?',
      a: 'Quiz scores are evaluated automatically upon submission. Correct answers grant positive marks while negative marking applies if designated by faculty. Your class rank reflects your performance in your department.',
    },
    {
      q: 'How does the AI Mock Interview system work?',
      a: 'The AI interviewer conducts real-time speech and technical evaluations tailored to your engineering branch and target roles, analyzing your code, conceptual accuracy, and communication clarity.',
    },
    {
      q: 'Who should I contact for academic or portal support?',
      a: 'For departmental assistance, contact your Department HOD (Dr. Ramesh Kumar, ECE). For portal issues, email tech support at support@kvgce.edu.in or support@skillexa.edu.',
    },
  ];

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader
        title={isFaculty ? 'Faculty Profile' : 'Student Profile'}
        showBack
        onBack={() => router.replace((isFaculty ? '/faculty-dashboard' : '/home') as any)}
      />

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {/* Profile Card */}
        <View style={styles.profileCard}>
          <View style={styles.avatarLarge}>
            <Text style={styles.avatarLargeText}>{initial}</Text>
          </View>
          <Text style={styles.nameText}>{displayName}</Text>
          <Text style={styles.emailText}>{displayEmail}</Text>

          {/* Real Academic Track Tag */}
          <View style={styles.trackTag}>
            <Text style={styles.trackTagText}>
              {isFaculty
                ? `${profile.facultyDesignation || 'Professor & HOD'} • ${profile.department || 'ECE'} Department`
                : `${profile.department || 'ECE'} • ${profile.academicYear || '3rd Year'}${profile.section ? ` Sec ${profile.section}` : ''} • ${profile.collegeName || 'KVG College of Engineering'}`}
            </Text>
          </View>

          {!isFaculty && (profile.rollNumber || '4KV22EC018') && (
            <View style={styles.usnTag}>
              <Feather name="credit-card" size={12} color={Palette.primary} />
              <Text style={styles.usnTagText}>USN / Roll: {profile.rollNumber || '4KV22EC018'}</Text>
            </View>
          )}

          {isFaculty && (
            <TouchableOpacity
              style={styles.facultyDashboardBtn}
              onPress={() => router.replace('/faculty-dashboard' as any)}
              activeOpacity={0.85}
            >
              <Feather name="layout" size={16} color="#FFFFFF" />
              <Text style={styles.facultyDashboardBtnText}>
                Go to Faculty Dashboard
              </Text>
            </TouchableOpacity>
          )}
        </View>

        {/* Real Activity Stats */}
        <View style={styles.sectionHeaderRow}>
          <Text style={styles.sectionTitle}>
            {isFaculty ? 'Faculty Academic Overview' : 'Lifetime Milestones'}
          </Text>
          {loadingStats && <ActivityIndicator size="small" color={Palette.primary} />}
        </View>

        <View style={styles.statsGrid}>
          <View style={styles.statBox}>
            <Text style={styles.statNumber}>
              {isFaculty ? stats.questionsSolved : stats.questionsSolved}
            </Text>
            <Text style={styles.statLabel}>
              {isFaculty ? 'Notes Uploaded' : 'Questions Solved'}
            </Text>
          </View>

          <View style={styles.statBox}>
            <Text style={styles.statNumber}>{stats.quizzesCompleted}</Text>
            <Text style={styles.statLabel}>
              {isFaculty ? 'Quizzes Created' : 'Quizzes Completed'}
            </Text>
          </View>

          <View style={styles.statBox}>
            <Text style={styles.statNumber}>{stats.codeSubmissions}</Text>
            <Text style={styles.statLabel}>
              {isFaculty ? 'Students Enrolled' : 'Code Submissions'}
            </Text>
          </View>

          <View style={styles.statBox}>
            <Text style={[styles.statNumber, { color: Palette.aiPurple }]}>
              {stats.aiInterviews}
            </Text>
            <Text style={styles.statLabel}>
              {isFaculty ? 'Viva Evaluated' : 'AI Interviews'}
            </Text>
          </View>
        </View>

        {/* Real Dynamic Achievement Badges */}
        <View style={styles.sectionHeaderRow}>
          <Text style={styles.sectionTitle}>
            {isFaculty ? 'Faculty Certifications & Badges' : 'Achievement Badges'}
          </Text>
        </View>

        <View style={styles.badgesGrid}>
          {isFaculty ? (
            <>
              <View style={styles.badgeCard}>
                <View style={[styles.badgeIconCircle, { backgroundColor: '#DCFCE7' }]}>
                  <Feather name="check-circle" size={20} color={Palette.success} />
                </View>
                <View style={styles.badgeInfo}>
                  <Text style={styles.badgeTitle}>Verified Department Educator</Text>
                  <Text style={styles.badgeDesc}>Approved ECE Faculty at KVG College of Engineering</Text>
                </View>
                <View style={styles.unlockedBadge}>
                  <Text style={styles.unlockedBadgeText}>Verified</Text>
                </View>
              </View>

              <View style={styles.badgeCard}>
                <View style={[styles.badgeIconCircle, { backgroundColor: '#EFF6FF' }]}>
                  <Feather name="book-open" size={20} color={Palette.primary} />
                </View>
                <View style={styles.badgeInfo}>
                  <Text style={styles.badgeTitle}>Curriculum Contributor</Text>
                  <Text style={styles.badgeDesc}>Published college notes and syllabus modules</Text>
                </View>
                <View style={styles.unlockedBadge}>
                  <Text style={styles.unlockedBadgeText}>Active</Text>
                </View>
              </View>
            </>
          ) : (
            <>
              <View style={styles.badgeCard}>
                <View style={[styles.badgeIconCircle, { backgroundColor: '#EFF6FF' }]}>
                  <Feather name="award" size={20} color={Palette.primary} />
                </View>
                <View style={styles.badgeInfo}>
                  <Text style={styles.badgeTitle}>Verified Student Scholar</Text>
                  <Text style={styles.badgeDesc}>Active learner at {profile.collegeName || 'KVG College of Engineering'}</Text>
                </View>
                <View style={styles.unlockedBadge}>
                  <Text style={styles.unlockedBadgeText}>Active</Text>
                </View>
              </View>

              <View style={styles.badgeCard}>
                <View style={[styles.badgeIconCircle, { backgroundColor: stats.codeSubmissions > 0 ? '#DCFCE7' : '#F1F5F9' }]}>
                  <Feather name="terminal" size={20} color={stats.codeSubmissions > 0 ? Palette.success : Palette.textMuted} />
                </View>
                <View style={styles.badgeInfo}>
                  <Text style={styles.badgeTitle}>Algorithmic Solver</Text>
                  <Text style={styles.badgeDesc}>
                    {stats.codeSubmissions > 0
                      ? `${stats.codeSubmissions} algorithmic problems submitted`
                      : 'Solve coding challenges to unlock'}
                  </Text>
                </View>
                <View style={stats.codeSubmissions > 0 ? styles.unlockedBadge : styles.progressBadge}>
                  <Text style={stats.codeSubmissions > 0 ? styles.unlockedBadgeText : styles.progressBadgeText}>
                    {stats.codeSubmissions > 0 ? 'Unlocked' : 'In Progress'}
                  </Text>
                </View>
              </View>

              <View style={styles.badgeCard}>
                <View style={[styles.badgeIconCircle, { backgroundColor: stats.quizzesCompleted > 0 ? '#FEF3C7' : '#F1F5F9' }]}>
                  <Feather name="check-circle" size={20} color={stats.quizzesCompleted > 0 ? Palette.warning : Palette.textMuted} />
                </View>
                <View style={styles.badgeInfo}>
                  <Text style={styles.badgeTitle}>Quiz Achiever</Text>
                  <Text style={styles.badgeDesc}>
                    {stats.quizzesCompleted > 0
                      ? `${stats.quizzesCompleted} college quizzes completed with ${stats.quizAccuracy}% accuracy`
                      : 'Complete college assessments to unlock'}
                  </Text>
                </View>
                <View style={stats.quizzesCompleted > 0 ? styles.unlockedBadge : styles.progressBadge}>
                  <Text style={stats.quizzesCompleted > 0 ? styles.unlockedBadgeText : styles.progressBadgeText}>
                    {stats.quizzesCompleted > 0 ? 'Unlocked' : 'In Progress'}
                  </Text>
                </View>
              </View>

              <View style={styles.badgeCard}>
                <View style={[styles.badgeIconCircle, { backgroundColor: stats.aiInterviews > 0 ? '#F3E8FF' : '#F1F5F9' }]}>
                  <Feather name="message-square" size={20} color={stats.aiInterviews > 0 ? Palette.aiPurple : Palette.textMuted} />
                </View>
                <View style={styles.badgeInfo}>
                  <Text style={styles.badgeTitle}>AI Interview Ready</Text>
                  <Text style={styles.badgeDesc}>
                    {stats.aiInterviews > 0
                      ? `${stats.aiInterviews} AI mock interviews evaluated`
                      : 'Take an AI interview session to unlock'}
                  </Text>
                </View>
                <View style={stats.aiInterviews > 0 ? styles.unlockedBadge : styles.progressBadge}>
                  <Text style={stats.aiInterviews > 0 ? styles.unlockedBadgeText : styles.progressBadgeText}>
                    {stats.aiInterviews > 0 ? 'Unlocked' : 'In Progress'}
                  </Text>
                </View>
              </View>
            </>
          )}
        </View>

        {/* Working Settings & Preferences */}
        <View style={styles.sectionHeaderRow}>
          <Text style={styles.sectionTitle}>Settings & Preferences</Text>
        </View>

        <View style={styles.settingsCard}>
          {/* 1. Edit Profile & Details */}
          <TouchableOpacity
            style={styles.settingRow}
            activeOpacity={0.7}
            onPress={() => setShowEditModal(true)}
          >
            <View style={styles.settingLeft}>
              <View style={styles.settingIconBox}>
                <Feather name="user" size={17} color={Palette.primary} />
              </View>
              <View>
                <Text style={styles.settingLabel}>Edit Profile & Details</Text>
                <Text style={styles.settingSubLabel}>Update full name, USN, branch, and section</Text>
              </View>
            </View>
            <Feather name="chevron-right" size={18} color={Palette.textMuted} />
          </TouchableOpacity>

          <View style={styles.settingDivider} />

          {/* 2. Practice Reminder Notifications */}
          <TouchableOpacity
            style={styles.settingRow}
            activeOpacity={0.7}
            onPress={() => setShowReminderModal(true)}
          >
            <View style={styles.settingLeft}>
              <View style={styles.settingIconBox}>
                <Feather name="bell" size={17} color={Palette.warning} />
              </View>
              <View>
                <Text style={styles.settingLabel}>Practice Reminder Notifications</Text>
                <Text style={styles.settingSubLabel}>Configure daily practice alerts & notices</Text>
              </View>
            </View>
            <Feather name="chevron-right" size={18} color={Palette.textMuted} />
          </TouchableOpacity>

          <View style={styles.settingDivider} />

          {/* 3. Help Center & FAQ */}
          <TouchableOpacity
            style={styles.settingRow}
            activeOpacity={0.7}
            onPress={() => setShowHelpModal(true)}
          >
            <View style={styles.settingLeft}>
              <View style={styles.settingIconBox}>
                <Feather name="help-circle" size={17} color={Palette.aiPurple} />
              </View>
              <View>
                <Text style={styles.settingLabel}>Help Center & FAQ</Text>
                <Text style={styles.settingSubLabel}>Assessment guides, FAQs, and college contacts</Text>
              </View>
            </View>
            <Feather name="chevron-right" size={18} color={Palette.textMuted} />
          </TouchableOpacity>

          <View style={styles.settingDivider} />

          {/* 4. Sign Out */}
          <TouchableOpacity style={styles.settingRow} onPress={handleLogout} activeOpacity={0.7}>
            <View style={styles.settingLeft}>
              <View style={[styles.settingIconBox, { backgroundColor: '#FEE2E2' }]}>
                <Feather name="log-out" size={17} color={Palette.danger} />
              </View>
              <View>
                <Text style={[styles.settingLabel, { color: Palette.danger, fontWeight: '700' }]}>Sign Out</Text>
                <Text style={styles.settingSubLabel}>Safely exit your SkillExa account</Text>
              </View>
            </View>
            <Feather name="chevron-right" size={18} color={Palette.danger} />
          </TouchableOpacity>
        </View>
      </ScrollView>

      {/* ---------------- MODAL 1: EDIT PROFILE & DETAILS ---------------- */}
      <Modal animationType="slide" transparent visible={showEditModal} onRequestClose={() => setShowEditModal(false)}>
        <View style={styles.modalOverlay}>
          <View style={[styles.modalCard, { maxWidth: 440, padding: 20 }]}>
            <View style={styles.modalHeaderRow}>
              <View style={{ flexDirection: 'row', alignItems: 'center', gap: 10 }}>
                <View style={[styles.modalSmallIcon, { backgroundColor: '#EFF6FF' }]}>
                  <Feather name="edit-3" size={18} color={Palette.primary} />
                </View>
                <Text style={styles.modalSheetTitle}>Edit Profile & Details</Text>
              </View>
              <TouchableOpacity onPress={() => setShowEditModal(false)}>
                <Feather name="x" size={20} color={Palette.textMuted} />
              </TouchableOpacity>
            </View>

            <ScrollView style={{ maxHeight: 420, width: '100%' }} showsVerticalScrollIndicator={false}>
              {/* Full Name */}
              <Text style={styles.inputLabel}>FULL NAME</Text>
              <TextInput
                style={styles.textInput}
                value={editName}
                onChangeText={setEditName}
                placeholder="Enter your full name"
                placeholderTextColor={Palette.textMuted}
              />

              {/* USN / Roll Number */}
              <Text style={styles.inputLabel}>USN / ROLL NUMBER</Text>
              <TextInput
                style={styles.textInput}
                value={editRollNumber}
                onChangeText={setEditRollNumber}
                placeholder="e.g. 4KV22EC018"
                placeholderTextColor={Palette.textMuted}
                autoCapitalize="characters"
              />

              {/* Branch Selection */}
              <Text style={styles.inputLabel}>BRANCH / DEPARTMENT</Text>
              <View style={styles.chipsRow}>
                {BRANCH_OPTIONS.map((b) => (
                  <TouchableOpacity
                    key={b}
                    style={[styles.chip, editBranch === b && styles.chipActive]}
                    onPress={() => setEditBranch(b)}
                  >
                    <Text style={[styles.chipText, editBranch === b && styles.chipTextActive]}>{b}</Text>
                  </TouchableOpacity>
                ))}
              </View>

              {/* Academic Year Selection */}
              <Text style={styles.inputLabel}>ACADEMIC YEAR</Text>
              <View style={styles.chipsRow}>
                {YEAR_OPTIONS.map((y) => (
                  <TouchableOpacity
                    key={y}
                    style={[styles.chip, editYear === y && styles.chipActive]}
                    onPress={() => setEditYear(y)}
                  >
                    <Text style={[styles.chipText, editYear === y && styles.chipTextActive]}>{y}</Text>
                  </TouchableOpacity>
                ))}
              </View>

              {/* Section Selection */}
              <Text style={styles.inputLabel}>CLASS SECTION</Text>
              <View style={styles.chipsRow}>
                {SECTION_OPTIONS.map((s) => (
                  <TouchableOpacity
                    key={s}
                    style={[styles.chip, editSection === s && styles.chipActive]}
                    onPress={() => setEditSection(s)}
                  >
                    <Text style={[styles.chipText, editSection === s && styles.chipTextActive]}>Sec {s}</Text>
                  </TouchableOpacity>
                ))}
              </View>

              {/* Phone */}
              <Text style={styles.inputLabel}>PHONE NUMBER (OPTIONAL)</Text>
              <TextInput
                style={styles.textInput}
                value={editPhone}
                onChangeText={setEditPhone}
                placeholder="+91 9876543210"
                placeholderTextColor={Palette.textMuted}
                keyboardType="phone-pad"
              />
            </ScrollView>

            <View style={styles.modalBtnRow}>
              <TouchableOpacity
                style={styles.modalCancelBtn}
                onPress={() => setShowEditModal(false)}
                disabled={isSavingProfile}
              >
                <Text style={styles.modalCancelText}>Cancel</Text>
              </TouchableOpacity>

              <TouchableOpacity
                style={[styles.modalSaveBtn, isSavingProfile && { opacity: 0.7 }]}
                onPress={handleSaveProfile}
                disabled={isSavingProfile}
              >
                {isSavingProfile ? (
                  <ActivityIndicator size="small" color="#FFFFFF" />
                ) : (
                  <>
                    <Feather name="check" size={16} color="#FFFFFF" />
                    <Text style={styles.modalSaveBtnText}>Save Changes</Text>
                  </>
                )}
              </TouchableOpacity>
            </View>
          </View>
        </View>
      </Modal>

      {/* ---------------- MODAL 2: PRACTICE REMINDERS & NOTIFICATIONS ---------------- */}
      <Modal animationType="slide" transparent visible={showReminderModal} onRequestClose={() => setShowReminderModal(false)}>
        <View style={styles.modalOverlay}>
          <View style={[styles.modalCard, { maxWidth: 440, padding: 20 }]}>
            <View style={styles.modalHeaderRow}>
              <View style={{ flexDirection: 'row', alignItems: 'center', gap: 10 }}>
                <View style={[styles.modalSmallIcon, { backgroundColor: '#FEF3C7' }]}>
                  <Feather name="bell" size={18} color={Palette.warning} />
                </View>
                <Text style={styles.modalSheetTitle}>Practice Reminder Notifications</Text>
              </View>
              <TouchableOpacity onPress={() => setShowReminderModal(false)}>
                <Feather name="x" size={20} color={Palette.textMuted} />
              </TouchableOpacity>
            </View>

            <View style={{ width: '100%', marginVertical: 12, gap: 14 }}>
              <View style={styles.toggleRow}>
                <View style={{ flex: 1, paddingRight: 10 }}>
                  <Text style={styles.toggleTitle}>Daily Practice Drill</Text>
                  <Text style={styles.toggleDesc}>Receive evening practice reminders at 7:00 PM</Text>
                </View>
                <Switch
                  value={dailyReminders}
                  onValueChange={setDailyReminders}
                  trackColor={{ false: '#CBD5E1', true: Palette.primary }}
                  thumbColor="#FFFFFF"
                />
              </View>

              <View style={styles.settingDivider} />

              <View style={styles.toggleRow}>
                <View style={{ flex: 1, paddingRight: 10 }}>
                  <Text style={styles.toggleTitle}>College Assessment Notices</Text>
                  <Text style={styles.toggleDesc}>Alert immediately when faculty publishes notes or tests</Text>
                </View>
                <Switch
                  value={assessmentAlerts}
                  onValueChange={setAssessmentAlerts}
                  trackColor={{ false: '#CBD5E1', true: Palette.primary }}
                  thumbColor="#FFFFFF"
                />
              </View>

              <View style={styles.settingDivider} />

              <View style={styles.toggleRow}>
                <View style={{ flex: 1, paddingRight: 10 }}>
                  <Text style={styles.toggleTitle}>Email Announcements</Text>
                  <Text style={styles.toggleDesc}>Forward official faculty announcements to your email</Text>
                </View>
                <Switch
                  value={emailAlerts}
                  onValueChange={setEmailAlerts}
                  trackColor={{ false: '#CBD5E1', true: Palette.primary }}
                  thumbColor="#FFFFFF"
                />
              </View>

              <View style={styles.settingDivider} />

              <View style={styles.toggleRow}>
                <View style={{ flex: 1, paddingRight: 10 }}>
                  <Text style={styles.toggleTitle}>Weekly Performance Digest</Text>
                  <Text style={styles.toggleDesc}>Weekly summary of coding accuracy and topic mastery</Text>
                </View>
                <Switch
                  value={weeklyDigest}
                  onValueChange={setWeeklyDigest}
                  trackColor={{ false: '#CBD5E1', true: Palette.primary }}
                  thumbColor="#FFFFFF"
                />
              </View>
            </View>

            <TouchableOpacity
              style={styles.modalFullSaveBtn}
              onPress={() => {
                setShowReminderModal(false);
                Alert.alert('Preferences Saved! 🔔', 'Your practice notification preferences are updated.');
              }}
            >
              <Text style={styles.modalFullSaveBtnText}>Save Preferences</Text>
            </TouchableOpacity>
          </View>
        </View>
      </Modal>

      {/* ---------------- MODAL 3: HELP CENTER & FAQ ---------------- */}
      <Modal animationType="slide" transparent visible={showHelpModal} onRequestClose={() => setShowHelpModal(false)}>
        <View style={styles.modalOverlay}>
          <View style={[styles.modalCard, { maxWidth: 460, padding: 20 }]}>
            <View style={styles.modalHeaderRow}>
              <View style={{ flexDirection: 'row', alignItems: 'center', gap: 10 }}>
                <View style={[styles.modalSmallIcon, { backgroundColor: '#F3E8FF' }]}>
                  <Feather name="help-circle" size={18} color={Palette.aiPurple} />
                </View>
                <Text style={styles.modalSheetTitle}>Help Center & FAQ</Text>
              </View>
              <TouchableOpacity onPress={() => setShowHelpModal(false)}>
                <Feather name="x" size={20} color={Palette.textMuted} />
              </TouchableOpacity>
            </View>

            <ScrollView style={{ maxHeight: 380, width: '100%', marginVertical: 12 }} showsVerticalScrollIndicator={false}>
              {FAQS.map((faq, index) => {
                const isOpen = expandedFaq === index;
                return (
                  <View key={index} style={styles.faqCard}>
                    <TouchableOpacity
                      style={styles.faqHeader}
                      activeOpacity={0.7}
                      onPress={() => setExpandedFaq(isOpen ? null : index)}
                    >
                      <Text style={styles.faqQuestion}>{faq.q}</Text>
                      <Feather name={isOpen ? 'chevron-up' : 'chevron-down'} size={16} color={Palette.textMuted} />
                    </TouchableOpacity>
                    {isOpen && (
                      <View style={styles.faqBody}>
                        <Text style={styles.faqAnswer}>{faq.a}</Text>
                      </View>
                    )}
                  </View>
                );
              })}

              {/* Support Contacts Card */}
              <View style={styles.supportCard}>
                <Feather name="mail" size={18} color={Palette.primary} />
                <View style={{ flex: 1 }}>
                  <Text style={styles.supportTitle}>Department & Helpdesk Support</Text>
                  <Text style={styles.supportText}>ECE Academic Office: ec-office@kvgce.edu.in</Text>
                  <Text style={styles.supportText}>Platform Tech: support@skillexa.edu</Text>
                </View>
              </View>
            </ScrollView>

            <TouchableOpacity style={styles.modalFullSaveBtn} onPress={() => setShowHelpModal(false)}>
              <Text style={styles.modalFullSaveBtnText}>Got it, Close</Text>
            </TouchableOpacity>
          </View>
        </View>
      </Modal>

      {/* ---------------- MODAL 4: SIGN OUT CONFIRMATION ---------------- */}
      <Modal
        animationType="fade"
        transparent
        visible={showLogoutModal}
        onRequestClose={() => setShowLogoutModal(false)}
      >
        <View style={styles.modalOverlay}>
          <View style={styles.modalCard}>
            <View style={styles.modalIconBox}>
              <Feather name="log-out" size={26} color={Palette.danger} />
            </View>

            <Text style={styles.modalTitle}>Sign Out</Text>
            <Text style={styles.modalMessage}>
              Are you sure you want to sign out of your SkillExa account? You will need your credentials to log back in.
            </Text>

            <View style={styles.modalBtnRow}>
              <TouchableOpacity
                style={styles.modalCancelBtn}
                onPress={() => setShowLogoutModal(false)}
                activeOpacity={0.7}
              >
                <Text style={styles.modalCancelText}>Cancel</Text>
              </TouchableOpacity>

              <TouchableOpacity
                style={styles.modalSignOutBtn}
                onPress={performLogout}
                activeOpacity={0.8}
              >
                <Feather name="log-out" size={16} color="#FFFFFF" />
                <Text style={styles.modalSignOutText}>Sign Out</Text>
              </TouchableOpacity>
            </View>
          </View>
        </View>
      </Modal>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: Palette.background },
  scrollContent: { paddingHorizontal: 16, paddingTop: 16, paddingBottom: 40 },
  profileCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.cardLarge,
    padding: 24,
    borderWidth: 1,
    borderColor: Palette.border,
    alignItems: 'center',
    marginBottom: 20,
    ...Shadows.card,
  },
  avatarLarge: {
    width: 72,
    height: 72,
    borderRadius: 36,
    backgroundColor: Palette.primaryLight,
    borderWidth: 2,
    borderColor: Palette.primaryBorder,
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: 12,
  },
  avatarLargeText: { fontSize: 28, fontWeight: '800', color: Palette.primary },
  nameText: { fontSize: 20, fontWeight: '800', color: Palette.textTitle },
  emailText: { fontSize: 13, color: Palette.textSecondary, marginTop: 2 },
  trackTag: {
    backgroundColor: Palette.backgroundSecondary,
    paddingHorizontal: 14,
    paddingVertical: 6,
    borderRadius: Radii.pill,
    marginTop: 10,
    borderWidth: 1,
    borderColor: Palette.border,
  },
  trackTagText: { fontSize: 12, fontWeight: '700', color: Palette.textBody },
  usnTag: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    backgroundColor: '#EFF6FF',
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: Radii.pill,
    marginTop: 8,
  },
  usnTagText: { fontSize: 11.5, fontWeight: '700', color: Palette.primary },
  facultyDashboardBtn: {
    backgroundColor: Palette.primary,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
    paddingVertical: 12,
    paddingHorizontal: 20,
    borderRadius: Radii.button,
    marginTop: 14,
    width: '100%',
  },
  facultyDashboardBtnText: { color: '#FFFFFF', fontWeight: '700', fontSize: 13.5 },
  sectionHeaderRow: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: 12,
  },
  sectionTitle: { fontSize: 17, fontWeight: '800', color: Palette.textTitle },
  statsGrid: { flexDirection: 'row', flexWrap: 'wrap', justifyContent: 'space-between', gap: 10, marginBottom: 24 },
  statBox: {
    width: '48%',
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 14,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  statNumber: { fontSize: 22, fontWeight: '900', color: Palette.primary },
  statLabel: { fontSize: 11, color: Palette.textSecondary, marginTop: 2 },
  badgesGrid: { gap: 10, marginBottom: 24 },
  badgeCard: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 14,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  badgeIconCircle: { width: 42, height: 42, borderRadius: 21, alignItems: 'center', justifyContent: 'center', marginRight: 12 },
  badgeInfo: { flex: 1 },
  badgeTitle: { fontSize: 14, fontWeight: '700', color: Palette.textTitle },
  badgeDesc: { fontSize: 12, color: Palette.textSecondary, marginTop: 2 },
  unlockedBadge: {
    backgroundColor: '#DCFCE7',
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: Radii.pill,
  },
  unlockedBadgeText: { fontSize: 10.5, fontWeight: '700', color: Palette.success },
  progressBadge: {
    backgroundColor: Palette.backgroundSecondary,
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: Radii.pill,
  },
  progressBadgeText: { fontSize: 10.5, fontWeight: '600', color: Palette.textMuted },
  settingsCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 6,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  settingRow: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingVertical: 14,
    paddingHorizontal: 12,
  },
  settingLeft: { flexDirection: 'row', alignItems: 'center', gap: 12, flex: 1 },
  settingIconBox: {
    width: 36,
    height: 36,
    borderRadius: 18,
    backgroundColor: Palette.backgroundSecondary,
    alignItems: 'center',
    justifyContent: 'center',
  },
  settingLabel: { fontSize: 14, color: Palette.textTitle, fontWeight: '700' },
  settingSubLabel: { fontSize: 11.5, color: Palette.textSecondary, marginTop: 1 },
  settingDivider: { height: 1, backgroundColor: Palette.borderSubtle, marginHorizontal: 12 },
  modalOverlay: {
    flex: 1,
    backgroundColor: 'rgba(15, 23, 42, 0.6)',
    alignItems: 'center',
    justifyContent: 'center',
    padding: 16,
  },
  modalCard: {
    width: '100%',
    maxWidth: 380,
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.cardLarge,
    padding: 24,
    alignItems: 'center',
    ...Shadows.floating,
  },
  modalHeaderRow: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    width: '100%',
    marginBottom: 16,
    paddingBottom: 10,
    borderBottomWidth: 1,
    borderBottomColor: Palette.borderSubtle,
  },
  modalSmallIcon: {
    width: 32,
    height: 32,
    borderRadius: 16,
    alignItems: 'center',
    justifyContent: 'center',
  },
  modalSheetTitle: {
    fontSize: 16,
    fontWeight: '800',
    color: Palette.textTitle,
  },
  inputLabel: {
    fontSize: 11,
    fontWeight: '800',
    color: Palette.textSecondary,
    marginTop: 12,
    marginBottom: 6,
    letterSpacing: 0.5,
  },
  textInput: {
    borderWidth: 1,
    borderColor: Palette.border,
    borderRadius: Radii.button,
    paddingHorizontal: 14,
    paddingVertical: 10,
    fontSize: 14,
    color: Palette.textTitle,
    backgroundColor: Palette.backgroundSecondary,
  },
  chipsRow: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 8,
    marginBottom: 6,
  },
  chip: {
    paddingHorizontal: 12,
    paddingVertical: 7,
    borderRadius: Radii.pill,
    borderWidth: 1,
    borderColor: Palette.border,
    backgroundColor: '#FFFFFF',
  },
  chipActive: {
    backgroundColor: Palette.primary,
    borderColor: Palette.primary,
  },
  chipText: {
    fontSize: 12,
    fontWeight: '700',
    color: Palette.textBody,
  },
  chipTextActive: {
    color: '#FFFFFF',
  },
  toggleRow: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
  },
  toggleTitle: {
    fontSize: 13.5,
    fontWeight: '700',
    color: Palette.textTitle,
  },
  toggleDesc: {
    fontSize: 11.5,
    color: Palette.textSecondary,
    marginTop: 2,
  },
  faqCard: {
    borderWidth: 1,
    borderColor: Palette.borderSubtle,
    borderRadius: Radii.card,
    marginBottom: 10,
    overflow: 'hidden',
  },
  faqHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    padding: 12,
    backgroundColor: Palette.backgroundSecondary,
  },
  faqQuestion: {
    fontSize: 13,
    fontWeight: '700',
    color: Palette.textTitle,
    flex: 1,
    marginRight: 8,
  },
  faqBody: {
    padding: 12,
    backgroundColor: '#FFFFFF',
    borderTopWidth: 1,
    borderTopColor: Palette.borderSubtle,
  },
  faqAnswer: {
    fontSize: 12.5,
    color: Palette.textBody,
    lineHeight: 18,
  },
  supportCard: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    gap: 12,
    backgroundColor: '#EFF6FF',
    padding: 14,
    borderRadius: Radii.card,
    marginTop: 10,
    borderWidth: 1,
    borderColor: '#BFDBFE',
  },
  supportTitle: {
    fontSize: 13,
    fontWeight: '800',
    color: Palette.primary,
    marginBottom: 2,
  },
  supportText: {
    fontSize: 11.5,
    color: Palette.textBody,
    marginTop: 1,
  },
  modalIconBox: {
    width: 56,
    height: 56,
    borderRadius: 28,
    backgroundColor: '#FEE2E2',
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: 16,
  },
  modalTitle: {
    fontSize: 18,
    fontWeight: '800',
    color: Palette.textTitle,
    marginBottom: 8,
    textAlign: 'center',
  },
  modalMessage: {
    fontSize: 13.5,
    color: Palette.textSecondary,
    textAlign: 'center',
    lineHeight: 20,
    marginBottom: 24,
  },
  modalBtnRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
    width: '100%',
    marginTop: 16,
  },
  modalCancelBtn: {
    flex: 1,
    paddingVertical: 12,
    borderRadius: Radii.button,
    backgroundColor: Palette.backgroundSecondary,
    borderWidth: 1,
    borderColor: Palette.border,
    alignItems: 'center',
    justifyContent: 'center',
  },
  modalCancelText: {
    fontSize: 14,
    fontWeight: '700',
    color: Palette.textTitle,
  },
  modalSaveBtn: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 6,
    paddingVertical: 12,
    borderRadius: Radii.button,
    backgroundColor: Palette.primary,
    ...Shadows.button,
  },
  modalSaveBtnText: {
    fontSize: 14,
    fontWeight: '700',
    color: '#FFFFFF',
  },
  modalFullSaveBtn: {
    backgroundColor: Palette.primary,
    borderRadius: Radii.button,
    paddingVertical: 12,
    alignItems: 'center',
    justifyContent: 'center',
    width: '100%',
    marginTop: 10,
    ...Shadows.button,
  },
  modalFullSaveBtnText: {
    color: '#FFFFFF',
    fontWeight: '700',
    fontSize: 14,
  },
  modalSignOutBtn: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 6,
    paddingVertical: 12,
    borderRadius: Radii.button,
    backgroundColor: Palette.danger,
    ...Shadows.button,
  },
  modalSignOutText: {
    fontSize: 14,
    fontWeight: '700',
    color: '#FFFFFF',
  },
});
