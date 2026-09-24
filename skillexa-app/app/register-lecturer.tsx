import { Feather } from "@expo/vector-icons";
import { router } from "expo-router";
import React, { useState } from "react";
import {
  KeyboardAvoidingView,
  Platform,
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  View,
} from "react-native";
import { useAuth } from "../components/auth-context";
import { GlassCard } from "../components/ui/GlassCard";
import { GradientButton } from "../components/ui/GradientButton";
import { Gradients, Palette } from "../constants/theme";

export default function RegisterLecturer() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [mobile, setMobile] = useState("");
  const [collegeName, setCollegeName] = useState("KVG College of Engineering");
  const [department, setDepartment] = useState("ECE");
  const [qualification, setQualification] = useState("");
  const [experience, setExperience] = useState("");
  const [skills, setSkills] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const { login } = useAuth();

  const handleRegister = () => {
    setIsLoading(true);
    setTimeout(() => {
      setIsLoading(false);
      login({
        name: name || "Prof. " + (name || "Educator"),
        email,
        password,
        role: "FACULTY",
        collegeId: "clg-kvg",
        collegeName: collegeName || "KVG College of Engineering",
        department: department || "ECE",
        facultyDesignation: qualification ? `Faculty (${qualification})` : "Associate Professor",
        subjectsTaught: skills ? skills.split(",").map((s) => s.trim()) : ["Embedded Systems", "Microcontrollers"],
        verificationStatus: "APPROVED",
      });
      router.replace("/faculty-dashboard" as any);
    }, 400);
  };

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="light-content" backgroundColor="#070B14" />

      <View style={styles.ambientContainer} pointerEvents="none">
        <View style={styles.glowOrbTop} />
        <View style={styles.glowOrbBottom} />
      </View>

      <KeyboardAvoidingView
        behavior={Platform.OS === "ios" ? "padding" : "height"}
        style={styles.keyboardView}
      >
        <ScrollView
          contentContainerStyle={styles.scrollContent}
          keyboardShouldPersistTaps="handled"
          showsVerticalScrollIndicator={false}
        >
          {/* Header */}
          <View style={styles.header}>
            <TouchableOpacity
              style={styles.backButton}
              onPress={() => router.back()}
              activeOpacity={0.8}
            >
              <Feather name="arrow-left" size={20} color="#FFFFFF" />
            </TouchableOpacity>
            <View style={styles.headerTextGroup}>
              <Text style={styles.badge}>FACULTY REGISTRATION</Text>
              <Text style={styles.title}>Educator Onboarding</Text>
            </View>
          </View>

          {/* Form Card */}
          <GlassCard
            style={styles.formCard}
            gradientColors={Gradients.darkGlass}
            borderColor={Palette.glassBorderPrimary}
            glow
          >
            {/* Full Name */}
            <View style={styles.inputWrapper}>
              <Feather name="user" size={18} color={Palette.purpleLight} style={styles.inputIcon} />
              <TextInput
                placeholder="Full Name (e.g. Dr. Alan Turing)"
                placeholderTextColor={Palette.textMutedDark}
                style={styles.input}
                value={name}
                onChangeText={setName}
              />
            </View>

            {/* Email */}
            <View style={styles.inputWrapper}>
              <Feather name="mail" size={18} color={Palette.purpleLight} style={styles.inputIcon} />
              <TextInput
                placeholder="Institutional / Personal Email"
                placeholderTextColor={Palette.textMutedDark}
                style={styles.input}
                keyboardType="email-address"
                autoCapitalize="none"
                value={email}
                onChangeText={setEmail}
              />
            </View>

            {/* Mobile */}
            <View style={styles.inputWrapper}>
              <Feather name="phone" size={18} color={Palette.purpleLight} style={styles.inputIcon} />
              <TextInput
                placeholder="Mobile Contact"
                placeholderTextColor={Palette.textMutedDark}
                style={styles.input}
                keyboardType="phone-pad"
                value={mobile}
                onChangeText={setMobile}
              />
            </View>

            {/* College Name */}
            <View style={styles.inputWrapper}>
              <Feather name="book-open" size={18} color={Palette.purpleLight} style={styles.inputIcon} />
              <TextInput
                placeholder="Affiliated College / Institution"
                placeholderTextColor={Palette.textMutedDark}
                style={styles.input}
                value={collegeName}
                onChangeText={setCollegeName}
              />
            </View>

            {/* Department */}
            <View style={styles.inputWrapper}>
              <Feather name="layers" size={18} color={Palette.purpleLight} style={styles.inputIcon} />
              <TextInput
                placeholder="Department (e.g. ECE, CSE)"
                placeholderTextColor={Palette.textMutedDark}
                style={styles.input}
                value={department}
                onChangeText={setDepartment}
              />
            </View>

            {/* Qualification */}
            <View style={styles.inputWrapper}>
              <Feather name="award" size={18} color={Palette.purpleLight} style={styles.inputIcon} />
              <TextInput
                placeholder="Highest Qualification (e.g. Ph.D, M.Tech)"
                placeholderTextColor={Palette.textMutedDark}
                style={styles.input}
                value={qualification}
                onChangeText={setQualification}
              />
            </View>

            {/* Experience */}
            <View style={styles.inputWrapper}>
              <Feather name="briefcase" size={18} color={Palette.purpleLight} style={styles.inputIcon} />
              <TextInput
                placeholder="Teaching Experience (e.g. 5+ Years)"
                placeholderTextColor={Palette.textMutedDark}
                style={styles.input}
                value={experience}
                onChangeText={setExperience}
              />
            </View>

            {/* Core Domain / Skills */}
            <View style={styles.inputWrapper}>
              <Feather name="code" size={18} color={Palette.purpleLight} style={styles.inputIcon} />
              <TextInput
                placeholder="Specializations (e.g. DSA, Cloud, OS)"
                placeholderTextColor={Palette.textMutedDark}
                style={styles.input}
                value={skills}
                onChangeText={setSkills}
              />
            </View>

            {/* Password */}
            <View style={styles.inputWrapper}>
              <Feather name="lock" size={18} color={Palette.purpleLight} style={styles.inputIcon} />
              <TextInput
                placeholder="Secure Password"
                placeholderTextColor={Palette.textMutedDark}
                secureTextEntry={!showPassword}
                style={styles.input}
                value={password}
                onChangeText={setPassword}
              />
              <TouchableOpacity
                onPress={() => setShowPassword(!showPassword)}
                style={styles.eyeButton}
              >
                <Feather
                  name={showPassword ? "eye-off" : "eye"}
                  size={18}
                  color={Palette.textMutedDark}
                />
              </TouchableOpacity>
            </View>

            {/* Submit */}
            <GradientButton
              title="Register as Faculty"
              onPress={handleRegister}
              loading={isLoading}
              gradientColors={Gradients.purpleIndigo}
              style={styles.registerBtn}
            />

            {/* Redirect */}
            <TouchableOpacity
              activeOpacity={0.8}
              onPress={() => router.replace("/login")}
              style={styles.loginRedirect}
            >
              <Text style={styles.loginRedirectText}>
                Already have an account? <Text style={styles.loginHighlight}>Sign In</Text>
              </Text>
            </TouchableOpacity>
          </GlassCard>
        </ScrollView>
      </KeyboardAvoidingView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: Palette.bgDark,
  },
  keyboardView: {
    flex: 1,
  },
  ambientContainer: {
    ...StyleSheet.absoluteFillObject,
    overflow: "hidden",
  },
  glowOrbTop: {
    position: "absolute",
    top: -50,
    right: -40,
    width: 250,
    height: 250,
    borderRadius: 125,
    backgroundColor: "rgba(139, 92, 246, 0.16)",
  },
  glowOrbBottom: {
    position: "absolute",
    bottom: -60,
    left: -40,
    width: 280,
    height: 280,
    borderRadius: 140,
    backgroundColor: "rgba(6, 182, 212, 0.14)",
  },
  scrollContent: {
    flexGrow: 1,
    paddingHorizontal: 22,
    paddingTop: 16,
    paddingBottom: 32,
  },
  header: {
    flexDirection: "row",
    alignItems: "center",
    marginBottom: 20,
  },
  backButton: {
    width: 42,
    height: 42,
    borderRadius: 21,
    backgroundColor: "rgba(255, 255, 255, 0.08)",
    borderWidth: 1,
    borderColor: Palette.glassBorder,
    alignItems: "center",
    justifyContent: "center",
    marginRight: 14,
  },
  headerTextGroup: {
    flex: 1,
  },
  badge: {
    fontSize: 11,
    fontWeight: "800",
    color: Palette.purpleLight,
    letterSpacing: 1.2,
    marginBottom: 2,
  },
  title: {
    fontSize: 22,
    fontWeight: "900",
    color: "#FFFFFF",
  },
  formCard: {
    borderRadius: 24,
    padding: 6,
  },
  inputWrapper: {
    flexDirection: "row",
    alignItems: "center",
    backgroundColor: "rgba(15, 23, 42, 0.75)",
    borderRadius: 14,
    borderWidth: 1,
    borderColor: Palette.glassBorder,
    marginBottom: 12,
    paddingHorizontal: 14,
  },
  inputIcon: {
    marginRight: 10,
  },
  input: {
    flex: 1,
    paddingVertical: 13,
    fontSize: 14,
    color: "#FFFFFF",
  },
  eyeButton: {
    padding: 6,
  },
  registerBtn: {
    marginTop: 8,
    marginBottom: 14,
  },
  loginRedirect: {
    alignItems: "center",
    paddingVertical: 6,
  },
  loginRedirectText: {
    color: Palette.textSecondaryDark,
    fontSize: 14,
  },
  loginHighlight: {
    color: Palette.purpleLight,
    fontWeight: "700",
  },
});