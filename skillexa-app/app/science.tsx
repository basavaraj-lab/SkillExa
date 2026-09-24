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

interface TopicItem {
  id: string;
  title: string;
  subtopics: string;
  questionsCount: string;
  progress: number;
  status: 'completed' | 'inprogress' | 'notstarted';
}

const SCIENCE_TOPICS: TopicItem[] = [
  { id: 'physics', title: 'Mechanics, Optics & Electricity', subtopics: '6 subtopics', questionsCount: '260+ questions', progress: 0.50, status: 'inprogress' },
  { id: 'chemistry', title: 'Periodic Table, Acids & Reactions', subtopics: '5 subtopics', questionsCount: '210+ questions', progress: 1.0, status: 'completed' },
  { id: 'biology', title: 'Human Anatomy, Nutrition & Health', subtopics: '6 subtopics', questionsCount: '290+ questions', progress: 0.0, status: 'notstarted' },
  { id: 'ecology', title: 'Ecology, Environment & Pollution', subtopics: '4 subtopics', questionsCount: '150+ questions', progress: 0.0, status: 'notstarted' },
  { id: 'discoveries', title: 'Scientific Discoveries & Inventions', subtopics: '4 subtopics', questionsCount: '140+ questions', progress: 0.0, status: 'notstarted' },
];

export default function SciencePage() {
  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader showBack title="General Science" subtitle="Competitive Track" />

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {/* Header Title */}
        <View style={styles.header}>
          <Text style={styles.title}>General Science</Text>
          <Text style={styles.subtitle}>Physics, Chemistry, and Biology essentials for competitive examinations.</Text>
        </View>

        {/* Progress Card */}
        <View style={styles.progressCard}>
          <View style={styles.progressRow}>
            <View>
              <Text style={styles.progressLabel}>SUBJECT PROGRESS</Text>
              <Text style={styles.progressValue}>30% Completed</Text>
            </View>
            <View style={styles.badge}>
              <Text style={styles.badgeText}>1 / 5 Topics Done</Text>
            </View>
          </View>
          <ProgressBar progress={0.30} color={Palette.success} />
        </View>

        {/* Topics List Heading */}
        <View style={styles.sectionHeader}>
          <Text style={styles.sectionTitle}>Curriculum Topics</Text>
          <Text style={styles.sectionSubtitle}>Select a topic to start structured notes & PYQ tests</Text>
        </View>

        {/* Topic Cards */}
        <View style={styles.topicsList}>
          {SCIENCE_TOPICS.map((topic) => {
            const isDone = topic.status === 'completed';
            const isInProgress = topic.status === 'inprogress';

            return (
              <TouchableOpacity
                key={topic.id}
                style={[styles.topicCard, isInProgress && styles.topicCardActive]}
                onPress={() =>
                  router.push({
                    pathname: '/topic-learning',
                    params: {
                      subject: 'General Science',
                      topic: topic.title,
                    },
                  })
                }
                activeOpacity={0.75}
              >
                <View style={styles.topicLeft}>
                  <View
                    style={[
                      styles.statusCircle,
                      isDone && styles.statusCircleDone,
                      isInProgress && styles.statusCircleProgress,
                    ]}
                  >
                    {isDone ? (
                      <Feather name="check" size={14} color="#FFFFFF" />
                    ) : (
                      <Feather name="layers" size={14} color={isInProgress ? Palette.success : Palette.textSecondary} />
                    )}
                  </View>
                  <View style={styles.topicInfo}>
                    <Text style={styles.topicTitle}>{topic.title}</Text>
                    <Text style={styles.topicMeta}>{topic.subtopics} • {topic.questionsCount}</Text>
                  </View>
                </View>

                <View style={styles.topicRight}>
                  {isInProgress && (
                    <View style={styles.progressPill}>
                      <Text style={styles.progressPillText}>{Math.round(topic.progress * 100)}%</Text>
                    </View>
                  )}
                  <Feather name="chevron-right" size={18} color={isInProgress ? Palette.success : Palette.textMuted} />
                </View>
              </TouchableOpacity>
            );
          })}
        </View>
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
  progressCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.border,
    marginBottom: 24,
    ...Shadows.card,
  },
  progressRow: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 10 },
  progressLabel: { fontSize: 11, fontWeight: '800', color: Palette.success, letterSpacing: 0.8 },
  progressValue: { fontSize: 16, fontWeight: '800', color: Palette.textTitle, marginTop: 2 },
  badge: { backgroundColor: Palette.successLight, paddingHorizontal: 10, paddingVertical: 4, borderRadius: 6 },
  badgeText: { fontSize: 12, fontWeight: '700', color: Palette.success },
  sectionHeader: { marginBottom: 14 },
  sectionTitle: { fontSize: 18, fontWeight: '800', color: Palette.textTitle },
  sectionSubtitle: { fontSize: 12, color: Palette.textSecondary, marginTop: 2 },
  topicsList: { gap: 10 },
  topicCard: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  topicCardActive: {
    borderColor: Palette.successBorder,
    backgroundColor: '#FFFFFF',
  },
  topicLeft: { flexDirection: 'row', alignItems: 'center', gap: 12, flex: 1, marginRight: 8 },
  statusCircle: { width: 32, height: 32, borderRadius: 16, backgroundColor: Palette.backgroundSecondary, alignItems: 'center', justifyContent: 'center' },
  statusCircleDone: { backgroundColor: Palette.success },
  statusCircleProgress: { backgroundColor: Palette.successLight },
  topicInfo: { flex: 1 },
  topicTitle: { fontSize: 15, fontWeight: '700', color: Palette.textTitle },
  topicMeta: { fontSize: 12, color: Palette.textSecondary, marginTop: 2 },
  topicRight: { flexDirection: 'row', alignItems: 'center', gap: 8 },
  progressPill: { backgroundColor: Palette.successLight, paddingHorizontal: 8, paddingVertical: 3, borderRadius: 6 },
  progressPillText: { fontSize: 11, fontWeight: '800', color: Palette.success },
});