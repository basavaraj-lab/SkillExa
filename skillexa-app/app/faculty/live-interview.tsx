import { Feather } from '@expo/vector-icons';
import { router, useLocalSearchParams } from 'expo-router';
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
import { Palette, Radii } from '../../constants/theme';

export default function LiveVideoInterviewScreen() {
  const {
    studentName = 'Ganesh Sharan',
    role = 'Embedded Systems Engineer',
    interviewType = 'Technical Interview',
  } = useLocalSearchParams<{
    studentName: string;
    role: string;
    interviewType: string;
  }>();

  const [micOn, setMicOn] = useState(true);
  const [camOn, setCamOn] = useState(true);
  const [seconds, setSeconds] = useState(0);
  const [currentQIdx, setCurrentQIdx] = useState(0);
  const [scoringNotes, setScoringNotes] = useState('');

  const questions = [
    'Q1. Explain the architectural differences between Harvard and Von Neumann architectures.',
    'Q2. What is an interrupt service routine (ISR) and why must delay functions never be used inside it?',
    'Q3. What is the role of the Watchdog Timer (WDT) in safety-critical firmware?',
    'Q4. How do I2C and SPI compare in terms of wire count, speed, and multi-device communication?',
    'Q5. Describe an embedded project where you resolved a difficult hardware/software timing bug.',
  ];

  useEffect(() => {
    const timer = setInterval(() => {
      setSeconds((s) => s + 1);
    }, 1000);
    return () => clearInterval(timer);
  }, []);

  const formatTimer = (sec: number) => {
    const m = Math.floor(sec / 60);
    const s = sec % 60;
    return `${m.toString().padStart(2, '0')}:${s.toString().padStart(2, '0')}`;
  };

  const handleEndCall = () => {
    Alert.alert('End Interview Call', 'Are you sure you want to end this interview session and proceed to evaluation?', [
      { text: 'Cancel', style: 'cancel' },
      {
        text: 'End & Grade',
        style: 'destructive',
        onPress: () => {
          router.replace({
            pathname: '/faculty/evaluation',
            params: {
              studentName,
              role,
            },
          });
        },
      },
    ]);
  };

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="light-content" backgroundColor="#0F172A" />

      {/* Top Session Call Header */}
      <View style={styles.callHeader}>
        <View style={styles.liveTag}>
          <View style={styles.liveDot} />
          <Text style={styles.liveTagText}>LIVE INTERVIEW • {formatTimer(seconds)}</Text>
        </View>

        <View style={{ alignItems: 'center' }}>
          <Text style={styles.candidateName}>{studentName}</Text>
          <Text style={styles.candidateRole}>{role}</Text>
        </View>

        <TouchableOpacity style={styles.headerEndBtn} onPress={handleEndCall}>
          <Feather name="phone-off" size={16} color="#FFFFFF" />
        </TouchableOpacity>
      </View>

      {/* Video Streams Container (Split View) */}
      <View style={styles.videoStage}>
        {/* Remote Candidate Stream (Primary) */}
        <View style={styles.remoteVideoBox}>
          <View style={styles.videoPlaceholder}>
            <View style={styles.avatarCircle}>
              <Text style={styles.avatarLetter}>{studentName.charAt(0)}</Text>
            </View>
            <Text style={styles.videoLabel}>{studentName} (Candidate)</Text>
            <Text style={styles.streamStatus}>Connected via WebRTC Media Stream</Text>
          </View>

          {/* Local Faculty Stream Picture-in-Picture */}
          <View style={styles.localPipBox}>
            {camOn ? (
              <View style={styles.pipContent}>
                <Feather name="user" size={18} color="#FFFFFF" />
                <Text style={styles.pipText}>You (Faculty)</Text>
              </View>
            ) : (
              <View style={styles.pipOff}>
                <Feather name="camera-off" size={16} color={Palette.danger} />
                <Text style={styles.pipOffText}>Cam Off</Text>
              </View>
            )}
          </View>
        </View>
      </View>

      {/* Faculty Question Prompt & Quick Scoring Drawer */}
      <View style={styles.drawer}>
        <View style={styles.drawerHeader}>
          <Text style={styles.drawerTitle}>
            Question {currentQIdx + 1} of {questions.length}
          </Text>
          <View style={styles.qNavBtns}>
            <TouchableOpacity
              style={[styles.qNavBtn, currentQIdx === 0 && { opacity: 0.4 }]}
              onPress={() => setCurrentQIdx(Math.max(0, currentQIdx - 1))}
              disabled={currentQIdx === 0}
            >
              <Feather name="chevron-left" size={16} color={Palette.textTitle} />
            </TouchableOpacity>
            <TouchableOpacity
              style={[styles.qNavBtn, currentQIdx === questions.length - 1 && { opacity: 0.4 }]}
              onPress={() => setCurrentQIdx(Math.min(questions.length - 1, currentQIdx + 1))}
              disabled={currentQIdx === questions.length - 1}
            >
              <Feather name="chevron-right" size={16} color={Palette.textTitle} />
            </TouchableOpacity>
          </View>
        </View>

        <Text style={styles.activePromptText}>{questions[currentQIdx]}</Text>

        <TextInput
          style={styles.notesInput}
          placeholder="Type live feedback or score notes during call..."
          placeholderTextColor={Palette.textMuted}
          multiline
          value={scoringNotes}
          onChangeText={setScoringNotes}
        />
      </View>

      {/* Bottom Media Controls */}
      <View style={styles.controlsBar}>
        <TouchableOpacity
          style={[styles.controlBtn, !micOn && styles.controlBtnOff]}
          onPress={() => setMicOn(!micOn)}
        >
          <Feather name={micOn ? 'mic' : 'mic-off'} size={20} color="#FFFFFF" />
        </TouchableOpacity>

        <TouchableOpacity
          style={[styles.controlBtn, !camOn && styles.controlBtnOff]}
          onPress={() => setCamOn(!camOn)}
        >
          <Feather name={camOn ? 'video' : 'video-off'} size={20} color="#FFFFFF" />
        </TouchableOpacity>

        <TouchableOpacity style={styles.endCallBigBtn} onPress={handleEndCall}>
          <Feather name="phone-off" size={22} color="#FFFFFF" />
          <Text style={styles.endCallText}>End Call</Text>
        </TouchableOpacity>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: '#0F172A' },
  callHeader: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    paddingHorizontal: 16,
    paddingVertical: 10,
    borderBottomWidth: 1,
    borderBottomColor: 'rgba(255, 255, 255, 0.1)',
  },
  liveTag: { flexDirection: 'row', alignItems: 'center', gap: 6, backgroundColor: 'rgba(239, 68, 68, 0.2)', paddingHorizontal: 8, paddingVertical: 4, borderRadius: 12 },
  liveDot: { width: 8, height: 8, borderRadius: 4, backgroundColor: '#EF4444' },
  liveTagText: { fontSize: 10, fontWeight: '800', color: '#EF4444' },
  candidateName: { fontSize: 14.5, fontWeight: '800', color: '#FFFFFF' },
  candidateRole: { fontSize: 11, color: '#94A3B8' },
  headerEndBtn: { backgroundColor: '#EF4444', padding: 8, borderRadius: 20 },
  videoStage: { flex: 1, padding: 12 },
  remoteVideoBox: {
    flex: 1,
    backgroundColor: '#1E293B',
    borderRadius: 16,
    borderWidth: 1,
    borderColor: 'rgba(255, 255, 255, 0.1)',
    overflow: 'hidden',
    position: 'relative',
    justifyContent: 'center',
    alignItems: 'center',
  },
  videoPlaceholder: { alignItems: 'center' },
  avatarCircle: { width: 72, height: 72, borderRadius: 36, backgroundColor: Palette.primary, alignItems: 'center', justifyContent: 'center', marginBottom: 10 },
  avatarLetter: { fontSize: 28, fontWeight: '900', color: '#FFFFFF' },
  videoLabel: { fontSize: 16, fontWeight: '800', color: '#FFFFFF' },
  streamStatus: { fontSize: 11, color: '#94A3B8', marginTop: 4 },
  localPipBox: {
    position: 'absolute',
    bottom: 12,
    right: 12,
    width: 100,
    height: 130,
    backgroundColor: '#0F172A',
    borderRadius: 12,
    borderWidth: 1.5,
    borderColor: Palette.primary,
    overflow: 'hidden',
    justifyContent: 'center',
    alignItems: 'center',
  },
  pipContent: { alignItems: 'center', gap: 4 },
  pipText: { fontSize: 10, color: '#FFFFFF', fontWeight: '700' },
  pipOff: { alignItems: 'center', gap: 4 },
  pipOffText: { fontSize: 10, color: Palette.danger, fontWeight: '700' },
  drawer: {
    backgroundColor: '#FFFFFF',
    borderTopLeftRadius: 20,
    borderTopRightRadius: 20,
    padding: 16,
    maxHeight: 180,
  },
  drawerHeader: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 6 },
  drawerTitle: { fontSize: 12, fontWeight: '800', color: Palette.primary, letterSpacing: 0.6 },
  qNavBtns: { flexDirection: 'row', gap: 8 },
  qNavBtn: { width: 28, height: 28, borderRadius: 14, backgroundColor: Palette.backgroundSecondary, alignItems: 'center', justifyContent: 'center' },
  activePromptText: { fontSize: 13.5, fontWeight: '700', color: Palette.textTitle, lineHeight: 18, marginBottom: 8 },
  notesInput: {
    height: 50,
    backgroundColor: Palette.backgroundSecondary,
    borderRadius: 8,
    borderWidth: 1,
    borderColor: Palette.border,
    padding: 8,
    fontSize: 12,
    color: Palette.textTitle,
    textAlignVertical: 'top',
  },
  controlsBar: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 16,
    backgroundColor: '#0F172A',
    paddingVertical: 14,
    borderTopWidth: 1,
    borderTopColor: 'rgba(255, 255, 255, 0.1)',
  },
  controlBtn: { width: 48, height: 48, borderRadius: 24, backgroundColor: '#334155', alignItems: 'center', justifyContent: 'center' },
  controlBtnOff: { backgroundColor: '#EF4444' },
  endCallBigBtn: {
    backgroundColor: '#EF4444',
    paddingHorizontal: 20,
    paddingVertical: 12,
    borderRadius: 24,
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  endCallText: { color: '#FFFFFF', fontSize: 14, fontWeight: '800' },
});
