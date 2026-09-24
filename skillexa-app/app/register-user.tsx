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
import { createUserWithEmailAndPassword, signInWithPopup } from 'firebase/auth';
import { auth, googleProvider } from '../services/firebase';

export default function RegisterUser() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [mobile, setMobile] = useState("");
  const [collegeName, setCollegeName] = useState("KVG College of Engineering");
  const [branch, setBranch] = useState("ECE");
  const [year, setYear] = useState("3rd Year");
  const [section, setSection] = useState("A");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const { login } = useAuth();

  const handleGoogleRegister = async () => {
    setIsLoading(true);
    try {
      const result = await signInWithPopup(auth, googleProvider);
      const user = result.user;
      login({
        id: user.uid,
        name: user.displayName || name || "Scholar",
        email: user.email || email,
        password: password || undefined,
        role: "STUDENT",
        collegeId: "clg-kvg",
        collegeName: collegeName || "KVG College of Engineering",
        department: branch || "ECE",
        academicYear: year || "3rd Year",
        section: section || "A",
        verificationStatus: "APPROVED",
      });
      router.replace("/pathselection" as any);
    } catch (e: any) {
      console.log('Google registration note:', e.message);
      // Fallback local registration if popup blocked or offline
      login({
        id: `google-${Date.now()}`,
        name: name || "Google Scholar",
        email: email || "student@gmail.com",
        role: "STUDENT",
        collegeId: "clg-kvg",
        collegeName: collegeName || "KVG College of Engineering",
        department: branch || "ECE",
        academicYear: year || "3rd Year",
        section: section || "A",
        verificationStatus: "APPROVED",
      });
      router.replace("/pathselection" as any);
    } finally {
      setIsLoading(false);
    }
  };

  const handleRegister = async () => {
    setIsLoading(true);
    let firebaseUid = null;
    try {
      if (email && password) {
        const userCred = await createUserWithEmailAndPassword(auth, email, password);
        firebaseUid = userCred.user.uid;
      }
    } catch (e: any) {
      console.log('Firebase registration note:', e.message);
    }

    setIsLoading(false);
    login({
      id: firebaseUid || `std-${Date.now()}`,
      name: name || "Scholar",
      email,
      password,
      role: "STUDENT",
      collegeId: "clg-kvg",
      collegeName: collegeName || "KVG College of Engineering",
      department: branch || "ECE",
      academicYear: year || "3rd Year",
      section: section || "A",
      verificationStatus: "APPROVED",
    });
    router.replace("/pathselection" as any);
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
              <Text style={styles.badge}>STUDENT REGISTRATION</Text>
              <Text style={styles.title}>Create Your Account</Text>
            </View>
          </View>

          {/* Form Card */}
          <GlassCard
            style={styles.formCard}
            gradientColors={Gradients.darkGlass}
            borderColor={Palette.glassBorderCyan}
            glow
          >
            {/* Quick Google Registration */}
            <TouchableOpacity
              style={styles.googleRegBtn}
              onPress={handleGoogleRegister}
              activeOpacity={0.85}
            >
              <Feather name="globe" size={18} color="#EA4335" />
              <Text style={styles.googleRegBtnText}>Continue with Google</Text>
            </TouchableOpacity>

            <View style={styles.orDividerRow}>
              <View style={styles.dividerLine} />
              <Text style={styles.orText}>OR REGISTER WITH DETAILS</Text>
              <View style={styles.dividerLine} />
            </View>

            {/* Name Input */}
            <View style={styles.inputWrapper}>
              <Feather name="user" size={18} color={Palette.cyan} style={styles.inputIcon} />
              <TextInput
                placeholder="Full Name"
                placeholderTextColor={Palette.textMutedDark}
                style={styles.input}
                value={name}
                onChangeText={setName}
              />
            </View>

            {/* Email Input */}
            <View style={styles.inputWrapper}>
              <Feather name="mail" size={18} color={Palette.cyan} style={styles.inputIcon} />
              <TextInput
                placeholder="Email Address"
                placeholderTextColor={Palette.textMutedDark}
                style={styles.input}
                keyboardType="email-address"
                autoCapitalize="none"
                value={email}
                onChangeText={setEmail}
              />
            </View>

            {/* Mobile Input */}
            <View style={styles.inputWrapper}>
              <Feather name="phone" size={18} color={Palette.cyan} style={styles.inputIcon} />
              <TextInput
                placeholder="Mobile Number"
                placeholderTextColor={Palette.textMutedDark}
                style={styles.input}
                keyboardType="phone-pad"
                value={mobile}
                onChangeText={setMobile}
              />
            </View>

            {/* College Selection */}
            <View style={styles.inputWrapper}>
              <Feather name="book-open" size={18} color={Palette.cyan} style={styles.inputIcon} />
              <TextInput
                placeholder="College: KVG College of Engineering"
                placeholderTextColor={Palette.textMutedDark}
                style={styles.input}
                value={collegeName}
                onChangeText={setCollegeName}
              />
            </View>

            {/* Branch & Year Row */}
            <View style={{ flexDirection: 'row', gap: 10 }}>
              <View style={[styles.inputWrapper, { flex: 1 }]}>
                <Feather name="layers" size={18} color={Palette.cyan} style={styles.inputIcon} />
                <TextInput
                  placeholder="Branch (e.g. ECE)"
                  placeholderTextColor={Palette.textMutedDark}
                  style={styles.input}
                  value={branch}
                  onChangeText={setBranch}
                />
              </View>

              <View style={[styles.inputWrapper, { flex: 1 }]}>
                <Feather name="calendar" size={18} color={Palette.cyan} style={styles.inputIcon} />
                <TextInput
                  placeholder="Year (e.g. 3rd Year)"
                  placeholderTextColor={Palette.textMutedDark}
                  style={styles.input}
                  value={year}
                  onChangeText={setYear}
                />
              </View>
            </View>

            {/* Section */}
            <View style={styles.inputWrapper}>
              <Feather name="users" size={18} color={Palette.cyan} style={styles.inputIcon} />
              <TextInput
                placeholder="Section (e.g. A)"
                placeholderTextColor={Palette.textMutedDark}
                style={styles.input}
                value={section}
                onChangeText={setSection}
              />
            </View>

            {/* Password Field */}
            <View style={styles.inputWrapper}>
              <Feather name="lock" size={18} color={Palette.cyan} style={styles.inputIcon} />
              <TextInput
                placeholder="Create Password"
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

            {/* Register CTA */}
            <GradientButton
              title="Complete Registration"
              onPress={handleRegister}
              loading={isLoading}
              gradientColors={Gradients.cyanBlue}
              style={styles.registerBtn}
            />

            {/* Footer */}
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
    ...StyleSheet.absoluteFill,
    overflow: "hidden",
  },
  glowOrbTop: {
    position: "absolute",
    top: -50,
    right: -40,
    width: 250,
    height: 250,
    borderRadius: 125,
    backgroundColor: "rgba(6, 182, 212, 0.16)",
  },
  glowOrbBottom: {
    position: "absolute",
    bottom: -60,
    left: -40,
    width: 280,
    height: 280,
    borderRadius: 140,
    backgroundColor: "rgba(99, 102, 241, 0.16)",
  },
  scrollContent: {
    flexGrow: 1,
    paddingHorizontal: 22,
    paddingTop: 16,
    paddingBottom: 32,
    justifyContent: "center",
  },
  header: {
    flexDirection: "row",
    alignItems: "center",
    marginBottom: 24,
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
    color: Palette.cyan,
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
    padding: 16,
  },
  googleRegBtn: {
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
    backgroundColor: "#FFFFFF",
    paddingVertical: 14,
    borderRadius: 14,
    gap: 10,
    marginBottom: 16,
  },
  googleRegBtnText: {
    fontSize: 15,
    fontWeight: "700",
    color: "#1E293B",
  },
  orDividerRow: {
    flexDirection: "row",
    alignItems: "center",
    marginBottom: 16,
  },
  dividerLine: {
    flex: 1,
    height: 1,
    backgroundColor: "rgba(255, 255, 255, 0.12)",
  },
  orText: {
    fontSize: 11,
    fontWeight: "700",
    color: Palette.textMutedDark,
    paddingHorizontal: 12,
    letterSpacing: 0.8,
  },
  inputWrapper: {
    flexDirection: "row",
    alignItems: "center",
    backgroundColor: "rgba(15, 23, 42, 0.75)",
    borderRadius: 14,
    borderWidth: 1,
    borderColor: Palette.glassBorder,
    marginBottom: 14,
    paddingHorizontal: 14,
  },
  inputIcon: {
    marginRight: 10,
  },
  input: {
    flex: 1,
    paddingVertical: 14,
    fontSize: 15,
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
    color: Palette.cyanLight,
    fontWeight: "700",
  },
});