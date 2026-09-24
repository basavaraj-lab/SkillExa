import { Feather } from '@expo/vector-icons';
import { router } from 'expo-router';
import React from 'react';
import {
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from 'react-native';
import { AppHeader } from '../components/common/AppHeader';
import { ProgressBar } from '../components/common/EducationalCards';
import { Palette, Radii, Shadows } from '../constants/theme';

export default function EngineeringDashboard() {
  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader showBack title="Engineering Learning" />

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {/* Header Title */}
        <View style={styles.header}>
          <Text style={styles.title}>Engineering Learning</Text>
          <Text style={styles.subtitle}>Build skills. Prepare for your career.</Text>
        </View>

        {/* Overall Progress Banner */}
        <View style={styles.progressCard}>
          <View style={styles.progressHeaderRow}>
            <View>
              <Text style={styles.progressLabel}>OVERALL ENGINEERING PROGRESS</Text>
              <Text style={styles.progressValue}>68% Complete</Text>
            </View>
            <View style={styles.progressPercentBadge}>
              <Text style={styles.progressPercentText}>68%</Text>
            </View>
          </View>
          <View style={styles.progressBarWrapper}>
            <ProgressBar progress={0.68} color={Palette.primary} />
          </View>
          <Text style={styles.progressMeta}>3 of 5 core modules in progress</Text>
        </View>

        {/* Section Heading */}
        <View style={styles.sectionHeader}>
          <Text style={styles.sectionTitle}>Your Learning Modules</Text>
          <Text style={styles.sectionSubtitle}>Structured career and technical curriculum</Text>
        </View>

        {/* Module 1: Coding Problems */}
        <View style={styles.moduleCard}>
          <View style={styles.moduleTopRow}>
            <View style={[styles.moduleIconCircle, { backgroundColor: Palette.primaryLight }]}>
              <Feather name="terminal" size={22} color={Palette.primary} />
            </View>
            <View style={styles.moduleInfo}>
              <Text style={styles.moduleTitle}>Coding Problems</Text>
              <Text style={styles.moduleDesc}>Practice real programming problems.</Text>
            </View>
          </View>
          <View style={styles.moduleStatsRow}>
            <Text style={styles.statLabel}>Solved: <Text style={styles.statValue}>42 / 100</Text></Text>
            <Text style={styles.statLabel}>Progress: <Text style={styles.statValue}>42%</Text></Text>
          </View>
          <View style={styles.moduleProgressTrack}>
            <ProgressBar progress={0.42} color={Palette.primary} />
          </View>
          <TouchableOpacity
            style={styles.moduleBtn}
            onPress={() => router.push('/coding-problems' as any)}
            activeOpacity={0.85}
          >
            <Text style={styles.moduleBtnText}>Practice Coding</Text>
            <Feather name="arrow-right" size={14} color="#FFFFFF" />
          </TouchableOpacity>
        </View>

        {/* Module 2: DSA Practice */}
        <View style={styles.moduleCard}>
          <View style={styles.moduleTopRow}>
            <View style={[styles.moduleIconCircle, { backgroundColor: Palette.successLight }]}>
              <Feather name="code" size={22} color={Palette.success} />
            </View>
            <View style={styles.moduleInfo}>
              <Text style={styles.moduleTitle}>DSA Practice</Text>
              <Text style={styles.moduleDesc}>Master data structures and algorithms step by step.</Text>
            </View>
          </View>
          <View style={styles.moduleStatsRow}>
            <Text style={styles.statLabel}>Topics: <Text style={styles.statValue}>12 / 20 Topics</Text></Text>
            <Text style={styles.statLabel}>Progress: <Text style={styles.statValue}>60%</Text></Text>
          </View>
          <View style={styles.moduleProgressTrack}>
            <ProgressBar progress={0.60} color={Palette.success} />
          </View>
          <TouchableOpacity
            style={[styles.moduleBtn, { backgroundColor: Palette.success }]}
            onPress={() => router.push('/dsa-practice' as any)}
            activeOpacity={0.85}
          >
            <Text style={styles.moduleBtnText}>Continue DSA Roadmap</Text>
            <Feather name="arrow-right" size={14} color="#FFFFFF" />
          </TouchableOpacity>
        </View>

        {/* Module 3: Resume Builder */}
        <View style={styles.moduleCard}>
          <View style={styles.moduleTopRow}>
            <View style={[styles.moduleIconCircle, { backgroundColor: Palette.warningLight }]}>
              <Feather name="file-text" size={22} color={Palette.warning} />
            </View>
            <View style={styles.moduleInfo}>
              <Text style={styles.moduleTitle}>Resume Builder</Text>
              <Text style={styles.moduleDesc}>Create your ATS-ready professional resume.</Text>
            </View>
          </View>
          <View style={styles.moduleStatsRow}>
            <Text style={styles.statLabel}>Profile Completion: <Text style={styles.statValue}>85%</Text></Text>
            <Text style={styles.statLabel}>Templates: <Text style={styles.statValue}>3 Standard</Text></Text>
          </View>
          <View style={styles.moduleProgressTrack}>
            <ProgressBar progress={0.85} color={Palette.warning} />
          </View>
          <TouchableOpacity
            style={[styles.moduleBtn, { backgroundColor: Palette.primary }]}
            onPress={() => router.push('/resume-builder' as any)}
            activeOpacity={0.85}
          >
            <Text style={styles.moduleBtnText}>Build Resume</Text>
            <Feather name="arrow-right" size={14} color="#FFFFFF" />
          </TouchableOpacity>
        </View>

        {/* Module 4: AI Mock Interview (Purple AI Theme) */}
        <View style={[styles.moduleCard, styles.aiCard]}>
          <View style={styles.moduleTopRow}>
            <View style={[styles.moduleIconCircle, { backgroundColor: Palette.aiPurpleLight }]}>
              <Feather name="message-square" size={22} color={Palette.aiPurple} />
            </View>
            <View style={styles.moduleInfo}>
              <View style={styles.aiBadgeRow}>
                <Text style={styles.moduleTitle}>AI Mock Interview</Text>
                <View style={styles.aiPill}>
                  <Text style={styles.aiPillText}>AI POWERED</Text>
                </View>
              </View>
              <Text style={styles.moduleDesc}>Practice technical and HR interviews with instant AI evaluation.</Text>
            </View>
          </View>
          <View style={styles.moduleStatsRow}>
            <Text style={styles.statLabel}>Completed: <Text style={styles.statValue}>3 Interviews</Text></Text>
            <Text style={styles.statLabel}>Average Score: <Text style={styles.statValue}>82 / 100</Text></Text>
          </View>
          <TouchableOpacity
            style={[styles.moduleBtn, { backgroundColor: Palette.aiPurple }]}
            onPress={() => router.push('/mock-interviews' as any)}
            activeOpacity={0.85}
          >
            <Text style={styles.moduleBtnText}>Start AI Interview</Text>
            <Feather name="arrow-right" size={14} color="#FFFFFF" />
          </TouchableOpacity>
        </View>

        {/* Module 5: Placement Preparation */}
        <View style={styles.moduleCard}>
          <View style={styles.moduleTopRow}>
            <View style={[styles.moduleIconCircle, { backgroundColor: Palette.primaryLight }]}>
              <Feather name="briefcase" size={22} color={Palette.primary} />
            </View>
            <View style={styles.moduleInfo}>
              <Text style={styles.moduleTitle}>Placement Preparation</Text>
              <Text style={styles.moduleDesc}>Prepare for aptitude, technical MCQs and HR rounds.</Text>
            </View>
          </View>
          <View style={styles.moduleStatsRow}>
            <Text style={styles.statLabel}>Overall Readiness: <Text style={styles.statValue}>54%</Text></Text>
            <Text style={styles.statLabel}>Company Profiles: <Text style={styles.statValue}>24 FAANG/MNC</Text></Text>
          </View>
          <View style={styles.moduleProgressTrack}>
            <ProgressBar progress={0.54} color={Palette.primary} />
          </View>
          <TouchableOpacity
            style={[styles.moduleBtn, { backgroundColor: Palette.primary }]}
            onPress={() => router.push('/placement-preparation' as any)}
            activeOpacity={0.85}
          >
            <Text style={styles.moduleBtnText}>Prepare for Placement</Text>
            <Feather name="arrow-right" size={14} color="#FFFFFF" />
          </TouchableOpacity>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: Palette.background,
  },
  scrollContent: {
    paddingHorizontal: 16,
    paddingTop: 16,
    paddingBottom: 40,
  },
  header: {
    marginBottom: 20,
  },
  title: {
    fontSize: 22,
    fontWeight: '800',
    color: Palette.textTitle,
    marginBottom: 4,
  },
  subtitle: {
    fontSize: 14,
    color: Palette.textSecondary,
  },
  progressCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 18,
    borderWidth: 1,
    borderColor: Palette.border,
    marginBottom: 24,
    ...Shadows.card,
  },
  progressHeaderRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 12,
  },
  progressLabel: {
    fontSize: 11,
    fontWeight: '800',
    color: Palette.primary,
    letterSpacing: 0.8,
  },
  progressValue: {
    fontSize: 17,
    fontWeight: '800',
    color: Palette.textTitle,
    marginTop: 2,
  },
  progressPercentBadge: {
    width: 44,
    height: 44,
    borderRadius: 22,
    backgroundColor: Palette.primaryLight,
    borderWidth: 2,
    borderColor: Palette.primary,
    alignItems: 'center',
    justifyContent: 'center',
  },
  progressPercentText: {
    fontSize: 13,
    fontWeight: '800',
    color: Palette.primary,
  },
  progressBarWrapper: {
    marginBottom: 8,
  },
  progressMeta: {
    fontSize: 12,
    color: Palette.textSecondary,
  },
  sectionHeader: {
    marginBottom: 14,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: '800',
    color: Palette.textTitle,
  },
  sectionSubtitle: {
    fontSize: 12,
    color: Palette.textSecondary,
    marginTop: 2,
  },
  moduleCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 18,
    borderWidth: 1,
    borderColor: Palette.border,
    marginBottom: 16,
    ...Shadows.card,
  },
  aiCard: {
    borderLeftWidth: 4,
    borderLeftColor: Palette.aiPurple,
  },
  moduleTopRow: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    marginBottom: 12,
  },
  moduleIconCircle: {
    width: 44,
    height: 44,
    borderRadius: 12,
    alignItems: 'center',
    justifyContent: 'center',
    marginRight: 12,
  },
  moduleInfo: {
    flex: 1,
  },
  aiBadgeRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  aiPill: {
    backgroundColor: Palette.aiPurpleLight,
    paddingHorizontal: 8,
    paddingVertical: 2,
    borderRadius: 6,
  },
  aiPillText: {
    fontSize: 9,
    fontWeight: '800',
    color: Palette.aiPurple,
    letterSpacing: 0.5,
  },
  moduleTitle: {
    fontSize: 16,
    fontWeight: '800',
    color: Palette.textTitle,
  },
  moduleDesc: {
    fontSize: 13,
    color: Palette.textBody,
    marginTop: 3,
    lineHeight: 18,
  },
  moduleStatsRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 10,
  },
  statLabel: {
    fontSize: 12,
    color: Palette.textSecondary,
  },
  statValue: {
    fontWeight: '700',
    color: Palette.textTitle,
  },
  moduleProgressTrack: {
    marginBottom: 14,
  },
  moduleBtn: {
    backgroundColor: Palette.primary,
    borderRadius: Radii.button,
    paddingVertical: 11,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
  },
  moduleBtnText: {
    color: '#FFFFFF',
    fontSize: 13.5,
    fontWeight: '700',
  },
});