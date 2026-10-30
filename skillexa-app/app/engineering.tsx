import { Feather } from '@expo/vector-icons';
import { router, useFocusEffect } from 'expo-router';
import React, { useCallback, useState } from 'react';
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
import { AppHeader } from '../components/common/AppHeader';
import { NotificationBellButton } from '../components/CollegeNotificationsModal';
import { ProgressStorage } from '../services/progressStorage';

export default function EngineeringDashboard() {
  const { width } = useWindowDimensions();
  const isDesktop = width >= 768;

  const totalCodingCount = 417;
  const totalDsaCount = 195;
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

  const codingPct = Math.round((codingSolved / totalCodingCount) * 100);
  const dsaPct = Math.round((dsaSolved / totalDsaCount) * 100);
  const totalSolved = codingSolved + dsaSolved;
  const overallPct = Math.round((codingPct + dsaPct) / 2);
  const completedModulesCount = totalSolved > 0 ? Math.min(5, Math.max(1, Math.floor(totalSolved / 25))) : 0;

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />

      {/* Top Header matching reference image: ← Back | Engineering Learning | Search, Bell, Profile */}
      <AppHeader
        showBack
        title="Engineering Learning"
        rightAction={
          <View style={styles.headerRightActions}>
            <TouchableOpacity
              style={styles.headerIconBtn}
              onPress={() => router.push('/coding-problems' as any)}
              activeOpacity={0.7}
            >
              <Feather name="search" size={19} color="#0F172A" />
            </TouchableOpacity>

            <NotificationBellButton />

            <TouchableOpacity
              style={styles.headerProfileBtn}
              onPress={() => router.push('/profile' as any)}
              activeOpacity={0.7}
            >
              <Feather name="user" size={16} color="#0F172A" />
            </TouchableOpacity>
          </View>
        }
      />

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        <View style={[styles.container, isDesktop && styles.containerDesktop]}>
          {/* Main Page Title Header */}
          <View style={styles.header}>
            <Text style={styles.title}>Engineering Learning</Text>
            <Text style={styles.subtitle}>Build skills, Prepare for your career.</Text>
          </View>

          {/* Overall Engineering Progress Card */}
          <View style={styles.progressCard}>
            <View style={styles.progressHeaderRow}>
              <Text style={styles.progressLabel}>OVERALL ENGINEERING PROGRESS</Text>
              <View style={styles.progressPercentBadge}>
                <Text style={styles.progressPercentText}>{overallPct}%</Text>
              </View>
            </View>

            {/* Clean Progress Bar Track */}
            <View style={styles.progressBarWrapper}>
              <View
                style={[
                  styles.progressBarFill,
                  { width: overallPct > 0 ? `${overallPct}%` : '0%' },
                ]}
              />
            </View>

            <Text style={styles.progressMeta}>
              {completedModulesCount > 0
                ? `${completedModulesCount} of 5 core modules completed (${totalSolved} solved)`
                : '0 of 5 core modules completed'}
            </Text>
          </View>

          {/* Section Heading */}
          <View style={styles.sectionHeader}>
            <Text style={styles.sectionTitle}>Your Learning Modules</Text>
            <Text style={styles.sectionSubtitle}>Structured career and technical curriculum</Text>
          </View>

          {/* Module 1: Coding Problems */}
          <View style={styles.moduleCard}>
            <View style={styles.moduleTopRow}>
              <View style={styles.moduleIconBox}>
                <Text style={styles.codeIconText}>{'< >'}</Text>
              </View>
              <View style={styles.moduleInfo}>
                <Text style={styles.moduleTitle}>Coding Problems</Text>
                <Text style={styles.moduleDesc}>Practice real programming problems</Text>
              </View>
            </View>

            <View style={styles.moduleStatsRow}>
              <Text style={styles.statLabel}>
                Solved: <Text style={styles.statValue}>{codingSolved} / {totalCodingCount}</Text>
              </Text>
              <Text style={styles.statLabel}>
                Progress: <Text style={styles.statValue}>{codingPct}%</Text>
              </Text>
            </View>

            <View style={styles.moduleProgressTrack}>
              <View
                style={[
                  styles.moduleProgressFill,
                  { width: codingPct > 0 ? `${codingPct}%` : '0%' },
                ]}
              />
            </View>

            <TouchableOpacity
              style={styles.moduleBtn}
              onPress={() => router.push('/coding-problems' as any)}
              activeOpacity={0.85}
            >
              <Text style={styles.moduleBtnText}>Practice Coding →</Text>
            </TouchableOpacity>
          </View>

          {/* Module 2: DSA Practice */}
          <View style={styles.moduleCard}>
            <View style={styles.moduleTopRow}>
              <View style={styles.moduleIconBox}>
                <Feather name="share-2" size={20} color="#18181B" />
              </View>
              <View style={styles.moduleInfo}>
                <Text style={styles.moduleTitle}>DSA Practice</Text>
                <Text style={styles.moduleDesc}>Master data structures and algorithms step by step</Text>
              </View>
            </View>

            <View style={styles.moduleStatsRow}>
              <Text style={styles.statLabel}>
                Solved: <Text style={styles.statValue}>{dsaSolved} / {totalDsaCount}</Text>
              </Text>
              <Text style={styles.statLabel}>
                Progress: <Text style={styles.statValue}>{dsaPct}%</Text>
              </Text>
            </View>

            <View style={styles.moduleProgressTrack}>
              <View
                style={[
                  styles.moduleProgressFill,
                  { width: dsaPct > 0 ? `${dsaPct}%` : '0%' },
                ]}
              />
            </View>

            <TouchableOpacity
              style={styles.moduleBtn}
              onPress={() => router.push('/dsa-practice' as any)}
              activeOpacity={0.85}
            >
              <Text style={styles.moduleBtnText}>Continue DSA Roadmap →</Text>
            </TouchableOpacity>
          </View>

          {/* Module 3: Resume Builder */}
          <View style={styles.moduleCard}>
            <View style={styles.moduleTopRow}>
              <View style={styles.moduleIconBox}>
                <Feather name="file-text" size={20} color="#18181B" />
              </View>
              <View style={styles.moduleInfo}>
                <Text style={styles.moduleTitle}>Resume Builder</Text>
                <Text style={styles.moduleDesc}>Create your ATS-ready professional resume</Text>
              </View>
            </View>

            <View style={styles.moduleStatsRow}>
              <Text style={styles.statLabel}>
                Profile Completion: <Text style={styles.statValue}>85%</Text>
              </Text>
              <Text style={styles.statLabel}>
                Templates: <Text style={styles.statValue}>3 Standard</Text>
              </Text>
            </View>

            <View style={styles.moduleProgressTrack}>
              <View style={[styles.moduleProgressFill, { width: '85%' }]} />
            </View>

            <TouchableOpacity
              style={styles.moduleBtn}
              onPress={() => router.push('/resume-builder' as any)}
              activeOpacity={0.85}
            >
              <Text style={styles.moduleBtnText}>Build Resume →</Text>
            </TouchableOpacity>
          </View>

          {/* Module 4: AI Mock Interview */}
          <View style={styles.moduleCard}>
            <View style={styles.moduleTopRow}>
              <View style={styles.moduleIconBox}>
                <Feather name="message-square" size={20} color="#18181B" />
              </View>
              <View style={styles.moduleInfo}>
                <Text style={styles.moduleTitle}>AI Mock Interview</Text>
                <Text style={styles.moduleDesc}>Practice technical and HR interviews with instant AI evaluation</Text>
              </View>
            </View>

            <View style={styles.moduleStatsRow}>
              <Text style={styles.statLabel}>
                Completed: <Text style={styles.statValue}>3 Interviews</Text>
              </Text>
              <Text style={styles.statLabel}>
                Average Score: <Text style={styles.statValue}>82 / 100</Text>
              </Text>
            </View>

            <View style={styles.moduleProgressTrack}>
              <View style={[styles.moduleProgressFill, { width: '82%' }]} />
            </View>

            <TouchableOpacity
              style={styles.moduleBtn}
              onPress={() => router.push('/mock-interviews' as any)}
              activeOpacity={0.85}
            >
              <Text style={styles.moduleBtnText}>Start AI Interview →</Text>
            </TouchableOpacity>
          </View>

          {/* Module 5: Placement Preparation */}
          <View style={styles.moduleCard}>
            <View style={styles.moduleTopRow}>
              <View style={styles.moduleIconBox}>
                <Feather name="briefcase" size={20} color="#18181B" />
              </View>
              <View style={styles.moduleInfo}>
                <Text style={styles.moduleTitle}>Placement Preparation</Text>
                <Text style={styles.moduleDesc}>Prepare for aptitude, technical MCQs and HR rounds</Text>
              </View>
            </View>

            <View style={styles.moduleStatsRow}>
              <Text style={styles.statLabel}>
                Overall Readiness: <Text style={styles.statValue}>54%</Text>
              </Text>
              <Text style={styles.statLabel}>
                Company Profiles: <Text style={styles.statValue}>24 FAANG/MNC</Text>
              </Text>
            </View>

            <View style={styles.moduleProgressTrack}>
              <View style={[styles.moduleProgressFill, { width: '54%' }]} />
            </View>

            <TouchableOpacity
              style={styles.moduleBtn}
              onPress={() => router.push('/placement-preparation' as any)}
              activeOpacity={0.85}
            >
              <Text style={styles.moduleBtnText}>Prepare for Placement →</Text>
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
  scrollContent: {
    paddingHorizontal: 16,
    paddingTop: 18,
    paddingBottom: 90,
  },
  container: {
    width: '100%',
  },
  containerDesktop: {
    maxWidth: 960,
    alignSelf: 'center',
  },

  // Header Right Actions
  headerRightActions: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
  },
  headerIconBtn: {
    width: 32,
    height: 32,
    alignItems: 'center',
    justifyContent: 'center',
  },
  headerProfileBtn: {
    width: 32,
    height: 32,
    borderRadius: 16,
    borderWidth: 1,
    borderColor: '#E2E8F0',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#FFFFFF',
  },

  // Page Header
  header: {
    marginBottom: 20,
    marginTop: 4,
  },
  title: {
    fontSize: 26,
    fontWeight: '800',
    color: '#0F172A',
    letterSpacing: -0.3,
    marginBottom: 4,
  },
  subtitle: {
    fontSize: 14,
    color: '#64748B',
    fontWeight: '400',
  },

  // Overall Progress Card
  progressCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 16,
    padding: 18,
    borderWidth: 1,
    borderColor: '#E5E7EB',
    marginBottom: 24,
  },
  progressHeaderRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 12,
  },
  progressLabel: {
    fontSize: 12,
    fontWeight: '700',
    color: '#475569',
    letterSpacing: 0.6,
  },
  progressPercentBadge: {
    paddingHorizontal: 12,
    paddingVertical: 3,
    borderRadius: 16,
    borderWidth: 1,
    borderColor: '#E5E7EB',
    backgroundColor: '#FFFFFF',
    alignItems: 'center',
    justifyContent: 'center',
  },
  progressPercentText: {
    fontSize: 12.5,
    fontWeight: '800',
    color: '#0F172A',
  },
  progressBarWrapper: {
    height: 6,
    backgroundColor: '#F3F4F6',
    borderRadius: 3,
    overflow: 'hidden',
    marginBottom: 10,
  },
  progressBarFill: {
    height: '100%',
    backgroundColor: '#18181B',
    borderRadius: 3,
  },
  progressMeta: {
    fontSize: 13,
    color: '#64748B',
    fontWeight: '400',
  },

  // Section Header
  sectionHeader: {
    marginBottom: 14,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: '800',
    color: '#0F172A',
    letterSpacing: -0.2,
  },
  sectionSubtitle: {
    fontSize: 13,
    color: '#64748B',
    marginTop: 2,
    fontWeight: '400',
  },

  // Module Card
  moduleCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 16,
    padding: 18,
    borderWidth: 1,
    borderColor: '#E5E7EB',
    marginBottom: 16,
  },
  moduleTopRow: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 14,
  },
  moduleIconBox: {
    width: 44,
    height: 44,
    borderRadius: 12,
    backgroundColor: '#F3F4F6',
    alignItems: 'center',
    justifyContent: 'center',
    marginRight: 14,
    borderWidth: 1,
    borderColor: '#E5E7EB',
  },
  codeIconText: {
    fontSize: 15,
    fontWeight: '800',
    color: '#18181B',
    letterSpacing: 1,
  },
  moduleInfo: {
    flex: 1,
  },
  moduleTitle: {
    fontSize: 16,
    fontWeight: '800',
    color: '#0F172A',
  },
  moduleDesc: {
    fontSize: 13,
    color: '#64748B',
    marginTop: 2,
    lineHeight: 18,
  },
  moduleStatsRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 8,
  },
  statLabel: {
    fontSize: 13,
    color: '#64748B',
    fontWeight: '400',
  },
  statValue: {
    fontWeight: '700',
    color: '#0F172A',
  },
  moduleProgressTrack: {
    height: 5,
    backgroundColor: '#F3F4F6',
    borderRadius: 3,
    overflow: 'hidden',
    marginBottom: 14,
  },
  moduleProgressFill: {
    height: '100%',
    backgroundColor: '#18181B',
    borderRadius: 3,
  },
  moduleBtn: {
    backgroundColor: '#18181B',
    borderRadius: 12,
    paddingVertical: 12,
    alignItems: 'center',
    justifyContent: 'center',
  },
  moduleBtnText: {
    color: '#FFFFFF',
    fontSize: 14,
    fontWeight: '700',
  },
});
