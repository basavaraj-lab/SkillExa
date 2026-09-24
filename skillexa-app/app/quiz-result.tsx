import { Feather } from '@expo/vector-icons';
import { router, useLocalSearchParams } from 'expo-router';
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
import { ProgressBar } from '../components/common/EducationalCards';
import { Palette, Radii, Shadows } from '../constants/theme';

export default function QuizResultPage() {
  const {
    topic = 'General Practice',
    total = '5',
    correct = '4',
    wrong = '1',
    skipped = '0',
    timeSpent = '3m 45s',
  } = useLocalSearchParams<{
    topic: string;
    total: string;
    correct: string;
    wrong: string;
    skipped: string;
    timeSpent: string;
  }>();

  const totalNum = parseInt(total, 10) || 5;
  const correctNum = parseInt(correct, 10) || 4;
  const percentage = Math.round((correctNum / totalNum) * 100);

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {/* Result Hero Card */}
        <View style={styles.heroCard}>
          <View style={styles.heroIconCircle}>
            <Feather name={percentage >= 70 ? 'award' : 'check-circle'} size={32} color={percentage >= 70 ? Palette.success : Palette.primary} />
          </View>
          <Text style={styles.heroTitle}>{percentage >= 70 ? 'Excellent Performance!' : 'Good Effort!'}</Text>
          <Text style={styles.heroTopic}>{topic}</Text>

          {/* Large Score Circle */}
          <View style={styles.scorePill}>
            <Text style={styles.scoreBigText}>{correctNum}</Text>
            <Text style={styles.scoreTotalText}> / {totalNum}</Text>
            <View style={styles.percentBadge}>
              <Text style={styles.percentBadgeText}>{percentage}%</Text>
            </View>
          </View>
        </View>

        {/* 4 Metric Stats Grid */}
        <View style={styles.statsGrid}>
          <View style={[styles.statBox, { borderLeftColor: Palette.success }]}>
            <Feather name="check" size={16} color={Palette.success} />
            <Text style={styles.statNum}>{correct}</Text>
            <Text style={styles.statLabel}>Correct</Text>
          </View>

          <View style={[styles.statBox, { borderLeftColor: Palette.danger }]}>
            <Feather name="x" size={16} color={Palette.danger} />
            <Text style={styles.statNum}>{wrong}</Text>
            <Text style={styles.statLabel}>Incorrect</Text>
          </View>

          <View style={[styles.statBox, { borderLeftColor: Palette.warning }]}>
            <Feather name="skip-forward" size={16} color={Palette.warning} />
            <Text style={styles.statNum}>{skipped}</Text>
            <Text style={styles.statLabel}>Skipped</Text>
          </View>

          <View style={[styles.statBox, { borderLeftColor: Palette.primary }]}>
            <Feather name="clock" size={16} color={Palette.primary} />
            <Text style={styles.statNum}>{timeSpent}</Text>
            <Text style={styles.statLabel}>Time Spent</Text>
          </View>
        </View>

        {/* Subject Breakdown Card */}
        <View style={styles.breakdownCard}>
          <Text style={styles.breakdownTitle}>Concept Performance Breakdown</Text>
          
          <View style={styles.breakdownItem}>
            <View style={styles.breakdownItemHeader}>
              <Text style={styles.breakdownItemLabel}>Subject-Verb Agreement</Text>
              <Text style={styles.breakdownItemVal}>100%</Text>
            </View>
            <ProgressBar progress={1.0} color={Palette.success} />
          </View>

          <View style={styles.breakdownItem}>
            <View style={styles.breakdownItemHeader}>
              <Text style={styles.breakdownItemLabel}>Conditional Clauses</Text>
              <Text style={styles.breakdownItemVal}>100%</Text>
            </View>
            <ProgressBar progress={1.0} color={Palette.success} />
          </View>

          <View style={styles.breakdownItem}>
            <View style={styles.breakdownItemHeader}>
              <Text style={styles.breakdownItemLabel}>Quantitative Speed Conversions</Text>
              <Text style={styles.breakdownItemVal}>50%</Text>
            </View>
            <ProgressBar progress={0.5} color={Palette.warning} />
          </View>
        </View>

        {/* Action Controls */}
        <View style={styles.actionsContainer}>
          <TouchableOpacity
            style={styles.reviewBtn}
            onPress={() =>
              router.push({
                pathname: '/answer-review',
                params: { topic },
              })
            }
            activeOpacity={0.85}
          >
            <Feather name="file-text" size={16} color={Palette.primary} />
            <Text style={styles.reviewBtnText}>Review Detailed Explanations</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.retryBtn}
            onPress={() =>
              router.replace({
                pathname: '/quizzpage',
                params: { topic },
              })
            }
            activeOpacity={0.85}
          >
            <Feather name="refresh-cw" size={16} color="#FFFFFF" />
            <Text style={styles.retryBtnText}>Retry Assessment</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={styles.homeBtn}
            onPress={() => router.replace('/home' as any)}
            activeOpacity={0.8}
          >
            <Text style={styles.homeBtnText}>Return to Home Dashboard</Text>
          </TouchableOpacity>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: Palette.background },
  scrollContent: { paddingHorizontal: 16, paddingTop: 20, paddingBottom: 40 },
  heroCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.cardLarge,
    padding: 24,
    borderWidth: 1,
    borderColor: Palette.border,
    alignItems: 'center',
    marginBottom: 20,
    ...Shadows.card,
  },
  heroIconCircle: {
    width: 64,
    height: 64,
    borderRadius: 32,
    backgroundColor: Palette.successLight,
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: 12,
  },
  heroTitle: { fontSize: 20, fontWeight: '800', color: Palette.textTitle },
  heroTopic: { fontSize: 13, color: Palette.textSecondary, marginTop: 2, marginBottom: 16 },
  scorePill: {
    flexDirection: 'row',
    alignItems: 'baseline',
    backgroundColor: Palette.backgroundSecondary,
    paddingHorizontal: 20,
    paddingVertical: 10,
    borderRadius: Radii.pill,
    borderWidth: 1,
    borderColor: Palette.border,
  },
  scoreBigText: { fontSize: 32, fontWeight: '900', color: Palette.textTitle },
  scoreTotalText: { fontSize: 18, fontWeight: '700', color: Palette.textSecondary },
  percentBadge: { marginLeft: 12, backgroundColor: Palette.primary, paddingHorizontal: 10, paddingVertical: 4, borderRadius: 8 },
  percentBadgeText: { color: '#FFFFFF', fontSize: 13, fontWeight: '800' },
  statsGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
    gap: 10,
    marginBottom: 20,
  },
  statBox: {
    width: '48%',
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 14,
    borderWidth: 1,
    borderColor: Palette.border,
    borderLeftWidth: 4,
    ...Shadows.card,
  },
  statNum: { fontSize: 18, fontWeight: '800', color: Palette.textTitle, marginTop: 4 },
  statLabel: { fontSize: 11, color: Palette.textSecondary, marginTop: 2 },
  breakdownCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 18,
    borderWidth: 1,
    borderColor: Palette.border,
    marginBottom: 24,
    ...Shadows.card,
  },
  breakdownTitle: { fontSize: 15, fontWeight: '800', color: Palette.textTitle, marginBottom: 14 },
  breakdownItem: { marginBottom: 12 },
  breakdownItemHeader: { flexDirection: 'row', justifyContent: 'space-between', marginBottom: 6 },
  breakdownItemLabel: { fontSize: 12.5, color: Palette.textBody },
  breakdownItemVal: { fontSize: 12, fontWeight: '700', color: Palette.textTitle },
  actionsContainer: { gap: 10 },
  reviewBtn: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.button,
    paddingVertical: 13,
    borderWidth: 1,
    borderColor: Palette.primary,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
  },
  reviewBtnText: { color: Palette.primary, fontSize: 14, fontWeight: '700' },
  retryBtn: {
    backgroundColor: Palette.primary,
    borderRadius: Radii.button,
    paddingVertical: 13,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
    ...Shadows.button,
  },
  retryBtnText: { color: '#FFFFFF', fontSize: 14, fontWeight: '700' },
  homeBtn: {
    paddingVertical: 12,
    alignItems: 'center',
  },
  homeBtnText: { color: Palette.textSecondary, fontSize: 13.5, fontWeight: '600' },
});
