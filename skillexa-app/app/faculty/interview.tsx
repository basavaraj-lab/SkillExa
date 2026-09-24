import { Feather } from '@expo/vector-icons';
import { router } from 'expo-router';
import React, { useEffect, useState } from 'react';
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
import { useAuth } from '../../components/auth-context';
import { AppHeader } from '../../components/common/AppHeader';
import { Palette, Radii, Shadows } from '../../constants/theme';
import { FacultyInterview } from '../../data/curriculumSchema';
import { CollegeStore } from '../../services/collegeStore';
import { FacultySystemStore } from '../../services/facultyStore';

const INTERVIEW_TYPES = [
  'Technical Interview',
  'HR Interview',
  'Coding Interview',
  'Engineering Viva',
  'Project Viva',
  'Placement Interview',
  'Custom Interview',
];

export default function FacultyInterviewScreen() {
  const { profile } = useAuth();
  const [interviews, setInterviews] = useState<FacultyInterview[]>([]);
  const [studentName, setStudentName] = useState('Ganesh Sharan');
  const [selectedType, setSelectedType] = useState('Technical Interview');
  const [role, setRole] = useState('Embedded Systems & IoT Engineer');
  const [scheduledTime, setScheduledTime] = useState('Tomorrow, 11:00 AM');
  const [questions, setQuestions] = useState<string[]>([
    'What is an embedded system and how does it differ from a general-purpose computer?',
    'Explain the differences between Microprocessors and Microcontrollers.',
    'What is an interrupt and how does the NVIC prevent priority inversion?',
    'Explain the role of a Watchdog Timer (WDT) in safety-critical firmware.',
    'Compare I2C, SPI, and UART in terms of wiring, speed, and communication distance.',
  ]);
  const [newQ, setNewQ] = useState('');

  useEffect(() => {
    setInterviews(FacultySystemStore.getInterviews());
    return FacultySystemStore.subscribe(() => {
      setInterviews(FacultySystemStore.getInterviews());
    });
  }, []);

  const handleAddQuestion = () => {
    if (!newQ.trim()) return;
    setQuestions([...questions, newQ.trim()]);
    setNewQ('');
  };

  const handleRemoveQuestion = (idx: number) => {
    setQuestions(questions.filter((_, i) => i !== idx));
  };

  const handleScheduleInterview = () => {
    if (!studentName.trim() || !role.trim() || questions.length === 0) {
      Alert.alert('Incomplete Details', 'Please provide student name, role/subject, and at least 1 question.');
      return;
    }

    FacultySystemStore.addInterview({
      studentId: 'std-101',
      studentName: studentName.trim(),
      interviewType: selectedType as any,
      subjectOrRole: role.trim(),
      difficulty: 'medium',
      scheduledTime: scheduledTime.trim() || 'Scheduled',
      status: 'Scheduled',
      questions,
      facultyName: profile.name || 'Dr. Ramesh Kumar',
    });

    CollegeStore.dispatchNotification({
      studentId: 'std-101',
      collegeId: profile.collegeId || 'clg-kvg',
      title: '🎤 Interview Invitation',
      message: `${profile.name || 'Faculty'} scheduled a ${selectedType} for ${role.trim()} (${scheduledTime.trim()}).`,
      type: 'INTERVIEW',
      actionRoute: '/my-college',
    });

    Alert.alert('Interview Scheduled!', `Interview invitation created for ${studentName}. The student has been notified on their College workspace.`);
  };

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader showBack title="Take & Schedule Interviews" subtitle="Faculty Interview Portal" />

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {/* Banner */}
        <View style={styles.banner}>
          <Feather name="message-square" size={22} color={Palette.primary} />
          <View style={{ flex: 1 }}>
            <Text style={styles.bannerTitle}>Faculty Viva & Placement Panels</Text>
            <Text style={styles.bannerDesc}>Conduct custom interviews with question prompts and live evaluation scorecards.</Text>
          </View>
        </View>

        {/* Setup Form */}
        <View style={styles.card}>
          <Text style={styles.cardHeader}>1. Interview Configuration</Text>

          <Text style={styles.label}>STUDENT NAME</Text>
          <TextInput style={styles.input} value={studentName} onChangeText={setStudentName} />

          <Text style={[styles.label, { marginTop: 10 }]}>INTERVIEW TYPE</Text>
          <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={styles.chipsRow}>
            {INTERVIEW_TYPES.map((t) => (
              <TouchableOpacity
                key={t}
                style={[styles.chip, selectedType === t && styles.chipActive]}
                onPress={() => setSelectedType(t)}
              >
                <Text style={[styles.chipText, selectedType === t && styles.chipTextActive]}>{t}</Text>
              </TouchableOpacity>
            ))}
          </ScrollView>

          <View style={[styles.gridRow, { marginTop: 10 }]}>
            <View style={{ flex: 1 }}>
              <Text style={styles.label}>ROLE / SUBJECT</Text>
              <TextInput style={styles.input} value={role} onChangeText={setRole} />
            </View>
            <View style={{ flex: 1 }}>
              <Text style={styles.label}>DATE / TIME</Text>
              <TextInput style={styles.input} value={scheduledTime} onChangeText={setScheduledTime} />
            </View>
          </View>

          {/* Questions Prompts List */}
          <Text style={[styles.label, { marginTop: 14 }]}>INTERVIEW QUESTIONS LIST ({questions.length})</Text>
          <View style={styles.questionsList}>
            {questions.map((q, idx) => (
              <View key={idx} style={styles.qItemRow}>
                <Text style={styles.qItemNum}>Q{idx + 1}.</Text>
                <Text style={styles.qItemText}>{q}</Text>
                <TouchableOpacity onPress={() => handleRemoveQuestion(idx)} style={styles.deleteQBtn}>
                  <Feather name="x" size={14} color={Palette.danger} />
                </TouchableOpacity>
              </View>
            ))}
          </View>

          {/* Add Question Input */}
          <View style={styles.addQRow}>
            <TextInput
              style={[styles.input, { flex: 1 }]}
              placeholder="Add question prompt..."
              placeholderTextColor={Palette.textMuted}
              value={newQ}
              onChangeText={setNewQ}
            />
            <TouchableOpacity style={styles.addQBtn} onPress={handleAddQuestion}>
              <Text style={styles.addQBtnText}>+ Add</Text>
            </TouchableOpacity>
          </View>

          {/* Schedule / Launch Action */}
          <View style={styles.btnRow}>
            <TouchableOpacity style={styles.scheduleBtn} onPress={handleScheduleInterview}>
              <Feather name="calendar" size={16} color={Palette.primary} />
              <Text style={styles.scheduleBtnText}>Schedule</Text>
            </TouchableOpacity>

            <TouchableOpacity
              style={styles.startLiveBtn}
              onPress={() =>
                router.push({
                  pathname: '/faculty/live-interview',
                  params: {
                    studentName,
                    role,
                    interviewType: selectedType,
                  },
                })
              }
            >
              <Feather name="video" size={16} color="#FFFFFF" />
              <Text style={styles.startLiveBtnText}>Launch Live Room</Text>
            </TouchableOpacity>
          </View>
        </View>

        {/* Existing Interviews */}
        <View style={styles.sectionHeaderRow}>
          <Text style={styles.sectionTitle}>Scheduled & Completed Interviews ({interviews.length})</Text>
        </View>

        <View style={styles.interviewsList}>
          {interviews.map((item) => (
            <View key={item.id} style={styles.interviewCard}>
              <View style={styles.intCardTop}>
                <View>
                  <Text style={styles.intStudentName}>{item.studentName}</Text>
                  <Text style={styles.intMetaText}>{item.interviewType} • {item.subjectOrRole}</Text>
                </View>
                <View style={styles.statusPill}>
                  <Text style={styles.statusPillText}>{item.status}</Text>
                </View>
              </View>

              <Text style={styles.intTimeText}>🕒 {item.scheduledTime} • {item.questions.length} Questions</Text>

              <View style={styles.intActions}>
                <TouchableOpacity
                  style={styles.enterRoomBtn}
                  onPress={() =>
                    router.push({
                      pathname: '/faculty/live-interview',
                      params: {
                        studentName: item.studentName,
                        role: item.subjectOrRole,
                        interviewType: item.interviewType,
                      },
                    })
                  }
                >
                  <Feather name="video" size={13} color="#FFFFFF" />
                  <Text style={styles.enterRoomText}>Enter Video Call</Text>
                </TouchableOpacity>

                <TouchableOpacity
                  style={styles.evalBtn}
                  onPress={() =>
                    router.push({
                      pathname: '/faculty/evaluation',
                      params: {
                        interviewId: item.id,
                        studentName: item.studentName,
                        role: item.subjectOrRole,
                      },
                    })
                  }
                >
                  <Text style={styles.evalBtnText}>Evaluate & Grade</Text>
                </TouchableOpacity>
              </View>
            </View>
          ))}
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: Palette.background },
  scrollContent: { paddingHorizontal: 16, paddingTop: 16, paddingBottom: 40 },
  banner: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.primaryBorder,
    borderLeftWidth: 4,
    borderLeftColor: Palette.primary,
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
    marginBottom: 18,
    ...Shadows.card,
  },
  bannerTitle: { fontSize: 15, fontWeight: '800', color: Palette.textTitle },
  bannerDesc: { fontSize: 12, color: Palette.textSecondary, marginTop: 2 },
  card: { backgroundColor: '#FFFFFF', borderRadius: Radii.card, padding: 18, borderWidth: 1, borderColor: Palette.border, marginBottom: 20, ...Shadows.card },
  cardHeader: { fontSize: 16, fontWeight: '800', color: Palette.textTitle, marginBottom: 12 },
  label: { fontSize: 10.5, fontWeight: '800', color: Palette.textTitle, letterSpacing: 0.6, marginBottom: 6 },
  input: { backgroundColor: Palette.backgroundSecondary, borderRadius: Radii.input, borderWidth: 1, borderColor: Palette.border, padding: 10, fontSize: 13, color: Palette.textTitle },
  chipsRow: { gap: 8, paddingVertical: 2, marginBottom: 10 },
  chip: { paddingHorizontal: 12, paddingVertical: 6, borderRadius: Radii.pill, backgroundColor: Palette.backgroundSecondary, borderWidth: 1, borderColor: Palette.border },
  chipActive: { backgroundColor: Palette.primary, borderColor: Palette.primary },
  chipText: { fontSize: 12, fontWeight: '600', color: Palette.textSecondary },
  chipTextActive: { color: '#FFFFFF', fontWeight: '700' },
  gridRow: { flexDirection: 'row', gap: 10 },
  questionsList: { gap: 6, marginBottom: 10 },
  qItemRow: { flexDirection: 'row', alignItems: 'center', backgroundColor: Palette.backgroundSecondary, padding: 8, borderRadius: 8, gap: 6 },
  qItemNum: { fontSize: 12, fontWeight: '800', color: Palette.primary },
  qItemText: { flex: 1, fontSize: 12.5, color: Palette.textBody },
  deleteQBtn: { padding: 4 },
  addQRow: { flexDirection: 'row', gap: 8, marginBottom: 16 },
  addQBtn: { backgroundColor: Palette.primaryLight, paddingHorizontal: 14, borderRadius: Radii.button, justifyContent: 'center' },
  addQBtnText: { fontSize: 13, fontWeight: '700', color: Palette.primary },
  btnRow: { flexDirection: 'row', gap: 10 },
  scheduleBtn: { flex: 1, backgroundColor: Palette.primaryLight, borderWidth: 1, borderColor: Palette.primaryBorder, borderRadius: Radii.button, paddingVertical: 12, flexDirection: 'row', alignItems: 'center', justifyContent: 'center', gap: 6 },
  scheduleBtnText: { fontSize: 13.5, fontWeight: '700', color: Palette.primary },
  startLiveBtn: { flex: 1.5, backgroundColor: Palette.danger, borderRadius: Radii.button, paddingVertical: 12, flexDirection: 'row', alignItems: 'center', justifyContent: 'center', gap: 6, ...Shadows.button },
  startLiveBtnText: { color: '#FFFFFF', fontSize: 13.5, fontWeight: '700' },
  sectionHeaderRow: { marginBottom: 10 },
  sectionTitle: { fontSize: 16, fontWeight: '800', color: Palette.textTitle },
  interviewsList: { gap: 10 },
  interviewCard: { backgroundColor: '#FFFFFF', borderRadius: Radii.card, padding: 14, borderWidth: 1, borderColor: Palette.border, ...Shadows.card },
  intCardTop: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 6 },
  intStudentName: { fontSize: 15, fontWeight: '800', color: Palette.textTitle },
  intMetaText: { fontSize: 12, color: Palette.textSecondary, marginTop: 1 },
  statusPill: { backgroundColor: Palette.primaryLight, paddingHorizontal: 8, paddingVertical: 3, borderRadius: 6 },
  statusPillText: { fontSize: 10.5, fontWeight: '700', color: Palette.primary },
  intTimeText: { fontSize: 12, color: Palette.textSecondary, marginBottom: 10 },
  intActions: { flexDirection: 'row', gap: 8, paddingTop: 8, borderTopWidth: 1, borderTopColor: Palette.borderSubtle },
  enterRoomBtn: { flex: 1, backgroundColor: Palette.danger, borderRadius: 8, paddingVertical: 8, flexDirection: 'row', alignItems: 'center', justifyContent: 'center', gap: 4 },
  enterRoomText: { color: '#FFFFFF', fontSize: 12, fontWeight: '700' },
  evalBtn: { flex: 1, backgroundColor: Palette.backgroundSecondary, borderWidth: 1, borderColor: Palette.border, borderRadius: 8, paddingVertical: 8, alignItems: 'center' },
  evalBtnText: { fontSize: 12, fontWeight: '700', color: Palette.textTitle },
});
