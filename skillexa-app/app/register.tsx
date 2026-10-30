import { Feather } from '@expo/vector-icons';
import { useRouter } from 'expo-router';
import React, { useState } from 'react';
import {
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TouchableOpacity,
  useWindowDimensions,
  View,
} from 'react-native';

export default function Register() {
  const router = useRouter();
  const { width } = useWindowDimensions();
  const isDesktop = width >= 768;

  const [selectedRole, setSelectedRole] = useState<'student' | 'faculty'>('student');

  const handleContinue = () => {
    if (selectedRole === 'student') {
      router.push('/register-user' as any);
    } else {
      router.push('/register-lecturer' as any);
    }
  };

  const handleGoBack = () => {
    if (router.canGoBack()) {
      router.back();
    } else {
      router.replace('/login' as any);
    }
  };

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />

      <ScrollView
        contentContainerStyle={styles.scrollContent}
        showsVerticalScrollIndicator={false}
      >
        <View style={[styles.container, isDesktop && styles.containerDesktop]}>
          {/* Top Bar matching reference: Circular back button on left, Step 1 of 3 pill on right */}
          <View style={styles.topBar}>
            <TouchableOpacity
              style={styles.backButton}
              onPress={handleGoBack}
              activeOpacity={0.7}
            >
              <Feather name="arrow-left" size={18} color="#0F172A" />
            </TouchableOpacity>

            <View style={styles.stepPill}>
              <View style={styles.stepDot} />
              <Text style={styles.stepPillText}>Step 1 of 3</Text>
            </View>
          </View>

          {/* Onboarding Heading Section */}
          <View style={styles.header}>
            <Text style={styles.badge}>ONBOARDING</Text>
            <Text style={styles.title}>Select Your Role</Text>
            <Text style={styles.subtitle}>
              Choose your learning or teaching profile to configure your personalized dashboard
            </Text>
          </View>

          {/* Role Cards Selection */}
          <View style={styles.rolesStack}>
            {/* Option 1: Student */}
            <TouchableOpacity
              style={[
                styles.roleCard,
                selectedRole === 'student' && styles.roleCardSelected,
              ]}
              onPress={() => setSelectedRole('student')}
              activeOpacity={0.85}
            >
              <View style={styles.cardContent}>
                <View style={styles.studentIconBox}>
                  <Feather name="user" size={24} color="#2563EB" />
                </View>

                <View style={styles.cardTexts}>
                  <View style={styles.roleTitleRow}>
                    <Text style={styles.roleTitle}>Student</Text>
                    <View style={styles.popularBadge}>
                      <Text style={styles.popularBadgeText}>POPULAR</Text>
                    </View>
                  </View>
                  <Text style={styles.roleDesc}>
                    Access engineering roadmaps, coding compiler, unit quizzes, and competitive exams.
                  </Text>
                </View>

                <View style={styles.rightActionRow}>
                  {selectedRole === 'student' ? (
                    <View style={styles.checkCircleActive}>
                      <Feather name="check" size={13} color="#FFFFFF" />
                    </View>
                  ) : (
                    <View style={styles.checkCircleInactive} />
                  )}
                  <Feather name="chevron-right" size={16} color="#94A3B8" style={{ marginLeft: 4 }} />
                </View>
              </View>
            </TouchableOpacity>

            {/* Option 2: Faculty / Teacher */}
            <TouchableOpacity
              style={[
                styles.roleCard,
                selectedRole === 'faculty' && styles.roleCardSelected,
              ]}
              onPress={() => setSelectedRole('faculty')}
              activeOpacity={0.85}
            >
              <View style={styles.cardContent}>
                <View style={styles.facultyIconBox}>
                  <Feather name="file-text" size={22} color="#A855F7" />
                </View>

                <View style={styles.cardTexts}>
                  <View style={styles.roleTitleRow}>
                    <Text style={styles.roleTitle}>Faculty / Teacher</Text>
                    <View style={styles.facultyBadge}>
                      <Text style={styles.facultyBadgeText}>FACULTY</Text>
                    </View>
                  </View>
                  <Text style={styles.roleDesc}>
                    Publish curriculum content, manage lab files, design quizzes, and monitor students.
                  </Text>
                </View>

                <View style={styles.rightActionRow}>
                  {selectedRole === 'faculty' ? (
                    <View style={styles.checkCircleActive}>
                      <Feather name="check" size={13} color="#FFFFFF" />
                    </View>
                  ) : (
                    <View style={styles.checkCircleInactive} />
                  )}
                  <Feather name="chevron-right" size={16} color="#94A3B8" style={{ marginLeft: 4 }} />
                </View>
              </View>
            </TouchableOpacity>
          </View>

          {/* Dynamic Continue Button */}
          <TouchableOpacity
            style={styles.continueButton}
            onPress={handleContinue}
            activeOpacity={0.85}
          >
            <Text style={styles.continueButtonText}>
              Continue as {selectedRole === 'student' ? 'Student' : 'Faculty'} →
            </Text>
          </TouchableOpacity>

          {/* Already have an account footer */}
          <View style={styles.loginRedirect}>
            <Text style={styles.loginRedirectText}>
              Already have an account?{' '}
              <Text
                style={styles.loginHighlight}
                onPress={() => router.replace('/login' as any)}
              >
                Sign In
              </Text>
            </Text>
          </View>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: '#FFFFFF',
  },
  scrollContent: {
    flexGrow: 1,
    paddingHorizontal: 20,
    paddingTop: 16,
    paddingBottom: 90,
    justifyContent: 'center',
  },
  container: {
    width: '100%',
  },
  containerDesktop: {
    maxWidth: 520,
    alignSelf: 'center',
  },

  // Top Bar matching reference: Circular back button and Step 1 of 3
  topBar: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: 36,
  },
  backButton: {
    width: 42,
    height: 42,
    borderRadius: 21,
    backgroundColor: '#FFFFFF',
    borderWidth: 1,
    borderColor: '#E2E8F0',
    alignItems: 'center',
    justifyContent: 'center',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 1 },
    shadowOpacity: 0.04,
    shadowRadius: 3,
    elevation: 1,
  },
  stepPill: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#EFF6FF',
    borderWidth: 1,
    borderColor: '#BFDBFE',
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: 16,
  },
  stepDot: {
    width: 6,
    height: 6,
    borderRadius: 3,
    backgroundColor: '#2563EB',
    marginRight: 6,
  },
  stepPillText: {
    fontSize: 12,
    fontWeight: '700',
    color: '#2563EB',
  },

  // Header
  header: {
    marginBottom: 24,
  },
  badge: {
    fontSize: 11.5,
    fontWeight: '800',
    color: '#2563EB',
    letterSpacing: 1.2,
    textTransform: 'uppercase',
    marginBottom: 8,
  },
  title: {
    fontSize: 28,
    fontWeight: '800',
    color: '#0F172A',
    letterSpacing: -0.5,
    marginBottom: 8,
  },
  subtitle: {
    fontSize: 14,
    color: '#64748B',
    lineHeight: 21,
  },

  // Role Cards Stack
  rolesStack: {
    gap: 14,
    marginBottom: 24,
  },
  roleCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 18,
    borderWidth: 1.5,
    borderColor: '#E2E8F0',
    padding: 16,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.03,
    shadowRadius: 6,
    elevation: 1,
  },
  roleCardSelected: {
    borderColor: '#2563EB',
    borderWidth: 2,
    backgroundColor: '#FFFFFF',
    shadowColor: '#2563EB',
    shadowOpacity: 0.08,
    shadowRadius: 8,
    elevation: 2,
  },
  cardContent: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 14,
  },

  // Icon Boxes
  studentIconBox: {
    width: 48,
    height: 48,
    borderRadius: 14,
    backgroundColor: '#EFF6FF',
    alignItems: 'center',
    justifyContent: 'center',
  },
  facultyIconBox: {
    width: 48,
    height: 48,
    borderRadius: 14,
    backgroundColor: '#FAF5FF',
    alignItems: 'center',
    justifyContent: 'center',
  },

  // Card Texts
  cardTexts: {
    flex: 1,
  },
  roleTitleRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    marginBottom: 4,
  },
  roleTitle: {
    fontSize: 16.5,
    fontWeight: '800',
    color: '#0F172A',
  },
  popularBadge: {
    backgroundColor: '#ECFEFF',
    paddingHorizontal: 8,
    paddingVertical: 2.5,
    borderRadius: 6,
  },
  popularBadgeText: {
    fontSize: 10,
    fontWeight: '800',
    color: '#0891B2',
    letterSpacing: 0.5,
  },
  facultyBadge: {
    backgroundColor: '#FDF4FF',
    paddingHorizontal: 8,
    paddingVertical: 2.5,
    borderRadius: 6,
  },
  facultyBadgeText: {
    fontSize: 10,
    fontWeight: '800',
    color: '#9333EA',
    letterSpacing: 0.5,
  },
  roleDesc: {
    fontSize: 12.5,
    color: '#64748B',
    lineHeight: 18,
  },

  // Checkbox / Radio Circle on Right
  rightActionRow: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  checkCircleActive: {
    width: 22,
    height: 22,
    borderRadius: 11,
    backgroundColor: '#2563EB',
    alignItems: 'center',
    justifyContent: 'center',
  },
  checkCircleInactive: {
    width: 22,
    height: 22,
    borderRadius: 11,
    borderWidth: 1.5,
    borderColor: '#CBD5E1',
    backgroundColor: '#FFFFFF',
  },

  // Continue Button
  continueButton: {
    backgroundColor: '#2563EB',
    paddingVertical: 14,
    borderRadius: 14,
    alignItems: 'center',
    justifyContent: 'center',
    shadowColor: '#2563EB',
    shadowOffset: { width: 0, height: 3 },
    shadowOpacity: 0.25,
    shadowRadius: 6,
    elevation: 3,
  },
  continueButtonText: {
    color: '#FFFFFF',
    fontSize: 15.5,
    fontWeight: '700',
  },

  // Footer Link
  loginRedirect: {
    marginTop: 22,
    alignItems: 'center',
  },
  loginRedirectText: {
    fontSize: 13.5,
    color: '#64748B',
  },
  loginHighlight: {
    color: '#2563EB',
    fontWeight: '700',
  },
});
