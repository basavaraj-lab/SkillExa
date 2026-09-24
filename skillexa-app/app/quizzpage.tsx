import { Feather } from '@expo/vector-icons';
import { router, useLocalSearchParams } from 'expo-router';
import React, { useEffect, useMemo, useState } from 'react';
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
import { ProgressBar } from '../components/common/EducationalCards';
import { Palette, Radii, Shadows } from '../constants/theme';
import { getTopicContent, QuizQuestion } from '../data/topicData';
import { FacultyStore } from '../services/facultyStore';

export default function QuizScreen() {
  const { topic = 'Percentage & Profit/Loss', subject = 'Quantitative Aptitude', count = '10' } = useLocalSearchParams<{
    topic: string;
    subject: string;
    count: string;
  }>();

  // Load standard topic questions + faculty questions
  const topicData = getTopicContent(subject, topic);
  const facultyQuestions = FacultyStore.getQuestionsForTopic(subject, topic);

  const hasFacultyQuestions = facultyQuestions.length > 0;

  const quizQuestions: QuizQuestion[] = useMemo(() => {
    // Convert faculty questions to QuizQuestion format with isFaculty flag
    const mappedFaculty: QuizQuestion[] = facultyQuestions.map((fq: any, idx: number) => ({
      id: 5000 + idx,
      question: fq.question,
      options: fq.options,
      correctIndex: fq.correctIndex,
      explanation: `${fq.explanation} (Author: ${fq.facultyName})`,
      isFaculty: true,
    }));

    const combined = [...mappedFaculty, ...topicData.quizQuestions];
    return combined.slice(0, parseInt(count, 10) || 10);
  }, [topic, subject, count, facultyQuestions.length]);

  const [currentIndex, setCurrentIndex] = useState<number>(0);
  const [selectedOptions, setSelectedOptions] = useState<{ [qId: number]: number }>({});
  const [secondsRemaining, setSecondsRemaining] = useState<number>(600); // 10 minutes

  useEffect(() => {
    const timer = setInterval(() => {
      setSecondsRemaining((prev) => {
        if (prev <= 1) {
          clearInterval(timer);
          handleSubmitQuiz();
          return 0;
        }
        return prev - 1;
      });
    }, 1000);
    return () => clearInterval(timer);
  }, [selectedOptions]);

  const formatTimer = (sec: number) => {
    const m = Math.floor(sec / 60);
    const s = sec % 60;
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  };

  const totalQuestions = quizQuestions.length || 1;
  const currentQ = quizQuestions[currentIndex] || quizQuestions[0];
  const progressRatio = (currentIndex + 1) / totalQuestions;

  const handleSelectOption = (index: number) => {
    setSelectedOptions({
      ...selectedOptions,
      [currentQ.id]: index,
    });
  };

  const handleNext = () => {
    if (currentIndex < totalQuestions - 1) {
      setCurrentIndex(currentIndex + 1);
    } else {
      handleSubmitQuiz();
    }
  };

  const handlePrev = () => {
    if (currentIndex > 0) {
      setCurrentIndex(currentIndex - 1);
    }
  };

  const handleSubmitQuiz = () => {
    let correctCount = 0;
    let wrongCount = 0;
    let skippedCount = 0;

    quizQuestions.forEach((q) => {
      const studentAns = selectedOptions[q.id];
      if (studentAns === undefined) {
        skippedCount++;
      } else if (studentAns === q.correctIndex) {
        correctCount++;
      } else {
        wrongCount++;
      }
    });

    router.replace({
      pathname: '/quiz-result',
      params: {
        topic,
        total: totalQuestions.toString(),
        correct: correctCount.toString(),
        wrong: wrongCount.toString(),
        skipped: skippedCount.toString(),
        timeSpent: `${Math.floor((600 - secondsRemaining) / 60)}m ${(600 - secondsRemaining) % 60}s`,
      },
    });
  };

  const handleExit = () => {
    Alert.alert(
      'Exit Quiz',
      'Are you sure you want to exit? Your progress in this session will not be saved.',
      [
        { text: 'Continue Quiz', style: 'cancel' },
        { text: 'Exit', style: 'destructive', onPress: () => router.back() },
      ]
    );
  };

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />

      {/* Distraction-Free Header */}
      <View style={styles.header}>
        <TouchableOpacity style={styles.exitBtn} onPress={handleExit}>
          <Feather name="x" size={20} color={Palette.textSecondary} />
          <Text style={styles.exitText}>Exit</Text>
        </TouchableOpacity>

        <View style={styles.headerCenter}>
          <View style={{ flexDirection: 'row', alignItems: 'center', gap: 6 }}>
            <Text style={styles.topicHeaderTitle} numberOfLines={1}>{topic}</Text>
            {hasFacultyQuestions && (
              <View style={styles.facultyBadge}>
                <Text style={styles.facultyBadgeText}>🎓 Faculty Quiz</Text>
              </View>
            )}
          </View>
          <Text style={styles.progressCounterText}>
            Question {currentIndex + 1} of {totalQuestions}
          </Text>
        </View>

        <View style={styles.timerBadge}>
          <Feather name="clock" size={13} color={secondsRemaining < 120 ? Palette.danger : Palette.primary} />
          <Text style={[styles.timerText, secondsRemaining < 120 && { color: Palette.danger }]}>
            {formatTimer(secondsRemaining)}
          </Text>
        </View>
      </View>

      {/* Top Thin Progress Bar */}
      <ProgressBar progress={progressRatio} color={Palette.primary} />

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {/* Question Statement Card */}
        <View style={styles.questionCard}>
          <View style={styles.questionMetaRow}>
            <View style={styles.questionNumTag}>
              <Text style={styles.questionNumText}>QUESTION {currentIndex + 1}</Text>
            </View>
            {currentQ?.isFaculty && (
              <View style={styles.facultyQTag}>
                <Text style={styles.facultyQTagText}>🎓 Verified Faculty Question</Text>
              </View>
            )}
          </View>
          <Text style={styles.questionText}>{currentQ?.question}</Text>
        </View>

        {/* Options List */}
        <View style={styles.optionsList}>
          {currentQ?.options?.map((option, optIdx) => {
            const isSelected = selectedOptions[currentQ.id] === optIdx;

            return (
              <TouchableOpacity
                key={optIdx}
                style={[
                  styles.optionCard,
                  isSelected && styles.optionCardSelected,
                ]}
                onPress={() => handleSelectOption(optIdx)}
                activeOpacity={0.8}
              >
                <View
                  style={[
                    styles.optLetterBox,
                    isSelected && styles.optLetterBoxSelected,
                  ]}
                >
                  <Text style={[styles.optLetterText, isSelected && styles.optLetterTextSelected]}>
                    {String.fromCharCode(65 + optIdx)}
                  </Text>
                </View>

                <Text style={[styles.optionLabel, isSelected && styles.optionLabelSelected]}>
                  {option}
                </Text>

                {isSelected && (
                  <Feather name="check" size={18} color={Palette.primary} />
                )}
              </TouchableOpacity>
            );
          })}
        </View>
      </ScrollView>

      {/* Bottom Distraction-Free Controls */}
      <View style={styles.footerControls}>
        <TouchableOpacity
          style={[styles.prevBtn, currentIndex === 0 && styles.btnDisabled]}
          onPress={handlePrev}
          disabled={currentIndex === 0}
        >
          <Feather name="arrow-left" size={16} color={currentIndex === 0 ? Palette.textMuted : Palette.textTitle} />
          <Text style={[styles.prevBtnText, currentIndex === 0 && { color: Palette.textMuted }]}>
            Previous
          </Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={styles.nextBtn}
          onPress={handleNext}
          activeOpacity={0.85}
        >
          <Text style={styles.nextBtnText}>
            {currentIndex === totalQuestions - 1 ? 'Submit Assessment' : 'Next Question'}
          </Text>
          <Feather name="arrow-right" size={16} color="#FFFFFF" />
        </TouchableOpacity>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: Palette.background },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: 16,
    paddingVertical: 12,
    backgroundColor: '#FFFFFF',
  },
  exitBtn: { flexDirection: 'row', alignItems: 'center', gap: 4, paddingVertical: 4 },
  exitText: { fontSize: 13.5, fontWeight: '600', color: Palette.textSecondary },
  headerCenter: { alignItems: 'center', flex: 1, paddingHorizontal: 8 },
  topicHeaderTitle: { fontSize: 13, fontWeight: '700', color: Palette.textTitle },
  facultyBadge: { backgroundColor: Palette.primaryLight, paddingHorizontal: 6, paddingVertical: 2, borderRadius: 4 },
  facultyBadgeText: { fontSize: 10, fontWeight: '800', color: Palette.primary },
  progressCounterText: { fontSize: 11, color: Palette.textSecondary, marginTop: 1 },
  timerBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 5,
    backgroundColor: Palette.primaryLight,
    paddingHorizontal: 10,
    paddingVertical: 5,
    borderRadius: Radii.pill,
  },
  timerText: { fontSize: 12.5, fontWeight: '800', color: Palette.primary },
  scrollContent: { paddingHorizontal: 16, paddingTop: 18, paddingBottom: 40 },
  questionCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 20,
    borderWidth: 1,
    borderColor: Palette.border,
    marginBottom: 20,
    ...Shadows.card,
  },
  questionMetaRow: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 10 },
  questionNumTag: {
    backgroundColor: Palette.backgroundSecondary,
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 6,
  },
  questionNumText: { fontSize: 10.5, fontWeight: '800', color: Palette.primary, letterSpacing: 0.8 },
  facultyQTag: { backgroundColor: Palette.primaryLight, paddingHorizontal: 8, paddingVertical: 3, borderRadius: 6 },
  facultyQTagText: { fontSize: 10.5, fontWeight: '700', color: Palette.primary },
  questionText: { fontSize: 16, fontWeight: '700', color: Palette.textTitle, lineHeight: 24 },
  optionsList: { gap: 12 },
  optionCard: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  optionCardSelected: {
    borderColor: Palette.primary,
    backgroundColor: Palette.primaryLight,
    borderWidth: 1.5,
  },
  optLetterBox: {
    width: 32,
    height: 32,
    borderRadius: 16,
    backgroundColor: Palette.backgroundSecondary,
    alignItems: 'center',
    justifyContent: 'center',
    marginRight: 12,
  },
  optLetterBoxSelected: {
    backgroundColor: Palette.primary,
  },
  optLetterText: { fontSize: 13, fontWeight: '700', color: Palette.textSecondary },
  optLetterTextSelected: { color: '#FFFFFF' },
  optionLabel: { flex: 1, fontSize: 14.5, color: Palette.textBody },
  optionLabelSelected: { color: Palette.primary, fontWeight: '700' },
  footerControls: {
    flexDirection: 'row',
    gap: 12,
    paddingHorizontal: 16,
    paddingVertical: 14,
    backgroundColor: '#FFFFFF',
    borderTopWidth: 1,
    borderTopColor: Palette.border,
  },
  prevBtn: {
    backgroundColor: '#FFFFFF',
    borderWidth: 1,
    borderColor: Palette.border,
    borderRadius: Radii.button,
    paddingVertical: 12,
    paddingHorizontal: 18,
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
  },
  btnDisabled: { opacity: 0.5 },
  prevBtnText: { fontSize: 14, fontWeight: '700', color: Palette.textTitle },
  nextBtn: {
    flex: 1,
    backgroundColor: Palette.primary,
    borderRadius: Radii.button,
    paddingVertical: 12,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
    ...Shadows.button,
  },
  nextBtnText: { fontSize: 14, fontWeight: '700', color: '#FFFFFF' },
});