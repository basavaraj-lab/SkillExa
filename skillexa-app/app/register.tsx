import { Feather } from "@expo/vector-icons";
import { LinearGradient } from "expo-linear-gradient";
import { useRouter } from "expo-router";
import React from "react";
import {
  SafeAreaView,
  StatusBar,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from "react-native";
import { GlassCard } from "../components/ui/GlassCard";
import { Gradients, Palette } from "../constants/theme";

export default function Register() {
  const router = useRouter();

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="light-content" backgroundColor="#070B14" />

      {/* Ambient background glows */}
      <View style={styles.ambientContainer} pointerEvents="none">
        <View style={styles.glowOrbTop} />
        <View style={styles.glowOrbBottom} />
      </View>

      <View style={styles.container}>
        {/* Back Button */}
        <TouchableOpacity
          style={styles.backButton}
          onPress={() => router.back()}
          activeOpacity={0.8}
        >
          <Feather name="arrow-left" size={20} color="#FFFFFF" />
        </TouchableOpacity>

        {/* Header */}
        <View style={styles.header}>
          <Text style={styles.badge}>ONBOARDING</Text>
          <Text style={styles.title}>Select Your Role</Text>
          <Text style={styles.subtitle}>
            Choose your learning or teaching profile to configure your personalized dashboard
          </Text>
        </View>

        {/* Option 1: Student / User */}
        <GlassCard
          style={styles.roleCard}
          borderColor={Palette.glassBorderCyan}
          onPress={() => router.push("/register-user")}
          glow
        >
          <View style={styles.cardContent}>
            <LinearGradient
              colors={Gradients.cyanBlue}
              start={{ x: 0, y: 0 }}
              end={{ x: 1, y: 1 }}
              style={styles.iconCircle}
            >
              <Feather name="user" size={28} color="#FFFFFF" />
            </LinearGradient>
            <View style={styles.cardTexts}>
              <View style={styles.roleRow}>
                <Text style={styles.roleTitle}>Student / Scholar</Text>
                <View style={styles.tagPill}>
                  <Text style={styles.tagText}>POPULAR</Text>
                </View>
              </View>
              <Text style={styles.roleDesc}>
                Access engineering roadmaps, coding compiler, unit quizzes, and competitive exams.
              </Text>
            </View>
            <Feather name="chevron-right" size={22} color={Palette.cyan} />
          </View>
        </GlassCard>

        {/* Option 2: Lecturer / Educator */}
        <GlassCard
          style={styles.roleCard}
          borderColor={Palette.glassBorderPrimary}
          onPress={() => router.push("/register-lecturer")}
          glow
        >
          <View style={styles.cardContent}>
            <LinearGradient
              colors={Gradients.purpleIndigo}
              start={{ x: 0, y: 0 }}
              end={{ x: 1, y: 1 }}
              style={styles.iconCircle}
            >
              <Feather name="book-open" size={28} color="#FFFFFF" />
            </LinearGradient>
            <View style={styles.cardTexts}>
              <View style={styles.roleRow}>
                <Text style={styles.roleTitle}>Educator / Lecturer</Text>
                <View style={[styles.tagPill, { backgroundColor: "rgba(139, 92, 246, 0.2)" }]}>
                  <Text style={[styles.tagText, { color: Palette.purpleLight }]}>FACULTY</Text>
                </View>
              </View>
              <Text style={styles.roleDesc}>
                Publish curriculum content, manage lab files, design quizzes, and monitor students.
              </Text>
            </View>
            <Feather name="chevron-right" size={22} color={Palette.purpleLight} />
          </View>
        </GlassCard>

        {/* Existing account footer */}
        <TouchableOpacity
          activeOpacity={0.8}
          onPress={() => router.replace("/login")}
          style={styles.loginRedirect}
        >
          <Text style={styles.loginRedirectText}>
            Already have an account? <Text style={styles.loginHighlight}>Sign In</Text>
          </Text>
        </TouchableOpacity>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: Palette.bgDark,
  },
  ambientContainer: {
    ...StyleSheet.absoluteFillObject,
    overflow: "hidden",
  },
  glowOrbTop: {
    position: "absolute",
    top: -50,
    right: -40,
    width: 240,
    height: 240,
    borderRadius: 120,
    backgroundColor: "rgba(99, 102, 241, 0.16)",
  },
  glowOrbBottom: {
    position: "absolute",
    bottom: -60,
    left: -40,
    width: 260,
    height: 260,
    borderRadius: 130,
    backgroundColor: "rgba(6, 182, 212, 0.14)",
  },
  container: {
    flex: 1,
    paddingHorizontal: 22,
    paddingTop: 16,
    justifyContent: "center",
  },
  backButton: {
    position: "absolute",
    top: 16,
    left: 22,
    width: 42,
    height: 42,
    borderRadius: 21,
    backgroundColor: "rgba(255, 255, 255, 0.08)",
    borderWidth: 1,
    borderColor: Palette.glassBorder,
    alignItems: "center",
    justifyContent: "center",
    zIndex: 10,
  },
  header: {
    marginBottom: 32,
    marginTop: 30,
  },
  badge: {
    fontSize: 11,
    fontWeight: "800",
    color: Palette.cyan,
    letterSpacing: 1.5,
    marginBottom: 8,
  },
  title: {
    fontSize: 30,
    fontWeight: "900",
    color: "#FFFFFF",
    marginBottom: 8,
  },
  subtitle: {
    fontSize: 14,
    color: Palette.textSecondaryDark,
    lineHeight: 20,
  },
  roleCard: {
    marginBottom: 20,
    borderRadius: 22,
  },
  cardContent: {
    flexDirection: "row",
    alignItems: "center",
  },
  iconCircle: {
    width: 58,
    height: 58,
    borderRadius: 29,
    alignItems: "center",
    justifyContent: "center",
    marginRight: 16,
  },
  cardTexts: {
    flex: 1,
    marginRight: 10,
  },
  roleRow: {
    flexDirection: "row",
    alignItems: "center",
    gap: 8,
    marginBottom: 4,
  },
  roleTitle: {
    fontSize: 17,
    fontWeight: "800",
    color: "#FFFFFF",
  },
  tagPill: {
    backgroundColor: "rgba(6, 182, 212, 0.2)",
    paddingVertical: 2,
    paddingHorizontal: 8,
    borderRadius: 10,
  },
  tagText: {
    fontSize: 10,
    fontWeight: "800",
    color: Palette.cyanLight,
    letterSpacing: 0.5,
  },
  roleDesc: {
    fontSize: 12,
    color: Palette.textSecondaryDark,
    lineHeight: 17,
  },
  loginRedirect: {
    marginTop: 20,
    alignItems: "center",
    paddingVertical: 10,
  },
  loginRedirectText: {
    color: Palette.textSecondaryDark,
    fontSize: 14,
  },
  loginHighlight: {
    color: Palette.cyanLight,
    fontWeight: "700",
  },
});