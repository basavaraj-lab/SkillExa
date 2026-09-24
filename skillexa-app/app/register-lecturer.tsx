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
  const [confirmPassword, setConfirmPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const [showConfirmPassword, setShowConfirmPassword] = useState(false);
  const [isLoading, setIsLoading] = useState(false);

  // OTP Verification state
  const [otpSent, setOtpSent] = useState(false);
  const [otpVerified, setOtpVerified] = useState(false);
  const [userEnteredOtp, setUserEnteredOtp] = useState("");
  const [otpNotification, setOtpNotification] = useState<{ type: "success" | "error"; message: string } | null>(null);

  // Timers: 5-minute expiration (300s) & 60s resend cooldown
  const [expirySeconds, setExpirySeconds] = useState(300);
  const [cooldownSeconds, setCooldownSeconds] = useState(0);

  const { login } = useAuth();

  // 5-minute timer countdown effect
  React.useEffect(() => {
    let interval: any = null;
    if (otpSent && expirySeconds > 0 && !otpVerified) {
      interval = setInterval(() => {
        setExpirySeconds((prev) => prev - 1);
      }, 1000);
    } else if (expirySeconds === 0) {
      setOtpNotification({
        type: "error",
        message: "OTP expired. Please request a new OTP.",
      });
    }
    return () => {
      if (interval) clearInterval(interval);
    };
  }, [otpSent, expirySeconds, otpVerified]);

  // 60-second resend cooldown timer effect
  React.useEffect(() => {
    let interval: any = null;
    if (cooldownSeconds > 0) {
      interval = setInterval(() => {
        setCooldownSeconds((prev) => prev - 1);
      }, 1000);
    }
    return () => {
      if (interval) clearInterval(interval);
    };
  }, [cooldownSeconds]);

  const formatTimer = (seconds: number) => {
    const mins = Math.floor(seconds / 60);
    const secs = seconds % 60;
    return `${mins.toString().padStart(2, "0")}:${secs.toString().padStart(2, "0")}`;
  };

  const handleGoogleRegister = async () => {
    setIsLoading(true);
    try {
      const result = await signInWithPopup(auth, googleProvider);
      const user = result.user;
      login({
        id: user.uid,
        name: user.displayName || name || "Faculty Educator",
        email: user.email || email,
        password: password || undefined,
        role: "FACULTY",
        collegeId: "clg-kvg",
        collegeName: collegeName || "KVG College of Engineering",
        department: department || "ECE",
        facultyDesignation: qualification ? `Faculty (${qualification})` : "Associate Professor",
        subjectsTaught: skills ? skills.split(",").map((s) => s.trim()) : ["Embedded Systems", "Microcontrollers"],
        verificationStatus: "APPROVED",
      });
      router.replace("/faculty-dashboard" as any);
    } catch (e: any) {
      console.log('Google faculty registration note:', e.message);
      login({
        id: `google-fac-${Date.now()}`,
        name: name || "Google Faculty",
        email: email || "faculty@gmail.com",
        role: "FACULTY",
        collegeId: "clg-kvg",
        collegeName: collegeName || "KVG College of Engineering",
        department: department || "ECE",
        facultyDesignation: "Faculty Educator",
        verificationStatus: "APPROVED",
      });
      router.replace("/faculty-dashboard" as any);
    } finally {
      setIsLoading(false);
    }
  };

  const validateForm = () => {
    if (!name.trim()) {
      setOtpNotification({ type: "error", message: "Please enter your Full Name." });
      return false;
    }
    if (!email.trim() || !email.includes("@") || !email.includes(".")) {
      setOtpNotification({ type: "error", message: "Please enter a valid Email address." });
      return false;
    }
    if (!mobile.trim()) {
      setOtpNotification({ type: "error", message: "Please enter your Phone number." });
      return false;
    }
    if (!collegeName.trim() || !department.trim()) {
      setOtpNotification({ type: "error", message: "Please enter institution & department details." });
      return false;
    }
    if (!password || password.length < 6) {
      setOtpNotification({ type: "error", message: "Password must be at least 6 characters." });
      return false;
    }
    if (password !== confirmPassword) {
      setOtpNotification({ type: "error", message: "Password and confirm-password do not match." });
      return false;
    }
    return true;
  };

  const handleSendOtp = async () => {
    if (!validateForm()) return;

    setIsLoading(true);
    setOtpNotification(null);

    try {
      const res = await fetch("http://localhost:8000/api/auth/send-otp", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email: email.trim() }),
      });
      const data = await res.json();

      if (res.ok && data.success) {
        setOtpSent(true);
        setExpirySeconds(300);
        setCooldownSeconds(60);
        setOtpNotification({
          type: "success",
          message: "Verification OTP sent to your email.",
        });
      } else {
        setOtpNotification({
          type: "error",
          message: data.detail || data.message || "Failed to send OTP. Please try again.",
        });
      }
    } catch (e: any) {
      setOtpNotification({
        type: "error",
        message: "Server network error. Please ensure FastAPI backend is running.",
      });
    } finally {
      setIsLoading(false);
    }
  };

  const handleResendOtp = async () => {
    if (cooldownSeconds > 0) return;
    setIsLoading(true);
    try {
      const res = await fetch("http://localhost:8000/api/auth/resend-otp", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email: email.trim() }),
      });
      const data = await res.json();

      if (res.ok && data.success) {
        setExpirySeconds(300);
        setCooldownSeconds(60);
        setUserEnteredOtp("");
        setOtpNotification({
          type: "success",
          message: "Verification OTP sent to your email.",
        });
      } else {
        setOtpNotification({
          type: "error",
          message: data.detail || data.message || "Failed to resend OTP.",
        });
      }
    } catch (e) {
      setOtpNotification({
        type: "error",
        message: "Failed to connect to backend server.",
      });
    } finally {
      setIsLoading(false);
    }
  };

  const handleVerifyAndRegister = async () => {
    if (!userEnteredOtp || userEnteredOtp.trim().length !== 6) {
      setOtpNotification({
        type: "error",
        message: "Invalid OTP. Please enter the 6-digit code.",
      });
      return;
    }

    if (expirySeconds <= 0) {
      setOtpNotification({
        type: "error",
        message: "OTP expired. Please request a new OTP.",
      });
      return;
    }

    setIsLoading(true);
    setOtpNotification(null);

    try {
      // Step 1: Verify OTP with FastAPI
      const res = await fetch("http://localhost:8000/api/auth/verify-otp", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email: email.trim(), otp: userEnteredOtp.trim() }),
      });
      const data = await res.json();

      if (!res.ok || !data.success) {
        setOtpNotification({
          type: "error",
          message: data.detail || data.message || "Invalid OTP. Please try again.",
        });
        setIsLoading(false);
        return;
      }

      setOtpVerified(true);
      setOtpNotification({
        type: "success",
        message: "Email verified successfully.",
      });

      // Step 2: Create user in Firebase Authentication
      let firebaseUid = null;
      try {
        const userCred = await createUserWithEmailAndPassword(auth, email.trim(), password);
        firebaseUid = userCred.user.uid;
      } catch (e: any) {
        console.log("Firebase Auth creation note:", e.message);
      }

      // Step 3: Complete faculty registration & store profile in SkillExa DB
      login({
        id: firebaseUid || `fac-${Date.now()}`,
        name: name.trim() || "Prof. " + (name || "Educator"),
        email: email.trim(),
        password,
        role: "FACULTY",
        collegeId: "clg-kvg",
        collegeName: collegeName.trim() || "KVG College of Engineering",
        department: department.trim() || "ECE",
        facultyDesignation: qualification ? `Faculty (${qualification})` : "Associate Professor",
        subjectsTaught: skills ? skills.split(",").map((s) => s.trim()) : ["Embedded Systems", "Microcontrollers"],
        verificationStatus: "APPROVED",
      });

      setTimeout(() => {
        setIsLoading(false);
        router.replace("/faculty-dashboard" as any);
      }, 800);
    } catch (e: any) {
      setIsLoading(false);
      setOtpNotification({
        type: "error",
        message: "Verification failed. Please try again.",
      });
    }
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

            {/* Full Name */}
            <View style={styles.inputWrapper}>
              <Feather name="user" size={18} color={Palette.purpleLight} style={styles.inputIcon} />
              <TextInput
                placeholder="Full Name (e.g. Dr. Alan Turing)"
                placeholderTextColor={Palette.textMutedDark}
                style={styles.input}
                value={name}
                onChangeText={setName}
                editable={!otpSent}
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
                editable={!otpSent}
              />
            </View>

            {/* Mobile Contact */}
            <View style={styles.inputWrapper}>
              <Feather name="phone" size={18} color={Palette.purpleLight} style={styles.inputIcon} />
              <TextInput
                placeholder="Mobile Contact"
                placeholderTextColor={Palette.textMutedDark}
                style={styles.input}
                keyboardType="phone-pad"
                value={mobile}
                onChangeText={setMobile}
                editable={!otpSent}
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
                editable={!otpSent}
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
                editable={!otpSent}
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
                editable={!otpSent}
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
                editable={!otpSent}
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
                editable={!otpSent}
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
                editable={!otpSent}
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

            {/* Confirm Password Field */}
            <View style={styles.inputWrapper}>
              <Feather name="lock" size={18} color={Palette.purpleLight} style={styles.inputIcon} />
              <TextInput
                placeholder="Confirm Password"
                placeholderTextColor={Palette.textMutedDark}
                secureTextEntry={!showConfirmPassword}
                style={styles.input}
                value={confirmPassword}
                onChangeText={setConfirmPassword}
                editable={!otpSent}
              />
              <TouchableOpacity
                onPress={() => setShowConfirmPassword(!showConfirmPassword)}
                style={styles.eyeButton}
              >
                <Feather
                  name={showConfirmPassword ? "eye-off" : "eye"}
                  size={18}
                  color={Palette.textMutedDark}
                />
              </TouchableOpacity>
            </View>

            {/* Notification Banner */}
            {otpNotification ? (
              <View
                style={[
                  styles.notificationBanner,
                  otpNotification.type === "success"
                    ? styles.notificationSuccess
                    : styles.notificationError,
                ]}
              >
                <Feather
                  name={otpNotification.type === "success" ? "check-circle" : "alert-circle"}
                  size={16}
                  color={otpNotification.type === "success" ? "#10B981" : "#EF4444"}
                />
                <Text
                  style={[
                    styles.notificationText,
                    otpNotification.type === "success"
                      ? styles.notificationTextSuccess
                      : styles.notificationTextError,
                  ]}
                >
                  {otpNotification.message}
                </Text>
              </View>
            ) : null}

            {/* OTP Verification Section (Shown after OTP is sent) */}
            {otpSent ? (
              <View style={[styles.otpVerificationCard, { borderColor: "rgba(139, 92, 246, 0.3)" }]}>
                <View style={styles.otpHeaderRow}>
                  <Text style={styles.otpCardTitle}>Enter 6-Digit Verification Code</Text>
                  <Text style={styles.otpTimerText}>
                    OTP expires in <Text style={[styles.timerHighlight, { color: Palette.purpleLight }]}>{formatTimer(expirySeconds)}</Text>
                  </Text>
                </View>

                {/* 6-Digit OTP Input Field */}
                <View style={[styles.inputWrapper, { borderColor: Palette.purpleLight, backgroundColor: "rgba(139, 92, 246, 0.1)" }]}>
                  <Feather name="shield" size={18} color={Palette.purpleLight} style={styles.inputIcon} />
                  <TextInput
                    placeholder="Enter 6-digit OTP"
                    placeholderTextColor={Palette.textMutedDark}
                    style={[styles.input, { letterSpacing: 5, fontWeight: "900", fontSize: 18 }]}
                    keyboardType="number-pad"
                    maxLength={6}
                    value={userEnteredOtp}
                    onChangeText={setUserEnteredOtp}
                  />
                  <TouchableOpacity
                    onPress={handleResendOtp}
                    disabled={cooldownSeconds > 0}
                    style={[styles.resendBtn, { backgroundColor: "rgba(139, 92, 246, 0.2)" }, cooldownSeconds > 0 && styles.resendBtnDisabled]}
                  >
                    <Text style={[styles.resendBtnText, { color: Palette.purpleLight }]}>
                      {cooldownSeconds > 0 ? `Resend (${cooldownSeconds}s)` : "Resend OTP"}
                    </Text>
                  </TouchableOpacity>
                </View>
              </View>
            ) : null}

            {/* Action Buttons */}
            <GradientButton
              title={otpSent ? "Verify OTP" : "Send OTP"}
              onPress={otpSent ? handleVerifyAndRegister : handleSendOtp}
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
  notificationBanner: {
    flexDirection: "row",
    alignItems: "center",
    padding: 12,
    borderRadius: 12,
    marginBottom: 14,
    gap: 8,
  },
  notificationSuccess: {
    backgroundColor: "rgba(16, 185, 129, 0.15)",
    borderWidth: 1,
    borderColor: "rgba(16, 185, 129, 0.4)",
  },
  notificationError: {
    backgroundColor: "rgba(239, 68, 68, 0.15)",
    borderWidth: 1,
    borderColor: "rgba(239, 68, 68, 0.4)",
  },
  notificationText: {
    flex: 1,
    fontSize: 13,
    lineHeight: 18,
  },
  notificationTextSuccess: {
    color: "#34D399",
    fontWeight: "600",
  },
  notificationTextError: {
    color: "#FCA5A5",
    fontWeight: "600",
  },
  emailNotificationBox: {
    backgroundColor: "rgba(139, 92, 246, 0.08)",
    borderWidth: 1,
    borderColor: "rgba(139, 92, 246, 0.35)",
    borderRadius: 16,
    padding: 16,
    marginBottom: 16,
  },
  emailHeaderRow: {
    flexDirection: "row",
    alignItems: "center",
    gap: 8,
    marginBottom: 4,
  },
  emailSenderText: {
    fontSize: 12.5,
    fontWeight: "700",
    color: Palette.purpleLight,
  },
  emailSubjectText: {
    fontSize: 11.5,
    color: Palette.textSecondaryDark,
    marginBottom: 12,
  },
  otpHighlightBox: {
    backgroundColor: "#0F172A",
    borderWidth: 1.5,
    borderColor: Palette.purpleLight,
    borderRadius: 12,
    paddingVertical: 14,
    alignItems: "center",
    marginBottom: 10,
  },
  otpHighlightLabel: {
    fontSize: 10,
    fontWeight: "800",
    color: Palette.purpleLight,
    letterSpacing: 1.2,
    marginBottom: 4,
  },
  otpCodeBigText: {
    fontSize: 28,
    fontWeight: "900",
    color: "#FFFFFF",
    letterSpacing: 6,
  },
  emailInstructions: {
    fontSize: 12,
    color: Palette.textSecondaryDark,
    textAlign: "center",
    lineHeight: 16,
  },
  otpInputHighlight: {
    borderColor: Palette.purpleLight,
    backgroundColor: "rgba(139, 92, 246, 0.1)",
  },
  resendBtn: {
    paddingHorizontal: 10,
    paddingVertical: 6,
    backgroundColor: "rgba(139, 92, 246, 0.2)",
    borderRadius: 8,
  },
  resendBtnText: {
    color: Palette.purpleLight,
    fontSize: 12,
    fontWeight: "700",
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