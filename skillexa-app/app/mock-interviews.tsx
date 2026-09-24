import { Feather } from '@expo/vector-icons';
import React, { useState } from 'react';
import {
  ActivityIndicator,
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
import { ProgressBar } from '../components/common/EducationalCards';
import { Palette, Radii, Shadows } from '../constants/theme';

const INTERVIEW_TYPES = [
  { id: 'hr', title: 'HR Interview', desc: 'Behavioral, leadership, and culture fit' },
  { id: 'technical', title: 'Technical Interview', desc: 'System design, core CS, and architecture' },
  { id: 'coding', title: 'Coding Interview', desc: 'DSA, algorithmic complexity, and edge cases' },
  { id: 'general', title: 'General Interview', desc: 'Comprehensive placement simulation' },
  { id: 'custom', title: 'Custom Interview', desc: 'Tailored for specialized engineering domains' },
];

const TARGET_ROLES = [
  'Software Developer',
  'Frontend Engineer',
  'Backend Engineer',
  'Full Stack Developer',
  'Embedded & IoT Engineer',
];

interface ConversationTurn {
  id: number;
  question: string;
  userAnswer?: string;
  feedback?: string;
}

export default function MockInterviewsPage() {
  const [sessionActive, setSessionActive] = useState(false);
  const [selectedType, setSelectedType] = useState('technical');
  const [selectedRole, setSelectedRole] = useState('Software Developer');
  const [customGoal, setCustomGoal] = useState('');

  // Conversation State
  const [turnIndex, setTurnIndex] = useState(0);
  const [currentInput, setCurrentInput] = useState('');
  const [isProcessing, setIsProcessing] = useState(false);
  const [history, setHistory] = useState<ConversationTurn[]>([]);
  const [interviewFinished, setInterviewFinished] = useState(false);

  // Dynamic Interview Engine
  const startSession = () => {
    setSessionActive(true);
    setInterviewFinished(false);
    setTurnIndex(0);
    setCurrentInput('');

    let initialQ = 'Welcome to your SkillExa Mock Interview. To start, walk me through your engineering background and your most technically challenging project.';
    if (selectedType === 'hr') {
      initialQ = 'Tell me about a time when you faced a strict project deadline and had to handle conflicting priorities with your team.';
    } else if (selectedType === 'coding') {
      initialQ = 'Given an array of integers, how would you design an algorithm to find the maximum subarray sum in linear time? Walk me through your intuition.';
    } else if (selectedType === 'general') {
      initialQ = 'Introduce yourself, your key technical competencies, and why you are interested in this software development role.';
    }

    setHistory([{ id: 1, question: initialQ }]);
  };

  const handleSendAnswer = () => {
    if (!currentInput.trim()) return;

    const currentAnswer = currentInput.trim();
    setIsProcessing(true);

    setTimeout(() => {
      setIsProcessing(false);

      const updatedHistory = [...history];
      updatedHistory[turnIndex].userAnswer = currentAnswer;

      if (turnIndex === 0) {
        // Dynamic follow-up 1 based on user answer
        let nextQ = `You mentioned your technical choices. How did you measure performance, and what trade-offs did you make in your architecture?`;
        if (selectedType === 'hr') {
          nextQ = 'How did that experience change the way you communicate with stakeholders during unexpected delays?';
        } else if (selectedType === 'coding') {
          nextQ = 'What are the space complexity constraints of that approach, and how would you handle negative numbers or empty inputs?';
        }
        updatedHistory.push({ id: 2, question: nextQ });
        setHistory(updatedHistory);
        setTurnIndex(1);
        setCurrentInput('');
      } else if (turnIndex === 1) {
        // Dynamic follow-up 2
        let nextQ = `Excellent. Final scenario: Suppose your service experiences a sudden 10x traffic spike with 500 error spikes. What is your systematic debugging protocol?`;
        if (selectedType === 'hr') {
          nextQ = 'Where do you see your career progression in the next 2-3 years within our engineering organization?';
        } else if (selectedType === 'coding') {
          nextQ = 'How would you scale this algorithm across a distributed cluster when the dataset exceeds RAM capacity?';
        }
        updatedHistory.push({ id: 3, question: nextQ });
        setHistory(updatedHistory);
        setTurnIndex(2);
        setCurrentInput('');
      } else {
        // Interview Completed
        setHistory(updatedHistory);
        setInterviewFinished(true);
      }
    }, 900);
  };

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader showBack title="AI Mock Interview" subtitle="Real-Time Conversational Simulator" />

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {!sessionActive ? (
          /* Step 1: Configuration Hub */
          <View>
            {/* AI Banner */}
            <View style={styles.heroCard}>
              <View style={styles.heroIconBox}>
                <Feather name="cpu" size={24} color={Palette.aiPurple} />
              </View>
              <View style={styles.heroTextCol}>
                <View style={styles.aiBadge}>
                  <Text style={styles.aiBadgeText}>AI CONVERSATIONAL EVALUATION</Text>
                </View>
                <Text style={styles.heroTitle}>Simulate Real Placement Interviews</Text>
                <Text style={styles.heroDesc}>
                  Practice multi-turn technical & HR panels with dynamic follow-ups and comprehensive rubric scoring.
                </Text>
              </View>
            </View>

            {/* Select Interview Type */}
            <View style={styles.configCard}>
              <Text style={styles.configLabel}>1. SELECT INTERVIEW TYPE</Text>
              <View style={styles.typesGrid}>
                {INTERVIEW_TYPES.map((t) => (
                  <TouchableOpacity
                    key={t.id}
                    style={[styles.typeCard, selectedType === t.id && styles.typeCardActive]}
                    onPress={() => setSelectedType(t.id)}
                    activeOpacity={0.8}
                  >
                    <View style={styles.typeCardTop}>
                      <Text style={[styles.typeTitle, selectedType === t.id && styles.typeTitleActive]}>{t.title}</Text>
                      {selectedType === t.id && <Feather name="check-circle" size={16} color={Palette.aiPurple} />}
                    </View>
                    <Text style={styles.typeDesc}>{t.desc}</Text>
                  </TouchableOpacity>
                ))}
              </View>

              {/* Select Role */}
              <Text style={[styles.configLabel, { marginTop: 18 }]}>2. SELECT TARGET ROLE</Text>
              <View style={styles.rolesRow}>
                {TARGET_ROLES.map((r) => (
                  <TouchableOpacity
                    key={r}
                    style={[styles.roleChip, selectedRole === r && styles.roleChipActive]}
                    onPress={() => setSelectedRole(r)}
                  >
                    <Text style={[styles.roleText, selectedRole === r && styles.roleTextActive]}>{r}</Text>
                  </TouchableOpacity>
                ))}
              </View>

              {selectedType === 'custom' && (
                <View style={{ marginTop: 14 }}>
                  <Text style={styles.configLabel}>CUSTOM INTERVIEW SPECIFICATIONS</Text>
                  <TextInput
                    style={styles.customInput}
                    placeholder="e.g. Focus on Spring Boot Microservices and Kafka"
                    placeholderTextColor={Palette.textMuted}
                    value={customGoal}
                    onChangeText={setCustomGoal}
                  />
                </View>
              )}

              <TouchableOpacity style={styles.startBtn} onPress={startSession} activeOpacity={0.85}>
                <Text style={styles.startBtnText}>Start Live Mock Interview</Text>
                <Feather name="arrow-right" size={16} color="#FFFFFF" />
              </TouchableOpacity>
            </View>
          </View>
        ) : !interviewFinished ? (
          /* Step 2: Live Multi-Turn Interview Session */
          <View>
            <View style={styles.sessionHeader}>
              <View style={styles.liveIndicator}>
                <View style={styles.liveDot} />
                <Text style={styles.liveLabel}>INTERVIEW IN PROGRESS • TURN {turnIndex + 1} OF 3</Text>
              </View>
              <TouchableOpacity onPress={() => setSessionActive(false)}>
                <Text style={styles.exitBtnText}>End Session</Text>
              </TouchableOpacity>
            </View>

            {/* Conversation Flow */}
            <View style={styles.conversationList}>
              {history.map((turn, i) => (
                <View key={turn.id} style={styles.turnBlock}>
                  {/* AI Question Box */}
                  <View style={styles.aiBubble}>
                    <View style={styles.aiBubbleHeader}>
                      <Feather name="cpu" size={14} color={Palette.aiPurple} />
                      <Text style={styles.aiBubbleName}>SkillExa AI Panelist</Text>
                    </View>
                    <Text style={styles.aiQuestionText}>{turn.question}</Text>
                  </View>

                  {/* Student Answer If submitted */}
                  {turn.userAnswer && (
                    <View style={styles.userBubble}>
                      <Text style={styles.userBubbleLabel}>Your Response:</Text>
                      <Text style={styles.userAnswerText}>{turn.userAnswer}</Text>
                    </View>
                  )}
                </View>
              ))}
            </View>

            {/* Active Input Box */}
            <View style={styles.inputAreaCard}>
              <View style={styles.inputAreaTop}>
                <Text style={styles.inputAreaLabel}>YOUR ANSWER</Text>
                <TouchableOpacity
                  style={styles.voiceHelper}
                  onPress={() =>
                    setCurrentInput(
                      'In my previous project, I architected a modular React Native client and implemented Redis caching to lower response latency by 35%.'
                    )
                  }
                >
                  <Feather name="mic" size={13} color={Palette.aiPurple} />
                  <Text style={styles.voiceHelperText}>Voice Assist</Text>
                </TouchableOpacity>
              </View>

              <TextInput
                style={styles.answerTextInput}
                placeholder="Structure your answer with situation, approach, technologies, and measurable results..."
                placeholderTextColor={Palette.textMuted}
                multiline
                value={currentInput}
                onChangeText={setCurrentInput}
              />

              <TouchableOpacity
                style={styles.submitAnswerBtn}
                onPress={handleSendAnswer}
                disabled={isProcessing}
                activeOpacity={0.85}
              >
                {isProcessing ? (
                  <ActivityIndicator size="small" color="#FFFFFF" />
                ) : (
                  <>
                    <Text style={styles.submitBtnText}>
                      {turnIndex === 2 ? 'Submit Final Response' : 'Submit & Hear Follow-Up'}
                    </Text>
                    <Feather name="send" size={15} color="#FFFFFF" />
                  </>
                )}
              </TouchableOpacity>
            </View>
          </View>
        ) : (
          /* Step 3: Final Comprehensive Scorecard */
          <View style={styles.scorecardContainer}>
            <View style={styles.scorecardHero}>
              <View style={styles.scoreCircle}>
                <Text style={styles.scoreNum}>84</Text>
                <Text style={styles.scoreTotal}>/ 100</Text>
              </View>
              <Text style={styles.scoreHeroTitle}>Placement Interview Assessment</Text>
              <Text style={styles.scoreHeroSub}>{selectedRole} • Strong Candidate</Text>
            </View>

            {/* Category Rubric */}
            <View style={styles.rubricCard}>
              <Text style={styles.rubricCardTitle}>Performance Category Breakdown</Text>
              
              <View style={styles.rubricRow}>
                <Text style={styles.rubricName}>Communication & Clarity</Text>
                <Text style={styles.rubricVal}>88%</Text>
              </View>
              <ProgressBar progress={0.88} color={Palette.success} />

              <View style={[styles.rubricRow, { marginTop: 12 }]}>
                <Text style={styles.rubricName}>Technical Knowledge & Accuracy</Text>
                <Text style={styles.rubricVal}>82%</Text>
              </View>
              <ProgressBar progress={0.82} color={Palette.primary} />

              <View style={[styles.rubricRow, { marginTop: 12 }]}>
                <Text style={styles.rubricName}>Confidence & Tone</Text>
                <Text style={styles.rubricVal}>85%</Text>
              </View>
              <ProgressBar progress={0.85} color={Palette.aiPurple} />

              <View style={[styles.rubricRow, { marginTop: 12 }]}>
                <Text style={styles.rubricName}>Answer Depth & Relevance</Text>
                <Text style={styles.rubricVal}>80%</Text>
              </View>
              <ProgressBar progress={0.80} color={Palette.warning} />
            </View>

            {/* Strengths & Weaknesses */}
            <View style={styles.insightsCard}>
              <Text style={styles.insightHeader}>Key Strengths:</Text>
              <Text style={styles.insightText}>• Clear structural presentation using Situation-Task-Action-Result format.</Text>
              <Text style={styles.insightText}>• Highlighted quantifiable performance metrics and throughput wins.</Text>

              <Text style={[styles.insightHeader, { marginTop: 12 }]}>Areas for Improvement:</Text>
              <Text style={styles.insightText}>• Elaborate on automated testing and edge-case rollback strategies.</Text>
            </View>

            {/* Recommended Topics */}
            <View style={styles.recTopicsCard}>
              <View style={styles.recHeaderRow}>
                <Feather name="book-open" size={16} color={Palette.primary} />
                <Text style={styles.recTitle}>Recommended Study Focus:</Text>
              </View>
              <Text style={styles.recItem}>• High-scale Distributed Systems & Caching (Redis/Kafka)</Text>
              <Text style={styles.recItem}>• Dynamic Programming & Subarray Optimization in Python/C</Text>
            </View>

            {/* Action Buttons */}
            <View style={styles.scoreActions}>
              <TouchableOpacity style={styles.retryInterviewBtn} onPress={startSession} activeOpacity={0.85}>
                <Feather name="refresh-cw" size={15} color="#FFFFFF" />
                <Text style={styles.retryBtnText}>Try Again</Text>
              </TouchableOpacity>

              <TouchableOpacity style={styles.newInterviewBtn} onPress={() => setSessionActive(false)} activeOpacity={0.8}>
                <Text style={styles.newInterviewText}>Start New Interview</Text>
              </TouchableOpacity>
            </View>
          </View>
        )}
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: Palette.background },
  scrollContent: { paddingHorizontal: 16, paddingTop: 16, paddingBottom: 40 },
  heroCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 18,
    borderWidth: 1,
    borderColor: Palette.aiPurpleBorder,
    borderLeftWidth: 4,
    borderLeftColor: Palette.aiPurple,
    flexDirection: 'row',
    alignItems: 'flex-start',
    marginBottom: 18,
    ...Shadows.card,
  },
  heroIconBox: { width: 44, height: 44, borderRadius: 12, backgroundColor: Palette.aiPurpleLight, alignItems: 'center', justifyContent: 'center', marginRight: 12 },
  heroTextCol: { flex: 1 },
  aiBadge: { alignSelf: 'flex-start', backgroundColor: Palette.aiPurpleLight, paddingHorizontal: 8, paddingVertical: 3, borderRadius: 6, marginBottom: 6 },
  aiBadgeText: { fontSize: 10, fontWeight: '800', color: Palette.aiPurple, letterSpacing: 0.6 },
  heroTitle: { fontSize: 16, fontWeight: '800', color: Palette.textTitle, marginBottom: 4 },
  heroDesc: { fontSize: 12.5, color: Palette.textBody, lineHeight: 18 },
  configCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 18,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  configLabel: { fontSize: 11, fontWeight: '800', color: Palette.textTitle, letterSpacing: 0.6, marginBottom: 8 },
  typesGrid: { gap: 8, marginBottom: 14 },
  typeCard: {
    backgroundColor: Palette.backgroundSecondary,
    borderRadius: Radii.card,
    padding: 12,
    borderWidth: 1,
    borderColor: Palette.border,
  },
  typeCardActive: { backgroundColor: Palette.aiPurpleLight, borderColor: Palette.aiPurple },
  typeCardTop: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 2 },
  typeTitle: { fontSize: 14, fontWeight: '700', color: Palette.textTitle },
  typeTitleActive: { color: Palette.aiPurple },
  typeDesc: { fontSize: 11.5, color: Palette.textSecondary },
  rolesRow: { flexDirection: 'row', flexWrap: 'wrap', gap: 8 },
  roleChip: {
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: Radii.pill,
    backgroundColor: Palette.backgroundSecondary,
    borderWidth: 1,
    borderColor: Palette.border,
  },
  roleChipActive: { backgroundColor: Palette.aiPurpleLight, borderColor: Palette.aiPurple },
  roleText: { fontSize: 12, fontWeight: '600', color: Palette.textSecondary },
  roleTextActive: { color: Palette.aiPurple, fontWeight: '700' },
  customInput: {
    backgroundColor: Palette.backgroundSecondary,
    borderRadius: Radii.input,
    borderWidth: 1,
    borderColor: Palette.border,
    padding: 10,
    fontSize: 13,
    color: Palette.textTitle,
  },
  startBtn: {
    backgroundColor: Palette.aiPurple,
    borderRadius: Radii.button,
    paddingVertical: 13,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
    marginTop: 20,
    ...Shadows.button,
  },
  startBtnText: { color: '#FFFFFF', fontSize: 14.5, fontWeight: '700' },
  sessionHeader: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 14 },
  liveIndicator: { flexDirection: 'row', alignItems: 'center', gap: 6 },
  liveDot: { width: 8, height: 8, borderRadius: 4, backgroundColor: Palette.success },
  liveLabel: { fontSize: 10.5, fontWeight: '800', color: Palette.success, letterSpacing: 0.8 },
  exitBtnText: { fontSize: 12, fontWeight: '600', color: Palette.danger },
  conversationList: { gap: 14, marginBottom: 16 },
  turnBlock: { gap: 8 },
  aiBubble: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.aiPurpleBorder,
    borderLeftWidth: 4,
    borderLeftColor: Palette.aiPurple,
    ...Shadows.card,
  },
  aiBubbleHeader: { flexDirection: 'row', alignItems: 'center', gap: 6, marginBottom: 6 },
  aiBubbleName: { fontSize: 12, fontWeight: '700', color: Palette.aiPurple },
  aiQuestionText: { fontSize: 14.5, fontWeight: '600', color: Palette.textTitle, lineHeight: 22 },
  userBubble: {
    alignSelf: 'flex-end',
    backgroundColor: Palette.primaryLight,
    borderRadius: Radii.card,
    padding: 14,
    maxWidth: '90%',
    borderWidth: 1,
    borderColor: Palette.primaryBorder,
  },
  userBubbleLabel: { fontSize: 10.5, fontWeight: '800', color: Palette.primary, marginBottom: 2 },
  userAnswerText: { fontSize: 13.5, color: Palette.textTitle, lineHeight: 19 },
  inputAreaCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  inputAreaTop: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 8 },
  inputAreaLabel: { fontSize: 11, fontWeight: '800', color: Palette.textTitle, letterSpacing: 0.6 },
  voiceHelper: { flexDirection: 'row', alignItems: 'center', gap: 4, backgroundColor: Palette.aiPurpleLight, paddingHorizontal: 8, paddingVertical: 4, borderRadius: 6 },
  voiceHelperText: { fontSize: 11, fontWeight: '700', color: Palette.aiPurple },
  answerTextInput: {
    height: 100,
    backgroundColor: Palette.backgroundSecondary,
    borderRadius: Radii.input,
    borderWidth: 1,
    borderColor: Palette.border,
    padding: 12,
    fontSize: 13.5,
    color: Palette.textTitle,
    textAlignVertical: 'top',
    marginBottom: 12,
  },
  submitAnswerBtn: {
    backgroundColor: Palette.aiPurple,
    borderRadius: Radii.button,
    paddingVertical: 12,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
  },
  submitBtnText: { color: '#FFFFFF', fontSize: 14, fontWeight: '700' },
  scorecardContainer: { gap: 16 },
  scorecardHero: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.cardLarge,
    padding: 22,
    borderWidth: 1,
    borderColor: Palette.border,
    alignItems: 'center',
    ...Shadows.card,
  },
  scoreCircle: { width: 76, height: 76, borderRadius: 38, backgroundColor: Palette.aiPurpleLight, alignItems: 'center', justifyContent: 'center', marginBottom: 10 },
  scoreNum: { fontSize: 28, fontWeight: '900', color: Palette.aiPurple },
  scoreTotal: { fontSize: 11, fontWeight: '700', color: Palette.aiPurple },
  scoreHeroTitle: { fontSize: 18, fontWeight: '800', color: Palette.textTitle },
  scoreHeroSub: { fontSize: 13, color: Palette.textSecondary, marginTop: 2 },
  rubricCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 18,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  rubricCardTitle: { fontSize: 15, fontWeight: '800', color: Palette.textTitle, marginBottom: 14 },
  rubricRow: { flexDirection: 'row', justifyContent: 'space-between', marginBottom: 6 },
  rubricName: { fontSize: 12.5, color: Palette.textBody },
  rubricVal: { fontSize: 12.5, fontWeight: '700', color: Palette.textTitle },
  insightsCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  insightHeader: { fontSize: 13, fontWeight: '800', color: Palette.textTitle, marginBottom: 4 },
  insightText: { fontSize: 12, color: Palette.textBody, lineHeight: 18 },
  recTopicsCard: {
    backgroundColor: Palette.primaryLight,
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.primaryBorder,
  },
  recHeaderRow: { flexDirection: 'row', alignItems: 'center', gap: 6, marginBottom: 8 },
  recTitle: { fontSize: 13, fontWeight: '800', color: Palette.primary },
  recItem: { fontSize: 12.5, color: Palette.textBody, lineHeight: 19 },
  scoreActions: { gap: 10, marginTop: 6 },
  retryInterviewBtn: {
    backgroundColor: Palette.aiPurple,
    borderRadius: Radii.button,
    paddingVertical: 13,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
    ...Shadows.button,
  },
  retryBtnText: { color: '#FFFFFF', fontSize: 14.5, fontWeight: '700' },
  newInterviewBtn: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.button,
    paddingVertical: 12,
    borderWidth: 1,
    borderColor: Palette.border,
    alignItems: 'center',
  },
  newInterviewText: { color: Palette.textSecondary, fontSize: 13.5, fontWeight: '600' },
});
