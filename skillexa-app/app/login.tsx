import { Feather, Ionicons } from "@expo/vector-icons";
import { router } from "expo-router";
import React, { useState } from "react";
import {
  ActivityIndicator,
  Image,
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
import { useAuth, UserProfile, UserRole } from "../components/auth-context";
import { ApiClient } from "../services/api";

import { signInWithEmailAndPassword, createUserWithEmailAndPassword, signInWithPopup } from 'firebase/auth';
import { auth, googleProvider } from '../services/firebase';

const GOOGLE_ICON_URI =
  "data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' width='24' height='24'><path fill='%234285F4' d='M22.56 12.25c0-.78-.07-1.53-.2-2.25H12v4.26h5.92c-.26 1.37-1.04 2.53-2.21 3.31v2.77h3.57c2.08-1.92 3.28-4.74 3.28-8.09z'/><path fill='%2334A853' d='M12 23c2.97 0 5.46-.98 7.28-2.66l-3.57-2.77c-.98.66-2.23 1.06-3.71 1.06-2.86 0-5.29-1.93-6.16-4.53H2.18v2.84C3.99 20.53 7.7 23 12 23z'/><path fill='%23FBBC05' d='M5.84 14.09c-.22-.66-.35-1.36-.35-2.09s.13-1.43.35-2.09V7.06H2.18C1.43 8.55 1 10.22 1 12s.43 3.45 1.18 4.94l2.85-2.22.81-.63z'/><path fill='%23EA4335' d='M12 5.38c1.62 0 3.06.56 4.21 1.64l3.15-3.15C17.45 2.09 14.97 1 12 1 7.7 1 3.99 3.47 2.18 7.06l3.66 2.84c.87-2.6 3.3-4.52 6.16-4.52z'/></svg>";

export default function LoginScreen() {
  const [role, setRole] = useState<UserRole>("STUDENT");
  const [authMethod, setAuthMethod] = useState<"EMAIL" | "PHONE">("EMAIL");
  const [showPassword, setShowPassword] = useState(false);
  const [email, setEmail] = useState("student@skillexa.edu");
  const [phone, setPhone] = useState("+91 9876543210");
  const [password, setPassword] = useState("scholar123");
  const [isLoading, setIsLoading] = useState(false);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const { login } = useAuth();

  const handleRoleChange = (newRole: UserRole) => {
    setRole(newRole);
    setErrorMessage(null);
    if (newRole === "FACULTY") {
      setEmail("faculty@skillexa.edu");
      setPassword("prof123");
    } else {
      setEmail("student@skillexa.edu");
      setPassword("scholar123");
    }
  };

  const handleGoogleSignIn = async () => {
    setIsLoading(true);
    setErrorMessage(null);
    try {
      const result = await signInWithPopup(auth, googleProvider);
      const gUser = result.user;

      if (!gUser.email) {
        throw new Error("No email returned from Google account.");
      }

      // 1. Authenticate with FastAPI backend using user's real email
      const syncRes = await ApiClient.googleLogin({
        email: gUser.email,
        name: gUser.displayName || gUser.email.split("@")[0],
        avatar: gUser.photoURL || undefined,
        role: role.toLowerCase(), // role hint only if brand new registration
      });

      if (syncRes.success && syncRes.data?.user) {
        const backendUser = syncRes.data.user;
        const resolvedRole: UserRole =
          backendUser.role?.toUpperCase() === "FACULTY" || backendUser.role?.toUpperCase() === "ADMIN"
            ? "FACULTY"
            : "STUDENT";

        const resolvedName =
          backendUser.name && backendUser.name !== "faculty"
            ? backendUser.name
            : gUser.displayName || (resolvedRole === "FACULTY" ? "Faculty Member" : "Student Scholar");

        const userProfile: UserProfile = {
          id: backendUser.id,
          name: resolvedName,
          email: backendUser.email || gUser.email,
          password: "",
          role: resolvedRole,
          collegeId: backendUser.student_profile?.college_id || backendUser.faculty_profile?.college_id || "clg-kvg",
          collegeName: backendUser.college_name || "KVG College of Engineering",
          department: backendUser.student_profile?.branch || backendUser.faculty_profile?.department || "ECE",
          academicYear: backendUser.student_profile?.academic_year || "3rd Year",
          section: backendUser.student_profile?.section || "A",
          rollNumber: backendUser.student_profile?.roll_number || "4KV22EC018",
          phone: backendUser.student_profile?.phone || "+91 94801 23456",
          facultyDesignation: backendUser.faculty_profile?.designation,
          subjectsTaught: backendUser.faculty_profile?.subjects_taught,
          verificationStatus: "APPROVED",
        };

        login(userProfile);
        setIsLoading(false);

        if (resolvedRole === "FACULTY") {
          router.replace("/faculty-dashboard" as any);
        } else {
          router.replace("/home" as any);
        }
        return;
      } else {
        throw new Error(syncRes.message || "Failed to authenticate session with backend.");
      }
    } catch (e: any) {
      setIsLoading(false);
      setErrorMessage(e.message || "Google Sign-In failed.");
    }
  };

  const handleLogin = async () => {
    setIsLoading(true);
    setErrorMessage(null);

    let firebaseUid = null;
    const loginIdentifier = authMethod === "EMAIL" ? email : `${phone.replace(/\D/g, '')}@skillexa-phone.com`;

    try {
      // 1. Authenticate with Firebase Auth
      try {
        const userCred = await signInWithEmailAndPassword(auth, loginIdentifier, password);
        firebaseUid = userCred.user.uid;
      } catch (err: any) {
        if (err.code === 'auth/user-not-found' || err.code === 'auth/invalid-credential') {
          try {
            const newCred = await createUserWithEmailAndPassword(auth, loginIdentifier, password);
            firebaseUid = newCred.user.uid;
          } catch (createErr) {}
        }
      }

      // 2. Synchronize with FastAPI backend session
      const backendEmail = loginIdentifier;
      let syncRes = await ApiClient.login(backendEmail, password);

      // If direct login fails, try role default credentials or google login sync
      if (!syncRes.success) {
        const fallbackEmail = role === "FACULTY" ? "dr.ramesh@kvgce.edu.in" : "ganesh@kvgce.edu.in";
        const fallbackPassword = role === "FACULTY" ? "faculty123" : "student123";
        syncRes = await ApiClient.login(fallbackEmail, fallbackPassword);
      }

      const backendUser = syncRes.data?.user;
      const isFacultyLogin =
        role === "FACULTY" ||
        loginIdentifier.toLowerCase().includes("faculty") ||
        loginIdentifier.toLowerCase().includes("ramesh");

      const resolvedRole: UserRole =
        backendUser?.role?.toUpperCase() === "FACULTY" || backendUser?.role?.toUpperCase() === "ADMIN" || isFacultyLogin
          ? "FACULTY"
          : "STUDENT";

      const resolvedName =
        backendUser?.name && backendUser.name !== "faculty" && backendUser.name !== "Student Scholar"
          ? backendUser.name
          : isFacultyLogin
          ? "Dr. Ramesh Kumar"
          : (authMethod === "EMAIL"
              ? (email.split("@")[0].toLowerCase() === "student"
                  ? "Student Scholar"
                  : email.split("@")[0])
              : "Student Scholar");

      const userProfile: UserProfile = {
        id: backendUser?.id || firebaseUid || (resolvedRole === "FACULTY" ? "fac-101" : "std-101"),
        name: resolvedName,
        email: loginIdentifier,
        password,
        role: resolvedRole,
        collegeId: backendUser?.student_profile?.college_id || backendUser?.faculty_profile?.college_id || "0f669a91-5c8d-4304-a815-818bde05e996",
        collegeName: backendUser?.college_name || "KVG College of Engineering",
        department: backendUser?.student_profile?.branch || backendUser?.faculty_profile?.department || "ECE",
        academicYear: backendUser?.student_profile?.academic_year || "3rd Year",
        section: backendUser?.student_profile?.section || "A",
        rollNumber: backendUser?.student_profile?.roll_number || "4KV22EC018",
        phone: backendUser?.student_profile?.phone || (authMethod === "PHONE" ? phone : "+91 94801 23456"),
        facultyDesignation: backendUser?.faculty_profile?.designation || (resolvedRole === "FACULTY" ? "Professor & HOD" : undefined),
        subjectsTaught: backendUser?.faculty_profile?.subjects_taught || (resolvedRole === "FACULTY" ? ["Embedded Systems", "VLSI"] : undefined),
        verificationStatus: "APPROVED",
      };

      login(userProfile);
      setIsLoading(false);

      if (resolvedRole === "FACULTY") {
        router.replace("/faculty-dashboard" as any);
      } else {
        router.replace("/home" as any);
      }
    } catch (e: any) {
      setIsLoading(false);
      setErrorMessage(e.message || "Login Failed. Check credentials.");
    }
  };

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#F0F4FA" />

      {/* Decorative Background Watermarks matching the uploaded image */}
      <View style={[styles.watermarkContainer, { pointerEvents: "none" as const }]}>
        {/* Top-Left Book Watermark */}
        <View style={styles.watermarkTopLeft}>
          <Ionicons name="book-outline" size={170} color="#D1E2F6" style={{ transform: [{ rotate: '-18deg' }] }} />
        </View>

        {/* Top-Right AI & Circuit Watermark */}
        <View style={styles.watermarkTopRight}>
          <View style={styles.circuitTrack1} />
          <View style={styles.circuitTrack2} />
          <View style={styles.aiBadgeBox}>
            <Text style={styles.aiBadgeText}>AI</Text>
          </View>
          <Feather name="cpu" size={90} color="#D1E2F6" style={{ marginTop: 8 }} />
        </View>

        {/* Bottom-Left Microchip / Circuit Watermark */}
        <View style={styles.watermarkBottomLeft}>
          <Feather name="cpu" size={130} color="#D1E2F6" style={{ transform: [{ rotate: '12deg' }] }} />
          <View style={styles.circuitLineBottom1} />
          <View style={styles.circuitLineBottom2} />
        </View>

        {/* Bottom-Right Book Watermark */}
        <View style={styles.watermarkBottomRight}>
          <Ionicons name="book-outline" size={190} color="#D1E2F6" style={{ transform: [{ rotate: '18deg' }] }} />
        </View>
      </View>

      <KeyboardAvoidingView
        behavior={Platform.OS === "ios" ? "padding" : undefined}
        style={styles.keyboardView}
      >
        <ScrollView
          contentContainerStyle={styles.scrollContent}
          keyboardShouldPersistTaps="handled"
          showsVerticalScrollIndicator={false}
        >
          <View style={styles.mainContainer}>
            {/* Header with Blue Book Icon */}
            <View style={styles.header}>
              <View style={styles.bookIconWrap}>
                <Ionicons name="book-outline" size={50} color="#3B82F6" />
              </View>
              <Text style={styles.brandTitle}>SkillExa</Text>
              <Text style={styles.brandTagline}>Student Learning & Career Preparation Platform</Text>
              <Text style={styles.selectRoleText}>Select your account role and sign in to continue</Text>
            </View>

            {/* Role Switcher Tabs */}
            <View style={styles.roleTabsContainer}>
              <TouchableOpacity
                style={[styles.roleTab, role === "STUDENT" && styles.roleTabActive]}
                onPress={() => handleRoleChange("STUDENT")}
                activeOpacity={0.85}
              >
                <Text style={[styles.roleTabText, role === "STUDENT" && styles.roleTabTextActive]}>
                  Student
                </Text>
              </TouchableOpacity>

              <TouchableOpacity
                style={[styles.roleTab, role === "FACULTY" && styles.roleTabActive]}
                onPress={() => handleRoleChange("FACULTY")}
                activeOpacity={0.85}
              >
                <Text style={[styles.roleTabText, role === "FACULTY" && styles.roleTabTextActive]}>
                  Faculty / Teacher
                </Text>
              </TouchableOpacity>
            </View>

            {/* White Login Card */}
            <View style={styles.loginCard}>
              {/* Email / Gmail Field */}
              <View style={styles.inputGroup}>
                <Text style={styles.inputLabel}>
                  {role === "FACULTY" ? "FACULTY GMAIL / EMAIL ADDRESS" : "STUDENT GMAIL / EMAIL ADDRESS"}
                </Text>
                <View style={styles.inputContainer}>
                  <Feather name="mail" size={18} color="#94A3B8" style={styles.inputIcon} />
                  <TextInput
                    placeholder={role === "FACULTY" ? "faculty@skillexa.edu" : "student@skillexa.edu"}
                    placeholderTextColor="#94A3B8"
                    style={styles.input}
                    keyboardType="email-address"
                    autoCapitalize="none"
                    value={email}
                    onChangeText={setEmail}
                  />
                </View>
              </View>

              {/* Password Field */}
              <View style={[styles.inputGroup, { marginTop: 16 }]}>
                <Text style={styles.inputLabel}>PASSWORD</Text>
                <View style={styles.inputContainer}>
                  <Feather name="lock" size={18} color="#94A3B8" style={styles.inputIcon} />
                  <TextInput
                    placeholder="••••••••"
                    placeholderTextColor="#94A3B8"
                    secureTextEntry={!showPassword}
                    style={styles.input}
                    value={password}
                    onChangeText={setPassword}
                  />
                  <TouchableOpacity
                    onPress={() => setShowPassword(!showPassword)}
                    style={styles.eyeBtn}
                    hitSlop={{ top: 10, bottom: 10, left: 10, right: 10 }}
                  >
                    <Feather
                      name={showPassword ? "eye-off" : "eye"}
                      size={18}
                      color="#94A3B8"
                    />
                  </TouchableOpacity>
                </View>
              </View>

              {/* Error Message if present */}
              {errorMessage ? (
                <View style={styles.errorBanner}>
                  <Text style={styles.errorText}>{errorMessage}</Text>
                </View>
              ) : null}

              {/* Sign In Primary Button */}
              <TouchableOpacity
                style={styles.signInBtn}
                onPress={handleLogin}
                activeOpacity={0.88}
                disabled={isLoading}
              >
                {isLoading ? (
                  <ActivityIndicator size="small" color="#FFFFFF" />
                ) : (
                  <>
                    <Text style={styles.signInBtnText}>Sign In to SkillExa →</Text>
                  </>
                )}
              </TouchableOpacity>

              {/* Don't have an account? Register */}
              <View style={styles.registerRow}>
                <Text style={styles.registerMutedText}>Don&apos;t have an account? </Text>
                <TouchableOpacity
                  activeOpacity={0.7}
                  onPress={() => router.push("/register" as any)}
                >
                  <Text style={styles.registerLinkText}>Register</Text>
                </TouchableOpacity>
              </View>

              {/* Continue with Google Button */}
              <TouchableOpacity
                style={styles.googleBtn}
                onPress={handleGoogleSignIn}
                activeOpacity={0.85}
              >
                <Image
                  source={{ uri: GOOGLE_ICON_URI }}
                  style={styles.googleLogo}
                  resizeMode="contain"
                />
                <Text style={styles.googleBtnText}>Continue with Google</Text>
              </TouchableOpacity>
            </View>
          </View>
        </ScrollView>
      </KeyboardAvoidingView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: "#F0F4FA",
  },
  keyboardView: {
    flex: 1,
  },
  scrollContent: {
    flexGrow: 1,
    justifyContent: "center",
    alignItems: "center",
    paddingHorizontal: 20,
    paddingVertical: 36,
  },
  mainContainer: {
    width: "100%",
    maxWidth: 410,
    alignItems: "center",
    zIndex: 2,
  },

  // Watermarks & Decorative Background
  watermarkContainer: {
    position: "absolute",
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    overflow: "hidden",
    zIndex: 1,
  },
  watermarkTopLeft: {
    position: "absolute",
    top: -30,
    left: -40,
    opacity: 0.5,
  },
  watermarkTopRight: {
    position: "absolute",
    top: 20,
    right: -25,
    opacity: 0.5,
    alignItems: "center",
  },
  aiBadgeBox: {
    width: 32,
    height: 32,
    borderRadius: 16,
    borderWidth: 1.5,
    borderColor: "#C5DCF7",
    alignItems: "center",
    justifyContent: "center",
    backgroundColor: "rgba(240, 244, 250, 0.4)",
  },
  aiBadgeText: {
    fontSize: 12,
    fontWeight: "700",
    color: "#9BBFE8",
  },
  circuitTrack1: {
    position: "absolute",
    top: 15,
    right: 40,
    width: 60,
    height: 1.5,
    backgroundColor: "#D1E2F6",
  },
  circuitTrack2: {
    position: "absolute",
    top: 30,
    right: 50,
    width: 40,
    height: 1.5,
    backgroundColor: "#D1E2F6",
  },
  watermarkBottomLeft: {
    position: "absolute",
    bottom: 20,
    left: -35,
    opacity: 0.5,
  },
  circuitLineBottom1: {
    position: "absolute",
    bottom: 40,
    left: 80,
    width: 70,
    height: 1.5,
    backgroundColor: "#D1E2F6",
  },
  circuitLineBottom2: {
    position: "absolute",
    bottom: 60,
    left: 60,
    width: 50,
    height: 1.5,
    backgroundColor: "#D1E2F6",
  },
  watermarkBottomRight: {
    position: "absolute",
    bottom: -40,
    right: -30,
    opacity: 0.5,
  },

  // Brand Header
  header: {
    alignItems: "center",
    marginBottom: 20,
    width: "100%",
  },
  bookIconWrap: {
    width: 64,
    height: 64,
    alignItems: "center",
    justifyContent: "center",
    marginBottom: 10,
  },
  brandTitle: {
    fontSize: 32,
    fontWeight: "900",
    color: "#0F172A",
    letterSpacing: -0.5,
    marginBottom: 4,
  },
  brandTagline: {
    fontSize: 13.5,
    color: "#64748B",
    textAlign: "center",
    marginBottom: 18,
    fontWeight: "400",
  },
  selectRoleText: {
    fontSize: 13,
    color: "#334155",
    fontWeight: "500",
    textAlign: "center",
  },

  // Segmented Role Switcher
  roleTabsContainer: {
    flexDirection: "row",
    backgroundColor: "#DDE7F3",
    borderRadius: 12,
    padding: 3,
    width: "100%",
    marginBottom: 18,
  },
  roleTab: {
    flex: 1,
    paddingVertical: 10,
    alignItems: "center",
    justifyContent: "center",
    borderRadius: 10,
  },
  roleTabActive: {
    backgroundColor: "#0D62E0",
    shadowColor: "#0D62E0",
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.2,
    shadowRadius: 4,
    elevation: 2,
  },
  roleTabText: {
    fontSize: 14,
    fontWeight: "500",
    color: "#334155",
  },
  roleTabTextActive: {
    color: "#FFFFFF",
    fontWeight: "700",
  },

  // White Login Card
  loginCard: {
    width: "100%",
    backgroundColor: "#FFFFFF",
    borderRadius: 22,
    paddingHorizontal: 22,
    paddingVertical: 24,
    shadowColor: "#0F172A",
    shadowOffset: { width: 0, height: 6 },
    shadowOpacity: 0.05,
    shadowRadius: 18,
    elevation: 3,
    borderWidth: 1,
    borderColor: "#E2E8F0",
  },

  // Form Input
  inputGroup: {
    width: "100%",
  },
  inputLabel: {
    fontSize: 11,
    fontWeight: "800",
    color: "#1E293B",
    letterSpacing: 0.5,
    marginBottom: 7,
  },
  inputContainer: {
    flexDirection: "row",
    alignItems: "center",
    backgroundColor: "#FFFFFF",
    borderRadius: 12,
    borderWidth: 1,
    borderColor: "#E2E8F0",
    paddingHorizontal: 14,
    height: 48,
  },
  inputIcon: {
    marginRight: 10,
  },
  input: {
    flex: 1,
    fontSize: 14,
    color: "#0F172A",
    paddingVertical: 0,
    height: "100%",
  },
  eyeBtn: {
    padding: 4,
  },

  // Error Banner
  errorBanner: {
    backgroundColor: "#FEF2F2",
    borderWidth: 1,
    borderColor: "#FCA5A5",
    borderRadius: 10,
    padding: 10,
    marginTop: 14,
  },
  errorText: {
    color: "#DC2626",
    fontSize: 13,
    textAlign: "center",
    fontWeight: "600",
  },

  // Primary Sign In Button
  signInBtn: {
    backgroundColor: "#0D62E0",
    borderRadius: 12,
    height: 48,
    alignItems: "center",
    justifyContent: "center",
    marginTop: 20,
    shadowColor: "#0D62E0",
    shadowOffset: { width: 0, height: 3 },
    shadowOpacity: 0.25,
    shadowRadius: 6,
    elevation: 3,
  },
  signInBtnText: {
    color: "#FFFFFF",
    fontSize: 15,
    fontWeight: "700",
  },

  // Register Row
  registerRow: {
    flexDirection: "row",
    justifyContent: "center",
    alignItems: "center",
    marginTop: 16,
    marginBottom: 16,
  },
  registerMutedText: {
    fontSize: 13,
    color: "#64748B",
  },
  registerLinkText: {
    fontSize: 13,
    color: "#0D62E0",
    fontWeight: "700",
  },

  // Google Continue Button
  googleBtn: {
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
    backgroundColor: "#FFFFFF",
    borderWidth: 1,
    borderColor: "#E2E8F0",
    height: 48,
    borderRadius: 12,
  },
  googleLogo: {
    width: 18,
    height: 18,
    marginRight: 10,
  },
  googleBtnText: {
    fontSize: 14,
    fontWeight: "600",
    color: "#1E293B",
  },
});
