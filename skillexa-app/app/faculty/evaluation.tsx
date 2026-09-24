import { Feather } from '@expo/vector-icons';
import { router, useLocalSearchParams } from 'expo-router';
import React, { useState } from 'react';
import {
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
import { AppHeader } from '../../components/common/AppHeader';
import { Palette, Radii, Shadows } from '../../constants/theme';
import { FacultySystemStore } from '../../services/facultyStore';

export default function InterviewEvaluationScreen() {
  const {
    interviewId = 'int-1',
    studentName = 'Ganesh Sharan',
    role = 'Embedded Systems Engineer',
  } = useLocalSearchParams<{
    interviewId: string;
    studentName: string;
    role: string;
  }>();

  const [techScore, setTechScore] = useState('85');
  const [commScore, setCommScore] = useState('88');
  const [confScore, setConfScore] = useState('80');
  const [probScore, setProbScore] = useState('82');
  const [overallScore, setOverallScore] = useState('84');

  const [strengths, setStrengths] = useState(
    'Strong grasp of ARM Cortex-M NVIC register structures and atomic bit-banding operations.'
  );
  const [weaknesses, setWeaknesses] = useState(
    'Could provide deeper elaboration on RTOS priority inversion resolution algorithms.'
  );
  const [suggestions, setSuggestions] = useState(
    'Practice more hands-on FreeRTOS mutex inheritance labs and low-power sleep modes.'
  );
  const [summary, setSummary] = useState(
    'Recommended for Advance Embedded Firmware Placement rounds. Solid candidate.'
  );

  const handlePublishEvaluation = () => {
    FacultySystemStore.evaluateInterview(interviewId, {
      status: 'Completed',
      scores: {
        technical: parseInt(techScore, 10) || 85,
        communication: parseInt(commScore, 10) || 85,
        confidence: parseInt(confScore, 10) || 80,
        problemSolving: parseInt(probScore, 10) || 80,
        overall: parseInt(overallScore, 10) || 84,
      },
      feedback: {
        strengths: strengths.split('\n').filter((s) => s.trim()),
        weaknesses: weaknesses.split('\n').filter((w) => w.trim()),
        suggestions: suggestions.split('\n').filter((s) => s.trim()),
        overallSummary: summary.trim(),
      },
    });

    Alert.alert(
      'Evaluation Published!',
      `Interview scorecard published for ${studentName}. The student can now view their evaluation feedback.`,
      [{ text: 'Return to Dashboard', onPress: () => router.replace('/faculty-dashboard') }]
    );
  };

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader showBack title="Interview Evaluation & Rubric" subtitle={`Candidate: ${studentName}`} />

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {/* Candidate Info Card */}
        <View style={styles.candidateCard}>
          <View style={styles.avatarCircle}>
            <Text style={styles.avatarText}>{studentName.charAt(0)}</Text>
          </View>
          <View style={{ flex: 1 }}>
            <Text style={styles.candidateName}>{studentName}</Text>
            <Text style={styles.candidateRole}>{role} • Technical Evaluation</Text>
            <Text style={styles.dateText}>Evaluated on {new Date().toISOString().split('T')[0]}</Text>
          </View>
        </View>

        {/* 1. Numerical Rubric Scores */}
        <View style={styles.card}>
          <Text style={styles.cardTitle}>1. Performance Rubric Scores (/100)</Text>

          <View style={styles.scoreInputRow}>
            <View style={styles.scoreCol}>
              <Text style={styles.scoreLabel}>TECHNICAL KNOWLEDGE</Text>
              <TextInput
                style={styles.scoreInput}
                keyboardType="numeric"
                value={techScore}
                onChangeText={setTechScore}
              />
            </View>

            <View style={styles.scoreCol}>
              <Text style={styles.scoreLabel}>COMMUNICATION</Text>
              <TextInput
                style={styles.scoreInput}
                keyboardType="numeric"
                value={commScore}
                onChangeText={setCommScore}
              />
            </View>
          </View>

          <View style={[styles.scoreInputRow, { marginTop: 10 }]}>
            <View style={styles.scoreCol}>
              <Text style={styles.scoreLabel}>CONFIDENCE & TONE</Text>
              <TextInput
                style={styles.scoreInput}
                keyboardType="numeric"
                value={confScore}
                onChangeText={setConfScore}
              />
            </View>

            <View style={styles.scoreCol}>
              <Text style={styles.scoreLabel}>PROBLEM SOLVING</Text>
              <TextInput
                style={styles.scoreInput}
                keyboardType="numeric"
                value={probScore}
                onChangeText={setProbScore}
              />
            </View>
          </View>

          <View style={[styles.scoreInputRow, { marginTop: 10 }]}>
            <View style={[styles.scoreCol, { width: '100%' }]}>
              <Text style={[styles.scoreLabel, { color: Palette.primary }]}>OVERALL COMPOSITE SCORE</Text>
              <TextInput
                style={[styles.scoreInput, styles.overallInput]}
                keyboardType="numeric"
                value={overallScore}
                onChangeText={setOverallScore}
              />
            </View>
          </View>
        </View>

        {/* 2. Qualitative Feedback */}
        <View style={styles.card}>
          <Text style={styles.cardTitle}>2. Qualitative Insights & Recommendations</Text>

          <Text style={styles.fieldLabel}>KEY STRENGTHS</Text>
          <TextInput
            style={[styles.textArea, { height: 60 }]}
            placeholder="Highlight what the candidate answered well..."
            placeholderTextColor={Palette.textMuted}
            multiline
            value={strengths}
            onChangeText={setStrengths}
          />

          <Text style={[styles.fieldLabel, { marginTop: 12 }]}>AREAS FOR IMPROVEMENT</Text>
          <TextInput
            style={[styles.textArea, { height: 60 }]}
            placeholder="Identify weak conceptual areas..."
            placeholderTextColor={Palette.textMuted}
            multiline
            value={weaknesses}
            onChangeText={setWeaknesses}
          />

          <Text style={[styles.fieldLabel, { marginTop: 12 }]}>ACTIONABLE STUDY SUGGESTIONS</Text>
          <TextInput
            style={[styles.textArea, { height: 60 }]}
            placeholder="What should the student study next?"
            placeholderTextColor={Palette.textMuted}
            multiline
            value={suggestions}
            onChangeText={setSuggestions}
          />

          <Text style={[styles.fieldLabel, { marginTop: 12 }]}>FACULTY SUMMARY VERDICT</Text>
          <TextInput
            style={[styles.textArea, { height: 50 }]}
            placeholder="Final recommendation summary..."
            placeholderTextColor={Palette.textMuted}
            multiline
            value={summary}
            onChangeText={setSummary}
          />
        </View>

        {/* Publish Action */}
        <TouchableOpacity style={styles.publishBtn} onPress={handlePublishEvaluation} activeOpacity={0.85}>
          <Feather name="check-circle" size={16} color="#FFFFFF" />
          <Text style={styles.publishBtnText}>Publish Evaluation to Student</Text>
        </TouchableOpacity>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: Palette.background },
  scrollContent: { paddingHorizontal: 16, paddingTop: 16, paddingBottom: 40 },
  candidateCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.border,
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
    marginBottom: 16,
    ...Shadows.card,
  },
  avatarCircle: { width: 44, height: 44, borderRadius: 22, backgroundColor: Palette.primaryLight, alignItems: 'center', justifyContent: 'center' },
  avatarText: { fontSize: 18, fontWeight: '800', color: Palette.primary },
  candidateName: { fontSize: 16, fontWeight: '800', color: Palette.textTitle },
  candidateRole: { fontSize: 12.5, color: Palette.textSecondary, marginTop: 1 },
  dateText: { fontSize: 11, color: Palette.textMuted, marginTop: 2 },
  card: { backgroundColor: '#FFFFFF', borderRadius: Radii.card, padding: 16, borderWidth: 1, borderColor: Palette.border, marginBottom: 16, ...Shadows.card },
  cardTitle: { fontSize: 15, fontWeight: '800', color: Palette.textTitle, marginBottom: 12 },
  scoreInputRow: { flexDirection: 'row', gap: 10 },
  scoreCol: { flex: 1 },
  scoreLabel: { fontSize: 9.5, fontWeight: '800', color: Palette.textTitle, letterSpacing: 0.6, marginBottom: 4 },
  scoreInput: {
    backgroundColor: Palette.backgroundSecondary,
    borderRadius: Radii.input,
    borderWidth: 1,
    borderColor: Palette.border,
    padding: 10,
    fontSize: 15,
    fontWeight: '800',
    color: Palette.textTitle,
    textAlign: 'center',
  },
  overallInput: { backgroundColor: Palette.primaryLight, borderColor: Palette.primary, color: Palette.primary },
  fieldLabel: { fontSize: 10.5, fontWeight: '800', color: Palette.textTitle, letterSpacing: 0.6, marginBottom: 4 },
  textArea: {
    backgroundColor: Palette.backgroundSecondary,
    borderRadius: Radii.input,
    borderWidth: 1,
    borderColor: Palette.border,
    padding: 10,
    fontSize: 12.5,
    color: Palette.textBody,
    textAlignVertical: 'top',
  },
  publishBtn: {
    backgroundColor: Palette.primary,
    borderRadius: Radii.button,
    paddingVertical: 14,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
    marginTop: 4,
    ...Shadows.button,
  },
  publishBtnText: { color: '#FFFFFF', fontSize: 14.5, fontWeight: '700' },
});
