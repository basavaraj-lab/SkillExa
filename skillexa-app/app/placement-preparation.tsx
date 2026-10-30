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

const ROADMAP_STAGES = [
  { id: 1, label: 'Quantitative Aptitude', status: 'completed', score: '82%' },
  { id: 2, label: 'Logical Reasoning', status: 'completed', score: '78%' },
  { id: 3, label: 'Core Coding Practice', status: 'current', score: '64%' },
  { id: 4, label: 'CS Technical MCQs', status: 'current', score: '55%' },
  { id: 5, label: 'Technical Panel Interview', status: 'pending', score: '--' },
  { id: 6, label: 'HR Behavioral Interview', status: 'pending', score: '--' },
  { id: 7, label: 'Placement Ready Certification', status: 'pending', score: '--' },
];

const WEAK_AREAS = [
  { topic: 'Dynamic Programming & Memoization', accuracy: '42%', track: 'Coding' },
  { topic: 'Permutations & Probability', accuracy: '48%', track: 'Aptitude' },
  { topic: 'Operating System Semaphores', accuracy: '52%', track: 'Technical MCQs' },
];

const COMPANIES = [
  { name: 'Google', pattern: 'DSA + System Design', questions: '180 Problems' },
  { name: 'Amazon', pattern: 'Leadership Principles + Coding', questions: '210 Problems' },
  { name: 'Microsoft', pattern: 'Data Structures + Algorithms', questions: '165 Problems' },
  { name: 'TCS & Infosys', pattern: 'Aptitude + CS Fundamentals', questions: '350 Questions' },
];

export default function PlacementPreparationPage() {
  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader showBack title="Placement Preparation" subtitle="Career Acceleration Roadmap" />

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {/* Header */}
        <View style={styles.header}>
          <Text style={styles.title}>Placement Acceleration</Text>
          <Text style={styles.subtitle}>Prepare for campus drives, online assessments, and interview rounds.</Text>
        </View>

        {/* Readiness Meter Card */}
        <View style={styles.readinessCard}>
          <View style={styles.readinessTopRow}>
            <View>
              <Text style={styles.readinessLabel}>OVERALL PLACEMENT READINESS</Text>
              <Text style={styles.readinessValue}>72% Ready</Text>
            </View>
            <View style={styles.readinessScoreCircle}>
              <Text style={styles.readinessScoreNum}>72</Text>
              <Text style={styles.readinessScoreSub}>INDEX</Text>
            </View>
          </View>
          <ProgressBar progress={0.72} color={Palette.primary} />
          <Text style={styles.readinessMeta}>4 of 7 milestone stages cleared</Text>
        </View>

        {/* Placement Roadmap Stages */}
        <View style={styles.sectionHeaderRow}>
          <Text style={styles.sectionTitle}>Placement Roadmap</Text>
          <Text style={styles.sectionSubtitle}>Step-by-step career milestone pipeline</Text>
        </View>

        <View style={styles.roadmapCard}>
          {ROADMAP_STAGES.map((stage, idx) => {
            const isCompleted = stage.status === 'completed';
            const isCurrent = stage.status === 'current';

            return (
              <View key={stage.id} style={styles.stageItemRow}>
                <View style={styles.stageLeftCol}>
                  <View
                    style={[
                      styles.stageDot,
                      isCompleted && styles.stageDotCompleted,
                      isCurrent && styles.stageDotCurrent,
                    ]}
                  >
                    {isCompleted ? (
                      <Feather name="check" size={12} color="#FFFFFF" />
                    ) : (
                      <Text style={[styles.stageNum, isCurrent && { color: '#FFFFFF' }]}>{stage.id}</Text>
                    )}
                  </View>
                  {idx < ROADMAP_STAGES.length - 1 && <View style={styles.stageLine} />}
                </View>

                <View style={styles.stageContent}>
                  <Text style={[styles.stageName, isCurrent && styles.stageNameCurrent]}>
                    {stage.label}
                  </Text>
                  <Text style={styles.stageScore}>
                    Status: {isCompleted ? '✓ Passed (' + stage.score + ')' : isCurrent ? '⚡ In Progress' : 'Locked'}
                  </Text>
                </View>
              </View>
            );
          })}
        </View>

        {/* Dynamic LLM Aptitude Test Banner */}
        <View style={styles.aptitudeBanner}>
          <View style={styles.aptitudeTopRow}>
            <View style={styles.aptitudeIconWrap}>
              <Feather name="zap" size={24} color="#FFFFFF" />
            </View>
            <View style={{ flex: 1 }}>
              <View style={{ flexDirection: 'row', alignItems: 'center', gap: 6, flexWrap: 'wrap' }}>
                <Text style={styles.aptitudeTitle}>AI Aptitude Test</Text>
                <View style={styles.aiBadge}>
                  <Text style={styles.aiBadgeText}>LLM GENERATED</Text>
                </View>
              </View>
              <Text style={styles.aptitudeSubtitle}>
                Dynamic, unique placement questions generated per attempt.
              </Text>
            </View>
          </View>

          <View style={styles.aptitudePillsRow}>
            <View style={styles.aptitudePill}>
              <Text style={styles.aptitudePillText}>📊 Quant (15 topics)</Text>
            </View>
            <View style={styles.aptitudePill}>
              <Text style={styles.aptitudePillText}>🧩 Logic (11 tracks)</Text>
            </View>
            <View style={styles.aptitudePill}>
              <Text style={styles.aptitudePillText}>📝 Verbal Ability</Text>
            </View>
            <View style={styles.aptitudePill}>
              <Text style={styles.aptitudePillText}>📈 Data Interpretation</Text>
            </View>
          </View>

          <View style={styles.aptitudeFooterRow}>
            <View style={styles.aptitudeMetaCol}>
              <Text style={styles.aptitudeMetaText}>• Easy, Intermediate, Advanced</Text>
              <Text style={styles.aptitudeMetaText}>• Secure answers & negative marking</Text>
            </View>
            <TouchableOpacity
              id="start-aptitude-test-btn"
              style={styles.aptitudeStartBtn}
              onPress={() => router.push('/aptitude-test' as any)}
              activeOpacity={0.85}
            >
              <Text style={styles.aptitudeStartBtnText}>Start Test</Text>
              <Feather name="arrow-right" size={16} color="#FFFFFF" />
            </TouchableOpacity>
          </View>
        </View>

        {/* Live Interview Portal Banner */}
        <TouchableOpacity
          style={styles.liveInterviewBanner}
          onPress={() => router.push('/live-interview' as any)}
          activeOpacity={0.88}
        >
          <View style={styles.liveInterviewBannerIcon}>
            <Feather name="video" size={24} color="#FFFFFF" />
          </View>
          <View style={{ flex: 1 }}>
            <View style={{ flexDirection: 'row', alignItems: 'center', gap: 6, marginBottom: 2 }}>
              <Text style={styles.liveInterviewBannerTitle}>SkillExa Live Interview</Text>
              <View style={styles.liveBadge}>
                <Text style={styles.liveBadgeText}>LIVE PANEL</Text>
              </View>
            </View>
            <Text style={styles.liveInterviewBannerDesc}>
              Face-to-face video mock & panel rounds with college faculty and placement interviewers.
            </Text>
          </View>
          <Feather name="arrow-right" size={20} color={Palette.primary} />
        </TouchableOpacity>

        {/* Targeted Weak Areas */}
        <View style={styles.sectionHeaderRow}>
          <Text style={styles.sectionTitle}>Targeted Weak Areas</Text>
          <Text style={styles.sectionSubtitle}>Improve these to reach 85%+ Readiness Index</Text>
        </View>

        <View style={styles.weakAreasContainer}>
          {WEAK_AREAS.map((item, index) => (
            <View key={index} style={styles.weakCard}>
              <View style={styles.weakCardInfo}>
                <Text style={styles.weakTopicTitle}>{item.topic}</Text>
                <Text style={styles.weakTrackText}>{item.track} • Accuracy: <Text style={{ color: Palette.danger, fontWeight: '700' }}>{item.accuracy}</Text></Text>
              </View>
              <TouchableOpacity
                style={styles.weakActionBtn}
                onPress={() => router.push('/quizzpage' as any)}
              >
                <Text style={styles.weakActionText}>Drill Topic</Text>
              </TouchableOpacity>
            </View>
          ))}
        </View>

        {/* Company Preparation Profiles */}
        <View style={styles.sectionHeaderRow}>
          <Text style={styles.sectionTitle}>Company Specific Question Banks</Text>
          <Text style={styles.sectionSubtitle}>Verified recruitment patterns</Text>
        </View>

        <View style={styles.companiesGrid}>
          {COMPANIES.map((c, i) => (
            <View key={i} style={styles.companyCard}>
              <View style={styles.companyTop}>
                <Text style={styles.companyName}>{c.name}</Text>
                <View style={styles.companyTag}>
                  <Text style={styles.companyTagText}>{c.questions}</Text>
                </View>
              </View>
              <Text style={styles.companyPattern}>{c.pattern}</Text>
              <TouchableOpacity
                style={styles.companyBtn}
                onPress={() => router.push('/coding-problems' as any)}
              >
                <Text style={styles.companyBtnText}>Practice Bank →</Text>
              </TouchableOpacity>
            </View>
          ))}
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: Palette.background },
  scrollContent: { maxWidth: 1040, width: '100%', alignSelf: 'center', paddingHorizontal: 16, paddingTop: 16, paddingBottom: 60 },
  header: { marginBottom: 18 },
  title: { fontSize: 22, fontWeight: '800', color: Palette.textTitle, marginBottom: 4 },
  subtitle: { fontSize: 13.5, color: Palette.textSecondary },
  readinessCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 18,
    borderWidth: 1,
    borderColor: Palette.border,
    marginBottom: 24,
    ...Shadows.card,
  },
  readinessTopRow: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 12 },
  readinessLabel: { fontSize: 11, fontWeight: '800', color: Palette.primary, letterSpacing: 0.8 },
  readinessValue: { fontSize: 18, fontWeight: '800', color: Palette.textTitle, marginTop: 2 },
  readinessScoreCircle: { width: 50, height: 50, borderRadius: 25, backgroundColor: Palette.primaryLight, alignItems: 'center', justifyContent: 'center' },
  readinessScoreNum: { fontSize: 18, fontWeight: '900', color: Palette.primary },
  readinessScoreSub: { fontSize: 9, fontWeight: '800', color: Palette.primary },
  readinessMeta: { fontSize: 12, color: Palette.textSecondary, marginTop: 8 },
  sectionHeaderRow: { marginBottom: 12 },
  sectionTitle: { fontSize: 17, fontWeight: '800', color: Palette.textTitle },
  sectionSubtitle: { fontSize: 12, color: Palette.textSecondary, marginTop: 2 },
  roadmapCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 18,
    borderWidth: 1,
    borderColor: Palette.border,
    marginBottom: 24,
    ...Shadows.card,
  },
  stageItemRow: { flexDirection: 'row', alignItems: 'flex-start', minHeight: 48 },
  stageLeftCol: { alignItems: 'center', marginRight: 14 },
  stageDot: {
    width: 24,
    height: 24,
    borderRadius: 12,
    backgroundColor: Palette.backgroundSecondary,
    borderWidth: 1,
    borderColor: Palette.border,
    alignItems: 'center',
    justifyContent: 'center',
  },
  stageDotCompleted: { backgroundColor: Palette.success, borderColor: Palette.success },
  stageDotCurrent: { backgroundColor: Palette.primary, borderColor: Palette.primary },
  stageNum: { fontSize: 10, fontWeight: '700', color: Palette.textSecondary },
  stageLine: { width: 2, flex: 1, backgroundColor: Palette.border, marginVertical: 4 },
  stageContent: { flex: 1, paddingBottom: 14 },
  stageName: { fontSize: 14, fontWeight: '700', color: Palette.textTitle },
  stageNameCurrent: { color: Palette.primary },
  stageScore: { fontSize: 12, color: Palette.textSecondary, marginTop: 2 },
  weakAreasContainer: { gap: 10, marginBottom: 24 },
  weakCard: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 14,
    borderWidth: 1,
    borderColor: Palette.border,
    borderLeftWidth: 4,
    borderLeftColor: Palette.danger,
    ...Shadows.card,
  },
  weakCardInfo: { flex: 1, marginRight: 10 },
  weakTopicTitle: { fontSize: 14, fontWeight: '700', color: Palette.textTitle },
  weakTrackText: { fontSize: 12, color: Palette.textSecondary, marginTop: 2 },
  weakActionBtn: { backgroundColor: Palette.primaryLight, paddingHorizontal: 12, paddingVertical: 6, borderRadius: 8 },
  weakActionText: { fontSize: 12, fontWeight: '700', color: Palette.primary },
  companiesGrid: { gap: 10, marginBottom: 20 },
  companyCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  companyTop: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 4 },
  companyName: { fontSize: 16, fontWeight: '800', color: Palette.textTitle },
  companyTag: { backgroundColor: Palette.primaryLight, paddingHorizontal: 8, paddingVertical: 3, borderRadius: 6 },
  companyTagText: { fontSize: 11, fontWeight: '700', color: Palette.primary },
  companyPattern: { fontSize: 12.5, color: Palette.textSecondary, marginBottom: 10 },
  companyBtn: { alignSelf: 'flex-start' },
  companyBtnText: { fontSize: 13, fontWeight: '700', color: Palette.primary },
  liveInterviewBanner: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1.5,
    borderColor: '#E0E7FF',
    marginBottom: 24,
    flexDirection: 'row',
    alignItems: 'center',
    gap: 14,
    ...Shadows.card,
  },
  liveInterviewBannerIcon: {
    width: 48,
    height: 48,
    borderRadius: 14,
    backgroundColor: Palette.primary,
    alignItems: 'center',
    justifyContent: 'center',
  },
  liveInterviewBannerTitle: {
    fontSize: 16,
    fontWeight: '800',
    color: Palette.textTitle,
  },
  liveBadge: {
    backgroundColor: '#EEF2FF',
    paddingHorizontal: 7,
    paddingVertical: 2,
    borderRadius: 6,
    borderWidth: 1,
    borderColor: '#C7D2FE',
  },
  liveBadgeText: {
    fontSize: 10,
    fontWeight: '800',
    color: Palette.primary,
    letterSpacing: 0.5,
  },
  liveInterviewBannerDesc: {
    fontSize: 12.5,
    color: Palette.textSecondary,
    lineHeight: 18,
    marginTop: 2,
  },
  aptitudeBanner: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 18,
    borderWidth: 1.5,
    borderColor: '#C7D2FE',
    marginBottom: 24,
    ...Shadows.card,
  },
  aptitudeTopRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 14,
    marginBottom: 12,
  },
  aptitudeIconWrap: {
    width: 48,
    height: 48,
    borderRadius: 14,
    backgroundColor: '#4F46E5',
    alignItems: 'center',
    justifyContent: 'center',
  },
  aptitudeTitle: {
    fontSize: 17,
    fontWeight: '800',
    color: Palette.textTitle,
  },
  aiBadge: {
    backgroundColor: '#EEF2FF',
    paddingHorizontal: 8,
    paddingVertical: 2,
    borderRadius: 6,
    borderWidth: 1,
    borderColor: '#818CF8',
  },
  aiBadgeText: {
    fontSize: 9.5,
    fontWeight: '800',
    color: '#4F46E5',
    letterSpacing: 0.5,
  },
  aptitudeSubtitle: {
    fontSize: 12.5,
    color: Palette.textSecondary,
    lineHeight: 17,
    marginTop: 2,
  },
  aptitudePillsRow: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 6,
    marginBottom: 14,
  },
  aptitudePill: {
    backgroundColor: '#F3F4F6',
    paddingHorizontal: 9,
    paddingVertical: 4,
    borderRadius: 8,
  },
  aptitudePillText: {
    fontSize: 11.5,
    fontWeight: '600',
    color: '#374151',
  },
  aptitudeFooterRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingTop: 12,
    borderTopWidth: 1,
    borderTopColor: '#F3F4F6',
    gap: 12,
  },
  aptitudeMetaCol: {
    flex: 1,
  },
  aptitudeMetaText: {
    fontSize: 11.5,
    color: Palette.textSecondary,
    lineHeight: 16,
  },
  aptitudeStartBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#4F46E5',
    paddingHorizontal: 16,
    paddingVertical: 10,
    borderRadius: 10,
    gap: 6,
    ...Shadows.button,
  },
  aptitudeStartBtnText: {
    color: '#FFFFFF',
    fontSize: 13.5,
    fontWeight: '700',
  },
});

