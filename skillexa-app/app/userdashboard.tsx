import { Feather } from "@expo/vector-icons";
import { LinearGradient } from "expo-linear-gradient";
import { router } from "expo-router";
import React from "react";
import {
  Dimensions,
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from "react-native";
import { GlassCard } from "../components/ui/GlassCard";
import { Gradients, Palette } from "../constants/theme";

const { width } = Dimensions.get("window");
const CARD_WIDTH = (width - 48) / 2;

const MODULES = [
  {
    title: "Introduction to Python Core",
    duration: "25 min",
    progress: 1.0,
    progressLabel: "100% Complete",
    buttonText: "Resume Track",
    isActive: true,
    route: "/subjectdashboard",
  },
  {
    title: "Variables & Memory Registers",
    duration: "40 min",
    progress: 0.3,
    progressLabel: "30% Complete",
    buttonText: "Launch Unit",
    isActive: true,
    route: "/subjectdashboard",
  },
  {
    title: "Advanced Data Structures",
    duration: "90 min",
    progress: 0.0,
    progressLabel: "Locked",
    buttonText: "Unlock Unit 2 First",
    isActive: false,
    route: "/subjectdashboard",
  },
  {
    title: "Conditional Logic & Loops",
    duration: "45 min",
    progress: 0.0,
    progressLabel: "Locked",
    buttonText: "Unlock Unit 3 First",
    isActive: false,
    route: "/subjectdashboard",
  },
];

export default function UserDashboard() {
  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="light-content" backgroundColor="#070B14" />

      {/* Ambient background glows */}
      <View style={styles.ambientContainer} pointerEvents="none">
        <View style={styles.glowOrbTop} />
        <View style={styles.glowOrbRight} />
      </View>

      <ScrollView contentContainerStyle={styles.container} showsVerticalScrollIndicator={false}>
        
        {/* Top Header */}
        <View style={styles.topBar}>
          <TouchableOpacity
            style={styles.backBtn}
            onPress={() => router.back()}
            activeOpacity={0.8}
          >
            <Feather name="chevron-left" size={20} color="#FFFFFF" />
          </TouchableOpacity>
          <View style={styles.headerTextGroup}>
            <Text style={styles.sectionLabel}>TRACK CURRICULUM</Text>
            <Text style={styles.headerTitle}>Python Master Syllabus</Text>
          </View>
        </View>

        {/* Stats Row */}
        <View style={styles.statsRow}>
          {/* Streak Card */}
          <GlassCard style={styles.statCard} borderColor={Palette.amberGlow} glow>
            <View style={styles.statTopRow}>
              <Text style={styles.statEmoji}>🔥</Text>
              <Text style={styles.statBadge}>STREAK</Text>
            </View>
            <Text style={styles.topCardValue}>12 Days</Text>
            <Text style={styles.topCardLabel}>Daily Fire Streak</Text>
          </GlassCard>

          {/* XP Card */}
          <GlassCard style={styles.statCard} borderColor={Palette.cyanGlow} glow>
            <View style={styles.statTopRow}>
              <Text style={styles.statEmoji}>⚡</Text>
              <Text style={[styles.statBadge, { color: Palette.cyanLight, backgroundColor: 'rgba(6, 182, 212, 0.15)' }]}>EXP</Text>
            </View>
            <Text style={styles.topCardValue}>2,450</Text>
            <Text style={styles.topCardLabel}>Platform XP</Text>
          </GlassCard>
        </View>

        {/* Syllabus Modules Header */}
        <View style={styles.modulesHeader}>
          <Text style={styles.modulesTitle}>Curriculum Modules</Text>
          <Text style={styles.modulesSubtitle}>Structured chapter units</Text>
        </View>

        {/* Modules Grid */}
        <View style={styles.modulesGrid}>
          {MODULES.map((item, index) => (
            <GlassCard
              key={index}
              style={[styles.moduleCard, !item.isActive && styles.moduleCardLocked]}
              borderColor={item.isActive ? Palette.glassBorderCyan : Palette.glassBorder}
            >
              <View style={styles.moduleTop}>
                <Text style={styles.moduleIndex}>MODULE {index + 1}</Text>
                {!item.isActive ? (
                  <View style={styles.lockBadge}>
                    <Feather name="lock" size={10} color={Palette.textMutedDark} />
                    <Text style={styles.lockLabel}>Locked</Text>
                  </View>
                ) : (
                  <View style={styles.activeBadge}>
                    <Feather name="check" size={10} color={Palette.emerald} />
                  </View>
                )}
              </View>

              <Text style={styles.moduleTitle} numberOfLines={2}>{item.title}</Text>
              <Text style={styles.moduleMeta}>{item.duration}</Text>

              {/* Progress */}
              <View style={styles.moduleProgressContainer}>
                <View style={styles.progressBarBackground}>
                  <LinearGradient
                    colors={item.isActive ? Gradients.cyanBlue : ['#334155', '#1e293b']}
                    start={{ x: 0, y: 0 }}
                    end={{ x: 1, y: 0 }}
                    style={[styles.progressBarFill, { width: `${item.progress * 100}%` }]}
                  />
                </View>
                <Text style={styles.moduleProgressText}>{item.progressLabel}</Text>
              </View>

              <TouchableOpacity
                style={styles.moduleButton}
                activeOpacity={item.isActive ? 0.8 : 1}
                onPress={() => item.isActive && router.push(item.route as any)}
                disabled={!item.isActive}
              >
                <LinearGradient
                  colors={item.isActive ? Gradients.cyanBlue : ['#1e293b', '#0f172a']}
                  start={{ x: 0, y: 0 }}
                  end={{ x: 1, y: 0 }}
                  style={styles.moduleBtnGradient}
                >
                  <Text style={[styles.buttonText, !item.isActive && styles.buttonTextDisabled]}>
                    {item.buttonText}
                  </Text>
                </LinearGradient>
              </TouchableOpacity>
            </GlassCard>
          ))}
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: Palette.bgDark,
  },
  ambientContainer: {
    ...StyleSheet.absoluteFill,
    overflow: "hidden",
  },
  glowOrbTop: {
    position: "absolute",
    top: -50,
    left: -40,
    width: 250,
    height: 250,
    borderRadius: 125,
    backgroundColor: "rgba(6, 182, 212, 0.14)",
  },
  glowOrbRight: {
    position: "absolute",
    top: 250,
    right: -40,
    width: 280,
    height: 280,
    borderRadius: 140,
    backgroundColor: "rgba(99, 102, 241, 0.12)",
  },
  container: {
    paddingHorizontal: 18,
    paddingTop: 14,
    paddingBottom: 32,
  },
  topBar: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 20,
  },
  backBtn: {
    width: 40,
    height: 40,
    borderRadius: 20,
    backgroundColor: 'rgba(255, 255, 255, 0.08)',
    borderWidth: 1,
    borderColor: Palette.glassBorder,
    alignItems: 'center',
    justifyContent: 'center',
    marginRight: 12,
  },
  headerTextGroup: {
    flex: 1,
  },
  sectionLabel: {
    fontSize: 11,
    fontWeight: "800",
    letterSpacing: 1.2,
    color: Palette.cyan,
    marginBottom: 2,
  },
  headerTitle: {
    fontSize: 22,
    fontWeight: "900",
    color: "#FFFFFF",
  },
  statsRow: {
    flexDirection: "row",
    gap: 12,
    marginBottom: 24,
  },
  statCard: {
    flex: 1,
    borderRadius: 20,
    padding: 4,
  },
  statTopRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: 8,
  },
  statEmoji: {
    fontSize: 20,
  },
  statBadge: {
    fontSize: 9,
    fontWeight: '800',
    color: Palette.amberLight,
    backgroundColor: 'rgba(245, 158, 11, 0.15)',
    paddingVertical: 2,
    paddingHorizontal: 6,
    borderRadius: 6,
  },
  topCardValue: {
    fontSize: 24,
    fontWeight: "900",
    color: "#FFFFFF",
    marginBottom: 2,
  },
  topCardLabel: {
    fontSize: 11,
    color: Palette.textMutedDark,
    fontWeight: "600",
  },
  modulesHeader: {
    marginBottom: 14,
  },
  modulesTitle: {
    fontSize: 18,
    fontWeight: "800",
    color: "#FFFFFF",
  },
  modulesSubtitle: {
    fontSize: 12,
    color: Palette.textMutedDark,
  },
  modulesGrid: {
    flexDirection: "row",
    flexWrap: "wrap",
    justifyContent: "space-between",
  },
  moduleCard: {
    width: CARD_WIDTH,
    borderRadius: 20,
    marginBottom: 14,
  },
  moduleCardLocked: {
    opacity: 0.55,
  },
  moduleTop: {
    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",
    marginBottom: 10,
  },
  moduleIndex: {
    fontSize: 10,
    fontWeight: "800",
    color: Palette.cyanLight,
    letterSpacing: 0.8,
  },
  lockBadge: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 4,
    backgroundColor: 'rgba(255, 255, 255, 0.05)',
    paddingVertical: 2,
    paddingHorizontal: 6,
    borderRadius: 6,
  },
  lockLabel: {
    fontSize: 9,
    fontWeight: "700",
    color: Palette.textMutedDark,
    textTransform: "uppercase",
  },
  activeBadge: {
    width: 18,
    height: 18,
    borderRadius: 9,
    backgroundColor: 'rgba(16, 185, 129, 0.15)',
    alignItems: 'center',
    justifyContent: 'center',
  },
  moduleTitle: {
    fontSize: 14,
    fontWeight: "800",
    color: "#FFFFFF",
    marginBottom: 6,
    minHeight: 38,
  },
  moduleMeta: {
    fontSize: 11,
    color: Palette.textMutedDark,
    marginBottom: 12,
  },
  moduleProgressContainer: {
    marginBottom: 14,
  },
  progressBarBackground: {
    height: 4,
    backgroundColor: 'rgba(255, 255, 255, 0.1)',
    borderRadius: 2,
    overflow: 'hidden',
    marginBottom: 6,
  },
  progressBarFill: {
    height: '100%',
    borderRadius: 2,
  },
  moduleProgressText: {
    fontSize: 11,
    color: Palette.textSecondaryDark,
    fontWeight: "700",
  },
  moduleButton: {
    borderRadius: 12,
    overflow: 'hidden',
  },
  moduleBtnGradient: {
    paddingVertical: 10,
    alignItems: "center",
    justifyContent: "center",
    paddingHorizontal: 8,
  },
  buttonText: {
    color: "#FFFFFF",
    fontWeight: "700",
    fontSize: 12,
    textAlign: 'center',
  },
  buttonTextDisabled: {
    color: Palette.textMutedDark,
  },
});