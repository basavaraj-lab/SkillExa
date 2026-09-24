import { Feather } from '@expo/vector-icons';
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
import { TargetAudienceSelector } from '../../components/TargetAudienceSelector';
import { useAuth } from '../../components/auth-context';
import { AppHeader } from '../../components/common/AppHeader';
import { Palette, Radii, Shadows } from '../../constants/theme';
import { TargetAudience } from '../../data/collegeData';
import { FacultyVideo } from '../../data/curriculumSchema';
import { CollegeStore } from '../../services/collegeStore';
import { FacultySystemStore } from '../../services/facultyStore';

export default function FacultyVideosScreen() {
  const { profile } = useAuth();
  const [videos, setVideos] = useState<FacultyVideo[]>([]);
  const [section, setSection] = useState<'engineering' | 'competitive'>('engineering');
  const [subject, setSubject] = useState('Embedded Systems');
  const [topic, setTopic] = useState('Microcontrollers');
  const [title, setTitle] = useState('');
  const [videoUrl, setVideoUrl] = useState('');
  const [description, setDescription] = useState('');
  const [duration, setDuration] = useState('20 mins');
  const [visibility, setVisibility] = useState<'college' | 'community'>('college');

  const [target, setTarget] = useState<TargetAudience>({
    targetType: 'SECTION',
    collegeId: profile.collegeId || 'clg-kvg',
    collegeName: profile.collegeName || 'KVG College of Engineering',
    department: profile.department || 'ECE',
    academicYear: '3rd Year',
    section: 'A',
  });

  useEffect(() => {
    setVideos(FacultySystemStore.getVideos());
    return FacultySystemStore.subscribe(() => {
      setVideos(FacultySystemStore.getVideos());
    });
  }, []);

  const handlePublishVideo = () => {
    if (!title.trim() || !videoUrl.trim() || !topic.trim()) {
      Alert.alert('Incomplete Form', 'Please provide Video Title, Topic Name, and Video URL.');
      return;
    }

    FacultySystemStore.addVideo({
      section,
      subject,
      topic: topic.trim(),
      title: title.trim(),
      videoUrl: videoUrl.trim(),
      description: description.trim() || 'Faculty curated lecture video.',
      duration: duration.trim(),
      facultyName: profile.name || 'Dr. Ramesh Kumar',
      facultyDesignation: profile.facultyDesignation || 'Associate Professor',
      facultyDepartment: profile.department || 'ECE Department',
      collegeId: profile.collegeId || 'clg-kvg',
      collegeName: profile.collegeName || 'KVG College of Engineering',
      isVerifiedFaculty: true,
      visibility,
      published: true,
    });

    if (visibility === 'college') {
      CollegeStore.dispatchNotification({
        studentId: 'std-101',
        collegeId: profile.collegeId || 'clg-kvg',
        title: '🎥 New Lecture Video',
        message: `${profile.name || 'Faculty'} uploaded "${title.trim()}" for ${topic.trim()}.`,
        type: 'VIDEO',
        actionRoute: '/topic-learning',
        actionParams: {
          topic: topic.trim(),
          subject,
          section,
        },
      });

      Alert.alert('Video Attached!', `Video lesson attached to "${topic}". Target students in ${profile.collegeName || 'your college'} have been notified!`);
    } else {
      Alert.alert(
        'Published to SkillExa Community! 🌍',
        `Video lecture "${title}" is now publicly discoverable by students across all colleges.`
      );
    }
    setTitle('');
    setVideoUrl('');
    setDescription('');
  };

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader showBack title="Faculty Video Lectures" subtitle="Attach Educational Videos to Topics" />

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {/* Banner */}
        <View style={styles.banner}>
          <Feather name="film" size={22} color={Palette.aiPurple} />
          <View style={{ flex: 1 }}>
            <Text style={styles.bannerTitle}>Attach Topic Video Lessons</Text>
            <Text style={styles.bannerDesc}>
              Lectures published here appear inside the corresponding student topic view marked with 🎥 Faculty Video.
            </Text>
          </View>
        </View>

        {/* Video Attacher Form */}
        <View style={styles.card}>
          <Text style={styles.cardTitle}>1. Target Topic & Video Metadata</Text>

          <View style={styles.gridRow}>
            <View style={{ flex: 1 }}>
              <Text style={styles.label}>SECTION</Text>
              <TextInput style={styles.input} value={section} onChangeText={(t) => setSection(t as any)} />
            </View>
            <View style={{ flex: 1 }}>
              <Text style={styles.label}>SUBJECT</Text>
              <TextInput style={styles.input} value={subject} onChangeText={setSubject} />
            </View>
          </View>

          <Text style={[styles.label, { marginTop: 10 }]}>TOPIC NAME *</Text>
          <TextInput style={styles.input} value={topic} onChangeText={setTopic} />

          <Text style={[styles.label, { marginTop: 10 }]}>VIDEO TITLE *</Text>
          <TextInput
            style={styles.input}
            placeholder="e.g. In-Depth ARM Cortex-M NVIC Interrupts"
            placeholderTextColor={Palette.textMuted}
            value={title}
            onChangeText={setTitle}
          />

          <Text style={[styles.label, { marginTop: 10 }]}>VIDEO URL (YOUTUBE / MP4 STREAM) *</Text>
          <TextInput
            style={styles.input}
            placeholder="https://www.youtube.com/watch?v=..."
            placeholderTextColor={Palette.textMuted}
            value={videoUrl}
            onChangeText={setVideoUrl}
          />

          <View style={[styles.gridRow, { marginTop: 10 }]}>
            <View style={{ flex: 1 }}>
              <Text style={styles.label}>DURATION</Text>
              <TextInput style={styles.input} value={duration} onChangeText={setDuration} />
            </View>
          </View>

          <Text style={[styles.label, { marginTop: 10 }]}>DESCRIPTION</Text>
          <TextInput
            style={[styles.input, { height: 60 }]}
            placeholder="Key concepts discussed in this lecture..."
            placeholderTextColor={Palette.textMuted}
            multiline
            value={description}
            onChangeText={setDescription}
          />

          {/* Target Audience Selector & Visibility */}
          <View style={{ marginTop: 14 }}>
            <TargetAudienceSelector
              visibility={visibility}
              onChangeVisibility={setVisibility}
              target={target}
              onChangeTarget={setTarget}
              collegeName={profile.collegeName || 'KVG College of Engineering'}
            />
          </View>

          <TouchableOpacity style={styles.publishBtn} onPress={handlePublishVideo} activeOpacity={0.85}>
            <Feather name="upload" size={16} color="#FFFFFF" />
            <Text style={styles.publishBtnText}>Publish Video to Topic</Text>
          </TouchableOpacity>
        </View>

        {/* Existing Attached Videos */}
        <View style={styles.sectionHeaderRow}>
          <Text style={styles.sectionTitle}>Attached Topic Videos ({videos.length})</Text>
        </View>

        <View style={styles.list}>
          {videos.map((v) => (
            <View key={v.id} style={styles.videoCard}>
              <View style={styles.cardHeader}>
                <View style={styles.badge}>
                  <Text style={styles.badgeText}>{v.subject} • {v.topic}</Text>
                </View>
                <TouchableOpacity onPress={() => FacultySystemStore.deleteVideo(v.id)}>
                  <Feather name="trash-2" size={15} color={Palette.danger} />
                </TouchableOpacity>
              </View>

              <Text style={styles.vTitle}>{v.title}</Text>
              <Text style={styles.vUrl} numberOfLines={1}>🔗 {v.videoUrl}</Text>
              <Text style={styles.vDesc}>{v.description}</Text>
              <Text style={styles.vMeta}>Duration: {v.duration || '15 mins'} • By {v.facultyName}</Text>
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
    borderColor: Palette.aiPurpleBorder,
    borderLeftWidth: 4,
    borderLeftColor: Palette.aiPurple,
    flexDirection: 'row',
    alignItems: 'center',
    gap: 12,
    marginBottom: 18,
    ...Shadows.card,
  },
  bannerTitle: { fontSize: 15, fontWeight: '800', color: Palette.textTitle },
  bannerDesc: { fontSize: 12, color: Palette.textSecondary, marginTop: 2 },
  card: { backgroundColor: '#FFFFFF', borderRadius: Radii.card, padding: 16, borderWidth: 1, borderColor: Palette.border, marginBottom: 20, ...Shadows.card },
  cardTitle: { fontSize: 15, fontWeight: '800', color: Palette.textTitle, marginBottom: 12 },
  gridRow: { flexDirection: 'row', gap: 10 },
  label: { fontSize: 10, fontWeight: '800', color: Palette.textTitle, letterSpacing: 0.6, marginBottom: 4 },
  input: { backgroundColor: Palette.backgroundSecondary, borderRadius: Radii.input, borderWidth: 1, borderColor: Palette.border, padding: 10, fontSize: 13, color: Palette.textTitle },
  publishBtn: {
    backgroundColor: Palette.aiPurple,
    borderRadius: Radii.button,
    paddingVertical: 13,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
    marginTop: 14,
    ...Shadows.button,
  },
  publishBtnText: { color: '#FFFFFF', fontSize: 14, fontWeight: '700' },
  sectionHeaderRow: { marginBottom: 10 },
  sectionTitle: { fontSize: 16, fontWeight: '800', color: Palette.textTitle },
  list: { gap: 10 },
  videoCard: { backgroundColor: '#FFFFFF', borderRadius: Radii.card, padding: 14, borderWidth: 1, borderColor: Palette.border, ...Shadows.card },
  cardHeader: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 6 },
  badge: { backgroundColor: Palette.aiPurpleLight, paddingHorizontal: 8, paddingVertical: 2, borderRadius: 6 },
  badgeText: { fontSize: 10.5, fontWeight: '700', color: Palette.aiPurple },
  vTitle: { fontSize: 14.5, fontWeight: '800', color: Palette.textTitle, marginBottom: 2 },
  vUrl: { fontSize: 11.5, color: Palette.primary, marginBottom: 4 },
  vDesc: { fontSize: 12, color: Palette.textSecondary, marginBottom: 6 },
  vMeta: { fontSize: 11, color: Palette.textMuted },
});
