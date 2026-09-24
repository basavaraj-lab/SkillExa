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

const COMPETITIVE_SUBJECTS = [
  {
    id: 'english',
    title: 'English Language',
    topicsCount: '7 Topics',
    questionsCount: '350+ Questions',
    progress: 0.48,
    icon: 'book-open',
    route: '/english',
    accent: Palette.primary,
  },
  {
    id: 'math',
    title: 'Quantitative Aptitude',
    topicsCount: '10 Topics',
    questionsCount: '500+ Questions',
    progress: 0.40,
    icon: 'percent',
    route: '/mathematics',
    accent: Palette.warning,
  },
  {
    id: 'reasoning',
    title: 'Logical Reasoning',
    topicsCount: '9 Topics',
    questionsCount: '450+ Questions',
    progress: 0.55,
    icon: 'activity',
    route: '/reasoning',
    accent: Palette.primary,
  },
  {
    id: 'awareness',
    title: 'General Awareness',
    topicsCount: '9 Topics',
    questionsCount: '600+ Questions',
    progress: 0.30,
    icon: 'globe',
    route: '/awareness',
    accent: Palette.success,
  },
  {
    id: 'science',
    title: 'General Science',
    topicsCount: '8 Topics',
    questionsCount: '400+ Questions',
    progress: 0.25,
    icon: 'layers',
    route: '/science',
    accent: Palette.danger,
  },
  {
    id: 'fitness',
    title: 'Physical Fitness',
    topicsCount: '8 Modules',
    questionsCount: '100+ Standards',
    progress: 0.85,
    icon: 'shield',
    route: '/fitness',
    accent: Palette.primary,
  },
];

export default function CompetitiveDashboard() {
  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader showBack title="Competitive Exams" subtitle="Aptitude & Govt Exam Suite" />

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {/* Header */}
        <View style={styles.header}>
          <Text style={styles.title}>Competitive Exams</Text>
          <Text style={styles.subtitle}>Prepare smarter. Practice consistently.</Text>
        </View>

        {/* Overall Progress Banner */}
        <View style={styles.progressCard}>
          <View style={styles.progressTopRow}>
            <View>
              <Text style={styles.progressLabel}>OVERALL COMPETITIVE MASTERY</Text>
              <Text style={styles.progressValue}>48% Completed</Text>
            </View>
            <View style={styles.percentBadge}>
              <Text style={styles.percentText}>48%</Text>
            </View>
          </View>
          <ProgressBar progress={0.48} color={Palette.primary} />
          <Text style={styles.progressMeta}>2,400+ of 5,000 questions answered</Text>
        </View>

        {/* Section Heading */}
        <View style={styles.sectionHeader}>
          <Text style={styles.sectionTitle}>Exam Subject Modules</Text>
          <Text style={styles.sectionSubtitle}>Select a subject to master topics & take PYQ quizzes</Text>
        </View>

        {/* 2-Column Responsive Subject Grid */}
        <View style={styles.subjectsGrid}>
          {COMPETITIVE_SUBJECTS.map((subj) => (
            <TouchableOpacity
              key={subj.id}
              style={styles.subjectCard}
              onPress={() => router.push(subj.route as any)}
              activeOpacity={0.8}
            >
              <View style={styles.subjectTop}>
                <View style={[styles.subjectIconBox, { backgroundColor: `${subj.accent}15` }]}>
                  <Feather name={subj.icon as any} size={20} color={subj.accent} />
                </View>
                <Text style={styles.subjectProgressText}>{Math.round(subj.progress * 100)}%</Text>
              </View>

              <Text style={styles.subjectTitle}>{subj.title}</Text>
              <Text style={styles.subjectMeta}>{subj.topicsCount} • {subj.questionsCount}</Text>

              <View style={styles.subjectProgressWrapper}>
                <ProgressBar progress={subj.progress} color={subj.accent} />
              </View>

              <View style={styles.subjectFooter}>
                <Text style={styles.continueText}>Continue Track</Text>
                <Feather name="arrow-right" size={14} color={Palette.primary} />
              </View>
            </TouchableOpacity>
          ))}
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: Palette.background },
  scrollContent: { paddingHorizontal: 16, paddingTop: 16, paddingBottom: 40 },
  header: { marginBottom: 20 },
  title: { fontSize: 22, fontWeight: '800', color: Palette.textTitle, marginBottom: 4 },
  subtitle: { fontSize: 13.5, color: Palette.textSecondary },
  progressCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 18,
    borderWidth: 1,
    borderColor: Palette.border,
    marginBottom: 24,
    ...Shadows.card,
  },
  progressTopRow: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 12 },
  progressLabel: { fontSize: 11, fontWeight: '800', color: Palette.primary, letterSpacing: 0.8 },
  progressValue: { fontSize: 17, fontWeight: '800', color: Palette.textTitle, marginTop: 2 },
  percentBadge: { width: 44, height: 44, borderRadius: 22, backgroundColor: Palette.primaryLight, borderWidth: 2, borderColor: Palette.primary, alignItems: 'center', justifyContent: 'center' },
  percentText: { fontSize: 13, fontWeight: '800', color: Palette.primary },
  progressMeta: { fontSize: 12, color: Palette.textSecondary, marginTop: 8 },
  sectionHeader: { marginBottom: 14 },
  sectionTitle: { fontSize: 18, fontWeight: '800', color: Palette.textTitle },
  sectionSubtitle: { fontSize: 12, color: Palette.textSecondary, marginTop: 2 },
  subjectsGrid: { flexDirection: 'row', flexWrap: 'wrap', justifyContent: 'space-between', gap: 12 },
  subjectCard: {
    width: '48%',
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  subjectTop: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 10 },
  subjectIconBox: { width: 38, height: 38, borderRadius: 10, alignItems: 'center', justifyContent: 'center' },
  subjectProgressText: { fontSize: 12, fontWeight: '700', color: Palette.textTitle },
  subjectTitle: { fontSize: 15, fontWeight: '700', color: Palette.textTitle, marginBottom: 4, minHeight: 38 },
  subjectMeta: { fontSize: 11, color: Palette.textSecondary, marginBottom: 10 },
  subjectProgressWrapper: { marginBottom: 12 },
  subjectFooter: { flexDirection: 'row', alignItems: 'center', gap: 4, paddingTop: 8, borderTopWidth: 1, borderTopColor: Palette.borderSubtle },
  continueText: { fontSize: 12, fontWeight: '700', color: Palette.primary },
});