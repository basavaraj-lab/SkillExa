import { Feather } from '@expo/vector-icons';
import { router } from 'expo-router';
import React, { useState } from 'react';
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

export default function ProgressScreen() {
  const [activeTrack, setActiveTrack] = useState<'engineering' | 'competitive'>('engineering');

  const engineeringStats = {
    overallProgress: 0.68,
    solved: 142,
    accuracy: '78%',
    streak: '7 Days',
    time: '34h 20m',
    strong: ['Array Two-Pointers', 'Binary Search', 'Resume Architecture'],
    weak: ['Dynamic Programming', 'Graph Dijkstra', 'OS Semaphores'],
  };

  const competitiveStats = {
    overallProgress: 0.48,
    solved: 212,
    accuracy: '74%',
    streak: '5 Days',
    time: '28h 15m',
    strong: ['Grammar Tenses', 'Vocabulary Roots', 'Reading Comprehension'],
    weak: ['Time & Speed Math', 'Syllogisms Reasoning', 'Modern History'],
  };

  const current = activeTrack === 'engineering' ? engineeringStats : competitiveStats;

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader title="Student Analytics" />

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {/* Header */}
        <View style={styles.header}>
          <Text style={styles.title}>Progress & Performance</Text>
          <Text style={styles.subtitle}>Track your learning trajectory and accuracy metrics.</Text>
        </View>

        {/* Track Switcher Tabs */}
        <View style={styles.trackTabs}>
          <TouchableOpacity
            style={[styles.trackTab, activeTrack === 'engineering' && styles.trackTabActive]}
            onPress={() => setActiveTrack('engineering')}
          >
            <Feather name="cpu" size={15} color={activeTrack === 'engineering' ? Palette.primary : Palette.textSecondary} />
            <Text style={[styles.trackTabText, activeTrack === 'engineering' && styles.trackTabTextActive]}>
              Engineering Track
            </Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={[styles.trackTab, activeTrack === 'competitive' && styles.trackTabActive]}
            onPress={() => setActiveTrack('competitive')}
          >
            <Feather name="award" size={15} color={activeTrack === 'competitive' ? Palette.primary : Palette.textSecondary} />
            <Text style={[styles.trackTabText, activeTrack === 'competitive' && styles.trackTabTextActive]}>
              Competitive Track
            </Text>
          </TouchableOpacity>
        </View>

        {/* Master Progress Card */}
        <View style={styles.masterCard}>
          <View style={styles.masterTop}>
            <View>
              <Text style={styles.masterLabel}>OVERALL TRACK MASTERY</Text>
              <Text style={styles.masterVal}>{Math.round(current.overallProgress * 100)}% Complete</Text>
            </View>
            <View style={styles.masterBadge}>
              <Text style={styles.masterBadgeText}>{Math.round(current.overallProgress * 100)}%</Text>
            </View>
          </View>
          <ProgressBar progress={current.overallProgress} color={Palette.primary} />
          <Text style={styles.masterMeta}>Curriculum milestones on schedule</Text>
        </View>

        {/* Lifetime Key Metrics */}
        <View style={styles.metricsGrid}>
          <View style={styles.metricCard}>
            <Text style={styles.metricVal}>{current.solved}</Text>
            <Text style={styles.metricLabel}>Solved Items</Text>
          </View>

          <View style={styles.metricCard}>
            <Text style={[styles.metricVal, { color: Palette.success }]}>{current.accuracy}</Text>
            <Text style={styles.metricLabel}>Average Accuracy</Text>
          </View>

          <View style={styles.metricCard}>
            <Text style={[styles.metricVal, { color: Palette.warning }]}>{current.streak}</Text>
            <Text style={styles.metricLabel}>Current Streak</Text>
          </View>

          <View style={styles.metricCard}>
            <Text style={styles.metricVal}>{current.time}</Text>
            <Text style={styles.metricLabel}>Practice Time</Text>
          </View>
        </View>

        {/* Strength & Weakness Breakdown */}
        <View style={styles.analysisRow}>
          {/* Strong Areas */}
          <View style={styles.analysisCard}>
            <View style={styles.analysisHeader}>
              <Feather name="trending-up" size={16} color={Palette.success} />
              <Text style={[styles.analysisTitle, { color: Palette.success }]}>Top Strengths</Text>
            </View>
            {current.strong.map((s, i) => (
              <View key={i} style={styles.bulletRow}>
                <Text style={[styles.bulletPoint, { color: Palette.success }]}>✓</Text>
                <Text style={styles.bulletText}>{s}</Text>
              </View>
            ))}
          </View>

          {/* Weak Areas */}
          <View style={styles.analysisCard}>
            <View style={styles.analysisHeader}>
              <Feather name="alert-triangle" size={16} color={Palette.warning} />
              <Text style={[styles.analysisTitle, { color: Palette.warning }]}>Focus Areas</Text>
            </View>
            {current.weak.map((w, i) => (
              <View key={i} style={styles.bulletRow}>
                <Text style={[styles.bulletPoint, { color: Palette.warning }]}>!</Text>
                <Text style={styles.bulletText}>{w}</Text>
              </View>
            ))}
          </View>
        </View>

        {/* Action Button */}
        <TouchableOpacity
          style={styles.actionBtn}
          onPress={() => router.push(activeTrack === 'engineering' ? '/dsa-practice' : '/topic-learning' as any)}
          activeOpacity={0.85}
        >
          <Text style={styles.actionBtnText}>
            {activeTrack === 'engineering' ? 'Continue Engineering Roadmap →' : 'Practice Weak Topics Now →'}
          </Text>
        </TouchableOpacity>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: Palette.background },
  scrollContent: { paddingHorizontal: 16, paddingTop: 16, paddingBottom: 40 },
  header: { marginBottom: 18 },
  title: { fontSize: 22, fontWeight: '800', color: Palette.textTitle, marginBottom: 4 },
  subtitle: { fontSize: 13.5, color: Palette.textSecondary },
  trackTabs: {
    flexDirection: 'row',
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.pill,
    padding: 4,
    borderWidth: 1,
    borderColor: Palette.border,
    marginBottom: 20,
    ...Shadows.card,
  },
  trackTab: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 6,
    paddingVertical: 10,
    borderRadius: Radii.pill,
  },
  trackTabActive: { backgroundColor: Palette.primaryLight },
  trackTabText: { fontSize: 13, fontWeight: '600', color: Palette.textSecondary },
  trackTabTextActive: { color: Palette.primary, fontWeight: '700' },
  masterCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 18,
    borderWidth: 1,
    borderColor: Palette.border,
    marginBottom: 20,
    ...Shadows.card,
  },
  masterTop: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 12 },
  masterLabel: { fontSize: 11, fontWeight: '800', color: Palette.primary, letterSpacing: 0.8 },
  masterVal: { fontSize: 18, fontWeight: '800', color: Palette.textTitle, marginTop: 2 },
  masterBadge: { width: 44, height: 44, borderRadius: 22, backgroundColor: Palette.primaryLight, borderWidth: 2, borderColor: Palette.primary, alignItems: 'center', justifyContent: 'center' },
  masterBadgeText: { fontSize: 13, fontWeight: '800', color: Palette.primary },
  masterMeta: { fontSize: 12, color: Palette.textSecondary, marginTop: 8 },
  metricsGrid: { flexDirection: 'row', flexWrap: 'wrap', justifyContent: 'space-between', gap: 10, marginBottom: 20 },
  metricCard: {
    width: '48%',
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 14,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  metricVal: { fontSize: 18, fontWeight: '800', color: Palette.primary },
  metricLabel: { fontSize: 11, color: Palette.textSecondary, marginTop: 2 },
  analysisRow: { gap: 12, marginBottom: 24 },
  analysisCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  analysisHeader: { flexDirection: 'row', alignItems: 'center', gap: 6, marginBottom: 10 },
  analysisTitle: { fontSize: 14, fontWeight: '800' },
  bulletRow: { flexDirection: 'row', alignItems: 'center', gap: 8, marginVertical: 4 },
  bulletPoint: { fontSize: 12, fontWeight: '800' },
  bulletText: { fontSize: 13, color: Palette.textBody },
  actionBtn: {
    backgroundColor: Palette.primary,
    borderRadius: Radii.button,
    paddingVertical: 13,
    alignItems: 'center',
    ...Shadows.button,
  },
  actionBtnText: { color: '#FFFFFF', fontSize: 14.5, fontWeight: '700' },
});
