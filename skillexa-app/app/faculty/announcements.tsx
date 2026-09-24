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
import { CollegeAnnouncement, TargetAudience } from '../../data/collegeData';
import { CollegeStore } from '../../services/collegeStore';

export default function FacultyAnnouncementsScreen() {
  const { profile } = useAuth();
  const [announcements, setAnnouncements] = useState<CollegeAnnouncement[]>([]);

  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [priority, setPriority] = useState<'NORMAL' | 'HIGH' | 'URGENT'>('HIGH');
  const [isPinned, setIsPinned] = useState(true);

  const [target, setTarget] = useState<TargetAudience>({
    targetType: 'SECTION',
    collegeId: profile.collegeId || 'clg-kvg',
    collegeName: profile.collegeName || 'KVG College of Engineering',
    department: profile.department || 'ECE',
    academicYear: '3rd Year',
    section: 'A',
  });

  useEffect(() => {
    setAnnouncements(CollegeStore.getAnnouncements());
    return CollegeStore.subscribe(() => {
      setAnnouncements(CollegeStore.getAnnouncements());
    });
  }, []);

  const handlePublishAnnouncement = () => {
    if (!title.trim() || !content.trim()) {
      Alert.alert('Incomplete Fields', 'Please provide a title and announcement message.');
      return;
    }

    CollegeStore.addAnnouncement({
      collegeId: profile.collegeId || 'clg-kvg',
      title: title.trim(),
      content: content.trim(),
      target,
      facultyId: profile.id || 'fac-101',
      facultyName: profile.name || 'Dr. Ramesh Kumar',
      facultyDept: `${profile.department || 'ECE'} Department`,
      priority,
      isPinned,
    });

    Alert.alert(
      'Announcement Published!',
      'Targeted students in your college have been notified immediately on their SkillExa workspace.'
    );

    setTitle('');
    setContent('');
  };

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader showBack title="College Announcements" subtitle="Department Notices & Alerts" />

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {/* Authoring Card */}
        <View style={styles.card}>
          <Text style={styles.cardHeader}>1. Create Targeted Announcement</Text>

          <Text style={styles.label}>ANNOUNCEMENT TITLE *</Text>
          <TextInput
            style={styles.input}
            placeholder="e.g. Tomorrow's Embedded Systems Quiz at 10:00 AM"
            placeholderTextColor={Palette.textMuted}
            value={title}
            onChangeText={setTitle}
          />

          <Text style={[styles.label, { marginTop: 10 }]}>MESSAGE / DETAILS *</Text>
          <TextInput
            style={[styles.input, styles.textArea]}
            placeholder="Write clear notice instructions for students..."
            placeholderTextColor={Palette.textMuted}
            multiline
            value={content}
            onChangeText={setContent}
          />

          {/* Priority & Pinned */}
          <View style={styles.rowGrid}>
            <View style={{ flex: 1 }}>
              <Text style={styles.label}>PRIORITY LEVEL</Text>
              <View style={styles.pillsRow}>
                {(['NORMAL', 'HIGH', 'URGENT'] as const).map((p) => (
                  <TouchableOpacity
                    key={p}
                    style={[styles.pPill, priority === p && styles.pPillActive]}
                    onPress={() => setPriority(p)}
                  >
                    <Text style={[styles.pPillText, priority === p && styles.pPillTextActive]}>{p}</Text>
                  </TouchableOpacity>
                ))}
              </View>
            </View>

            <TouchableOpacity
              style={[styles.pinToggle, isPinned && styles.pinToggleActive]}
              onPress={() => setIsPinned(!isPinned)}
            >
              <Feather name="anchor" size={14} color={isPinned ? '#FFFFFF' : Palette.textSecondary} />
              <Text style={[styles.pinText, isPinned && styles.pinTextActive]}>
                {isPinned ? 'Pinned' : 'Normal'}
              </Text>
            </TouchableOpacity>
          </View>

          {/* Target Audience Selector */}
          <View style={{ marginTop: 14 }}>
            <TargetAudienceSelector
              target={target}
              onChangeTarget={setTarget}
              collegeName={profile.collegeName || 'KVG College of Engineering'}
            />
          </View>

          {/* Publish Action */}
          <TouchableOpacity style={styles.publishBtn} onPress={handlePublishAnnouncement} activeOpacity={0.85}>
            <Feather name="send" size={16} color="#FFFFFF" />
            <Text style={styles.publishBtnText}>Publish & Notify Students</Text>
          </TouchableOpacity>
        </View>

        {/* Existing Announcements List */}
        <View style={styles.sectionHeaderRow}>
          <Text style={styles.sectionTitle}>Active College Notices ({announcements.length})</Text>
        </View>

        <View style={styles.annList}>
          {announcements.map((ann) => (
            <View key={ann.id} style={styles.annCard}>
              <View style={styles.annCardTop}>
                <View style={styles.tag}>
                  <Text style={styles.tagText}>{ann.priority} • {ann.target.targetType}</Text>
                </View>
                <TouchableOpacity onPress={() => CollegeStore.deleteAnnouncement(ann.id)}>
                  <Feather name="trash-2" size={15} color={Palette.danger} />
                </TouchableOpacity>
              </View>

              <Text style={styles.annTitle}>{ann.title}</Text>
              <Text style={styles.annMsg}>{ann.content}</Text>
              <Text style={styles.annTargetMeta}>
                Target: {ann.target.department || 'All'} {ann.target.academicYear ? `• ${ann.target.academicYear}` : ''} {ann.target.section ? `• Sec ${ann.target.section}` : ''}
              </Text>
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
  card: { backgroundColor: '#FFFFFF', borderRadius: Radii.card, padding: 16, borderWidth: 1, borderColor: Palette.border, marginBottom: 20, ...Shadows.card },
  cardHeader: { fontSize: 16, fontWeight: '800', color: Palette.textTitle, marginBottom: 12 },
  label: { fontSize: 10, fontWeight: '800', color: Palette.textTitle, letterSpacing: 0.6, marginBottom: 4 },
  input: { backgroundColor: Palette.backgroundSecondary, borderRadius: Radii.input, borderWidth: 1, borderColor: Palette.border, padding: 10, fontSize: 13, color: Palette.textTitle },
  textArea: { height: 70, textAlignVertical: 'top' },
  rowGrid: { flexDirection: 'row', alignItems: 'flex-end', gap: 10, marginTop: 10 },
  pillsRow: { flexDirection: 'row', gap: 6 },
  pPill: { paddingHorizontal: 10, paddingVertical: 5, borderRadius: Radii.pill, backgroundColor: Palette.backgroundSecondary, borderWidth: 1, borderColor: Palette.border },
  pPillActive: { backgroundColor: Palette.primary, borderColor: Palette.primary },
  pPillText: { fontSize: 11, fontWeight: '700', color: Palette.textSecondary },
  pPillTextActive: { color: '#FFFFFF' },
  pinToggle: { flexDirection: 'row', alignItems: 'center', gap: 6, backgroundColor: Palette.backgroundSecondary, paddingHorizontal: 12, paddingVertical: 8, borderRadius: Radii.button, borderWidth: 1, borderColor: Palette.border },
  pinToggleActive: { backgroundColor: Palette.primary, borderColor: Palette.primary },
  pinText: { fontSize: 12, fontWeight: '700', color: Palette.textSecondary },
  pinTextActive: { color: '#FFFFFF' },
  publishBtn: { backgroundColor: Palette.primary, borderRadius: Radii.button, paddingVertical: 13, flexDirection: 'row', alignItems: 'center', justifyContent: 'center', gap: 8, marginTop: 14, ...Shadows.button },
  publishBtnText: { color: '#FFFFFF', fontSize: 14, fontWeight: '700' },
  sectionHeaderRow: { marginBottom: 10 },
  sectionTitle: { fontSize: 16, fontWeight: '800', color: Palette.textTitle },
  annList: { gap: 10 },
  annCard: { backgroundColor: '#FFFFFF', borderRadius: Radii.card, padding: 14, borderWidth: 1, borderColor: Palette.border, ...Shadows.card },
  annCardTop: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', marginBottom: 6 },
  tag: { backgroundColor: Palette.primaryLight, paddingHorizontal: 8, paddingVertical: 2, borderRadius: 6 },
  tagText: { fontSize: 10.5, fontWeight: '700', color: Palette.primary },
  annTitle: { fontSize: 14.5, fontWeight: '800', color: Palette.textTitle, marginBottom: 4 },
  annMsg: { fontSize: 12.5, color: Palette.textSecondary, marginBottom: 6 },
  annTargetMeta: { fontSize: 11, color: Palette.textMuted },
});
