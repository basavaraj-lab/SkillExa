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

const GK_TOPICS: TopicItem[] = [
  { id: 'polity', title: 'Indian Polity & Constitution', subtopics: '6 subtopics', questionsCount: '320+ questions', progress: 0.65, status: 'inprogress' },
  { id: 'history', title: 'Modern Indian History & Movement', subtopics: '5 subtopics', questionsCount: '280+ questions', progress: 1.0, status: 'completed' },
  { id: 'geography', title: 'Physical & Indian Geography', subtopics: '6 subtopics', questionsCount: '250+ questions', progress: 0.0, status: 'notstarted' },
  { id: 'economy', title: 'Indian Economy & Union Budget', subtopics: '4 subtopics', questionsCount: '190+ questions', progress: 0.0, status: 'notstarted' },
  { id: 'current', title: 'National & Global Current Affairs', subtopics: 'Monthly capsules', questionsCount: '400+ questions', progress: 0.0, status: 'notstarted' },
];

export default function AwarenessPage() {
  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader showBack title="General Awareness" subtitle="Competitive Track" />

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {/* Header Title */}
        <View style={styles.header}>
          <Text style={styles.title}>General Awareness</Text>
          <Text style={styles.subtitle}>Polity, History, Geography, Economy, and Current Events mastery.</Text>
        </View>

        {/* Progress Card */}
        <View style={styles.progressCard}>
          <View style={styles.progressRow}>
            <View>
              <Text style={styles.progressLabel}>SUBJECT PROGRESS</Text>
              <Text style={styles.progressValue}>42% Completed</Text>
            </View>
            <View style={styles.badge}>
              <Text style={styles.badgeText}>2 / 5 Topics Done</Text>
            </View>
          </View>
          <ProgressBar progress={0.42} color={Palette.warning} />
        </View>

        {/* Topics List Heading */}
        <View style={styles.sectionHeader}>
          <Text style={styles.sectionTitle}>Curriculum Topics</Text>
          <Text style={styles.sectionSubtitle}>Select a topic to start structured notes & PYQ tests</Text>
        </View>

        {/* Topic Cards */}
        <View style={styles.topicsList}>
          {GK_TOPICS.map((topic) => {
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
                      subject: 'General Awareness',
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
                      <Feather name="globe" size={14} color={isInProgress ? Palette.warning : Palette.textSecondary} />
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
                  <Feather name="chevron-right" size={18} color={isInProgress ? Palette.warning : Palette.textMuted} />
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
  progressLabel: { fontSize: 11, fontWeight: '800', color: Palette.warning, letterSpacing: 0.8 },
  progressValue: { fontSize: 16, fontWeight: '800', color: Palette.textTitle, marginTop: 2 },
  badge: { backgroundColor: Palette.warningLight, paddingHorizontal: 10, paddingVertical: 4, borderRadius: 6 },
  badgeText: { fontSize: 12, fontWeight: '700', color: Palette.warning },
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
    borderColor: Palette.warning,
    backgroundColor: '#FFFFFF',
  },
  topicLeft: { flexDirection: 'row', alignItems: 'center', gap: 12, flex: 1, marginRight: 8 },
  statusCircle: { width: 32, height: 32, borderRadius: 16, backgroundColor: Palette.backgroundSecondary, alignItems: 'center', justifyContent: 'center' },
  statusCircleDone: { backgroundColor: Palette.success },
  statusCircleProgress: { backgroundColor: Palette.warningLight },
  topicInfo: { flex: 1 },
  topicTitle: { fontSize: 15, fontWeight: '700', color: Palette.textTitle },
  topicMeta: { fontSize: 12, color: Palette.textSecondary, marginTop: 2 },
  topicRight: { flexDirection: 'row', alignItems: 'center', gap: 8 },
  progressPill: { backgroundColor: Palette.warningLight, paddingHorizontal: 8, paddingVertical: 3, borderRadius: 6 },
  progressPillText: { fontSize: 11, fontWeight: '800', color: Palette.warning },
});