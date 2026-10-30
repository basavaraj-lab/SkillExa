import { Feather } from '@expo/vector-icons';
import { router } from 'expo-router';
import React, { useEffect, useState } from 'react';
import {
  ActivityIndicator,
  Alert,
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  View,
} from 'react-native';
import { TargetAudienceSelector } from '../../components/TargetAudienceSelector';
import { useAuth } from '../../components/auth-context';
import { AppHeader } from '../../components/common/AppHeader';
import { Palette, Radii, Shadows } from '../../constants/theme';
import { TargetAudience } from '../../data/collegeData';
import { QuestionMetadata } from '../../data/curriculumSchema';
import { ApiClient } from '../../services/api';
import { CollegeStore } from '../../services/collegeStore';
import { FacultySystemStore } from '../../services/facultyStore';

interface QuestionDraft {
  id: string;
  question: string;
  options: string[];
  correctAnswer: number;
  explanation: string;
  marks: number;
}

export default function CreateQuizScreen() {
  const { profile } = useAuth();
  const [section, setSection] = useState<'Engineering' | 'Competitive Exams'>('Engineering');
  const [subject, setSubject] = useState('Embedded Systems');
  const [topic, setTopic] = useState('Microcontrollers');
  const [subtopic, setSubtopic] = useState('NVIC & Timers');
  const [visibility, setVisibility] = useState<'college' | 'community'>('college');

  const [target, setTarget] = useState<TargetAudience>({
    targetType: 'SECTION',
    collegeId: profile.collegeId || 'clg-kvg',
    collegeName: profile.collegeName || 'KVG College of Engineering',
    department: profile.department || 'ECE',
    academicYear: '3rd Year',
    section: 'A',
  });

  // Quiz Meta
  const [quizName, setQuizName] = useState('');
  const [description, setDescription] = useState('');
  const [duration, setDuration] = useState('15');
  const [difficulty, setDifficulty] = useState<'easy' | 'medium' | 'hard'>('medium');
  const [negativeMarks, setNegativeMarks] = useState('0.5');
  const [passingScore, setPassingScore] = useState('60');

  const [isPublishing, setIsPublishing] = useState(false);
  const [publishedSuccessTitle, setPublishedSuccessTitle] = useState<string | null>(null);
  const [deletingId, setDeletingId] = useState<string | null>(null);
  const [publishedQuizzes, setPublishedQuizzes] = useState<any[]>([]);

  // Multiple Questions List
  const [questions, setQuestions] = useState<QuestionDraft[]>([
    {
      id: 'q-1',
      question: 'Which register in ARM Cortex-M enables atomic bit setting without read-modify-write?',
      options: ['ODR (Output Data Register)', 'BSRR (Bit Set/Reset Register)', 'IDR (Input Data Register)', 'MODER'],
      correctAnswer: 1,
      explanation: 'BSRR allows atomic pin setting in 1 CPU cycle, preventing race conditions.',
      marks: 2,
    },
    {
      id: 'q-2',
      question: 'What is the function of the SysTick timer in ARM Cortex-M?',
      options: [
        'Dedicated 24-bit downcounter used to generate periodic RTOS ticks',
        'High speed watchdog reset',
        'PWM audio DAC generator',
        'Flash memory programmer',
      ],
      correctAnswer: 0,
      explanation: 'SysTick is an integrated system timer calibrated for RTOS timebase generation.',
      marks: 2,
    },
  ]);

  const fetchPublishedQuizzes = async () => {
    try {
      const res = await ApiClient.getFacultyQuizzes();
      if (res?.success && Array.isArray(res.data)) {
        setPublishedQuizzes(res.data);
        return;
      }
    } catch (err) {
      console.log('Error loading faculty quizzes:', err);
    }
    setPublishedQuizzes(FacultySystemStore.getQuizzes());
  };

  useEffect(() => {
    fetchPublishedQuizzes();
    const unsub = FacultySystemStore.subscribe(() => {
      fetchPublishedQuizzes();
    });
    return unsub;
  }, []);

  const resetForm = () => {
    setPublishedSuccessTitle(null);
    setQuizName('');
    setDescription('');
    setTopic('Microcontrollers');
    setSubtopic('Architecture & Peripherals');
    setDuration('15');
    setDifficulty('medium');
    setNegativeMarks('0.5');
    setPassingScore('60');
    setQuestions([
      {
        id: `q-${Date.now()}-1`,
        question: '',
        options: ['', '', '', ''],
        correctAnswer: 0,
        explanation: '',
        marks: 2,
      },
      {
        id: `q-${Date.now()}-2`,
        question: '',
        options: ['', '', '', ''],
        correctAnswer: 0,
        explanation: '',
        marks: 2,
      },
    ]);
  };

  const handleAddQuestion = () => {
    const newQ: QuestionDraft = {
      id: `q-${Date.now()}`,
      question: '',
      options: ['', '', '', ''],
      correctAnswer: 0,
      explanation: '',
      marks: 2,
    };
    setQuestions([...questions, newQ]);
  };

  const handleUpdateQuestion = (index: number, field: keyof QuestionDraft, val: any) => {
    const updated = [...questions];
    updated[index] = { ...updated[index], [field]: val };
    setQuestions(updated);
  };

  const handleUpdateOption = (qIdx: number, optIdx: number, text: string) => {
    const updated = [...questions];
    const newOptions = [...updated[qIdx].options];
    newOptions[optIdx] = text;
    updated[qIdx].options = newOptions;
    setQuestions(updated);
  };

  const handleDeleteQuestion = (index: number) => {
    if (questions.length <= 1) {
      Alert.alert('Minimum Question Required', 'A quiz must contain at least 1 question.');
      return;
    }
    const updated = questions.filter((_, i) => i !== index);
    setQuestions(updated);
  };

  const handleDuplicateQuestion = (index: number) => {
    const target = questions[index];
    const duplicated: QuestionDraft = {
      ...target,
      id: `q-${Date.now()}`,
      question: `${target.question} (Copy)`,
      options: [...target.options],
    };
    const updated = [...questions];
    updated.splice(index + 1, 0, duplicated);
    setQuestions(updated);
  };

  const handlePublishQuiz = async () => {
    if (!quizName.trim() || !topic.trim()) {
      Alert.alert('Missing Fields', 'Please enter an Assessment / Quiz Title and Topic.');
      return;
    }

    const invalidQ = questions.find((q) => !q.question.trim() || q.options.some((o) => !o.trim()));
    if (invalidQ) {
      Alert.alert('Incomplete Questions', 'Please fill out all question statements and 4 options.');
      return;
    }

    setIsPublishing(true);
    const totalMarks = questions.reduce((sum, q) => sum + (q.marks || 2), 0);

    const convertedQuestions: QuestionMetadata[] = questions.map((q, idx) => ({
      id: `fac-q-${Date.now()}-${idx}`,
      section: section === 'Engineering' ? 'engineering' : 'competitive',
      category: 'subjects',
      subject,
      topic: topic.trim(),
      subtopic: subtopic.trim(),
      difficulty,
      questionType: 'mcq',
      question: q.question.trim(),
      options: q.options.map((o) => o.trim()),
      correctAnswer: q.correctAnswer,
      explanation: q.explanation.trim() || 'Verified by Faculty Educator.',
      marks: q.marks,
      negativeMarks: parseFloat(negativeMarks) || 0,
      isFacultyCreated: true,
      facultyName: profile.name || 'Dr. Ramesh Kumar',
    }));

    try {
      const targetDepts =
        target.targetType === 'ENTIRE_COLLEGE'
          ? ['All']
          : [target.department || profile.department || 'ECE'];
      const targetYears = target.academicYear ? [target.academicYear] : [];
      const targetSecs = target.section ? [target.section] : [];

      const payload = {
        title: quizName.trim(),
        description: description.trim() || 'Faculty curated multi-question assessment.',
        section: section === 'Engineering' ? 'engineering' : 'competitive',
        subject,
        topic: topic.trim(),
        subtopic: subtopic.trim() || undefined,
        difficulty: difficulty.toUpperCase(),
        duration_minutes: parseInt(duration, 10) || 15,
        total_marks: totalMarks,
        negative_marks: parseFloat(negativeMarks) || 0.25,
        visibility: (visibility || 'college').toLowerCase() as any,
        published: true,
        target_departments: targetDepts,
        target_years: targetYears,
        target_sections: targetSecs,
        questions: questions.map((q, idx) => ({
          section: section === 'Engineering' ? 'engineering' : 'competitive',
          subject,
          topic: topic.trim(),
          subtopic: subtopic.trim() || undefined,
          difficulty: difficulty.toUpperCase(),
          question_type: 'mcq',
          question_text: q.question.trim(),
          options: q.options.map((o) => o.trim()),
          correct_answer: q.correctAnswer,
          explanation: q.explanation.trim() || 'Verified by Faculty Educator.',
          marks: q.marks || 2,
          negative_marks: parseFloat(negativeMarks) || 0.25,
          order_index: idx,
        })),
      };

      const res = await ApiClient.createQuiz(payload);
      if (!res?.success) {
        throw new Error(res?.message || 'Failed to publish assessment to database.');
      }

      // Local store synchronization
      FacultySystemStore.addQuiz({
        section: section === 'Engineering' ? 'engineering' : 'competitive',
        subject,
        topic: topic.trim(),
        subtopic: subtopic.trim(),
        quizName: quizName.trim(),
        description: description.trim() || 'Faculty curated multi-question assessment.',
        durationMinutes: parseInt(duration, 10) || 15,
        difficulty,
        totalMarks,
        negativeMarks: parseFloat(negativeMarks) || 0,
        passingScore: parseInt(passingScore, 10) || 60,
        questions: convertedQuestions,
        published: true,
        facultyName: profile.name || 'Dr. Ramesh Kumar',
        facultyDesignation: profile.facultyDesignation || 'Associate Professor',
        facultyDepartment: profile.department || 'ECE Department',
        collegeId: profile.collegeId || '0f669a91-5c8d-4304-a815-818bde05e996',
        collegeName: profile.collegeName || 'KVG College of Engineering',
        isVerifiedFaculty: true,
        visibility,
      });

      const justPublishedTitle = quizName.trim();
      setPublishedSuccessTitle(justPublishedTitle);
      resetForm();
      await fetchPublishedQuizzes();

      Alert.alert(
        'Assessment Published & Uploaded! 🎯',
        `"${justPublishedTitle}" has been saved to the database and is live on the College Workspace for students.`,
        [
          {
            text: 'Create Another Assessment',
            onPress: () => {
              setPublishedSuccessTitle(null);
              resetForm();
            },
          },
          {
            text: 'View Dashboard',
            onPress: () => {
              router.replace('/faculty-dashboard' as any);
            },
          },
        ]
      );
    } catch (err: any) {
      console.log('Error publishing quiz to backend:', err);
      Alert.alert(
        'Publishing Error',
        err?.message || 'Could not publish assessment to the backend server. Please verify all questions and try again.'
      );
    } finally {
      setIsPublishing(false);
    }
  };

  const handleDeleteQuiz = async (id: string) => {
    setDeletingId(id);
    try {
      await ApiClient.deleteFacultyQuiz(id);
    } catch (err) {
      console.log('Error deleting quiz on backend:', err);
    }
    FacultySystemStore.deleteQuiz(id);
    await fetchPublishedQuizzes();
    setDeletingId(null);
  };

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader
        showBack
        onBack={() => router.replace('/faculty-dashboard' as any)}
        title="Create Assessment Quiz"
        subtitle="Author Multi-Question Assessments"
      />

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {/* Published Success Alert Card */}
        {publishedSuccessTitle && (
          <View style={styles.successBannerCard}>
            <View style={{ flexDirection: 'row', alignItems: 'center', gap: 12 }}>
              <View style={styles.successIconBox}>
                <Feather name="check" size={20} color="#FFFFFF" />
              </View>
              <View style={{ flex: 1 }}>
                <Text style={styles.successCardTitle}>Assessment Published Successfully! 🎯</Text>
                <Text style={styles.successCardSub}>
                  "{publishedSuccessTitle}" is now live for students in KVG College Workspace.
                </Text>
              </View>
            </View>
            <View style={styles.successBtnRow}>
              <TouchableOpacity
                style={styles.createAnotherPrimaryBtn}
                onPress={() => {
                  setPublishedSuccessTitle(null);
                  resetForm();
                }}
                activeOpacity={0.8}
              >
                <Feather name="plus-circle" size={16} color="#FFFFFF" />
                <Text style={styles.createAnotherPrimaryBtnText}>+ Create Another Assessment</Text>
              </TouchableOpacity>
              <TouchableOpacity
                style={styles.viewInWorkspaceBtn}
                onPress={() => router.replace('/my-college' as any)}
                activeOpacity={0.8}
              >
                <Feather name="external-link" size={15} color={Palette.primary} />
                <Text style={styles.viewInWorkspaceBtnText}>View in Student Workspace</Text>
              </TouchableOpacity>
            </View>
          </View>
        )}

        {/* Banner with Action Buttons */}
        <View style={styles.banner}>
          <Feather name="plus-circle" size={24} color={Palette.success} />
          <View style={{ flex: 1 }}>
            <Text style={styles.bannerTitle}>Multi-Question Quiz Builder</Text>
            <Text style={styles.bannerDesc}>Add 4-option MCQs with negative marking. Students take them directly in their College Workspace.</Text>
          </View>
          <TouchableOpacity style={styles.newDraftBtn} onPress={resetForm} activeOpacity={0.8}>
            <Feather name="plus" size={13} color="#FFFFFF" />
            <Text style={styles.newDraftBtnText}>Create Another Assessment</Text>
          </TouchableOpacity>
        </View>

        {/* 1. Quiz Settings Card */}
        <View style={styles.card}>
          <View style={styles.cardHeaderRow}>
            <Text style={styles.cardHeader}>1. Quiz Configuration & Details</Text>
            <TouchableOpacity style={styles.resetHeaderBtn} onPress={resetForm}>
              <Feather name="rotate-ccw" size={12} color={Palette.textSecondary} />
              <Text style={styles.resetHeaderBtnText}>Clear / New Draft</Text>
            </TouchableOpacity>
          </View>

          <View style={styles.inputGrid}>
            <View style={{ flex: 1 }}>
              <Text style={styles.label}>SECTION</Text>
              <TextInput style={styles.input} value={section} onChangeText={(t) => setSection(t as any)} />
            </View>
            <View style={{ flex: 1 }}>
              <Text style={styles.label}>SUBJECT</Text>
              <TextInput style={styles.input} value={subject} onChangeText={setSubject} />
            </View>
          </View>

          <View style={[styles.inputGrid, { marginTop: 10 }]}>
            <View style={{ flex: 1 }}>
              <Text style={styles.label}>TOPIC NAME *</Text>
              <TextInput style={styles.input} value={topic} onChangeText={setTopic} />
            </View>
            <View style={{ flex: 1 }}>
              <Text style={styles.label}>SUBTOPIC</Text>
              <TextInput style={styles.input} value={subtopic} onChangeText={setSubtopic} />
            </View>
          </View>

          <Text style={[styles.label, { marginTop: 12 }]}>QUIZ TITLE *</Text>
          <TextInput
            style={styles.input}
            placeholder="e.g. Unit 3: ARM Cortex-M Mastery Quiz"
            placeholderTextColor={Palette.textMuted}
            value={quizName}
            onChangeText={setQuizName}
          />

          <Text style={[styles.label, { marginTop: 12 }]}>QUIZ DESCRIPTION</Text>
          <TextInput
            style={[styles.input, { height: 50 }]}
            placeholder="Instructions for students..."
            placeholderTextColor={Palette.textMuted}
            multiline
            value={description}
            onChangeText={setDescription}
          />

          {/* Numerical Parameters Row */}
          <View style={[styles.inputGrid, { marginTop: 10 }]}>
            <View style={{ flex: 1 }}>
              <Text style={styles.label}>DURATION (MINS)</Text>
              <TextInput style={styles.input} keyboardType="numeric" value={duration} onChangeText={setDuration} />
            </View>
            <View style={{ flex: 1 }}>
              <Text style={styles.label}>NEGATIVE MARKS</Text>
              <TextInput style={styles.input} keyboardType="numeric" value={negativeMarks} onChangeText={setNegativeMarks} />
            </View>
            <View style={{ flex: 1 }}>
              <Text style={styles.label}>PASSING SCORE (%)</Text>
              <TextInput style={styles.input} keyboardType="numeric" value={passingScore} onChangeText={setPassingScore} />
            </View>
          </View>

          {/* Target Audience Delivery & Visibility */}
          <View style={{ marginTop: 14 }}>
            <TargetAudienceSelector
              visibility={visibility}
              onChangeVisibility={setVisibility}
              target={target}
              onChangeTarget={setTarget}
              collegeName={profile.collegeName || 'KVG College of Engineering'}
            />
          </View>
        </View>

        {/* 2. Questions List */}
        <View style={styles.sectionHeaderRow}>
          <Text style={styles.sectionTitle}>Questions Builder ({questions.length})</Text>
          <Text style={styles.sectionSubtitle}>Add, edit, duplicate, or delete questions</Text>
        </View>

        <View style={styles.questionsContainer}>
          {questions.map((q, qIdx) => (
            <View key={q.id} style={styles.qBlockCard}>
              <View style={styles.qBlockHeader}>
                <View style={styles.qIndexBadge}>
                  <Text style={styles.qIndexText}>QUESTION {qIdx + 1}</Text>
                </View>
                <View style={styles.qActionsRow}>
                  <TouchableOpacity onPress={() => handleDuplicateQuestion(qIdx)} style={styles.actionBtn}>
                    <Feather name="copy" size={15} color={Palette.primary} />
                  </TouchableOpacity>
                  <TouchableOpacity onPress={() => handleDeleteQuestion(qIdx)} style={styles.actionBtn}>
                    <Feather name="trash-2" size={15} color={Palette.danger} />
                  </TouchableOpacity>
                </View>
              </View>

              {/* Statement */}
              <Text style={styles.label}>QUESTION STATEMENT</Text>
              <TextInput
                style={[styles.input, styles.textArea]}
                placeholder="Type question statement..."
                placeholderTextColor={Palette.textMuted}
                multiline
                value={q.question}
                onChangeText={(t) => handleUpdateQuestion(qIdx, 'question', t)}
              />

              {/* 4 Options */}
              <Text style={[styles.label, { marginTop: 10 }]}>OPTIONS (SELECT RADIO FOR CORRECT ANSWER)</Text>
              {q.options.map((opt, optIdx) => (
                <View key={optIdx} style={styles.optRow}>
                  <TouchableOpacity
                    style={[styles.radio, q.correctAnswer === optIdx && styles.radioActive]}
                    onPress={() => handleUpdateQuestion(qIdx, 'correctAnswer', optIdx)}
                  >
                    {q.correctAnswer === optIdx && <View style={styles.radioDot} />}
                  </TouchableOpacity>
                  <TextInput
                    style={styles.optInput}
                    placeholder={`Option ${String.fromCharCode(65 + optIdx)}`}
                    placeholderTextColor={Palette.textMuted}
                    value={opt}
                    onChangeText={(t) => handleUpdateOption(qIdx, optIdx, t)}
                  />
                </View>
              ))}

              {/* Explanation */}
              <Text style={[styles.label, { marginTop: 10 }]}>EXPLANATION & SOLUTION</Text>
              <TextInput
                style={[styles.input, { height: 50 }]}
                placeholder="Why is this answer correct?"
                placeholderTextColor={Palette.textMuted}
                multiline
                value={q.explanation}
                onChangeText={(t) => handleUpdateQuestion(qIdx, 'explanation', t)}
              />
            </View>
          ))}
        </View>

        {/* Add Question Button */}
        <TouchableOpacity style={styles.addQBtn} onPress={handleAddQuestion} activeOpacity={0.8}>
          <Feather name="plus" size={18} color={Palette.primary} />
          <Text style={styles.addQBtnText}>Add Another Question</Text>
        </TouchableOpacity>

        {/* Final Actions */}
        <View style={styles.finalActionsRow}>
          <TouchableOpacity style={styles.draftBtn} onPress={resetForm} activeOpacity={0.8}>
            <Feather name="rotate-ccw" size={15} color={Palette.textSecondary} />
            <Text style={styles.draftBtnText}>Create Another Assessment</Text>
          </TouchableOpacity>

          <TouchableOpacity
            style={[styles.publishQuizBtn, isPublishing && { opacity: 0.7 }]}
            onPress={handlePublishQuiz}
            disabled={isPublishing}
            activeOpacity={0.85}
          >
            {isPublishing ? (
              <ActivityIndicator color="#FFFFFF" size="small" />
            ) : (
              <Feather name="check-circle" size={16} color="#FFFFFF" />
            )}
            <Text style={styles.publishQuizBtnText}>
              {isPublishing ? 'Uploading Assessment...' : `Publish Quiz (${questions.length} Qs)`}
            </Text>
          </TouchableOpacity>
        </View>

        {/* Active Published Assessments List */}
        <View style={[styles.sectionHeaderRow, { marginTop: 28 }]}>
          <Text style={styles.sectionTitle}>Active College Assessments ({publishedQuizzes.length})</Text>
          <Text style={styles.sectionSubtitle}>Assessments visible to students in KVG College Workspace</Text>
        </View>

        <View style={styles.publishedList}>
          {publishedQuizzes.length === 0 ? (
            <View style={styles.emptyCard}>
              <Feather name="check-circle" size={28} color={Palette.textMuted} />
              <Text style={styles.emptyCardText}>No assessments published yet.</Text>
            </View>
          ) : (
            publishedQuizzes.map((q) => (
              <View key={q.id} style={styles.publishedCard}>
                <View style={styles.publishedTop}>
                  <View style={styles.tag}>
                    <Text style={styles.tagText}>{q.subject} • {q.topic}</Text>
                  </View>
                  <TouchableOpacity
                    onPress={() => handleDeleteQuiz(q.id)}
                    disabled={deletingId === q.id}
                    style={styles.trashBtn}
                  >
                    {deletingId === q.id ? (
                      <ActivityIndicator size="small" color={Palette.danger} />
                    ) : (
                      <Feather name="trash-2" size={15} color={Palette.danger} />
                    )}
                  </TouchableOpacity>
                </View>

                <Text style={styles.publishedTitle}>{q.title || q.quizName}</Text>
                <Text style={styles.publishedDesc}>{q.description || 'Faculty assessment quiz'}</Text>
                <View style={styles.publishedMetaRow}>
                  <Text style={styles.publishedMeta}>
                    ⏱ {q.duration_minutes || q.durationMinutes || 15} Mins • 🎯 {q.total_marks || q.totalMarks || 20} Marks • ❓ {q.questions_count ?? q.questions?.length ?? 0} Questions
                  </Text>
                </View>
              </View>
            ))
          )}
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: Palette.background },
  scrollContent: { paddingHorizontal: 16, paddingTop: 16, paddingBottom: 40 },
  successBannerCard: {
    backgroundColor: '#F0FDF4',
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1.5,
    borderColor: '#86EFAC',
    marginBottom: 18,
    ...Shadows.card,
  },
  successIconBox: {
    width: 36,
    height: 36,
    borderRadius: 18,
    backgroundColor: Palette.success,
    alignItems: 'center',
    justifyContent: 'center',
  },
  successCardTitle: {
    fontSize: 16,
    fontWeight: '800',
    color: '#15803D',
  },
  successCardSub: {
    fontSize: 12.5,
    color: '#166534',
    marginTop: 3,
    lineHeight: 18,
  },
  successBtnRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 10,
    marginTop: 14,
    flexWrap: 'wrap',
  },
  createAnotherPrimaryBtn: {
    backgroundColor: Palette.primary,
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    paddingHorizontal: 14,
    paddingVertical: 9,
    borderRadius: Radii.button,
  },
  createAnotherPrimaryBtnText: {
    color: '#FFFFFF',
    fontWeight: '700',
    fontSize: 12.5,
  },
  viewInWorkspaceBtn: {
    backgroundColor: '#FFFFFF',
    borderWidth: 1,
    borderColor: Palette.primary,
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    paddingHorizontal: 14,
    paddingVertical: 8.5,
    borderRadius: Radii.button,
  },
  viewInWorkspaceBtnText: {
    color: Palette.primary,
    fontWeight: '700',
    fontSize: 12.5,
  },
  banner: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.successBorder,
    borderLeftWidth: 4,
    borderLeftColor: Palette.success,
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
    marginBottom: 18,
    ...Shadows.card,
  },
  bannerTitle: { fontSize: 15, fontWeight: '800', color: Palette.textTitle },
  bannerDesc: { fontSize: 12, color: Palette.textSecondary, marginTop: 2 },
  newDraftBtn: {
    backgroundColor: Palette.primary,
    paddingHorizontal: 10,
    paddingVertical: 7,
    borderRadius: Radii.button,
    flexDirection: 'row',
    alignItems: 'center',
    gap: 5,
  },
  newDraftBtnText: { color: '#FFFFFF', fontSize: 11.5, fontWeight: '700' },
  card: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 18,
    borderWidth: 1,
    borderColor: Palette.border,
    marginBottom: 20,
    ...Shadows.card,
  },
  cardHeaderRow: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 12 },
  cardHeader: { fontSize: 16, fontWeight: '800', color: Palette.textTitle },
  resetHeaderBtn: { flexDirection: 'row', alignItems: 'center', gap: 5, padding: 4 },
  resetHeaderBtnText: { fontSize: 11.5, fontWeight: '700', color: Palette.textSecondary },
  label: { fontSize: 10.5, fontWeight: '800', color: Palette.textTitle, letterSpacing: 0.6, marginBottom: 6 },
  inputGrid: { flexDirection: 'row', gap: 10 },
  input: {
    backgroundColor: Palette.backgroundSecondary,
    borderRadius: Radii.input,
    borderWidth: 1,
    borderColor: Palette.border,
    padding: 10,
    fontSize: 13,
    color: Palette.textTitle,
  },
  textArea: { height: 60, textAlignVertical: 'top' },
  sectionHeaderRow: { marginBottom: 12 },
  sectionTitle: { fontSize: 17, fontWeight: '800', color: Palette.textTitle },
  sectionSubtitle: { fontSize: 12, color: Palette.textSecondary, marginTop: 2 },
  questionsContainer: { gap: 14, marginBottom: 16 },
  qBlockCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  qBlockHeader: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 10 },
  qIndexBadge: { backgroundColor: Palette.primaryLight, paddingHorizontal: 8, paddingVertical: 3, borderRadius: 6 },
  qIndexText: { fontSize: 11, fontWeight: '800', color: Palette.primary },
  qActionsRow: { flexDirection: 'row', gap: 12 },
  actionBtn: { padding: 4 },
  optRow: { flexDirection: 'row', alignItems: 'center', gap: 10, marginBottom: 8 },
  radio: { width: 22, height: 22, borderRadius: 11, borderWidth: 2, borderColor: Palette.border, alignItems: 'center', justifyContent: 'center' },
  radioActive: { borderColor: Palette.primary },
  radioDot: { width: 10, height: 10, borderRadius: 5, backgroundColor: Palette.primary },
  optInput: { flex: 1, backgroundColor: Palette.backgroundSecondary, borderRadius: Radii.input, borderWidth: 1, borderColor: Palette.border, paddingHorizontal: 10, paddingVertical: 8, fontSize: 13, color: Palette.textTitle },
  addQBtn: {
    backgroundColor: Palette.primaryLight,
    borderRadius: Radii.button,
    paddingVertical: 13,
    borderWidth: 1,
    borderColor: Palette.primaryBorder,
    borderStyle: 'dashed',
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 6,
    marginBottom: 20,
  },
  addQBtnText: { fontSize: 14, fontWeight: '700', color: Palette.primary },
  finalActionsRow: { flexDirection: 'row', gap: 10 },
  draftBtn: { flex: 1, backgroundColor: Palette.backgroundSecondary, borderWidth: 1, borderColor: Palette.border, borderRadius: Radii.button, paddingVertical: 13, flexDirection: 'row', alignItems: 'center', justifyContent: 'center', gap: 6 },
  draftBtnText: { fontSize: 13, fontWeight: '700', color: Palette.textSecondary },
  publishQuizBtn: { flex: 1.5, backgroundColor: Palette.primary, borderRadius: Radii.button, paddingVertical: 13, flexDirection: 'row', alignItems: 'center', justifyContent: 'center', gap: 8, ...Shadows.button },
  publishQuizBtnText: { color: '#FFFFFF', fontSize: 14.5, fontWeight: '700' },
  publishedList: { gap: 12 },
  emptyCard: { backgroundColor: '#FFFFFF', borderRadius: Radii.card, padding: 24, alignItems: 'center', gap: 8, borderWidth: 1, borderColor: Palette.border },
  emptyCardText: { color: Palette.textMuted, fontSize: 13 },
  publishedCard: { backgroundColor: '#FFFFFF', borderRadius: Radii.card, padding: 14, borderWidth: 1, borderColor: Palette.border, ...Shadows.card },
  publishedTop: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 8 },
  tag: { backgroundColor: Palette.primaryLight, paddingHorizontal: 8, paddingVertical: 3, borderRadius: 6 },
  tagText: { fontSize: 11, fontWeight: '700', color: Palette.primary },
  trashBtn: { padding: 4 },
  publishedTitle: { fontSize: 15, fontWeight: '800', color: Palette.textTitle, marginBottom: 4 },
  publishedDesc: { fontSize: 12.5, color: Palette.textSecondary, marginBottom: 8 },
  publishedMetaRow: { flexDirection: 'row', alignItems: 'center' },
  publishedMeta: { fontSize: 11.5, color: Palette.textMuted, fontWeight: '600' },
});
