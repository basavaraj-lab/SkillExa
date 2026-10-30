import { Feather } from '@expo/vector-icons';
import { router } from 'expo-router';
import React, { useEffect, useState } from 'react';
import {
  ActivityIndicator,
  RefreshControl,
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
import { ApiClient } from '../services/api';

const COMPANIES = [
  { name: 'Google', pattern: 'DSA + System Design', questions: '180 Problems' },
  { name: 'Amazon', pattern: 'Leadership Principles + Coding', questions: '210 Problems' },
  { name: 'Microsoft', pattern: 'Data Structures + Algorithms', questions: '165 Problems' },
  { name: 'TCS & Infosys', pattern: 'Aptitude + CS Fundamentals', questions: '350 Questions' },
];

export default function PlacementPreparationPage() {
  const [stats, setStats] = useState<any>(null);
  const [loading, setLoading] = useState(true);
  const [refreshing, setRefreshing] = useState(false);

  const loadRealStats = async () => {
    try {
      const res = await ApiClient.getStudentStats();
      if (res?.success && res.data) {
        setStats(res.data);
      }
    } catch (e) {
      console.warn('Failed to load real placement stats:', e);
    } finally {
      setLoading(false);
      setRefreshing(false);
    }
  };

  useEffect(() => {
    loadRealStats();
  }, []);

  const wp = stats?.weekly_progress;
  const questionsSolved = stats?.questions_solved ?? 0;
  const codingSolved = stats?.total_coding_solved ?? 0;
  const quizAccuracy = Math.round(stats?.quiz_accuracy ?? 0);
  const quizzesCompleted = stats?.total_quizzes_completed ?? 0;
  const aiInterviews = stats?.total_ai_interviews ?? 0;
  const interviewScore = Math.round(stats?.interview_average_score ?? 0);
  const streakDays = wp?.streak_days ?? 0;
  const totalSolvedWeek = wp?.total_solved_this_week ?? 0;

  // Real placement readiness calculation based on actual student activity
  // Weighted: 35% Aptitude Accuracy, 35% Coding Problems (target 20), 15% Quizzes (target 10), 15% Interview
  const calculatedScore = Math.min(
    100,
    Math.round(
      (quizAccuracy * 0.35) +
      Math.min(35, (codingSolved / 20) * 35) +
      Math.min(15, (quizzesCompleted / 10) * 15) +
      (interviewScore > 0 ? (interviewScore * 0.15) : Math.min(15, (aiInterviews / 2) * 15))
    )
  );

  const readinessIndex = stats?.overall_score ? Math.round(stats.overall_score) : calculatedScore;
  const progressRatio = Math.min(1.0, Math.max(0, readinessIndex / 100));

  // Extract verified weak topics from weekly diagnostic report
  const realWeakTopics: { topic: string; accuracy: string; track: string; route?: string }[] = [];
  if (Array.isArray(wp?.weak_topics) && wp.weak_topics.length > 0) {
    wp.weak_topics.forEach((wt: string) => {
      const match = wt.match(/^(.*?)\s*\((\d+)%\)$/);
      if (match) {
        realWeakTopics.push({
          topic: match[1],
          accuracy: `${match[2]}%`,
          track: 'Aptitude Diagnostic',
          route: `/aptitude-test?category=Quantitative%20Aptitude&topic=${encodeURIComponent(match[1])}&difficulty=Easy&autoStart=true`,
        });
      } else {
        realWeakTopics.push({
          topic: wt,
          accuracy: '< 75%',
          track: 'Aptitude Diagnostic',
          route: `/aptitude-test?category=Quantitative%20Aptitude&topic=${encodeURIComponent(wt)}&difficulty=Easy&autoStart=true`,
        });
      }
    });
  }

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader showBack title="Placement Preparation" subtitle="Real-Time Readiness & Assessments" />

      <ScrollView
        contentContainerStyle={styles.scrollContent}
        showsVerticalScrollIndicator={false}
        refreshControl={
          <RefreshControl
            refreshing={refreshing}
            onRefresh={() => {
              setRefreshing(true);
              loadRealStats();
            }}
            colors={[Palette.primary]}
          />
        }
      >
        {/* Header */}
        <View style={styles.header}>
          <Text style={styles.title}>Placement Acceleration</Text>
          <Text style={styles.subtitle}>
            Live readiness diagnostics, verified aptitude assessments, and company question banks.
          </Text>
        </View>

        {/* Real Readiness Meter Card */}
        <View style={styles.readinessCard}>
          <View style={styles.readinessTopRow}>
            <View>
              <Text style={styles.readinessLabel}>OVERALL PLACEMENT READINESS</Text>
              <Text style={styles.readinessValue}>{readinessIndex}% Ready</Text>
            </View>
            <View style={styles.readinessScoreCircle}>
              <Text style={styles.readinessScoreNum}>{readinessIndex}</Text>
              <Text style={styles.readinessScoreSub}>INDEX</Text>
            </View>
          </View>
          <ProgressBar progress={progressRatio} color={Palette.primary} />
          <Text style={styles.readinessMeta}>
            {questionsSolved > 0
              ? `${questionsSolved} verified questions solved • ${codingSolved} coding challenges cleared • ${quizzesCompleted} assessments passed`
              : 'Complete your first AI assessment or coding challenge to calculate your index'}
          </Text>
        </View>

        {/* Real Performance Pillars Breakdown (Replaces fake static roadmap) */}
        <View style={styles.sectionHeaderRow}>
          <Text style={styles.sectionTitle}>Real-Time Performance Pillars</Text>
          <Text style={styles.sectionSubtitle}>Verified statistics from your learning activity</Text>
        </View>

        <View style={styles.metricsGrid}>
          <TouchableOpacity
            style={styles.metricCard}
            onPress={() => router.push('/aptitude-test' as any)}
            activeOpacity={0.8}
          >
            <View style={[styles.metricIconWrap, { backgroundColor: '#EEF2FF' }]}>
              <Feather name="target" size={18} color="#4F46E5" />
            </View>
            <Text style={styles.metricNum}>{quizAccuracy}%</Text>
            <Text style={styles.metricTitle}>Aptitude Accuracy</Text>
            <Text style={styles.metricSub}>
              {quizzesCompleted > 0 ? `${quizzesCompleted} tests passed` : 'Take aptitude test'}
            </Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.metricCard}
            onPress={() => router.push('/coding-problems' as any)}
            activeOpacity={0.8}
          >
            <View style={[styles.metricIconWrap, { backgroundColor: '#ECFDF5' }]}>
              <Feather name="code" size={18} color="#059669" />
            </View>
            <Text style={styles.metricNum}>{codingSolved}</Text>
            <Text style={styles.metricTitle}>Core Coding</Text>
            <Text style={styles.metricSub}>
              {codingSolved > 0 ? `${stats?.code_submissions ?? codingSolved} submissions` : 'Practice problems'}
            </Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.metricCard}
            onPress={() => router.push('/live-interview' as any)}
            activeOpacity={0.8}
          >
            <View style={[styles.metricIconWrap, { backgroundColor: '#FEF3C7' }]}>
              <Feather name="video" size={18} color="#D97706" />
            </View>
            <Text style={styles.metricNum}>
              {interviewScore > 0 ? `${interviewScore}%` : `${aiInterviews}`}
            </Text>
            <Text style={styles.metricTitle}>Mock Interviews</Text>
            <Text style={styles.metricSub}>
              {aiInterviews > 0 ? `${aiInterviews} rounds conducted` : 'AI / Faculty panel'}
            </Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.metricCard}
            onPress={() => router.push('/progress' as any)}
            activeOpacity={0.8}
          >
            <View style={[styles.metricIconWrap, { backgroundColor: '#F5F3FF' }]}>
              <Feather name="activity" size={18} color="#7C3AED" />
            </View>
            <Text style={styles.metricNum}>{totalSolvedWeek}</Text>
            <Text style={styles.metricTitle}>Weekly Solved</Text>
            <Text style={styles.metricSub}>
              {streakDays > 0 ? `${streakDays} day streak 🔥` : 'Active learning'}
            </Text>
          </TouchableOpacity>
        </View>

        {/* Personalized Diagnostic Recommendation (from real backend evaluation) */}
        {wp?.recommendation && (
          <View style={styles.recommendationCard}>
            <View style={styles.recommendationIconWrap}>
              <Feather name="trending-up" size={20} color="#4F46E5" />
            </View>
            <View style={{ flex: 1 }}>
              <View style={{ flexDirection: 'row', alignItems: 'center', gap: 6, marginBottom: 2 }}>
                <Text style={styles.recommendationTitle}>Personalized Placement Boost</Text>
                <View style={styles.recBadge}>
                  <Text style={styles.recBadgeText}>RECOMMENDED</Text>
                </View>
              </View>
              <Text style={styles.recommendationText}>{wp.recommendation.reason}</Text>
            </View>
            <TouchableOpacity
              style={styles.recommendationBtn}
              onPress={() => router.push(wp.recommendation.practice_route as any)}
              activeOpacity={0.85}
            >
              <Text style={styles.recommendationBtnText}>Practice</Text>
              <Feather name="arrow-right" size={13} color="#FFFFFF" />
            </TouchableOpacity>
          </View>
        )}

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

        {/* Real Targeted Weak Areas */}
        <View style={styles.sectionHeaderRow}>
          <Text style={styles.sectionTitle}>Targeted Weak Areas</Text>
          <Text style={styles.sectionSubtitle}>Identified from your recent assessment mistakes</Text>
        </View>

        <View style={styles.weakAreasContainer}>
          {realWeakTopics.length > 0 ? (
            realWeakTopics.map((item, index) => (
              <View key={index} style={styles.weakCard}>
                <View style={styles.weakCardInfo}>
                  <Text style={styles.weakTopicTitle}>{item.topic}</Text>
                  <Text style={styles.weakTrackText}>
                    {item.track} • Accuracy: <Text style={{ color: Palette.danger, fontWeight: '700' }}>{item.accuracy}</Text>
                  </Text>
                </View>
                <TouchableOpacity
                  style={styles.weakActionBtn}
                  onPress={() => {
                    if (item.route) router.push(item.route as any);
                    else router.push('/aptitude-test' as any);
                  }}
                >
                  <Text style={styles.weakActionText}>Drill Topic</Text>
                </TouchableOpacity>
              </View>
            ))
          ) : (
            <View style={styles.emptyWeakCard}>
              <View style={styles.emptyWeakIconWrap}>
                <Feather name="check-circle" size={20} color="#10B981" />
              </View>
              <View style={{ flex: 1 }}>
                <Text style={styles.emptyWeakTitle}>No Critical Weak Areas Detected</Text>
                <Text style={styles.emptyWeakSubtitle}>
                  Great job! Continue solving AI Aptitude Tests and core coding problems to identify advanced mastery gaps.
                </Text>
              </View>
            </View>
          )}
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

  // Readiness Meter
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

  // Real Metrics 4-Pillar Grid
  metricsGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 10,
    marginBottom: 24,
  },
  metricCard: {
    flex: 1,
    minWidth: 155,
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 14,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  metricIconWrap: {
    width: 34,
    height: 34,
    borderRadius: 10,
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: 8,
  },
  metricNum: {
    fontSize: 18,
    fontWeight: '800',
    color: Palette.textTitle,
    marginBottom: 2,
  },
  metricTitle: {
    fontSize: 12,
    fontWeight: '700',
    color: Palette.textSecondary,
    marginBottom: 4,
  },
  metricSub: {
    fontSize: 11,
    color: '#6B7280',
  },

  // Recommendation Card
  recommendationCard: {
    backgroundColor: '#EEF2FF',
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1.5,
    borderColor: '#C7D2FE',
    marginBottom: 24,
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
    ...Shadows.card,
  },
  recommendationIconWrap: {
    width: 40,
    height: 40,
    borderRadius: 12,
    backgroundColor: '#FFFFFF',
    alignItems: 'center',
    justifyContent: 'center',
  },
  recommendationTitle: {
    fontSize: 13.5,
    fontWeight: '800',
    color: Palette.textTitle,
  },
  recBadge: {
    backgroundColor: '#4F46E5',
    paddingHorizontal: 6,
    paddingVertical: 1,
    borderRadius: 4,
  },
  recBadgeText: {
    fontSize: 8.5,
    fontWeight: '800',
    color: '#FFFFFF',
    letterSpacing: 0.5,
  },
  recommendationText: {
    fontSize: 12,
    color: Palette.textSecondary,
    lineHeight: 16,
    marginTop: 2,
  },
  recommendationBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#4F46E5',
    paddingHorizontal: 12,
    paddingVertical: 7,
    borderRadius: 8,
    gap: 4,
  },
  recommendationBtnText: {
    color: '#FFFFFF',
    fontSize: 12,
    fontWeight: '700',
  },

  // Weak Areas
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

  emptyWeakCard: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#F0FDF4',
    borderRadius: Radii.card,
    padding: 14,
    borderWidth: 1,
    borderColor: '#BBF7D0',
    gap: 10,
  },
  emptyWeakIconWrap: {
    width: 36,
    height: 36,
    borderRadius: 18,
    backgroundColor: '#DCFCE7',
    alignItems: 'center',
    justifyContent: 'center',
  },
  emptyWeakTitle: {
    fontSize: 13.5,
    fontWeight: '700',
    color: '#166534',
  },
  emptyWeakSubtitle: {
    fontSize: 12,
    color: '#15803D',
    lineHeight: 16,
    marginTop: 2,
  },

  // Company Profiles
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

  // Live Interview Banner
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

  // AI Aptitude Test Banner
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
