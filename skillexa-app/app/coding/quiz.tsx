import { Feather } from '@expo/vector-icons';
import { router, useLocalSearchParams } from 'expo-router';
import React, { useMemo, useState } from 'react';
import {
  Alert,
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from 'react-native';
import { AppHeader } from '../../components/common/AppHeader';
import { Palette, Radii, Shadows } from '../../constants/theme';
import { getEngineeringTopic } from '../../data/engineeringCurriculum';

export default function CodingQuizScreen() {
  const {
    topic = 'Functions & Scope',
    subject = 'Programming in Python',
    language = 'Python',
    count = '5',
  } = useLocalSearchParams<{
    topic: string;
    subject: string;
    language: string;
    count: string;
  }>();

  const curriculum = useMemo(() => getEngineeringTopic(language || subject, topic), [language, subject, topic]);
  const questions = useMemo(() => {
    return curriculum.questions.slice(0, parseInt(count, 10) || 5);
  }, [curriculum, count]);

  const [currentIndex, setCurrentIndex] = useState(0);
  const [selectedAnswers, setSelectedAnswers] = useState<Record<number, number>>({});
  const [submitted, setSubmitted] = useState(false);

  const currentQ = questions[currentIndex] || questions[0];

  const handleSelectOption = (optIdx: number) => {
    if (submitted) return;
    setSelectedAnswers((prev) => ({ ...prev, [currentIndex]: optIdx }));
  };

  const calculateScore = () => {
    let score = 0;
    questions.forEach((q, idx) => {
      if (selectedAnswers[idx] === q.correctAnswer) {
        score += 1;
      }
    });
    return score;
  };

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader showBack title={`${topic} Quiz`} subtitle={`${language} Track`} />

      <ScrollView contentContainerStyle={styles.content} showsVerticalScrollIndicator={false}>
        <View style={styles.card}>
          <View style={styles.progressRow}>
            <Text style={styles.qNumText}>
              Question {currentIndex + 1} of {questions.length}
            </Text>
            <Text style={styles.diffBadge}>{currentQ?.difficulty?.toUpperCase() || 'MEDIUM'}</Text>
          </View>

          <Text style={styles.questionText}>{currentQ?.question}</Text>

          <View style={styles.optionsList}>
            {currentQ?.options?.map((opt, idx) => {
              const isSelected = selectedAnswers[currentIndex] === idx;
              const isCorrect = currentQ.correctAnswer === idx;

              let btnStyle: any = styles.optionBtn;
              if (submitted) {
                if (isCorrect) btnStyle = [styles.optionBtn, styles.optionCorrect];
                else if (isSelected) btnStyle = [styles.optionBtn, styles.optionWrong];
              } else if (isSelected) {
                btnStyle = [styles.optionBtn, styles.optionSelected];
              }

              return (
                <TouchableOpacity
                  key={idx}
                  style={btnStyle}
                  onPress={() => handleSelectOption(idx)}
                  activeOpacity={0.8}
                >
                  <Text style={styles.optionText}>{opt}</Text>
                </TouchableOpacity>
              );
            })}
          </View>

          {submitted && currentQ?.explanation ? (
            <View style={styles.explanationBox}>
              <Text style={styles.explanationTitle}>💡 Explanation:</Text>
              <Text style={styles.explanationText}>{currentQ.explanation}</Text>
            </View>
          ) : null}

          {/* Navigation Controls */}
          <View style={styles.navRow}>
            <TouchableOpacity
              style={[styles.navBtn, currentIndex === 0 && styles.navBtnDisabled]}
              disabled={currentIndex === 0}
              onPress={() => setCurrentIndex((prev) => prev - 1)}
            >
              <Feather name="arrow-left" size={16} color={currentIndex === 0 ? Palette.textMuted : Palette.textTitle} />
              <Text style={[styles.navBtnText, currentIndex === 0 && { color: Palette.textMuted }]}>Previous</Text>
            </TouchableOpacity>

            {currentIndex < questions.length - 1 ? (
              <TouchableOpacity
                style={[styles.navBtn, styles.navBtnPrimary]}
                onPress={() => setCurrentIndex((prev) => prev + 1)}
              >
                <Text style={styles.navBtnPrimaryText}>Next</Text>
                <Feather name="arrow-right" size={16} color="#FFFFFF" />
              </TouchableOpacity>
            ) : !submitted ? (
              <TouchableOpacity
                style={[styles.navBtn, styles.navBtnSuccess]}
                onPress={() => {
                  setSubmitted(true);
                  const s = calculateScore();
                  Alert.alert('Quiz Completed! 🎉', `You scored ${s} out of ${questions.length}!`);
                }}
              >
                <Text style={styles.navBtnPrimaryText}>Submit Assessment</Text>
                <Feather name="check" size={16} color="#FFFFFF" />
              </TouchableOpacity>
            ) : (
              <TouchableOpacity
                style={[styles.navBtn, styles.navBtnSuccess]}
                onPress={() => router.back()}
              >
                <Text style={styles.navBtnPrimaryText}>Return to Track</Text>
              </TouchableOpacity>
            )}
          </View>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: Palette.background },
  content: { padding: 16 },
  card: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  progressRow: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 12 },
  qNumText: { fontSize: 12, fontWeight: '800', color: Palette.primary },
  diffBadge: { fontSize: 10.5, fontWeight: '800', color: Palette.warning, backgroundColor: Palette.warningLight, paddingHorizontal: 6, paddingVertical: 2, borderRadius: 4 },
  questionText: { fontSize: 15, fontWeight: '800', color: Palette.textTitle, lineHeight: 22, marginBottom: 16 },
  optionsList: { gap: 8, marginBottom: 16 },
  optionBtn: {
    padding: 12,
    borderRadius: Radii.button,
    backgroundColor: '#FFFFFF',
    borderWidth: 1,
    borderColor: Palette.border,
  },
  optionSelected: { backgroundColor: Palette.primaryLight, borderColor: Palette.primary },
  optionCorrect: { backgroundColor: Palette.successLight, borderColor: Palette.success },
  optionWrong: { backgroundColor: Palette.dangerLight, borderColor: Palette.danger },
  optionText: { fontSize: 13, fontWeight: '600', color: Palette.textTitle },
  explanationBox: { backgroundColor: Palette.backgroundSecondary, padding: 12, borderRadius: 8, marginBottom: 16, borderWidth: 1, borderColor: Palette.borderSubtle },
  explanationTitle: { fontSize: 11.5, fontWeight: '800', color: Palette.textTitle, marginBottom: 4 },
  explanationText: { fontSize: 12, color: Palette.textSecondary, lineHeight: 17 },
  navRow: { flexDirection: 'row', justifyContent: 'space-between', gap: 10, marginTop: 6 },
  navBtn: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 11,
    borderRadius: Radii.button,
    borderWidth: 1,
    borderColor: Palette.border,
    gap: 6,
  },
  navBtnDisabled: { opacity: 0.5 },
  navBtnText: { fontSize: 13, fontWeight: '700', color: Palette.textTitle },
  navBtnPrimary: { backgroundColor: Palette.primary, borderColor: Palette.primary },
  navBtnSuccess: { backgroundColor: Palette.success, borderColor: Palette.success },
  navBtnPrimaryText: { fontSize: 13, fontWeight: '700', color: '#FFFFFF' },
});
