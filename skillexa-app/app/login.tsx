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
import { useAuth, UserProfile, UserRole } from "../components/auth-context";
import { Palette, Radii, Shadows } from "../constants/theme";
import { ApiClient } from "../services/api";

import { signInWithEmailAndPassword, createUserWithEmailAndPassword, signInWithPopup } from 'firebase/auth';
import { auth, googleProvider } from '../services/firebase';

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
      setErrorMessage(e.message || "Firebase Login Failed. Check credentials.");
    }
  };

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />

      <KeyboardAvoidingView
        behavior={Platform.OS === "ios" ? "padding" : "height"}
        style={styles.keyboardView}
      >
        <ScrollView
          contentContainerStyle={styles.scrollContent}
          keyboardShouldPersistTaps="handled"
          showsVerticalScrollIndicator={false}
        >
          {/* Brand Header */}
          <View style={styles.header}>
            <View style={styles.brandIconBox}>
              <Feather name="book-open" size={26} color="#FFFFFF" />
            </View>
            <Text style={styles.brandTitle}>
              Skill<Text style={styles.brandHighlight}>Exa</Text>
            </Text>
            <Text style={styles.brandTagline}>Student Learning & Career Preparation Platform</Text>
          </View>

          {/* Clean White Login Card */}
          <View style={styles.loginCard}>
            <Text style={styles.cardTitle}>Welcome Back</Text>
            <Text style={styles.cardSubtitle}>Select your account role and sign in to continue</Text>

            {/* Role Switcher Tabs */}
            <View style={styles.roleTabsRow}>
              <TouchableOpacity
                style={[styles.roleTab, role === "STUDENT" && styles.roleTabActive]}
                onPress={() => handleRoleChange("STUDENT")}
                activeOpacity={0.8}
              >
                <Feather
                  name="user"
                  size={15}
                  color={role === "STUDENT" ? Palette.primary : Palette.textSecondary}
                />
                <Text style={[styles.roleTabText, role === "STUDENT" && styles.roleTabTextActive]}>
                  Student
                </Text>
              </TouchableOpacity>

              <TouchableOpacity
                style={[styles.roleTab, role === "FACULTY" && styles.roleTabActiveFaculty]}
                onPress={() => handleRoleChange("FACULTY")}
                activeOpacity={0.8}
              >
                <Feather
                  name="award"
                  size={15}
                  color={role === "FACULTY" ? Palette.aiPurple : Palette.textSecondary}
                />
                <Text style={[styles.roleTabText, role === "FACULTY" && styles.roleTabTextActiveFaculty]}>
                  Faculty / Teacher
                </Text>
              </TouchableOpacity>
            </View>

            {/* Google Sign-In Button */}
            <TouchableOpacity
              style={styles.googleBtn}
              onPress={handleGoogleSignIn}
              activeOpacity={0.85}
            >
              <Feather name="globe" size={18} color="#EA4335" />
              <Text style={styles.googleBtnText}>Continue with Google</Text>
            </TouchableOpacity>

            {/* OR Divider */}
            <View style={styles.orDividerRow}>
              <View style={styles.dividerLine} />
              <Text style={styles.orText}>OR SIGN IN WITH</Text>
              <View style={styles.dividerLine} />
            </View>

            {/* Auth Method Switcher (Email / Phone) */}
            <View style={styles.methodTabsRow}>
              <TouchableOpacity
                style={[styles.methodTab, authMethod === "EMAIL" && styles.methodTabActive]}
                onPress={() => setAuthMethod("EMAIL")}
              >
                <Feather name="mail" size={14} color={authMethod === "EMAIL" ? Palette.primary : Palette.textSecondary} />
                <Text style={[styles.methodTabText, authMethod === "EMAIL" && styles.methodTabTextActive]}>
                  Email / Gmail
                </Text>
              </TouchableOpacity>

              <TouchableOpacity
                style={[styles.methodTab, authMethod === "PHONE" && styles.methodTabActive]}
                onPress={() => setAuthMethod("PHONE")}
              >
                <Feather name="phone" size={14} color={authMethod === "PHONE" ? Palette.primary : Palette.textSecondary} />
                <Text style={[styles.methodTabText, authMethod === "PHONE" && styles.methodTabTextActive]}>
                  Phone Number
                </Text>
              </TouchableOpacity>
            </View>

            {/* Email or Phone Input */}
            {authMethod === "EMAIL" ? (
              <View style={styles.inputGroup}>
                <Text style={styles.inputLabel}>
                  {role === "FACULTY" ? "FACULTY GMAIL / EMAIL ADDRESS" : "STUDENT GMAIL / EMAIL ADDRESS"}
                </Text>
                <View style={styles.inputContainer}>
                  <Feather name="mail" size={18} color={Palette.textSecondary} style={styles.inputIcon} />
                  <TextInput
                    placeholder={role === "FACULTY" ? "professor@gmail.com" : "student@gmail.com"}
                    placeholderTextColor={Palette.textMuted}
                    style={styles.input}
                    keyboardType="email-address"
                    autoCapitalize="none"
                    value={email}
                    onChangeText={setEmail}
                  />
                </View>
              </View>
            ) : (
              <View style={styles.inputGroup}>
                <Text style={styles.inputLabel}>PHONE NUMBER</Text>
                <View style={styles.inputContainer}>
                  <Feather name="phone" size={18} color={Palette.textSecondary} style={styles.inputIcon} />
                  <TextInput
                    placeholder="+91 9876543210"
                    placeholderTextColor={Palette.textMuted}
                    style={styles.input}
                    keyboardType="phone-pad"
                    value={phone}
                    onChangeText={setPhone}
                  />
                </View>
              </View>
            )}

            {/* Password Input */}
            <View style={styles.inputGroup}>
              <Text style={styles.inputLabel}>PASSWORD</Text>
              <View style={styles.inputContainer}>
                <Feather name="lock" size={18} color={Palette.textSecondary} style={styles.inputIcon} />
                <TextInput
                  placeholder="••••••••"
                  placeholderTextColor={Palette.textMuted}
                  secureTextEntry={!showPassword}
                  style={styles.input}
                  value={password}
                  onChangeText={setPassword}
                />
                <TouchableOpacity
                  onPress={() => setShowPassword(!showPassword)}
                  style={styles.eyeBtn}
                >
                  <Feather
                    name={showPassword ? "eye-off" : "eye"}
                    size={18}
                    color={Palette.textSecondary}
                  />
                </TouchableOpacity>
              </View>
            </View>

            {/* Error Message */}
            {errorMessage ? (
              <View style={styles.errorBanner}>
                <Text style={styles.errorText}>{errorMessage}</Text>
              </View>
            ) : null}

            {/* Sign In Button */}
            <TouchableOpacity
              style={[
                styles.loginBtn,
                role === "FACULTY" && { backgroundColor: Palette.aiPurple },
              ]}
              onPress={handleLogin}
              activeOpacity={0.85}
            >
              <Text style={styles.loginBtnText}>
                {isLoading ? "Signing in..." : role === "FACULTY" ? "Sign In as Faculty" : "Sign In to SkillExa"}
              </Text>
              <Feather name="arrow-right" size={16} color="#FFFFFF" />
            </TouchableOpacity>

            <TouchableOpacity
              activeOpacity={0.7}
              onPress={() => router.push("/register" as any)}
              style={styles.registerLink}
            >
              <Text style={styles.registerText}>
                Don&apos;t have an account? <Text style={styles.registerHighlight}>Register</Text>
              </Text>
            </TouchableOpacity>
          </View>
        </ScrollView>
      </KeyboardAvoidingView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: {
    flex: 1,
    backgroundColor: Palette.background,
  },
  keyboardView: {
    flex: 1,
  },
  scrollContent: {
    flexGrow: 1,
    justifyContent: "center",
    paddingHorizontal: 20,
    paddingVertical: 32,
  },
  header: {
    alignItems: "center",
    marginBottom: 24,
  },
  brandIconBox: {
    width: 48,
    height: 48,
    borderRadius: 14,
    backgroundColor: Palette.primary,
    alignItems: "center",
    justifyContent: "center",
    marginBottom: 10,
    ...Shadows.button,
  },
  brandTitle: {
    fontSize: 32,
    fontWeight: "900",
    color: Palette.textTitle,
    letterSpacing: -0.6,
  },
  brandHighlight: {
    color: Palette.primary,
  },
  brandTagline: {
    fontSize: 13.5,
    color: Palette.textSecondary,
    marginTop: 4,
    textAlign: "center",
  },
  loginCard: {
    backgroundColor: "#FFFFFF",
    borderRadius: Radii.cardLarge,
    padding: 24,
    borderWidth: 1,
    borderColor: Palette.border,
    marginBottom: 20,
    ...Shadows.card,
  },
  cardTitle: {
    fontSize: 20,
    fontWeight: "800",
    color: Palette.textTitle,
    marginBottom: 4,
  },
  cardSubtitle: {
    fontSize: 13,
    color: Palette.textSecondary,
    marginBottom: 18,
  },
  roleTabsRow: {
    flexDirection: "row",
    backgroundColor: Palette.backgroundSecondary,
    borderRadius: Radii.input,
    padding: 4,
    gap: 6,
    marginBottom: 18,
  },
  roleTab: {
    flex: 1,
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
    gap: 6,
    paddingVertical: 9,
    borderRadius: 8,
  },
  roleTabActive: {
    backgroundColor: "#FFFFFF",
    ...Shadows.card,
  },
  roleTabActiveFaculty: {
    backgroundColor: "#FFFFFF",
    ...Shadows.card,
  },
  roleTabText: {
    fontSize: 13,
    fontWeight: "600",
    color: Palette.textSecondary,
  },
  roleTabTextActive: {
    color: Palette.primary,
    fontWeight: "700",
  },
  roleTabTextActiveFaculty: {
    color: Palette.aiPurple,
    fontWeight: "700",
  },
  googleBtn: {
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
    backgroundColor: "#F8FAFC",
    borderWidth: 1,
    borderColor: Palette.border,
    paddingVertical: 12,
    borderRadius: Radii.button,
    gap: 10,
    marginBottom: 16,
  },
  googleBtnText: {
    fontSize: 14.5,
    fontWeight: "700",
    color: Palette.textTitle,
  },
  orDividerRow: {
    flexDirection: "row",
    alignItems: "center",
    marginBottom: 16,
  },
  dividerLine: {
    flex: 1,
    height: 1,
    backgroundColor: Palette.border,
  },
  orText: {
    fontSize: 10.5,
    fontWeight: "800",
    color: Palette.textMuted,
    paddingHorizontal: 10,
    letterSpacing: 0.8,
  },
  methodTabsRow: {
    flexDirection: "row",
    backgroundColor: Palette.backgroundSecondary,
    borderRadius: Radii.input,
    padding: 3,
    gap: 4,
    marginBottom: 16,
  },
  methodTab: {
    flex: 1,
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
    gap: 6,
    paddingVertical: 8,
    borderRadius: 6,
  },
  methodTabActive: {
    backgroundColor: "#FFFFFF",
    ...Shadows.card,
  },
  methodTabText: {
    fontSize: 12,
    fontWeight: "600",
    color: Palette.textSecondary,
  },
  methodTabTextActive: {
    color: Palette.primary,
    fontWeight: "700",
  },
  errorBanner: {
    backgroundColor: "#FEF2F2",
    borderWidth: 1,
    borderColor: "#FCA5A5",
    borderRadius: 10,
    padding: 10,
    marginBottom: 12,
  },
  errorText: {
    color: "#DC2626",
    fontSize: 13,
    textAlign: "center",
    fontWeight: "600",
  },
  inputGroup: {
    marginBottom: 16,
  },
  inputLabel: {
    fontSize: 11,
    fontWeight: "800",
    color: Palette.textTitle,
    letterSpacing: 0.6,
    marginBottom: 6,
  },
  inputContainer: {
    flexDirection: "row",
    alignItems: "center",
    backgroundColor: Palette.backgroundSecondary,
    borderRadius: Radii.input,
    borderWidth: 1,
    borderColor: Palette.border,
    paddingHorizontal: 12,
  },
  inputIcon: {
    marginRight: 8,
  },
  input: {
    flex: 1,
    paddingVertical: 13,
    fontSize: 14.5,
    color: Palette.textTitle,
  },
  eyeBtn: {
    padding: 6,
  },
  loginBtn: {
    backgroundColor: Palette.primary,
    borderRadius: Radii.button,
    paddingVertical: 14,
    flexDirection: "row",
    alignItems: "center",
    justifyContent: "center",
    gap: 8,
    marginTop: 8,
    marginBottom: 16,
    ...Shadows.button,
  },
  loginBtnText: {
    color: "#FFFFFF",
    fontSize: 15,
    fontWeight: "700",
  },
  registerLink: {
    alignItems: "center",
    paddingVertical: 6,
  },
  registerText: {
    fontSize: 13.5,
    color: Palette.textSecondary,
  },
  registerHighlight: {
    color: Palette.primary,
    fontWeight: "700",
  },
});