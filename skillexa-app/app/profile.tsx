import { Feather } from '@expo/vector-icons';
import { router } from 'expo-router';
import React, { useState } from 'react';
import {
  Alert,
  Modal,
  Platform,
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from 'react-native';
import { useAuth } from '../components/auth-context';
import { AppHeader } from '../components/common/AppHeader';
import { Palette, Radii, Shadows } from '../constants/theme';
import { setAuthToken } from '../services/api';

const BADGES = [
  { id: 1, title: '7-Day Streak', icon: 'zap', color: Palette.warning, desc: 'Logged in and solved daily drills' },
  { id: 2, title: '100+ Solved', icon: 'award', color: Palette.success, desc: 'Completed over 100 practice questions' },
  { id: 3, title: 'Code Warrior', icon: 'terminal', color: Palette.primary, desc: 'Solved 25+ algorithmic problems' },
  { id: 4, title: 'AI Pioneer', icon: 'message-square', color: Palette.aiPurple, desc: 'Completed AI mock interview' },
];

export default function ProfileScreen() {
  const { profile, logout } = useAuth();
  const [showLogoutModal, setShowLogoutModal] = useState(false);

  const isFaculty = profile?.role === 'FACULTY';
  const displayName = profile?.name || (isFaculty ? 'Dr. Kusumadhara S' : 'Ganesh Kumar');
  const displayEmail = profile?.email || (isFaculty ? 'kusumadhara.s@kvgce.edu.in' : 'ganesh@skillexa.edu');
  const initial = displayName.charAt(0).toUpperCase();

  const performLogout = () => {
    setShowLogoutModal(false);
    logout();
    setAuthToken(null);
    if (typeof window !== 'undefined' && window.localStorage) {
      try {
        window.localStorage.removeItem('skillexa_jwt_token');
        window.localStorage.removeItem('skillexa_user_profile');
      } catch (e) {}
    }
    router.replace('/login' as any);
  };

  const handleLogout = () => {
    setShowLogoutModal(true);
  };

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader title={isFaculty ? "Faculty Profile" : "Student Profile"} />

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {/* Profile Card */}
        <View style={styles.profileCard}>
          <View style={styles.avatarLarge}>
            <Text style={styles.avatarLargeText}>{initial}</Text>
          </View>
          <Text style={styles.nameText}>{displayName}</Text>
          <Text style={styles.emailText}>{displayEmail}</Text>
          <View style={styles.trackTag}>
            <Text style={styles.trackTagText}>
              {isFaculty
                ? `${profile.facultyDesignation || 'Associate Professor'} • ${profile.department || 'ECE'} Department`
                : 'Computer Science • Placement & Competitive Track'}
            </Text>
          </View>
        </View>

        {/* Lifetime Activity Stats */}
        <View style={styles.sectionHeaderRow}>
          <Text style={styles.sectionTitle}>Lifetime Milestones</Text>
        </View>

        <View style={styles.statsGrid}>
          <View style={styles.statBox}>
            <Text style={styles.statNumber}>354</Text>
            <Text style={styles.statLabel}>Questions Solved</Text>
          </View>

          <View style={styles.statBox}>
            <Text style={styles.statNumber}>28</Text>
            <Text style={styles.statLabel}>Quizzes Completed</Text>
          </View>

          <View style={styles.statBox}>
            <Text style={styles.statNumber}>42</Text>
            <Text style={styles.statLabel}>Code Submissions</Text>
          </View>

          <View style={styles.statBox}>
            <Text style={[styles.statNumber, { color: Palette.aiPurple }]}>3</Text>
            <Text style={styles.statLabel}>AI Interviews</Text>
          </View>
        </View>

        {/* Achievement Badges */}
        <View style={styles.sectionHeaderRow}>
          <Text style={styles.sectionTitle}>Achievement Badges</Text>
        </View>

        <View style={styles.badgesGrid}>
          {BADGES.map((b) => (
            <View key={b.id} style={styles.badgeCard}>
              <View style={[styles.badgeIconCircle, { backgroundColor: `${b.color}15` }]}>
                <Feather name={b.icon as any} size={20} color={b.color} />
              </View>
              <View style={styles.badgeInfo}>
                <Text style={styles.badgeTitle}>{b.title}</Text>
                <Text style={styles.badgeDesc}>{b.desc}</Text>
              </View>
            </View>
          ))}
        </View>

        {/* Settings & Preferences */}
        <View style={styles.sectionHeaderRow}>
          <Text style={styles.sectionTitle}>Settings & Preferences</Text>
        </View>

        <View style={styles.settingsCard}>
          <TouchableOpacity style={styles.settingRow} activeOpacity={0.7}>
            <View style={styles.settingLeft}>
              <Feather name="user" size={18} color={Palette.textTitle} />
              <Text style={styles.settingLabel}>Edit Profile & Details</Text>
            </View>
            <Feather name="chevron-right" size={18} color={Palette.textMuted} />
          </TouchableOpacity>

          <View style={styles.settingDivider} />

          <TouchableOpacity style={styles.settingRow} activeOpacity={0.7}>
            <View style={styles.settingLeft}>
              <Feather name="bell" size={18} color={Palette.textTitle} />
              <Text style={styles.settingLabel}>Practice Reminder Notifications</Text>
            </View>
            <Feather name="chevron-right" size={18} color={Palette.textMuted} />
          </TouchableOpacity>

          <View style={styles.settingDivider} />

          <TouchableOpacity style={styles.settingRow} activeOpacity={0.7}>
            <View style={styles.settingLeft}>
              <Feather name="help-circle" size={18} color={Palette.textTitle} />
              <Text style={styles.settingLabel}>Help Center & FAQ</Text>
            </View>
            <Feather name="chevron-right" size={18} color={Palette.textMuted} />
          </TouchableOpacity>

          <View style={styles.settingDivider} />

          <TouchableOpacity style={styles.settingRow} onPress={handleLogout} activeOpacity={0.7}>
            <View style={styles.settingLeft}>
              <Feather name="log-out" size={18} color={Palette.danger} />
              <Text style={[styles.settingLabel, { color: Palette.danger, fontWeight: '700' }]}>Sign Out</Text>
            </View>
          </TouchableOpacity>
        </View>
      </ScrollView>

      {/* Sign Out Confirmation Modal */}
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
    paddingHorizontal: 12,
    paddingVertical: 5,
    borderRadius: Radii.pill,
    marginTop: 12,
  },
  trackTagText: { fontSize: 11.5, fontWeight: '600', color: Palette.textBody },
  sectionHeaderRow: { marginBottom: 12 },
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
  settingLeft: { flexDirection: 'row', alignItems: 'center', gap: 12 },
  settingLabel: { fontSize: 13.5, color: Palette.textBody, fontWeight: '500' },
  settingDivider: { height: 1, backgroundColor: Palette.borderSubtle, marginHorizontal: 12 },
  modalOverlay: {
    flex: 1,
    backgroundColor: 'rgba(15, 23, 42, 0.6)',
    alignItems: 'center',
    justifyContent: 'center',
    padding: 20,
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
