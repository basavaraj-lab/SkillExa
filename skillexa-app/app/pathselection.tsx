import { Feather } from "@expo/vector-icons";
import { router } from "expo-router";
import React from "react";
import {
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from "react-native";
import { AppHeader } from "../components/common/AppHeader";
import { Palette, Radii, Shadows } from "../constants/theme";

export default function PathSelection() {
  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader />

      <ScrollView
        contentContainerStyle={styles.scrollContent}
        showsVerticalScrollIndicator={false}
      >
        {/* Header */}
        <View style={styles.header}>
          <Text style={styles.title}>Choose Your Learning Path</Text>
          <Text style={styles.subtitle}>
            What do you want to prepare for today?
          </Text>
        </View>

        {/* 1. Engineering Learning Card */}
        <View style={styles.pathCard}>
          <View style={styles.cardTopRow}>
            <View style={styles.iconCircle}>
              <Feather name="cpu" size={26} color={Palette.primary} />
            </View>
            <View style={styles.badge}>
              <Text style={styles.badgeText}>5 Learning Modules</Text>
            </View>
          </View>

          <Text style={styles.cardTitle}>Engineering Learning</Text>
          <Text style={styles.cardDesc}>
            Build technical skills, practice coding, and become placement ready.
          </Text>

          {/* Module Topics List */}
          <View style={styles.topicsRow}>
            <View style={styles.topicChip}>
              <Feather name="terminal" size={13} color={Palette.primary} />
              <Text style={styles.topicChipText}>Coding</Text>
            </View>
            <View style={styles.topicChip}>
              <Feather name="code" size={13} color={Palette.primary} />
              <Text style={styles.topicChipText}>DSA</Text>
            </View>
            <View style={styles.topicChip}>
              <Feather name="file-text" size={13} color={Palette.primary} />
              <Text style={styles.topicChipText}>Resume</Text>
            </View>
            <View style={styles.topicChip}>
              <Feather name="message-square" size={13} color={Palette.primary} />
              <Text style={styles.topicChipText}>Interview</Text>
            </View>
            <View style={styles.topicChip}>
              <Feather name="briefcase" size={13} color={Palette.primary} />
              <Text style={styles.topicChipText}>Placement</Text>
            </View>
          </View>

          <TouchableOpacity
            style={styles.exploreBtn}
            onPress={() => router.push("/engineering" as any)}
            activeOpacity={0.85}
          >
            <Text style={styles.exploreBtnText}>Explore Engineering</Text>
            <Feather name="arrow-right" size={16} color="#FFFFFF" />
          </TouchableOpacity>
        </View>

        {/* 2. Competitive Exams Card */}
        <View style={styles.pathCard}>
          <View style={styles.cardTopRow}>
            <View style={[styles.iconCircle, { backgroundColor: Palette.warningLight }]}>
              <Feather name="award" size={26} color={Palette.warning} />
            </View>
            <View style={[styles.badge, { backgroundColor: Palette.warningLight }]}>
              <Text style={[styles.badgeText, { color: Palette.warning }]}>6 Subjects • 5,000+ Questions</Text>
            </View>
          </View>

          <Text style={styles.cardTitle}>Competitive Exams</Text>
          <Text style={styles.cardDesc}>
            Prepare for aptitude, reasoning, English and general awareness.
          </Text>

          {/* Module Topics List */}
          <View style={styles.topicsRow}>
            <View style={styles.topicChip}>
              <Feather name="percent" size={13} color={Palette.warning} />
              <Text style={styles.topicChipText}>Aptitude</Text>
            </View>
            <View style={styles.topicChip}>
              <Feather name="activity" size={13} color={Palette.warning} />
              <Text style={styles.topicChipText}>Reasoning</Text>
            </View>
            <View style={styles.topicChip}>
              <Feather name="book-open" size={13} color={Palette.warning} />
              <Text style={styles.topicChipText}>English</Text>
            </View>
            <View style={styles.topicChip}>
              <Feather name="globe" size={13} color={Palette.warning} />
              <Text style={styles.topicChipText}>GK</Text>
            </View>
            <View style={styles.topicChip}>
              <Feather name="layers" size={13} color={Palette.warning} />
              <Text style={styles.topicChipText}>Science</Text>
            </View>
          </View>

          <TouchableOpacity
            style={[styles.exploreBtn, { backgroundColor: Palette.primary }]}
            onPress={() => router.push("/competitive" as any)}
            activeOpacity={0.85}
          >
            <Text style={styles.exploreBtnText}>Explore Competitive</Text>
            <Feather name="arrow-right" size={16} color="#FFFFFF" />
          </TouchableOpacity>
        </View>

        {/* 3. Faculty & Educator Portal Card */}
        <View style={styles.pathCard}>
          <View style={styles.cardTopRow}>
            <View style={[styles.iconCircle, { backgroundColor: Palette.aiPurpleLight }]}>
              <Feather name="edit-3" size={24} color={Palette.aiPurple} />
            </View>
            <View style={[styles.badge, { backgroundColor: Palette.aiPurpleLight }]}>
              <Text style={[styles.badgeText, { color: Palette.aiPurple }]}>Faculty & Educator Mode</Text>
            </View>
          </View>

          <Text style={styles.cardTitle}>Faculty Assessment Portal</Text>
          <Text style={styles.cardDesc}>
            Create, edit, and publish topic-based 4-option MCQs directly to student quizzes.
          </Text>

          <TouchableOpacity
            style={[styles.exploreBtn, { backgroundColor: Palette.aiPurple }]}
            onPress={() => router.push("/faculty" as any)}
            activeOpacity={0.85}
          >
            <Text style={styles.exploreBtnText}>Open Faculty Portal</Text>
            <Feather name="arrow-right" size={16} color="#FFFFFF" />
          </TouchableOpacity>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: Palette.background,
  },
  scrollContent: {
    paddingHorizontal: 16,
    paddingTop: 20,
    paddingBottom: 40,
  },
  header: {
    marginBottom: 22,
  },
  title: {
    fontSize: 22,
    fontWeight: "800",
    color: Palette.textTitle,
    marginBottom: 4,
  },
  subtitle: {
    fontSize: 14,
    color: Palette.textSecondary,
  },
  pathCard: {
    backgroundColor: "#FFFFFF",
    borderRadius: Radii.cardLarge,
    padding: 20,
    borderWidth: 1,
    borderColor: Palette.border,
    marginBottom: 20,
    ...Shadows.card,
  },
  cardTopRow: {
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
    marginBottom: 14,
  },
  iconCircle: {
    width: 48,
    height: 48,
    borderRadius: 14,
    backgroundColor: Palette.primaryLight,
    alignItems: "center",
    justifyContent: "center",
  },
  badge: {
    backgroundColor: Palette.primaryLight,
    paddingHorizontal: 10,
    paddingVertical: 5,
    borderRadius: 8,
  },
  badgeText: {
    fontSize: 12,
    fontWeight: "700",
    color: Palette.primary,
  },
  cardTitle: {
    fontSize: 18,
    fontWeight: "800",
    color: Palette.textTitle,
    marginBottom: 6,
  },
  cardDesc: {
    fontSize: 13.5,
    color: Palette.textBody,
    lineHeight: 20,
    marginBottom: 16,
  },
  topicsRow: {
    flexDirection: "row",
    flexWrap: "wrap",
    gap: 8,
    marginBottom: 18,
  },
  topicChip: {
    flexDirection: "row",
    alignItems: "center",
    gap: 5,
    backgroundColor: Palette.backgroundSecondary,
    paddingVertical: 5,
    paddingHorizontal: 10,
    borderRadius: 8,
    borderWidth: 1,
    borderColor: Palette.border,
  },
  topicChipText: {
    fontSize: 12,
    color: Palette.textTitle,
    fontWeight: "600",
  },
  exploreBtn: {
    backgroundColor: Palette.primary,
    borderRadius: Radii.button,
    paddingVertical: 13,
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
    gap: 8,
    ...Shadows.button,
  },
  exploreBtnText: {
    color: "#FFFFFF",
    fontSize: 14.5,
    fontWeight: "700",
  },
});