import { Feather } from '@expo/vector-icons';
import { router } from 'expo-router';
import React, { useEffect, useMemo, useRef } from 'react';
import {
  Platform,
  SafeAreaView,
  StatusBar,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from 'react-native';
import { useAuth } from '../components/auth-context';
import { AppHeader } from '../components/common/AppHeader';
import { Palette } from '../constants/theme';

export default function CompetitiveDashboard() {
  const { profile } = useAuth();
  const iframeRef = useRef<HTMLIFrameElement | null>(null);

  // Unified student profile parameters from SkillExa login & registration
  const userEmail = profile?.email || 'ganesh@kvgce.edu.in';
  const userName = profile?.name || 'Ganesh Sharan';
  const userPhone = profile?.phone || '+91 98765 43210';
  const userCollege = profile?.collegeName || 'KVG College of Engineering';
  const userBranch = profile?.department || 'ECE';
  const userYear = profile?.academicYear || '3rd Year';
  const userSection = profile?.section || 'A';
  const userRoll = profile?.rollNumber || '4KV22EC018';
  const userRole = profile?.role === 'FACULTY' ? 'admin' : 'student';

  const competitiveUrl = useMemo(() => {
    const params = new URLSearchParams({
      email: userEmail,
      name: userName,
      phone: userPhone,
      college: userCollege,
      branch: userBranch,
      year: userYear,
      section: userSection,
      roll: userRoll,
      role: userRole,
    });
    return `http://localhost:5173?${params.toString()}`;
  }, [userEmail, userName, userPhone, userCollege, userBranch, userYear, userSection, userRoll, userRole]);

  // Seamlessly sync student profile into Competitive platform backend
  useEffect(() => {
    if (userEmail) {
      fetch('http://localhost:3001/api/user/sync', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          email: userEmail,
          name: userName,
          phone: userPhone,
          college: userCollege,
          branch: userBranch,
          year: userYear,
          section: userSection,
          rollNumber: userRoll,
          role: userRole,
        }),
      }).catch((err) => {
        console.log('Competitive sync notice:', err);
      });
    }
  }, [userEmail, userName, userPhone, userCollege, userBranch, userYear, userSection, userRoll, userRole]);

  if (Platform.OS === 'web') {
    return (
      <SafeAreaView style={styles.safeArea}>
        <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
        <AppHeader showBack title="Competitive Exams Suite" subtitle={`Logged in as ${userName} (${userEmail})`} />
        <View style={styles.webContainer}>
          <iframe
            ref={iframeRef as any}
            src={competitiveUrl}
            style={{
              width: '100%',
              height: '100%',
              border: 'none',
              flex: 1,
            } as any}
            title="Competitive Exams Platform"
          />
        </View>
      </SafeAreaView>
    );
  }

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader showBack title="Competitive Exams" subtitle="Aptitude & Govt Exam Suite" />
      <View style={styles.fallbackContainer}>
        <Feather name="award" size={48} color={Palette.primary} />
        <Text style={styles.fallbackTitle}>Competitive Exams Platform</Text>
        <Text style={styles.fallbackSubtitle}>
          Unified with your SkillExa account ({userEmail}). Open in your browser to continue.
        </Text>
        <TouchableOpacity
          style={styles.openBtn}
          onPress={() => {
            if (typeof window !== 'undefined') {
              window.open(competitiveUrl, '_blank');
            }
          }}
        >
          <Text style={styles.openBtnText}>Open Competitive Platform</Text>
          <Feather name="external-link" size={16} color="#FFFFFF" />
        </TouchableOpacity>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: '#F8FAFC' },
  webContainer: { flex: 1, backgroundColor: '#F8FAFC' },
  fallbackContainer: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    padding: 24,
    backgroundColor: Palette.background,
  },
  fallbackTitle: {
    fontSize: 20,
    fontWeight: '800',
    color: Palette.textTitle,
    marginTop: 16,
    marginBottom: 8,
  },
  fallbackSubtitle: {
    fontSize: 14,
    color: Palette.textSecondary,
    textAlign: 'center',
    marginBottom: 24,
  },
  openBtn: {
    backgroundColor: Palette.primary,
    paddingVertical: 14,
    paddingHorizontal: 24,
    borderRadius: 12,
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  openBtnText: {
    color: '#FFFFFF',
    fontSize: 15,
    fontWeight: '700',
  },
});