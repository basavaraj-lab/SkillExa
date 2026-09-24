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
import { AppHeader } from '../components/common/AppHeader';
import { Palette, Radii, Shadows } from '../constants/theme';

const REVIEW_ITEMS = [
  {
    id: 1,
    question: "Neither the principal nor the teachers ______ present at the annual convocation ceremony.",
    userAnswer: "were",
    correctAnswer: "were",
    isCorrect: true,
    explanation: "When subjects are connected by 'neither...nor', the verb agrees with the closer subject ('teachers' is plural, so 'were' is correct).",
  },
  {
    id: 2,
    question: "If I ______ known about the seminar earlier, I would have registered immediately.",
    userAnswer: "had",
    correctAnswer: "had",
    isCorrect: true,
    explanation: "Third conditional structure requires 'had + past participle' in the if-clause and 'would have + past participle' in the main clause.",
  },
  {
    id: 3,
    question: "The speed of a train is 72 km/hr. How many meters will it cover in 15 seconds?",
    userAnswer: "250 m",
    correctAnswer: "300 m",
    isCorrect: false,
    explanation: "Convert km/hr to m/s: 72 * (5/18) = 20 m/s. Distance = Speed * Time = 20 * 15 = 300 meters.",
  },
  {
    id: 4,
    question: "Choose the synonym for the word 'METICULOUS':",
    userAnswer: "Thorough & Precise",
    correctAnswer: "Thorough & Precise",
    isCorrect: true,
    explanation: "Meticulous means showing great attention to detail; very careful and precise.",
  },
  {
    id: 5,
    question: "In a binary search algorithm, what is the worst-case time complexity for an array of size N?",
    userAnswer: "O(log N)",
    correctAnswer: "O(log N)",
    isCorrect: true,
    explanation: "Binary search halves the search space at each comparison step, resulting in O(log N) worst-case time complexity.",
  },
];

export default function AnswerReviewPage() {
  const { topic = 'General Practice' } = useLocalSearchParams<{ topic: string }>();

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader showBack title="Answer Key & Solutions" subtitle={topic} />

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {/* Header */}
        <View style={styles.header}>
          <Text style={styles.title}>Detailed Explanations</Text>
          <Text style={styles.subtitle}>Review your answers and understand key principles.</Text>
        </View>

        {/* Review List */}
        <View style={styles.list}>
          {REVIEW_ITEMS.map((item, idx) => (
            <View
              key={item.id}
              style={[
                styles.reviewCard,
                item.isCorrect ? styles.cardCorrect : styles.cardWrong,
              ]}
            >
              {/* Card Header Row */}
              <View style={styles.cardHeader}>
                <View style={styles.qNumBox}>
                  <Text style={styles.qNumText}>Q{idx + 1}</Text>
                </View>
                <View
                  style={[
                    styles.statusPill,
                    item.isCorrect ? styles.statusPillCorrect : styles.statusPillWrong,
                  ]}
                >
                  <Feather
                    name={item.isCorrect ? 'check' : 'x'}
                    size={12}
                    color={item.isCorrect ? Palette.success : Palette.danger}
                  />
                  <Text
                    style={[
                      styles.statusPillText,
                      item.isCorrect ? { color: Palette.success } : { color: Palette.danger },
                    ]}
                  >
                    {item.isCorrect ? 'Correct' : 'Incorrect'}
                  </Text>
                </View>
              </View>

              {/* Question Text */}
              <Text style={styles.questionText}>{item.question}</Text>

              {/* Answers Comparison */}
              <View style={styles.answersBlock}>
                <View style={styles.ansRow}>
                  <Text style={styles.ansLabel}>Your Answer:</Text>
                  <Text
                    style={[
                      styles.ansValue,
                      item.isCorrect ? { color: Palette.success } : { color: Palette.danger },
                    ]}
                  >
                    {item.userAnswer}
                  </Text>
                </View>

                {!item.isCorrect && (
                  <View style={[styles.ansRow, { marginTop: 4 }]}>
                    <Text style={styles.ansLabel}>Correct Answer:</Text>
                    <Text style={[styles.ansValue, { color: Palette.success, fontWeight: '700' }]}>
                      {item.correctAnswer}
                    </Text>
                  </View>
                )}
              </View>

              {/* Explanation Box */}
              <View style={styles.explanationBox}>
                <Text style={styles.explanationHeading}>Concept & Rule:</Text>
                <Text style={styles.explanationBody}>{item.explanation}</Text>
              </View>
            </View>
          ))}
        </View>

        <TouchableOpacity
          style={styles.doneBtn}
          onPress={() => router.replace('/home' as any)}
        >
          <Text style={styles.doneBtnText}>Back to Dashboard</Text>
        </TouchableOpacity>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: Palette.background },
  scrollContent: { paddingHorizontal: 16, paddingTop: 16, paddingBottom: 40 },
  header: { marginBottom: 18 },
  title: { fontSize: 20, fontWeight: '800', color: Palette.textTitle, marginBottom: 4 },
  subtitle: { fontSize: 13, color: Palette.textSecondary },
  list: { gap: 14, marginBottom: 20 },
  reviewCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  cardCorrect: { borderLeftWidth: 4, borderLeftColor: Palette.success },
  cardWrong: { borderLeftWidth: 4, borderLeftColor: Palette.danger },
  cardHeader: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 10 },
  qNumBox: { backgroundColor: Palette.backgroundSecondary, paddingHorizontal: 8, paddingVertical: 3, borderRadius: 6 },
  qNumText: { fontSize: 11, fontWeight: '800', color: Palette.textTitle },
  statusPill: { flexDirection: 'row', alignItems: 'center', gap: 4, paddingHorizontal: 8, paddingVertical: 3, borderRadius: Radii.pill },
  statusPillCorrect: { backgroundColor: Palette.successLight },
  statusPillWrong: { backgroundColor: Palette.dangerLight },
  statusPillText: { fontSize: 11, fontWeight: '700' },
  questionText: { fontSize: 14.5, fontWeight: '700', color: Palette.textTitle, lineHeight: 21, marginBottom: 12 },
  answersBlock: { backgroundColor: Palette.backgroundSecondary, padding: 10, borderRadius: 8, marginBottom: 10 },
  ansRow: { flexDirection: 'row', justifyContent: 'space-between' },
  ansLabel: { fontSize: 12, color: Palette.textSecondary },
  ansValue: { fontSize: 12.5, fontWeight: '600' },
  explanationBox: { backgroundColor: '#F8FAFC', padding: 10, borderRadius: 8, borderWidth: 1, borderColor: Palette.border },
  explanationHeading: { fontSize: 11.5, fontWeight: '700', color: Palette.textTitle, marginBottom: 2 },
  explanationBody: { fontSize: 12, color: Palette.textBody, lineHeight: 17 },
  doneBtn: {
    backgroundColor: Palette.primary,
    borderRadius: Radii.button,
    paddingVertical: 13,
    alignItems: 'center',
    ...Shadows.button,
  },
  doneBtnText: { color: '#FFFFFF', fontSize: 14.5, fontWeight: '700' },
});
