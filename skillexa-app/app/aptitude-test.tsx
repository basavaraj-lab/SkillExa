import { Feather } from '@expo/vector-icons';
import { router, useLocalSearchParams } from 'expo-router';
import React, { useEffect, useMemo, useRef, useState } from 'react';
import {
  ActivityIndicator,
  Alert,
  Modal,
  Platform,
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  View,
} from 'react-native';
import { AppHeader } from '../components/common/AppHeader';
import { Palette, Radii, Shadows } from '../constants/theme';
import { ApiClient } from '../services/api';

// Aptitude test categories and topics
const CATEGORY_MAP: Record<string, string[]> = {
  'Quantitative Aptitude': [
    'Mixed Topics',
    'Number System',
    'Percentages',
    'Profit and Loss',
    'Simple and Compound Interest',
    'Ratio and Proportion',
    'Averages',
    'Time and Work',
    'Time, Speed and Distance',
    'Problems on Ages',
    'Probability',
    'Permutations and Combinations',
    'Mixtures and Allegations',
    'HCF and LCM',
    'Simplification',
    'Data Interpretation',
  ],
  'Logical Reasoning': [
    'Mixed Topics',
    'Number and Alphabet Series',
    'Coding and Decoding',
    'Blood Relations',
    'Direction Sense',
    'Seating Arrangements',
    'Syllogisms',
    'Analogies',
    'Statement and Conclusion',
    'Puzzles',
    'Ranking and Order',
    'Clocks and Calendars',
  ],
  'Verbal Ability': [
    'Mixed Topics',
    'Grammar',
    'Tenses',
    'Subject-Verb Agreement',
    'Vocabulary',
    'Synonyms and Antonyms',
    'Sentence Correction',
    'Fill in the Blanks',
    'Reading Comprehension',
    'Error Detection',
    'Sentence Rearrangement',
  ],
  'Data Interpretation': [
    'Mixed Topics',
    'Tables',
    'Bar Graphs',
    'Pie Charts',
    'Line Graphs',
    'Caselets',
    'Data Comparison',
  ],
  'Mixed Aptitude': ['Mixed Topics'],
};

const TEST_PRESETS = [
  { id: 'quick', label: 'Quick Test', questions: 10, minutes: 15, icon: 'zap' },
  { id: 'standard', label: 'Standard Test', questions: 20, minutes: 30, icon: 'clock' },
  { id: 'full', label: 'Full-Length Test', questions: 30, minutes: 45, icon: 'award' },
  { id: 'custom', label: 'Custom Test', questions: 15, minutes: 20, icon: 'sliders' },
];

const DIFFICULTIES = ['Easy', 'Intermediate', 'Advanced'];

interface QuestionOption {
  id: string;
  text: string;
}

interface QuestionPublic {
  id: string;
  order_index: number;
  question_text: string;
  options: QuestionOption[];
  category: string;
  topic: string;
  difficulty: string;
  marks: number;
  negative_marks: number;
}

interface QuestionGraded extends QuestionPublic {
  correct_answer: string;
  explanation: string;
  selected_option?: string;
  student_answer?: string;
  is_correct?: boolean;
}

interface AttemptResult {
  attempt_id: string;
  category: string;
  topic: string;
  difficulty: string;
  test_mode?: string;
  question_count: number;
  time_spent_seconds: number;
  duration_minutes?: number;
  started_at: string;
  submitted_at: string;
  final_score?: number;
  score?: number;
  marks_obtained?: number;
  total_marks: number;
  correct_count: number;
  incorrect_count: number;
  unattempted_count: number;
  total_negative_marks: number;
  accuracy_percentage: number;
  status?: string;
  questions: QuestionGraded[];
}

export default function AptitudeTestScreen() {
  const params = useLocalSearchParams<{ attemptId?: string }>();

  // Screen View Mode: 'config' | 'generating' | 'runner' | 'result' | 'history'
  const [viewMode, setViewMode] = useState<'config' | 'generating' | 'runner' | 'result' | 'history'>('config');

  // Config State
  const [selectedCategory, setSelectedCategory] = useState<string>('Quantitative Aptitude');
  const [selectedTopic, setSelectedTopic] = useState<string>('Mixed Topics');
  const [selectedDifficulty, setSelectedDifficulty] = useState<string>('Intermediate');
  const [selectedPreset, setSelectedPreset] = useState<string>('quick');
  const [customQuestionCount, setCustomQuestionCount] = useState<string>('15');
  const [customMinutes, setCustomMinutes] = useState<string>('20');
  const [generationError, setGenerationError] = useState<string | null>(null);

  // Runner State
  const [attemptId, setAttemptId] = useState<string | null>(params.attemptId || null);
  const [questions, setQuestions] = useState<QuestionPublic[]>([]);
  const [currentIndex, setCurrentIndex] = useState<number>(0);
  const [selectedAnswers, setSelectedAnswers] = useState<Record<string, string>>({});
  const [remainingSeconds, setRemainingSeconds] = useState<number>(15 * 60);
  const [totalSecondsAllowed, setTotalSecondsAllowed] = useState<number>(15 * 60);
  const [showSubmitModal, setShowSubmitModal] = useState<boolean>(false);
  const [isSubmitting, setIsSubmitting] = useState<boolean>(false);
  const [showPaletteModal, setShowPaletteModal] = useState<boolean>(false);

  // Result State
  const [resultReport, setResultReport] = useState<AttemptResult | null>(null);

  // History State
  const [historyList, setHistoryList] = useState<any[]>([]);
  const [isLoadingHistory, setIsLoadingHistory] = useState<boolean>(false);

  const timerRef = useRef<any>(null);

  // On mount: check if there's an ongoing attempt in URL or localStorage
  useEffect(() => {
    const resumeSavedAttempt = async () => {
      let savedAttemptId = params.attemptId;
      if (!savedAttemptId && typeof window !== 'undefined' && window.localStorage) {
        savedAttemptId = window.localStorage.getItem('skillexa_active_aptitude_attempt') || undefined;
      }
      if (savedAttemptId) {
        try {
          const res = await ApiClient.getAptitudeTestAttempt(savedAttemptId);
          if (res && res.data) {
            const data = res.data;
            if (data.status === 'in_progress') {
              setAttemptId(data.attempt_id);
              setQuestions(data.questions || []);
              setSelectedAnswers(data.saved_responses || {});
              setRemainingSeconds(data.remaining_seconds || 15 * 60);
              setTotalSecondsAllowed((data.duration_minutes || 15) * 60);
              setViewMode('runner');
            } else if (data.status === 'completed') {
              setResultReport(data);
              setViewMode('result');
            }
          }
        } catch (e) {
          if (typeof window !== 'undefined' && window.localStorage) {
            window.localStorage.removeItem('skillexa_active_aptitude_attempt');
          }
        }
      }
    };

    resumeSavedAttempt();
  }, [params.attemptId]);

  // Timer countdown
  useEffect(() => {
    if (viewMode === 'runner' && remainingSeconds > 0) {
      timerRef.current = setInterval(() => {
        setRemainingSeconds((prev) => {
          if (prev <= 1) {
            clearInterval(timerRef.current);
            handleAutoSubmitOnExpiry();
            return 0;
          }
          return prev - 1;
        });
      }, 1000);
    }

    return () => {
      if (timerRef.current) clearInterval(timerRef.current);
    };
  }, [viewMode]);

  // Topics for selected category
  const availableTopics = useMemo(() => {
    return CATEGORY_MAP[selectedCategory] || ['Mixed Topics'];
  }, [selectedCategory]);

  // Question count resolved from preset
  const resolvedQuestionCount = useMemo(() => {
    if (selectedPreset === 'quick') return 10;
    if (selectedPreset === 'standard') return 20;
    if (selectedPreset === 'full') return 30;
    const parsed = parseInt(customQuestionCount, 10);
    return isNaN(parsed) ? 15 : Math.max(5, Math.min(parsed, 50));
  }, [selectedPreset, customQuestionCount]);

  // Duration in minutes resolved
  const resolvedDurationMinutes = useMemo(() => {
    if (selectedPreset === 'quick') return 15;
    if (selectedPreset === 'standard') return 30;
    if (selectedPreset === 'full') return 45;
    const parsed = parseInt(customMinutes, 10);
    return isNaN(parsed) ? 20 : Math.max(5, Math.min(parsed, 120));
  }, [selectedPreset, customMinutes]);

  // Format MM:SS
  const formatTime = (secs: number) => {
    const mins = Math.floor(secs / 60);
    const s = secs % 60;
    return `${mins.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  };

  // Start / Generate Test Attempt
  const handleStartTest = async () => {
    setViewMode('generating');
    setGenerationError(null);

    try {
      const payload = {
        category: selectedCategory,
        topic: selectedTopic,
        difficulty: selectedDifficulty,
        question_count: resolvedQuestionCount,
        test_mode: selectedPreset,
        duration_minutes: resolvedDurationMinutes,
      };

      const res = await ApiClient.createAptitudeTestAttempt(payload);
      if (res && res.data) {
        const data = res.data;
        setAttemptId(data.attempt_id);
        setQuestions(data.questions);
        setSelectedAnswers({});
        setCurrentIndex(0);
        const durationSec = (data.duration_minutes || resolvedDurationMinutes) * 60;
        setRemainingSeconds(durationSec);
        setTotalSecondsAllowed(durationSec);

        if (typeof window !== 'undefined' && window.localStorage) {
          window.localStorage.setItem('skillexa_active_aptitude_attempt', data.attempt_id);
        }

        setViewMode('runner');
      } else {
        throw new Error('Failed to retrieve generated test questions.');
      }
    } catch (err: any) {
      console.error('Error generating aptitude test:', err);
      setGenerationError(err?.message || 'Failed to generate test. Please try again.');
      setViewMode('config');
    }
  };

  // Select Option
  const handleSelectOption = (questionId: string, optionId: string) => {
    setSelectedAnswers((prev) => {
      const updated = { ...prev, [questionId]: optionId };
      // Auto-save on backend
      if (attemptId) {
        ApiClient.saveAptitudeResponse(attemptId, {
          question_id: questionId,
          selected_option: optionId,
          time_spent_seconds: totalSecondsAllowed - remainingSeconds,
        }).catch((e) => console.warn('Auto-save response failed:', e));
      }
      return updated;
    });
  };

  // Clear current question selection
  const handleClearAnswer = (questionId: string) => {
    setSelectedAnswers((prev) => {
      const updated = { ...prev };
      delete updated[questionId];
      if (attemptId) {
        ApiClient.saveAptitudeResponse(attemptId, {
          question_id: questionId,
          selected_option: '',
        }).catch(() => {});
      }
      return updated;
    });
  };

  // Submit Test
  const handleSubmitTest = async () => {
    if (!attemptId) return;
    setIsSubmitting(true);
    try {
      const timeSpent = Math.max(1, totalSecondsAllowed - remainingSeconds);
      const res = await ApiClient.submitAptitudeTest(attemptId, {
        responses: selectedAnswers,
        time_spent_seconds: timeSpent,
      });

      if (res && res.data) {
        setResultReport(res.data);
        if (typeof window !== 'undefined' && window.localStorage) {
          window.localStorage.removeItem('skillexa_active_aptitude_attempt');
        }
        setShowSubmitModal(false);
        setViewMode('result');
      }
    } catch (e: any) {
      Alert.alert('Submission Error', e?.message || 'Could not submit test. Please retry.');
    } finally {
      setIsSubmitting(false);
    }
  };

  const handleAutoSubmitOnExpiry = async () => {
    if (!attemptId) return;
    try {
      const res = await ApiClient.submitAptitudeTest(attemptId, {
        responses: selectedAnswers,
        time_spent_seconds: totalSecondsAllowed,
      });
      if (res && res.data) {
        setResultReport(res.data);
        if (typeof window !== 'undefined' && window.localStorage) {
          window.localStorage.removeItem('skillexa_active_aptitude_attempt');
        }
        setViewMode('result');
      }
    } catch (e) {
      console.error('Auto submit error:', e);
    }
  };

  // Load Past History
  const handleOpenHistory = async () => {
    setIsLoadingHistory(true);
    setViewMode('history');
    try {
      const res = await ApiClient.getAptitudeHistory();
      setHistoryList(res.data || []);
    } catch (e) {
      console.warn('Failed to load history:', e);
    } finally {
      setIsLoadingHistory(false);
    }
  };

  // Load specific past attempt
  const handleViewPastAttempt = async (pastAttemptId: string) => {
    try {
      const res = await ApiClient.getAptitudeTestAttempt(pastAttemptId);
      if (res && res.data) {
        setResultReport(res.data);
        setViewMode('result');
      }
    } catch (e) {
      Alert.alert('Error', 'Unable to load test result.');
    }
  };

  const currentQ = questions[currentIndex];
  const answeredCount = Object.keys(selectedAnswers).length;

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />

      {/* VIEW: CONFIGURATION */}
      {viewMode === 'config' && (
        <>
          <AppHeader
            showBack
            title="Aptitude Test"
            subtitle="LLM-Powered Dynamic Assessment"
            onBack={() => router.push('/placement-preparation' as any)}
          />

          <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
            {/* Header Card */}
            <View style={styles.heroCard}>
              <View style={styles.heroTop}>
                <View style={styles.heroIconBadge}>
                  <Feather name="cpu" size={24} color="#FFFFFF" />
                </View>
                <View style={{ flex: 1 }}>
                  <View style={{ flexDirection: 'row', alignItems: 'center', gap: 6 }}>
                    <Text style={styles.heroTitle}>AI Dynamic Test Generator</Text>
                    <View style={styles.aiTag}>
                      <Text style={styles.aiTagText}>ACTIVE LLM</Text>
                    </View>
                  </View>
                  <Text style={styles.heroSubtitle}>
                    Every test generates fresh numerical values, scenarios, and reasoning patterns.
                  </Text>
                </View>
              </View>

              <TouchableOpacity
                id="view-past-history-btn"
                style={styles.historyBtn}
                onPress={handleOpenHistory}
                activeOpacity={0.8}
              >
                <Feather name="bar-chart-2" size={15} color={Palette.primary} />
                <Text style={styles.historyBtnText}>View Past Test Attempts</Text>
              </TouchableOpacity>
            </View>

            {generationError && (
              <View style={styles.errorAlert}>
                <Feather name="alert-circle" size={18} color={Palette.danger} />
                <Text style={styles.errorAlertText}>{generationError}</Text>
              </View>
            )}

            {/* 1. Category Selection */}
            <View style={styles.sectionCard}>
              <Text style={styles.sectionHeading}>1. Select Aptitude Category</Text>
              <Text style={styles.sectionSub}>Choose domain or test across all mixed tracks</Text>

              <View style={styles.categoryGrid}>
                {Object.keys(CATEGORY_MAP).map((cat) => {
                  const isSelected = selectedCategory === cat;
                  let iconName: keyof typeof Feather.glyphMap = 'pie-chart';
                  if (cat.includes('Quantitative')) iconName = 'trending-up';
                  else if (cat.includes('Logical')) iconName = 'git-branch';
                  else if (cat.includes('Verbal')) iconName = 'book-open';
                  else if (cat.includes('Mixed')) iconName = 'layers';

                  return (
                    <TouchableOpacity
                      key={cat}
                      style={[styles.categoryCard, isSelected && styles.categoryCardSelected]}
                      onPress={() => {
                        setSelectedCategory(cat);
                        setSelectedTopic('Mixed Topics');
                      }}
                      activeOpacity={0.8}
                    >
                      <View style={[styles.catIconWrap, isSelected && styles.catIconWrapSelected]}>
                        <Feather name={iconName} size={18} color={isSelected ? '#FFFFFF' : Palette.primary} />
                      </View>
                      <Text style={[styles.catTitle, isSelected && styles.catTitleSelected]}>{cat}</Text>
                    </TouchableOpacity>
                  );
                })}
              </View>
            </View>

            {/* 2. Specific Topic */}
            <View style={styles.sectionCard}>
              <Text style={styles.sectionHeading}>2. Select Topic</Text>
              <Text style={styles.sectionSub}>Drill a specific subject or test comprehensive mixed topics</Text>

              <ScrollView horizontal showsHorizontalScrollIndicator={false} style={styles.topicScrollView}>
                {availableTopics.map((top) => {
                  const isSelected = selectedTopic === top;
                  return (
                    <TouchableOpacity
                      key={top}
                      style={[styles.topicChip, isSelected && styles.topicChipSelected]}
                      onPress={() => setSelectedTopic(top)}
                    >
                      <Text style={[styles.topicChipText, isSelected && styles.topicChipTextSelected]}>
                        {top}
                      </Text>
                    </TouchableOpacity>
                  );
                })}
              </ScrollView>
            </View>

            {/* 3. Difficulty Level */}
            <View style={styles.sectionCard}>
              <Text style={styles.sectionHeading}>3. Select Difficulty Level</Text>
              <Text style={styles.sectionSub}>Calibrate problem complexity according to your current level</Text>

              <View style={styles.diffRow}>
                {DIFFICULTIES.map((diff) => {
                  const isSelected = selectedDifficulty === diff;
                  return (
                    <TouchableOpacity
                      key={diff}
                      style={[styles.diffBtn, isSelected && styles.diffBtnSelected]}
                      onPress={() => setSelectedDifficulty(diff)}
                    >
                      <Text style={[styles.diffBtnText, isSelected && styles.diffBtnTextSelected]}>{diff}</Text>
                      <Text style={[styles.diffSub, isSelected && { color: '#E0E7FF' }]}>
                        {diff === 'Easy'
                          ? 'Foundational'
                          : diff === 'Intermediate'
                          ? 'Campus Standard'
                          : 'Tier-1 High-Bar'}
                      </Text>
                    </TouchableOpacity>
                  );
                })}
              </View>
            </View>

            {/* 4. Test Mode & Question Count */}
            <View style={styles.sectionCard}>
              <Text style={styles.sectionHeading}>4. Select Test Format</Text>
              <Text style={styles.sectionSub}>Choose question bundle and duration</Text>

              <View style={styles.presetGrid}>
                {TEST_PRESETS.map((preset) => {
                  const isSelected = selectedPreset === preset.id;
                  return (
                    <TouchableOpacity
                      key={preset.id}
                      style={[styles.presetCard, isSelected && styles.presetCardSelected]}
                      onPress={() => setSelectedPreset(preset.id)}
                    >
                      <View style={{ flexDirection: 'row', alignItems: 'center', gap: 6, marginBottom: 4 }}>
                        <Feather
                          name={preset.icon as any}
                          size={16}
                          color={isSelected ? '#FFFFFF' : Palette.primary}
                        />
                        <Text style={[styles.presetTitle, isSelected && { color: '#FFFFFF' }]}>
                          {preset.label}
                        </Text>
                      </View>
                      <Text style={[styles.presetMeta, isSelected && { color: '#E0E7FF' }]}>
                        {preset.questions} Qs • {preset.minutes} Mins
                      </Text>
                    </TouchableOpacity>
                  );
                })}
              </View>

              {selectedPreset === 'custom' && (
                <View style={styles.customRow}>
                  <View style={{ flex: 1 }}>
                    <Text style={styles.inputLabel}>Questions (5 - 50)</Text>
                    <TextInput
                      style={styles.inputField}
                      keyboardType="numeric"
                      value={customQuestionCount}
                      onChangeText={setCustomQuestionCount}
                      maxLength={2}
                    />
                  </View>
                  <View style={{ flex: 1 }}>
                    <Text style={styles.inputLabel}>Duration (Minutes)</Text>
                    <TextInput
                      style={styles.inputField}
                      keyboardType="numeric"
                      value={customMinutes}
                      onChangeText={setCustomMinutes}
                      maxLength={3}
                    />
                  </View>
                </View>
              )}
            </View>

            {/* Summary & Start Button */}
            <View style={styles.launchCard}>
              <View style={styles.summaryRow}>
                <View>
                  <Text style={styles.summaryTitle}>Ready to begin assessment?</Text>
                  <Text style={styles.summarySubtitle}>
                    {resolvedQuestionCount} Questions • {resolvedDurationMinutes} Minutes • -0.25 Negative Marking
                  </Text>
                </View>
              </View>

              <TouchableOpacity
                id="start-assessment-action-btn"
                style={styles.startActionBtn}
                onPress={handleStartTest}
                activeOpacity={0.88}
              >
                <Feather name="play" size={18} color="#FFFFFF" />
                <Text style={styles.startActionBtnText}>Generate & Start Test</Text>
              </TouchableOpacity>
            </View>
          </ScrollView>
        </>
      )}

      {/* VIEW: GENERATING LOADING SCREEN */}
      {viewMode === 'generating' && (
        <View style={styles.generatingContainer}>
          <ActivityIndicator size="large" color="#4F46E5" />
          <Text style={styles.generatingHeading}>Generating your personalized aptitude test…</Text>
          <Text style={styles.generatingSubtitle}>
            Prompting LLM for {resolvedQuestionCount} fresh {selectedDifficulty.toLowerCase()} questions in{' '}
            {selectedTopic === 'Mixed Topics' ? selectedCategory : `${selectedCategory} (${selectedTopic})`}.
          </Text>
          <View style={styles.generatingStepsBox}>
            <Text style={styles.stepItem}>✓ Constructing domain scenarios & randomized parameters</Text>
            <Text style={styles.stepItem}>✓ Calculating exact numeric keys & 4 distinct options</Text>
            <Text style={styles.stepItem}>✓ Validating answer security on backend...</Text>
          </View>
        </View>
      )}

      {/* VIEW: RUNNER / TEST RUNNER */}
      {viewMode === 'runner' && questions.length > 0 && currentQ && (
        <>
          {/* Runner Header */}
          <View style={styles.runnerHeader}>
            <View>
              <Text style={styles.runnerTopicText}>
                {currentQ.category} • {currentQ.topic}
              </Text>
              <Text style={styles.runnerCounterText}>
                Question {currentIndex + 1} of {questions.length}
              </Text>
            </View>

            <View style={styles.timerWrap}>
              <Feather name="clock" size={15} color={remainingSeconds < 180 ? Palette.danger : Palette.primary} />
              <Text
                style={[
                  styles.timerText,
                  remainingSeconds < 180 && { color: Palette.danger, fontWeight: '800' },
                ]}
              >
                {formatTime(remainingSeconds)}
              </Text>
            </View>

            <TouchableOpacity
              id="open-palette-btn"
              style={styles.paletteToggleBtn}
              onPress={() => setShowPaletteModal(true)}
            >
              <Feather name="grid" size={18} color="#4F46E5" />
            </TouchableOpacity>
          </View>

          {/* Progress Bar */}
          <View style={styles.progressBarBg}>
            <View
              style={[
                styles.progressBarFill,
                { width: `${((currentIndex + 1) / questions.length) * 100}%` },
              ]}
            />
          </View>

          <ScrollView contentContainerStyle={styles.runnerScroll} showsVerticalScrollIndicator={false}>
            {/* Question Card */}
            <View style={styles.questionCard}>
              <View style={styles.qMetaRow}>
                <View style={styles.diffBadge}>
                  <Text style={styles.diffBadgeText}>{currentQ.difficulty.toUpperCase()}</Text>
                </View>
                <Text style={styles.marksBadge}>+1.0 / -0.25 Mark</Text>
              </View>

              <Text style={styles.questionBody}>{currentQ.question_text}</Text>
            </View>

            {/* Options */}
            <View style={styles.optionsContainer}>
              {currentQ.options.map((opt) => {
                const isSelected = selectedAnswers[currentQ.id] === opt.id;
                return (
                  <TouchableOpacity
                    key={opt.id}
                    id={`question-opt-${opt.id}`}
                    style={[styles.optionCard, isSelected && styles.optionCardSelected]}
                    onPress={() => handleSelectOption(currentQ.id, opt.id)}
                    activeOpacity={0.8}
                  >
                    <View style={[styles.optionLetter, isSelected && styles.optionLetterSelected]}>
                      <Text style={[styles.optionLetterText, isSelected && { color: '#FFFFFF' }]}>
                        {opt.id}
                      </Text>
                    </View>
                    <Text style={[styles.optionText, isSelected && styles.optionTextSelected]}>
                      {opt.text}
                    </Text>
                    {isSelected && <Feather name="check" size={18} color="#4F46E5" style={{ marginLeft: 'auto' }} />}
                  </TouchableOpacity>
                );
              })}
            </View>

            {selectedAnswers[currentQ.id] && (
              <TouchableOpacity
                style={styles.clearBtn}
                onPress={() => handleClearAnswer(currentQ.id)}
              >
                <Feather name="x" size={14} color={Palette.textSecondary} />
                <Text style={styles.clearBtnText}>Clear Selected Answer</Text>
              </TouchableOpacity>
            )}
          </ScrollView>

          {/* Footer Controls */}
          <View style={styles.runnerFooter}>
            <TouchableOpacity
              style={[styles.navBtn, currentIndex === 0 && styles.navBtnDisabled]}
              disabled={currentIndex === 0}
              onPress={() => setCurrentIndex((prev) => Math.max(0, prev - 1))}
            >
              <Feather name="chevron-left" size={18} color={currentIndex === 0 ? '#9CA3AF' : '#374151'} />
              <Text style={[styles.navBtnText, currentIndex === 0 && { color: '#9CA3AF' }]}>Previous</Text>
            </TouchableOpacity>

            <TouchableOpacity
              id="submit-test-early-btn"
              style={styles.submitEarlyBtn}
              onPress={() => setShowSubmitModal(true)}
            >
              <Text style={styles.submitEarlyBtnText}>Submit Test</Text>
            </TouchableOpacity>

            {currentIndex < questions.length - 1 ? (
              <TouchableOpacity
                style={styles.navBtnPrimary}
                onPress={() => setCurrentIndex((prev) => Math.min(questions.length - 1, prev + 1))}
              >
                <Text style={styles.navBtnPrimaryText}>Next</Text>
                <Feather name="chevron-right" size={18} color="#FFFFFF" />
              </TouchableOpacity>
            ) : (
              <TouchableOpacity
                id="finish-review-submit-btn"
                style={styles.navBtnPrimary}
                onPress={() => setShowSubmitModal(true)}
              >
                <Text style={styles.navBtnPrimaryText}>Review & Submit</Text>
                <Feather name="check-circle" size={18} color="#FFFFFF" />
              </TouchableOpacity>
            )}
          </View>

          {/* Question Palette Modal */}
          <Modal visible={showPaletteModal} transparent animationType="slide">
            <View style={styles.modalOverlay}>
              <View style={styles.paletteModalCard}>
                <View style={styles.paletteHeader}>
                  <Text style={styles.paletteModalTitle}>Question Palette</Text>
                  <TouchableOpacity onPress={() => setShowPaletteModal(false)}>
                    <Feather name="x" size={20} color="#374151" />
                  </TouchableOpacity>
                </View>

                <View style={styles.paletteLegendRow}>
                  <View style={styles.legendItem}>
                    <View style={[styles.legendDot, { backgroundColor: '#4F46E5' }]} />
                    <Text style={styles.legendLabel}>Answered ({answeredCount})</Text>
                  </View>
                  <View style={styles.legendItem}>
                    <View style={[styles.legendDot, { backgroundColor: '#E5E7EB' }]} />
                    <Text style={styles.legendLabel}>Unanswered ({questions.length - answeredCount})</Text>
                  </View>
                </View>

                <ScrollView style={{ maxHeight: 300 }}>
                  <View style={styles.paletteGrid}>
                    {questions.map((q, idx) => {
                      const isAnswered = !!selectedAnswers[q.id];
                      const isCurr = idx === currentIndex;
                      return (
                        <TouchableOpacity
                          key={q.id}
                          style={[
                            styles.paletteItem,
                            isAnswered && styles.paletteItemAnswered,
                            isCurr && styles.paletteItemCurrent,
                          ]}
                          onPress={() => {
                            setCurrentIndex(idx);
                            setShowPaletteModal(false);
                          }}
                        >
                          <Text
                            style={[
                              styles.paletteItemText,
                              isAnswered && { color: '#FFFFFF' },
                              isCurr && { fontWeight: '900' },
                            ]}
                          >
                            {idx + 1}
                          </Text>
                        </TouchableOpacity>
                      );
                    })}
                  </View>
                </ScrollView>

                <TouchableOpacity
                  style={styles.closePaletteBtn}
                  onPress={() => setShowPaletteModal(false)}
                >
                  <Text style={styles.closePaletteBtnText}>Resume Test</Text>
                </TouchableOpacity>
              </View>
            </View>
          </Modal>

          {/* Submit Confirmation Modal */}
          <Modal visible={showSubmitModal} transparent animationType="fade">
            <View style={styles.modalOverlay}>
              <View style={styles.confirmModalCard}>
                <Feather name="alert-triangle" size={32} color="#F59E0B" style={{ alignSelf: 'center', marginBottom: 10 }} />
                <Text style={styles.confirmModalTitle}>Submit Aptitude Test?</Text>
                <Text style={styles.confirmModalSub}>
                  You have answered {answeredCount} out of {questions.length} questions.
                  {questions.length - answeredCount > 0 &&
                    ` (${questions.length - answeredCount} unanswered)`}
                </Text>

                <View style={styles.confirmMetaBox}>
                  <Text style={styles.confirmMetaText}>• Correct Answer: +1.0 Mark</Text>
                  <Text style={styles.confirmMetaText}>• Incorrect Answer: -0.25 Mark</Text>
                  <Text style={styles.confirmMetaText}>• Unattempted: 0 Mark</Text>
                </View>

                <View style={styles.confirmActionsRow}>
                  <TouchableOpacity
                    style={styles.cancelBtn}
                    onPress={() => setShowSubmitModal(false)}
                    disabled={isSubmitting}
                  >
                    <Text style={styles.cancelBtnText}>Continue Test</Text>
                  </TouchableOpacity>
                  <TouchableOpacity
                    id="confirm-test-submission-btn"
                    style={styles.confirmBtn}
                    onPress={handleSubmitTest}
                    disabled={isSubmitting}
                  >
                    {isSubmitting ? (
                      <ActivityIndicator size="small" color="#FFFFFF" />
                    ) : (
                      <Text style={styles.confirmBtnText}>Submit Now</Text>
                    )}
                  </TouchableOpacity>
                </View>
              </View>
            </View>
          </Modal>
        </>
      )}

      {/* VIEW: RESULT & DETAILED REVIEW */}
      {viewMode === 'result' && resultReport && (
        <>
          <AppHeader
            showBack
            title="Aptitude Test Results"
            subtitle={`${resultReport.category} • ${resultReport.difficulty}`}
            onBack={() => setViewMode('config')}
          />

          <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
            {/* Score Summary Card */}
            {(() => {
              const score = Number(resultReport.final_score ?? resultReport.score ?? resultReport.marks_obtained ?? 0);
              const totalMarks = Number(resultReport.total_marks ?? resultReport.question_count ?? 10);
              const accuracy = Number(resultReport.accuracy_percentage ?? 0);
              const negativeMarks = Number(resultReport.total_negative_marks ?? 0);
              const isHigh = score >= totalMarks * 0.7;
              const isMid = score >= totalMarks * 0.4;

              return (
                <View style={styles.scoreSummaryCard}>
                  <View style={styles.scoreHeaderRow}>
                    <View>
                      <Text style={styles.scoreCardTitle}>Final Test Score</Text>
                      <Text style={styles.scoreCardDate}>
                        Submitted: {new Date(resultReport.submitted_at || Date.now()).toLocaleTimeString()}
                      </Text>
                    </View>
                    <View
                      style={[
                        styles.performanceTag,
                        isHigh ? styles.perfTagHigh : isMid ? styles.perfTagMid : styles.perfTagLow,
                      ]}
                    >
                      <Text style={styles.performanceTagText}>
                        {isHigh ? 'EXCELLENT' : isMid ? 'GOOD EFFORT' : 'NEEDS PRACTICE'}
                      </Text>
                    </View>
                  </View>

                  <View style={styles.bigScoreRow}>
                    <View style={styles.scoreCircle}>
                      <Text style={styles.bigScoreNum}>{score.toFixed(2)}</Text>
                      <Text style={styles.bigScoreSub}>/ {totalMarks} Marks</Text>
                    </View>

                    <View style={styles.scoreStatsCol}>
                      <View style={styles.statLine}>
                        <Text style={styles.statLabel}>Accuracy</Text>
                        <Text style={styles.statValue}>{accuracy.toFixed(1)}%</Text>
                      </View>
                      <View style={styles.statLine}>
                        <Text style={styles.statLabel}>Time Spent</Text>
                        <Text style={styles.statValue}>{Math.round((resultReport.time_spent_seconds || 60) / 60)} mins</Text>
                      </View>
                      <View style={styles.statLine}>
                        <Text style={styles.statLabel}>Negative Marks</Text>
                        <Text style={[styles.statValue, { color: Palette.danger }]}>
                          -{negativeMarks.toFixed(2)}
                        </Text>
                      </View>
                    </View>
                  </View>

                  <View style={styles.breakdownRow}>
                    <View style={[styles.breakdownPill, { backgroundColor: '#ECFDF5' }]}>
                      <Feather name="check" size={14} color="#059669" />
                      <Text style={[styles.breakdownPillText, { color: '#059669' }]}>
                        {resultReport.correct_count ?? 0} Correct
                      </Text>
                    </View>
                    <View style={[styles.breakdownPill, { backgroundColor: '#FEF2F2' }]}>
                      <Feather name="x" size={14} color="#DC2626" />
                      <Text style={[styles.breakdownPillText, { color: '#DC2626' }]}>
                        {resultReport.incorrect_count ?? 0} Wrong
                      </Text>
                    </View>
                    <View style={[styles.breakdownPill, { backgroundColor: '#F3F4F6' }]}>
                      <Feather name="minus" size={14} color="#4B5563" />
                      <Text style={[styles.breakdownPillText, { color: '#4B5563' }]}>
                        {resultReport.unattempted_count ?? 0} Skipped
                      </Text>
                    </View>
                  </View>

                  <View style={styles.resultActionsRow}>
                    <TouchableOpacity
                      id="take-another-test-btn"
                      style={styles.retakeBtn}
                      onPress={() => {
                        setViewMode('config');
                        setResultReport(null);
                      }}
                    >
                      <Feather name="rotate-ccw" size={15} color="#FFFFFF" />
                      <Text style={styles.retakeBtnText}>Take New Fresh Test</Text>
                    </TouchableOpacity>

                    <TouchableOpacity
                      style={styles.doneBtn}
                      onPress={() => router.push('/placement-preparation' as any)}
                    >
                      <Text style={styles.doneBtnText}>Back to Placement Hub</Text>
                    </TouchableOpacity>
                  </View>
                </View>
              );
            })()}

            {/* Detailed Question Explanations */}
            <View style={styles.reviewSectionHeader}>
              <Text style={styles.reviewSectionTitle}>Question-by-Question Solutions</Text>
              <Text style={styles.reviewSectionSubtitle}>
                Step-by-step verified explanations from the backend answer key
              </Text>
            </View>

            {(resultReport.questions || []).map((q, idx) => {
              const studentPick = q.selected_option || q.student_answer;
              const isCorrect = q.is_correct ?? (!!studentPick && studentPick.toUpperCase() === q.correct_answer?.toUpperCase());
              const isSkipped = !studentPick;

              return (
                <View key={q.id || idx} style={styles.reviewCard}>
                  <View style={styles.reviewTopRow}>
                    <Text style={styles.reviewQNum}>Q{idx + 1}</Text>
                    <View
                      style={[
                        styles.reviewStatusBadge,
                        isCorrect
                          ? { backgroundColor: '#ECFDF5' }
                          : isSkipped
                          ? { backgroundColor: '#F3F4F6' }
                          : { backgroundColor: '#FEF2F2' },
                      ]}
                    >
                      <Text
                        style={[
                          styles.reviewStatusText,
                          isCorrect
                            ? { color: '#059669' }
                            : isSkipped
                            ? { color: '#4B5563' }
                            : { color: '#DC2626' },
                        ]}
                      >
                        {isCorrect ? '✓ CORRECT (+1)' : isSkipped ? '— SKIPPED (0)' : '✗ INCORRECT (-0.25)'}
                      </Text>
                    </View>
                  </View>

                  <Text style={styles.reviewQText}>{q.question_text}</Text>

                  {/* Options with color-coded answers */}
                  <View style={styles.reviewOptionsList}>
                    {q.options.map((opt) => {
                      const isKey = opt.id?.toUpperCase() === q.correct_answer?.toUpperCase();
                      const isPicked = !!studentPick && opt.id?.toUpperCase() === studentPick?.toUpperCase();

                      return (
                        <View
                          key={opt.id}
                          style={[
                            styles.reviewOptionRow,
                            isKey && styles.reviewOptionKey,
                            isPicked && !isCorrect && styles.reviewOptionWrong,
                          ]}
                        >
                          <View
                            style={[
                              styles.reviewOptionLetter,
                              isKey && { backgroundColor: '#059669' },
                              isPicked && !isCorrect && { backgroundColor: '#DC2626' },
                            ]}
                          >
                            <Text
                              style={[
                                styles.reviewOptionLetterText,
                                (isKey || (isPicked && !isCorrect)) && { color: '#FFFFFF' },
                              ]}
                            >
                              {opt.id}
                            </Text>
                          </View>
                          <Text
                            style={[
                              styles.reviewOptionText,
                              isKey && { fontWeight: '700', color: '#065F46' },
                              isPicked && !isCorrect && { color: '#991B1B' },
                            ]}
                          >
                            {opt.text}
                          </Text>
                          {isKey && <Text style={styles.correctKeyLabel}>Correct Answer</Text>}
                          {isPicked && !isCorrect && <Text style={styles.yourAnswerLabel}>Your Pick</Text>}
                        </View>
                      );
                    })}
                  </View>

                  {/* Step-by-Step Explanation */}
                  <View style={styles.explanationBox}>
                    <View style={{ flexDirection: 'row', alignItems: 'center', gap: 6, marginBottom: 4 }}>
                      <Feather name="info" size={14} color="#4F46E5" />
                      <Text style={styles.explanationHeading}>Step-by-Step Explanation</Text>
                    </View>
                    <Text style={styles.explanationContent}>{q.explanation}</Text>
                  </View>
                </View>
              );
            })}
          </ScrollView>
        </>
      )}

      {/* VIEW: HISTORY */}
      {viewMode === 'history' && (
        <>
          <AppHeader
            showBack
            title="Aptitude History"
            subtitle="Previous Attempts & Performance Records"
            onBack={() => setViewMode('config')}
          />

          <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
            {isLoadingHistory ? (
              <ActivityIndicator size="large" color="#4F46E5" style={{ marginTop: 40 }} />
            ) : historyList.length === 0 ? (
              <View style={styles.emptyHistoryBox}>
                <Feather name="inbox" size={40} color="#9CA3AF" />
                <Text style={styles.emptyHistoryText}>No past test attempts found.</Text>
                <TouchableOpacity style={styles.historyStartBtn} onPress={() => setViewMode('config')}>
                  <Text style={styles.historyStartBtnText}>Start Your First Test</Text>
                </TouchableOpacity>
              </View>
            ) : (
              historyList.map((item) => (
                <TouchableOpacity
                  key={item.id}
                  style={styles.historyCard}
                  onPress={() => handleViewPastAttempt(item.id)}
                  activeOpacity={0.8}
                >
                  <View style={styles.historyCardTop}>
                    <Text style={styles.historyCardCat}>{item.category}</Text>
                    <View style={styles.historyStatusPill}>
                      <Text style={styles.historyStatusPillText}>{item.status.toUpperCase()}</Text>
                    </View>
                  </View>
                  <Text style={styles.historyCardTopic}>{item.topic || 'Mixed Topics'} • {item.difficulty}</Text>

                  <View style={styles.historyScoreRow}>
                    <Text style={styles.historyScoreNum}>
                      Score: {item.score?.toFixed(1) || '0.0'} / {item.total_marks || item.question_count}
                    </Text>
                    <Text style={styles.historyAccuracy}>
                      Accuracy: {item.accuracy_percentage ? `${item.accuracy_percentage.toFixed(0)}%` : '--'}
                    </Text>
                  </View>
                  <Text style={styles.historyDate}>
                    Attempted: {new Date(item.started_at).toLocaleDateString()} at{' '}
                    {new Date(item.started_at).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
                  </Text>
                </TouchableOpacity>
              ))
            )}
          </ScrollView>
        </>
      )}
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: Palette.background },
  scrollContent: { paddingHorizontal: 16, paddingTop: 16, paddingBottom: 40 },

  // Hero Card
  heroCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 18,
    borderWidth: 1.5,
    borderColor: '#C7D2FE',
    marginBottom: 16,
    ...Shadows.card,
  },
  heroTop: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
    marginBottom: 12,
  },
  heroIconBadge: {
    width: 46,
    height: 46,
    borderRadius: 12,
    backgroundColor: '#4F46E5',
    alignItems: 'center',
    justifyContent: 'center',
  },
  heroTitle: { fontSize: 16, fontWeight: '800', color: Palette.textTitle },
  aiTag: {
    backgroundColor: '#EEF2FF',
    paddingHorizontal: 7,
    paddingVertical: 2,
    borderRadius: 6,
    borderWidth: 1,
    borderColor: '#818CF8',
  },
  aiTagText: { fontSize: 9.5, fontWeight: '800', color: '#4F46E5' },
  heroSubtitle: { fontSize: 12.5, color: Palette.textSecondary, lineHeight: 17, marginTop: 2 },
  historyBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    paddingTop: 10,
    borderTopWidth: 1,
    borderTopColor: '#F3F4F6',
    alignSelf: 'flex-start',
  },
  historyBtnText: { fontSize: 13, fontWeight: '700', color: Palette.primary },

  errorAlert: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    backgroundColor: '#FEF2F2',
    padding: 12,
    borderRadius: 10,
    borderWidth: 1,
    borderColor: '#FECACA',
    marginBottom: 16,
  },
  errorAlertText: { fontSize: 13, color: Palette.danger, flex: 1 },

  // Sections
  sectionCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.border,
    marginBottom: 16,
    ...Shadows.card,
  },
  sectionHeading: { fontSize: 15, fontWeight: '800', color: Palette.textTitle },
  sectionSub: { fontSize: 12, color: Palette.textSecondary, marginBottom: 12, marginTop: 2 },

  categoryGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 8,
  },
  categoryCard: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    paddingVertical: 10,
    paddingHorizontal: 12,
    borderRadius: 10,
    borderWidth: 1.5,
    borderColor: Palette.border,
    backgroundColor: '#F9FAFB',
    minWidth: '47%',
    flex: 1,
  },
  categoryCardSelected: {
    borderColor: '#4F46E5',
    backgroundColor: '#EEF2FF',
  },
  catIconWrap: {
    width: 32,
    height: 32,
    borderRadius: 8,
    backgroundColor: '#E0E7FF',
    alignItems: 'center',
    justifyContent: 'center',
  },
  catIconWrapSelected: {
    backgroundColor: '#4F46E5',
  },
  catTitle: { fontSize: 13, fontWeight: '700', color: Palette.textTitle },
  catTitleSelected: { color: '#4F46E5' },

  topicScrollView: { flexDirection: 'row' },
  topicChip: {
    paddingHorizontal: 12,
    paddingVertical: 7,
    borderRadius: 20,
    borderWidth: 1,
    borderColor: Palette.border,
    backgroundColor: '#F9FAFB',
    marginRight: 8,
  },
  topicChipSelected: {
    backgroundColor: '#4F46E5',
    borderColor: '#4F46E5',
  },
  topicChipText: { fontSize: 12, fontWeight: '600', color: '#4B5563' },
  topicChipTextSelected: { color: '#FFFFFF' },

  diffRow: { flexDirection: 'row', gap: 8 },
  diffBtn: {
    flex: 1,
    paddingVertical: 12,
    paddingHorizontal: 10,
    borderRadius: 10,
    borderWidth: 1.5,
    borderColor: Palette.border,
    backgroundColor: '#F9FAFB',
    alignItems: 'center',
  },
  diffBtnSelected: {
    backgroundColor: '#4F46E5',
    borderColor: '#4F46E5',
  },
  diffBtnText: { fontSize: 13.5, fontWeight: '800', color: Palette.textTitle },
  diffBtnTextSelected: { color: '#FFFFFF' },
  diffSub: { fontSize: 10.5, color: Palette.textSecondary, marginTop: 2 },

  presetGrid: { flexDirection: 'row', flexWrap: 'wrap', gap: 8 },
  presetCard: {
    flex: 1,
    minWidth: '47%',
    padding: 12,
    borderRadius: 10,
    borderWidth: 1.5,
    borderColor: Palette.border,
    backgroundColor: '#F9FAFB',
  },
  presetCardSelected: {
    backgroundColor: '#4F46E5',
    borderColor: '#4F46E5',
  },
  presetTitle: { fontSize: 13.5, fontWeight: '700', color: Palette.textTitle },
  presetMeta: { fontSize: 11.5, color: Palette.textSecondary, marginTop: 2 },

  customRow: { flexDirection: 'row', gap: 12, marginTop: 12 },
  inputLabel: { fontSize: 11.5, fontWeight: '700', color: Palette.textSecondary, marginBottom: 4 },
  inputField: {
    backgroundColor: '#F9FAFB',
    borderWidth: 1,
    borderColor: Palette.border,
    borderRadius: 8,
    paddingHorizontal: 12,
    paddingVertical: 8,
    fontSize: 14,
    fontWeight: '700',
    color: Palette.textTitle,
  },

  launchCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 18,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  summaryRow: { marginBottom: 12 },
  summaryTitle: { fontSize: 15, fontWeight: '800', color: Palette.textTitle },
  summarySubtitle: { fontSize: 12.5, color: Palette.textSecondary, marginTop: 2 },
  startActionBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#4F46E5',
    paddingVertical: 14,
    borderRadius: 10,
    gap: 8,
    ...Shadows.button,
  },
  startActionBtnText: { color: '#FFFFFF', fontSize: 15, fontWeight: '800' },

  // Generating Screen
  generatingContainer: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    padding: 24,
  },
  generatingHeading: {
    fontSize: 18,
    fontWeight: '800',
    color: Palette.textTitle,
    textAlign: 'center',
    marginTop: 20,
    marginBottom: 8,
  },
  generatingSubtitle: {
    fontSize: 13.5,
    color: Palette.textSecondary,
    textAlign: 'center',
    lineHeight: 20,
    marginBottom: 24,
  },
  generatingStepsBox: {
    backgroundColor: '#FFFFFF',
    padding: 16,
    borderRadius: 12,
    borderWidth: 1,
    borderColor: Palette.border,
    width: '100%',
    maxWidth: 420,
    gap: 10,
    ...Shadows.card,
  },
  stepItem: { fontSize: 12.5, color: '#374151', fontWeight: '600' },

  // Runner
  runnerHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: 16,
    paddingVertical: 12,
    backgroundColor: '#FFFFFF',
    borderBottomWidth: 1,
    borderBottomColor: Palette.border,
  },
  runnerTopicText: { fontSize: 11.5, color: Palette.textSecondary, fontWeight: '600' },
  runnerCounterText: { fontSize: 15, fontWeight: '800', color: Palette.textTitle },
  timerWrap: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    backgroundColor: '#F3F4F6',
    paddingHorizontal: 10,
    paddingVertical: 5,
    borderRadius: 8,
  },
  timerText: { fontSize: 14, fontWeight: '700', color: Palette.textTitle },
  paletteToggleBtn: {
    padding: 8,
    borderRadius: 8,
    backgroundColor: '#EEF2FF',
  },
  progressBarBg: { height: 4, backgroundColor: '#E5E7EB' },
  progressBarFill: { height: 4, backgroundColor: '#4F46E5' },
  runnerScroll: { padding: 16, paddingBottom: 90 },

  questionCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 18,
    borderWidth: 1,
    borderColor: Palette.border,
    marginBottom: 16,
    ...Shadows.card,
  },
  qMetaRow: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 10 },
  diffBadge: {
    backgroundColor: '#EEF2FF',
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 6,
  },
  diffBadgeText: { fontSize: 10.5, fontWeight: '800', color: '#4F46E5' },
  marksBadge: { fontSize: 11.5, color: Palette.textSecondary, fontWeight: '600' },
  questionBody: { fontSize: 15.5, fontWeight: '600', color: Palette.textTitle, lineHeight: 23 },

  optionsContainer: { gap: 10 },
  optionCard: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
    backgroundColor: '#FFFFFF',
    borderRadius: 12,
    padding: 14,
    borderWidth: 1.5,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  optionCardSelected: {
    borderColor: '#4F46E5',
    backgroundColor: '#EEF2FF',
  },
  optionLetter: {
    width: 32,
    height: 32,
    borderRadius: 8,
    backgroundColor: '#F3F4F6',
    alignItems: 'center',
    justifyContent: 'center',
  },
  optionLetterSelected: { backgroundColor: '#4F46E5' },
  optionLetterText: { fontSize: 14, fontWeight: '800', color: Palette.textTitle },
  optionText: { fontSize: 14, color: Palette.textTitle, flex: 1, fontWeight: '500' },
  optionTextSelected: { fontWeight: '700', color: '#4F46E5' },

  clearBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    alignSelf: 'center',
    gap: 4,
    marginTop: 14,
    paddingVertical: 6,
    paddingHorizontal: 10,
  },
  clearBtnText: { fontSize: 12, color: Palette.textSecondary },

  runnerFooter: {
    position: 'absolute',
    bottom: 0,
    left: 0,
    right: 0,
    backgroundColor: '#FFFFFF',
    borderTopWidth: 1,
    borderTopColor: Palette.border,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: 16,
    paddingVertical: 12,
  },
  navBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
    paddingHorizontal: 14,
    paddingVertical: 10,
    borderRadius: 8,
    borderWidth: 1,
    borderColor: Palette.border,
  },
  navBtnDisabled: { opacity: 0.5 },
  navBtnText: { fontSize: 13.5, fontWeight: '700', color: '#374151' },
  submitEarlyBtn: {
    paddingHorizontal: 12,
    paddingVertical: 10,
  },
  submitEarlyBtnText: { fontSize: 13, fontWeight: '700', color: Palette.danger },
  navBtnPrimary: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    backgroundColor: '#4F46E5',
    paddingHorizontal: 16,
    paddingVertical: 10,
    borderRadius: 8,
    ...Shadows.button,
  },
  navBtnPrimaryText: { color: '#FFFFFF', fontSize: 13.5, fontWeight: '700' },

  // Modals
  modalOverlay: {
    flex: 1,
    backgroundColor: 'rgba(0,0,0,0.5)',
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  paletteModalCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 16,
    padding: 20,
    width: '100%',
    maxWidth: 400,
    ...Shadows.card,
  },
  paletteHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 12,
  },
  paletteModalTitle: { fontSize: 17, fontWeight: '800', color: Palette.textTitle },
  paletteLegendRow: { flexDirection: 'row', gap: 14, marginBottom: 14 },
  legendItem: { flexDirection: 'row', alignItems: 'center', gap: 6 },
  legendDot: { width: 10, height: 10, borderRadius: 5 },
  legendLabel: { fontSize: 11.5, color: Palette.textSecondary, fontWeight: '600' },
  paletteGrid: { flexDirection: 'row', flexWrap: 'wrap', gap: 8, paddingBottom: 10 },
  paletteItem: {
    width: 44,
    height: 44,
    borderRadius: 10,
    backgroundColor: '#F3F4F6',
    alignItems: 'center',
    justifyContent: 'center',
    borderWidth: 1,
    borderColor: Palette.border,
  },
  paletteItemAnswered: { backgroundColor: '#4F46E5', borderColor: '#4F46E5' },
  paletteItemCurrent: { borderWidth: 2.5, borderColor: '#10B981' },
  paletteItemText: { fontSize: 14, fontWeight: '700', color: Palette.textTitle },
  closePaletteBtn: {
    backgroundColor: '#F3F4F6',
    paddingVertical: 12,
    borderRadius: 10,
    alignItems: 'center',
    marginTop: 12,
  },
  closePaletteBtnText: { fontSize: 14, fontWeight: '700', color: '#374151' },

  confirmModalCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 16,
    padding: 22,
    width: '100%',
    maxWidth: 360,
    ...Shadows.card,
  },
  confirmModalTitle: { fontSize: 18, fontWeight: '800', color: Palette.textTitle, textAlign: 'center' },
  confirmModalSub: { fontSize: 13, color: Palette.textSecondary, textAlign: 'center', marginTop: 4, marginBottom: 12 },
  confirmMetaBox: { backgroundColor: '#F9FAFB', padding: 12, borderRadius: 8, marginBottom: 18, gap: 4 },
  confirmMetaText: { fontSize: 11.5, color: '#4B5563', fontWeight: '500' },
  confirmActionsRow: { flexDirection: 'row', gap: 10 },
  cancelBtn: { flex: 1, paddingVertical: 12, borderRadius: 10, borderWidth: 1, borderColor: Palette.border, alignItems: 'center' },
  cancelBtnText: { fontSize: 13.5, fontWeight: '700', color: '#374151' },
  confirmBtn: { flex: 1, backgroundColor: '#4F46E5', paddingVertical: 12, borderRadius: 10, alignItems: 'center' },
  confirmBtnText: { fontSize: 13.5, fontWeight: '700', color: '#FFFFFF' },

  // Result View
  scoreSummaryCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 20,
    borderWidth: 1.5,
    borderColor: '#C7D2FE',
    marginBottom: 24,
    ...Shadows.card,
  },
  scoreHeaderRow: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: 16 },
  scoreCardTitle: { fontSize: 18, fontWeight: '800', color: Palette.textTitle },
  scoreCardDate: { fontSize: 12, color: Palette.textSecondary, marginTop: 2 },
  performanceTag: { paddingHorizontal: 10, paddingVertical: 4, borderRadius: 8 },
  perfTagHigh: { backgroundColor: '#ECFDF5' },
  perfTagMid: { backgroundColor: '#EEF2FF' },
  perfTagLow: { backgroundColor: '#FEF2F2' },
  performanceTagText: { fontSize: 11, fontWeight: '800', color: '#4F46E5' },

  bigScoreRow: { flexDirection: 'row', alignItems: 'center', gap: 20, marginBottom: 18 },
  scoreCircle: {
    width: 100,
    height: 100,
    borderRadius: 50,
    backgroundColor: '#EEF2FF',
    borderWidth: 3,
    borderColor: '#4F46E5',
    alignItems: 'center',
    justifyContent: 'center',
  },
  bigScoreNum: { fontSize: 26, fontWeight: '900', color: '#4F46E5' },
  bigScoreSub: { fontSize: 11, fontWeight: '700', color: Palette.textSecondary },
  scoreStatsCol: { flex: 1, gap: 6 },
  statLine: { flexDirection: 'row', justifyContent: 'space-between' },
  statLabel: { fontSize: 13, color: Palette.textSecondary },
  statValue: { fontSize: 13.5, fontWeight: '800', color: Palette.textTitle },

  breakdownRow: { flexDirection: 'row', gap: 8, marginBottom: 18 },
  breakdownPill: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 4,
    paddingVertical: 8,
    borderRadius: 8,
  },
  breakdownPillText: { fontSize: 12, fontWeight: '700' },

  resultActionsRow: { gap: 10 },
  retakeBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#4F46E5',
    paddingVertical: 12,
    borderRadius: 10,
    gap: 6,
  },
  retakeBtnText: { color: '#FFFFFF', fontSize: 14, fontWeight: '700' },
  doneBtn: {
    alignItems: 'center',
    paddingVertical: 10,
  },
  doneBtnText: { color: Palette.textSecondary, fontSize: 13.5, fontWeight: '600' },

  reviewSectionHeader: { marginBottom: 14 },
  reviewSectionTitle: { fontSize: 16, fontWeight: '800', color: Palette.textTitle },
  reviewSectionSubtitle: { fontSize: 12.5, color: Palette.textSecondary, marginTop: 2 },

  reviewCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.border,
    marginBottom: 16,
    ...Shadows.card,
  },
  reviewTopRow: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 8 },
  reviewQNum: { fontSize: 14, fontWeight: '800', color: Palette.textTitle },
  reviewStatusBadge: { paddingHorizontal: 8, paddingVertical: 3, borderRadius: 6 },
  reviewStatusText: { fontSize: 11, fontWeight: '800' },
  reviewQText: { fontSize: 14.5, fontWeight: '600', color: Palette.textTitle, lineHeight: 21, marginBottom: 12 },

  reviewOptionsList: { gap: 8, marginBottom: 12 },
  reviewOptionRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 10,
    padding: 10,
    borderRadius: 8,
    borderWidth: 1,
    borderColor: Palette.border,
    backgroundColor: '#F9FAFB',
  },
  reviewOptionKey: {
    borderColor: '#10B981',
    backgroundColor: '#ECFDF5',
  },
  reviewOptionWrong: {
    borderColor: '#EF4444',
    backgroundColor: '#FEF2F2',
  },
  reviewOptionLetter: {
    width: 26,
    height: 26,
    borderRadius: 6,
    backgroundColor: '#E5E7EB',
    alignItems: 'center',
    justifyContent: 'center',
  },
  reviewOptionLetterText: { fontSize: 12, fontWeight: '800', color: Palette.textTitle },
  reviewOptionText: { fontSize: 13, color: Palette.textTitle, flex: 1 },
  correctKeyLabel: { fontSize: 10.5, fontWeight: '800', color: '#059669' },
  yourAnswerLabel: { fontSize: 10.5, fontWeight: '800', color: '#DC2626' },

  explanationBox: {
    backgroundColor: '#EEF2FF',
    borderRadius: 10,
    padding: 12,
    borderWidth: 1,
    borderColor: '#C7D2FE',
  },
  explanationHeading: { fontSize: 12, fontWeight: '800', color: '#4F46E5' },
  explanationContent: { fontSize: 12.5, color: '#374151', lineHeight: 18 },

  // History Screen
  emptyHistoryBox: { alignItems: 'center', marginTop: 60, gap: 12 },
  emptyHistoryText: { fontSize: 15, color: Palette.textSecondary, fontWeight: '600' },
  historyStartBtn: { backgroundColor: '#4F46E5', paddingHorizontal: 18, paddingVertical: 10, borderRadius: 10 },
  historyStartBtnText: { color: '#FFFFFF', fontSize: 13.5, fontWeight: '700' },
  historyCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.border,
    marginBottom: 12,
    ...Shadows.card,
  },
  historyCardTop: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 4 },
  historyCardCat: { fontSize: 15, fontWeight: '800', color: Palette.textTitle },
  historyStatusPill: { backgroundColor: '#EEF2FF', paddingHorizontal: 7, paddingVertical: 2, borderRadius: 6 },
  historyStatusPillText: { fontSize: 10, fontWeight: '800', color: '#4F46E5' },
  historyCardTopic: { fontSize: 12.5, color: Palette.textSecondary, marginBottom: 8 },
  historyScoreRow: { flexDirection: 'row', justifyContent: 'space-between', marginBottom: 4 },
  historyScoreNum: { fontSize: 13.5, fontWeight: '700', color: Palette.textTitle },
  historyAccuracy: { fontSize: 13, fontWeight: '600', color: '#059669' },
  historyDate: { fontSize: 11.5, color: Palette.textSecondary, marginTop: 4 },
});
