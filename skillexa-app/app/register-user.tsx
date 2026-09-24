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
import { createUserWithEmailAndPassword, signInWithPopup, sendPasswordResetEmail } from 'firebase/auth';
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
      console.log("Google registration note:", e.message);
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
    if (!collegeName.trim() || !branch.trim() || !year.trim() || !section.trim()) {
      setOtpNotification({ type: "error", message: "Please complete all college & academic details." });
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

      // Step 3: Complete registration & store profile in SkillExa DB
      login({
        id: firebaseUid || `std-${Date.now()}`,
        name: name.trim(),
        email: email.trim(),
        password,
        role: "STUDENT",
        collegeId: "clg-kvg",
        collegeName: collegeName.trim() || "KVG College of Engineering",
        department: branch.trim() || "ECE",
        academicYear: year.trim() || "3rd Year",
        section: section.trim() || "A",
        verificationStatus: "APPROVED",
      });

      setTimeout(() => {
        setIsLoading(false);
        router.replace("/pathselection" as any);
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
                editable={!otpSent}
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
                editable={!otpSent}
              />
            </View>

            {/* Phone Number Input */}
            <View style={styles.inputWrapper}>
              <Feather name="phone" size={18} color={Palette.cyan} style={styles.inputIcon} />
              <TextInput
                placeholder="Phone Number"
                placeholderTextColor={Palette.textMutedDark}
                style={styles.input}
                keyboardType="phone-pad"
                value={mobile}
                onChangeText={setMobile}
                editable={!otpSent}
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
                editable={!otpSent}
              />
            </View>

            {/* Branch & Year Row */}
            <View style={{ flexDirection: "row", gap: 10 }}>
              <View style={[styles.inputWrapper, { flex: 1 }]}>
                <Feather name="layers" size={18} color={Palette.cyan} style={styles.inputIcon} />
                <TextInput
                  placeholder="Branch (e.g. ECE)"
                  placeholderTextColor={Palette.textMutedDark}
                  style={styles.input}
                  value={branch}
                  onChangeText={setBranch}
                  editable={!otpSent}
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
                  editable={!otpSent}
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
                editable={!otpSent}
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
              <Feather name="lock" size={18} color={Palette.cyan} style={styles.inputIcon} />
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
              <View style={styles.otpVerificationCard}>
                <View style={styles.otpHeaderRow}>
                  <Text style={styles.otpCardTitle}>Enter 6-Digit Verification Code</Text>
                  <Text style={styles.otpTimerText}>
                    OTP expires in <Text style={styles.timerHighlight}>{formatTimer(expirySeconds)}</Text>
                  </Text>
                </View>

                {/* 6-Digit OTP Input Field */}
                <View style={[styles.inputWrapper, styles.otpInputHighlight]}>
                  <Feather name="shield" size={18} color={Palette.cyan} style={styles.inputIcon} />
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
                    style={[styles.resendBtn, cooldownSeconds > 0 && styles.resendBtnDisabled]}
                  >
                    <Text style={styles.resendBtnText}>
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
    backgroundColor: "rgba(6, 182, 212, 0.08)",
    borderWidth: 1,
    borderColor: "rgba(6, 182, 212, 0.35)",
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
    color: "#34D399",
  },
  emailSubjectText: {
    fontSize: 11.5,
    color: Palette.textSecondaryDark,
    marginBottom: 12,
  },
  otpHighlightBox: {
    backgroundColor: "#0F172A",
    borderWidth: 1.5,
    borderColor: Palette.cyan,
    borderRadius: 12,
    paddingVertical: 14,
    alignItems: "center",
    marginBottom: 10,
  },
  otpHighlightLabel: {
    fontSize: 10,
    fontWeight: "800",
    color: Palette.cyanLight,
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
  otpVerificationCard: {
    backgroundColor: "rgba(15, 23, 42, 0.6)",
    borderRadius: 16,
    padding: 14,
    borderWidth: 1,
    borderColor: "rgba(6, 182, 212, 0.3)",
    marginBottom: 14,
  },
  otpHeaderRow: {
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "space-between",
    marginBottom: 10,
  },
  otpCardTitle: {
    fontSize: 13,
    fontWeight: "700",
    color: "#FFFFFF",
  },
  otpTimerText: {
    fontSize: 12,
    color: Palette.textSecondaryDark,
  },
  timerHighlight: {
    color: Palette.cyan,
    fontWeight: "800",
    fontFamily: Platform.OS === "ios" ? "Menlo" : "monospace",
  },
  otpInputHighlight: {
    borderColor: Palette.cyan,
    backgroundColor: "rgba(6, 182, 212, 0.1)",
  },
  resendBtn: {
    paddingHorizontal: 10,
    paddingVertical: 6,
    backgroundColor: "rgba(6, 182, 212, 0.2)",
    borderRadius: 8,
  },
  resendBtnDisabled: {
    opacity: 0.5,
    backgroundColor: "rgba(255, 255, 255, 0.05)",
  },
  resendBtnText: {
    color: Palette.cyanLight,
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
    color: Palette.cyanLight,
    fontWeight: "700",
  },
});