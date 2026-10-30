import { Feather } from '@expo/vector-icons';
import { router, useFocusEffect } from 'expo-router';
import React, { useCallback, useState } from 'react';
import {
  Platform,
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TouchableOpacity,
  useWindowDimensions,
  View,
} from 'react-native';
import { useAuth } from '../components/auth-context';
import { NotificationBellButton } from '../components/CollegeNotificationsModal';
import { ProgressStorage } from '../services/progressStorage';

export default function EngineeringDashboard() {
  const { width } = useWindowDimensions();
  const isDesktop = width >= 768;
  const { profile } = useAuth();

  const userInitial = (profile?.name || 'Ganesh').charAt(0).toUpperCase();

  const [codingSolved, setCodingSolved] = useState<number>(0);
  const [dsaSolved, setDsaSolved] = useState<number>(0);

  // Load actual solved questions from user session storage
  const loadUserProgress = useCallback(() => {
    const actualDsa = ProgressStorage.getSolvedDsaProblems();
    const actualCoding = ProgressStorage.getSolvedCodingTopics();
    setDsaSolved(actualDsa.length);
    setCodingSolved(actualCoding.length);
  }, []);

  useFocusEffect(
    useCallback(() => {
      loadUserProgress();
    }, [loadUserProgress])
  );

  const handleBack = () => {
    if (router.canGoBack()) {
      router.back();
    } else {
      router.replace('/pathselection' as any);
    }
  };

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />

      {/* Top Header matching reference image: ← Back to Paths | Engineering Learning | Bell, Avatar (G) */}
      <View style={styles.topBar}>
        <TouchableOpacity
          style={styles.backButton}
          onPress={handleBack}
          activeOpacity={0.7}
        >
          <Feather name="arrow-left" size={17} color="#475569" />
          <Text style={styles.backButtonText}>Back to Paths</Text>
        </TouchableOpacity>

        <Text style={styles.topBarTitle}>Engineering Learning</Text>

        <View style={styles.topBarRight}>
          <NotificationBellButton />

          <TouchableOpacity
            style={styles.avatarButton}
            onPress={() => router.push('/profile' as any)}
            activeOpacity={0.7}
          >
            <Text style={styles.avatarText}>{userInitial}</Text>
          </TouchableOpacity>
        </View>
      </View>

      <ScrollView
        contentContainerStyle={styles.scrollContent}
        showsVerticalScrollIndicator={false}
      >
        <View style={[styles.container, isDesktop && styles.containerDesktop]}>
          {/* Main Section Header */}
          <View style={styles.sectionHeader}>
            <Text style={styles.sectionTitle}>Your Learning Modules</Text>
            <Text style={styles.sectionSubtitle}>
              Structured career and technical curriculum
            </Text>
          </View>

          {/* Module 1: Coding Problems */}
          <View style={styles.card}>
            <View style={styles.cardHeader}>
              <View style={styles.iconBox}>
                <Text style={styles.terminalIconText}>{'>_'}</Text>
              </View>
              <View style={styles.cardTitles}>
                <Text style={styles.cardTitle}>Coding Problems</Text>
                <Text style={styles.cardSubtitle}>
                  Practice real programming problems.
                </Text>
              </View>
            </View>

            <TouchableOpacity
              style={styles.actionButton}
              onPress={() => router.push('/coding-problems' as any)}
              activeOpacity={0.85}
            >
              <Text style={styles.actionButtonText}>Practice Coding →</Text>
            </TouchableOpacity>
          </View>

          {/* Module 2: DSA Practice */}
          <View style={styles.card}>
            <View style={styles.cardHeader}>
              <View style={styles.iconBox}>
                <Text style={styles.dsaIconText}>{'< >'}</Text>
              </View>
              <View style={styles.cardTitles}>
                <Text style={styles.cardTitle}>DSA Practice</Text>
                <Text style={styles.cardSubtitle}>
                  Master data structures and algorithms step by step.
                </Text>
              </View>
            </View>

            <TouchableOpacity
              style={styles.actionButton}
              onPress={() => router.push('/dsa-practice' as any)}
              activeOpacity={0.85}
            >
              <Text style={styles.actionButtonText}>Continue DSA Roadmap →</Text>
            </TouchableOpacity>
          </View>

          {/* Module 3: Resume Builder */}
          <View style={styles.card}>
            <View style={styles.cardHeader}>
              <View style={styles.iconBox}>
                <Feather name="file-text" size={20} color="#2563EB" />
              </View>
              <View style={styles.cardTitles}>
                <Text style={styles.cardTitle}>Resume Builder</Text>
                <Text style={styles.cardSubtitle}>
                  Create your ATS-ready professional resume.
                </Text>
              </View>
            </View>

            <View style={styles.metaRowRight}>
              <Text style={styles.metaText}>
                Templates: <Text style={styles.metaHighlight}>3 Standard</Text>
              </Text>
            </View>

            <TouchableOpacity
              style={styles.actionButton}
              onPress={() => router.push('/resume-builder' as any)}
              activeOpacity={0.85}
            >
              <Text style={styles.actionButtonText}>Build Resume →</Text>
            </TouchableOpacity>
          </View>

          {/* Module 4: AI Mock Interview */}
          <View style={styles.card}>
            <View style={styles.cardHeader}>
              <View style={styles.iconBox}>
                <Feather name="message-square" size={20} color="#2563EB" />
              </View>
              <View style={styles.cardTitles}>
                <View style={styles.titleBadgeRow}>
                  <Text style={styles.cardTitle}>AI Mock Interview</Text>
                  <View style={styles.aiBadge}>
                    <Text style={styles.aiBadgeText}>AI POWERED</Text>
                  </View>
                </View>
                <Text style={styles.cardSubtitle}>
                  Practice technical and HR interviews with instant AI evaluation.
                </Text>
              </View>
            </View>

            <View style={styles.metaRowRight}>
              <Text style={styles.metaText}>
                Average Score: <Text style={styles.metaHighlight}>-</Text>
              </Text>
            </View>

            <TouchableOpacity
              style={styles.actionButton}
              onPress={() => router.push('/mock-interviews' as any)}
              activeOpacity={0.85}
            >
              <Text style={styles.actionButtonText}>Start AI Interview →</Text>
            </TouchableOpacity>
          </View>

          {/* Module 5: Placement Preparation */}
          <View style={styles.card}>
            <View style={styles.cardHeader}>
              <View style={styles.iconBox}>
                <Feather name="briefcase" size={20} color="#2563EB" />
              </View>
              <View style={styles.cardTitles}>
                <Text style={styles.cardTitle}>Placement Preparation</Text>
                <Text style={styles.cardSubtitle}>
                  Prepare for aptitude, technical MCQs and HR rounds.
                </Text>
              </View>
            </View>

            <View style={styles.metaRowRight}>
              <Text style={styles.metaText}>
                Company Profiles: <Text style={styles.metaHighlight}>24 FAANG/MNC</Text>
              </Text>
            </View>

            <TouchableOpacity
              style={styles.actionButton}
              onPress={() => router.push('/placement-preparation' as any)}
              activeOpacity={0.85}
            >
              <Text style={styles.actionButtonText}>Prepare for Placement →</Text>
            </TouchableOpacity>
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

  // Top Bar
  topBar: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: 16,
    paddingVertical: 12,
    backgroundColor: '#FFFFFF',
    borderBottomWidth: 1,
    borderBottomColor: '#F1F5F9',
  },
  backButton: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    paddingVertical: 4,
  },
  backButtonText: {
    fontSize: 13.5,
    fontWeight: '600',
    color: '#475569',
  },
  topBarTitle: {
    fontSize: 16,
    fontWeight: '700',
    color: '#0F172A',
  },
  topBarRight: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 10,
  },
  avatarButton: {
    width: 34,
    height: 34,
    borderRadius: 17,
    backgroundColor: '#EFF6FF',
    borderWidth: 1.5,
    borderColor: '#BFDBFE',
    alignItems: 'center',
    justifyContent: 'center',
  },
  avatarText: {
    fontSize: 14,
    fontWeight: '700',
    color: '#2563EB',
  },

  // Scroll Content
  scrollContent: {
    paddingHorizontal: 16,
    paddingTop: 20,
    paddingBottom: 40,
  },
  container: {
    width: '100%',
  },
  containerDesktop: {
    maxWidth: 680,
    alignSelf: 'center',
  },

  // Section Header
  sectionHeader: {
    marginBottom: 20,
  },
  sectionTitle: {
    fontSize: 22,
    fontWeight: '800',
    color: '#0F172A',
    letterSpacing: -0.3,
  },
  sectionSubtitle: {
    fontSize: 14,
    color: '#64748B',
    marginTop: 4,
    fontWeight: '400',
  },

  // Module Card
  card: {
    backgroundColor: '#FFFFFF',
    borderRadius: 20,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    padding: 18,
    marginBottom: 16,
    shadowColor: '#0F172A',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.04,
    shadowRadius: 8,
    elevation: 2,
  },
  cardHeader: {
    flexDirection: 'row',
    alignItems: 'flex-start',
  },
  iconBox: {
    width: 44,
    height: 44,
    borderRadius: 12,
    backgroundColor: '#EFF6FF',
    borderWidth: 1,
    borderColor: '#DBEAFE',
    alignItems: 'center',
    justifyContent: 'center',
    marginRight: 14,
  },
  terminalIconText: {
    fontSize: 16,
    fontWeight: '800',
    color: '#2563EB',
    fontFamily: Platform.OS === 'ios' ? 'Menlo' : 'monospace',
    letterSpacing: -0.5,
  },
  dsaIconText: {
    fontSize: 14,
    fontWeight: '800',
    color: '#2563EB',
    letterSpacing: 1,
  },
  cardTitles: {
    flex: 1,
  },
  titleBadgeRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    flexWrap: 'wrap',
  },
  cardTitle: {
    fontSize: 17,
    fontWeight: '700',
    color: '#0F172A',
    marginBottom: 4,
  },
  cardSubtitle: {
    fontSize: 13.5,
    color: '#64748B',
    lineHeight: 18,
  },
  aiBadge: {
    backgroundColor: '#EFF6FF',
    borderWidth: 1,
    borderColor: '#DBEAFE',
    borderRadius: 6,
    paddingHorizontal: 8,
    paddingVertical: 2,
    marginBottom: 4,
  },
  aiBadgeText: {
    fontSize: 10.5,
    fontWeight: '800',
    color: '#2563EB',
    letterSpacing: 0.5,
  },

  // Right-aligned Metadata
  metaRowRight: {
    alignItems: 'flex-end',
    marginTop: 10,
    marginBottom: 2,
  },
  metaText: {
    fontSize: 12.5,
    color: '#64748B',
  },
  metaHighlight: {
    fontWeight: '700',
    color: '#0F172A',
  },

  // Action Button
  actionButton: {
    backgroundColor: '#2563EB',
    borderRadius: 12,
    paddingVertical: 13,
    alignItems: 'center',
    justifyContent: 'center',
    marginTop: 14,
    shadowColor: '#2563EB',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.15,
    shadowRadius: 6,
    elevation: 3,
  },
  actionButtonText: {
    color: '#FFFFFF',
    fontSize: 14.5,
    fontWeight: '700',
    letterSpacing: 0.2,
  },
});
