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
import { useAuth, UserRole } from "../components/auth-context";
import { Palette, Radii, Shadows } from "../constants/theme";

export default function LoginScreen() {
  const [role, setRole] = useState<UserRole>("STUDENT");
  const [showPassword, setShowPassword] = useState(false);
  const [email, setEmail] = useState("student@skillexa.edu");
  const [password, setPassword] = useState("scholar123");
  const [isLoading, setIsLoading] = useState(false);
  const { login } = useAuth();

  const handleRoleChange = (newRole: UserRole) => {
    setRole(newRole);
    if (newRole === "FACULTY") {
      setEmail("faculty@skillexa.edu");
      setPassword("prof123");
    } else {
      setEmail("student@skillexa.edu");
      setPassword("scholar123");
    }
  };

  const handleLogin = () => {
    setIsLoading(true);
    setTimeout(() => {
      setIsLoading(false);
      if (role === "FACULTY") {
        login({
          id: "fac-101",
          name: "Dr. Kusumadhara S",
          email,
          password,
          role: "FACULTY",
          collegeId: "clg-kvg",
          collegeName: "KVG College of Engineering",
          department: "ECE",
          facultyDesignation: "Associate Professor & HOD in-charge",
          subjectsTaught: ["Embedded Systems", "Microcontrollers", "VLSI Design"],
          verificationStatus: "APPROVED",
        });
      } else {
        login({
          id: "std-101",
          name: email.split("@")[0] || "Ganesh Sharan",
          email,
          password,
          role: "STUDENT",
          collegeId: "clg-kvg",
          collegeName: "KVG College of Engineering",
          department: "ECE",
          academicYear: "3rd Year",
          section: "A",
          verificationStatus: "APPROVED",
        });
      }

      if (role === "FACULTY") {
        router.replace("/faculty-dashboard" as any);
      } else {
        router.replace("/home" as any);
      }
    }, 300);
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

            {/* Email Input */}
            <View style={styles.inputGroup}>
              <Text style={styles.inputLabel}>
                {role === "FACULTY" ? "FACULTY EMAIL ADDRESS" : "STUDENT EMAIL ADDRESS"}
              </Text>
              <View style={styles.inputContainer}>
                <Feather name="mail" size={18} color={Palette.textSecondary} style={styles.inputIcon} />
                <TextInput
                  placeholder={role === "FACULTY" ? "professor@university.edu" : "name@university.edu"}
                  placeholderTextColor={Palette.textMuted}
                  style={styles.input}
                  keyboardType="email-address"
                  autoCapitalize="none"
                  value={email}
                  onChangeText={setEmail}
                />
              </View>
            </View>

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