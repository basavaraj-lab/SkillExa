import { Feather } from "@expo/vector-icons";
import { LinearGradient } from "expo-linear-gradient";
import { router, usePathname } from "expo-router";
import React, { createContext, useContext, useMemo, useState } from "react";
import {
    Modal,
    Pressable,
    StyleSheet,
    Text,
    TouchableOpacity,
    View,
} from "react-native";
import { useSafeAreaInsets } from "react-native-safe-area-context";
import { Gradients, Palette } from "../constants/theme";

export type UserRole = 'STUDENT' | 'FACULTY' | 'ADMIN';

export type UserProfile = {
  id?: string;
  name: string;
  email: string;
  password?: string;
  role: UserRole;
  collegeId: string;
  collegeName: string;
  department: string; // or branch e.g. 'ECE', 'CSE'
  academicYear?: string; // '1st Year' | '2nd Year' | '3rd Year' | '4th Year'
  section?: string; // 'A' | 'B' | 'C'
  facultyDesignation?: string; // e.g. 'Associate Professor'
  subjectsTaught?: string[]; // e.g. ['Embedded Systems', 'VLSI']
  verificationStatus?: 'APPROVED' | 'PENDING' | 'REJECTED';
};

type AuthContextType = {
  isAuthenticated: boolean;
  profile: UserProfile;
  login: (profile: UserProfile) => void;
  logout: () => void;
  updateProfile: (updates: Partial<UserProfile>) => void;
  isFaculty: boolean;
};

export const defaultStudentProfile: UserProfile = {
  id: 'std-101',
  name: 'Ganesh Sharan',
  email: 'ganesh@kvgce.edu.in',
  password: 'scholar123',
  role: 'STUDENT',
  collegeId: 'clg-kvg',
  collegeName: 'KVG College of Engineering',
  department: 'ECE',
  academicYear: '3rd Year',
  section: 'A',
  verificationStatus: 'APPROVED',
};

export const defaultFacultyProfile: UserProfile = {
  id: 'fac-101',
  name: 'Dr. Kusumadhara S',
  email: 'kusumadhara.s@kvgce.edu.in',
  password: 'prof123',
  role: 'FACULTY',
  collegeId: 'clg-kvg',
  collegeName: 'KVG College of Engineering',
  department: 'ECE',
  facultyDesignation: 'Associate Professor & HOD in-charge',
  subjectsTaught: ['Embedded Systems', 'Microcontrollers', 'VLSI Design'],
  verificationStatus: 'APPROVED',
};

const defaultProfile: UserProfile = defaultStudentProfile;

const AuthContext = createContext<AuthContextType>({
  isAuthenticated: true,
  profile: defaultProfile,
  login: () => {},
  logout: () => {},
  updateProfile: () => {},
  isFaculty: false,
});

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [isAuthenticated, setIsAuthenticated] = useState(true);
  const [profile, setProfile] = useState<UserProfile>(defaultStudentProfile);

  const login = React.useCallback((nextProfile: UserProfile) => {
    setProfile(nextProfile);
    setIsAuthenticated(true);
  }, []);

  const logout = React.useCallback(() => {
    setProfile(defaultStudentProfile);
    setIsAuthenticated(false);
  }, []);

  const updateProfile = React.useCallback((updates: Partial<UserProfile>) => {
    setProfile((prev) => ({ ...prev, ...updates }));
  }, []);

  const isFaculty = profile.role === 'FACULTY';

  const value = useMemo(
    () => ({ isAuthenticated, profile, login, logout, updateProfile, isFaculty }),
    [isAuthenticated, profile, login, logout, updateProfile, isFaculty],
  );

  return <AuthContext.Provider value={value}>{children}</AuthContext.Provider>;
}

export function useAuth() {
  return useContext(AuthContext);
}

export function TopProfileMenu() {
  const { isAuthenticated, profile, logout } = useAuth();
  const pathname = usePathname();
  const insets = useSafeAreaInsets();
  const [menuVisible, setMenuVisible] = useState(false);
  const [detailsVisible, setDetailsVisible] = useState(false);

  const hiddenRoutes = ["/login", "/register", "/register-user", "/register-lecturer"];

  if (!isAuthenticated || hiddenRoutes.includes(pathname)) {
    return null;
  }

  const handleLogout = () => {
    setMenuVisible(false);
    logout();
    router.replace("/login");
  };

  const initial = (profile.name || "U").charAt(0).toUpperCase();

  return (
    <>
      <View style={[styles.container, { top: insets.top + 8 }]}>
        <TouchableOpacity
          activeOpacity={0.8}
          onPress={() => setMenuVisible(true)}
          style={styles.pillButton}
        >
          <LinearGradient
            colors={Gradients.primary}
            start={{ x: 0, y: 0 }}
            end={{ x: 1, y: 1 }}
            style={styles.avatarCircle}
          >
            <Text style={styles.avatarText}>{initial}</Text>
          </LinearGradient>
          <View style={styles.onlineDot} />
        </TouchableOpacity>
      </View>

      {/* Floating Menu */}
      <Modal
        animationType="fade"
        transparent
        visible={menuVisible}
        onRequestClose={() => setMenuVisible(false)}
      >
        <Pressable style={styles.backdrop} onPress={() => setMenuVisible(false)}>
          <View style={styles.menuCard}>
            <View style={styles.menuHeader}>
              <Text style={styles.menuUserName} numberOfLines={1}>{profile.name || "Learner"}</Text>
              <Text style={styles.menuUserEmail} numberOfLines={1}>{profile.email || "Active"}</Text>
            </View>
            <View style={styles.menuDivider} />

            <TouchableOpacity
              style={styles.menuItem}
              onPress={() => {
                setMenuVisible(false);
                setDetailsVisible(true);
              }}
            >
              <Feather name="user" size={16} color={Palette.cyan} />
              <Text style={styles.menuText}>View Profile</Text>
            </TouchableOpacity>

            <TouchableOpacity style={[styles.menuItem, styles.logoutItem]} onPress={handleLogout}>
              <Feather name="log-out" size={16} color={Palette.rose} />
              <Text style={[styles.menuText, styles.logoutText]}>Sign Out</Text>
            </TouchableOpacity>
          </View>
        </Pressable>
      </Modal>

      {/* Profile Details Modal */}
      <Modal
        animationType="fade"
        transparent
        visible={detailsVisible}
        onRequestClose={() => setDetailsVisible(false)}
      >
        <View style={styles.detailsBackdrop}>
          <View style={styles.detailsCard}>
            <View style={styles.profileHeader}>
              <LinearGradient
                colors={Gradients.primary}
                start={{ x: 0, y: 0 }}
                end={{ x: 1, y: 1 }}
                style={styles.modalAvatar}
              >
                <Text style={styles.modalAvatarText}>{initial}</Text>
              </LinearGradient>
              <Text style={styles.title}>{profile.name || "SkillExa Scholar"}</Text>
              <View style={styles.badgeRow}>
                <Text style={styles.badgeText}>Pro Member • Level 4</Text>
              </View>
            </View>

            <View style={styles.infoSection}>
              <View style={styles.infoRow}>
                <Feather name="book-open" size={16} color={Palette.primary} />
                <View style={styles.infoContent}>
                  <Text style={styles.infoLabel}>COLLEGE / INSTITUTION</Text>
                  <Text style={styles.detailText}>{profile.collegeName || "KVG College of Engineering"}</Text>
                </View>
              </View>

              <View style={styles.infoRow}>
                <Feather name="layers" size={16} color={Palette.cyan} />
                <View style={styles.infoContent}>
                  <Text style={styles.infoLabel}>DEPARTMENT & CLASS</Text>
                  <Text style={styles.detailText}>
                    {profile.department || "ECE"}
                    {profile.academicYear ? ` • ${profile.academicYear}` : ""}
                    {profile.section ? ` • Sec ${profile.section}` : ""}
                  </Text>
                </View>
              </View>

              <View style={styles.infoRow}>
                <Feather name="mail" size={16} color={Palette.cyan} />
                <View style={styles.infoContent}>
                  <Text style={styles.infoLabel}>EMAIL ADDRESS</Text>
                  <Text style={styles.detailText}>{profile.email || "Not set"}</Text>
                </View>
              </View>

              <View style={styles.infoRow}>
                <Feather name="shield" size={16} color={Palette.emerald} />
                <View style={styles.infoContent}>
                  <Text style={styles.infoLabel}>VERIFICATION STATUS</Text>
                  <Text style={[styles.detailText, { color: Palette.emerald, fontWeight: '700' }]}>
                    {profile.verificationStatus || "APPROVED"} • {profile.role}
                  </Text>
                </View>
              </View>
            </View>

            <TouchableOpacity
              activeOpacity={0.85}
              style={styles.closeButton}
              onPress={() => setDetailsVisible(false)}
            >
              <LinearGradient
                colors={Gradients.cyanBlue}
                start={{ x: 0, y: 0 }}
                end={{ x: 1, y: 0 }}
                style={styles.closeButtonGradient}
              >
                <Text style={styles.closeButtonText}>Done</Text>
              </LinearGradient>
            </TouchableOpacity>
          </View>
        </View>
      </Modal>
    </>
  );
}

const styles = StyleSheet.create({
  container: {
    position: "absolute",
    right: 18,
    zIndex: 999,
  },
  pillButton: {
    padding: 3,
    backgroundColor: "rgba(15, 23, 42, 0.85)",
    borderRadius: 24,
    borderWidth: 1.5,
    borderColor: Palette.glassBorderCyan,
    shadowColor: Palette.cyan,
    shadowOpacity: 0.3,
    shadowRadius: 10,
    shadowOffset: { width: 0, height: 4 },
    elevation: 8,
  },
  avatarCircle: {
    width: 36,
    height: 36,
    borderRadius: 18,
    alignItems: "center",
    justifyContent: "center",
  },
  avatarText: {
    color: "#FFFFFF",
    fontSize: 16,
    fontWeight: "800",
  },
  onlineDot: {
    position: "absolute",
    bottom: 2,
    right: 2,
    width: 10,
    height: 10,
    borderRadius: 5,
    backgroundColor: Palette.emerald,
    borderWidth: 2,
    borderColor: "#070B14",
  },
  backdrop: {
    flex: 1,
    justifyContent: "flex-start",
    alignItems: "flex-end",
    paddingTop: 68,
    paddingRight: 18,
    backgroundColor: "rgba(7, 11, 20, 0.6)",
  },
  menuCard: {
    backgroundColor: "#0F172A",
    borderRadius: 18,
    paddingVertical: 10,
    paddingHorizontal: 6,
    width: 190,
    borderWidth: 1,
    borderColor: Palette.glassBorder,
    shadowColor: "#000",
    shadowOpacity: 0.5,
    shadowRadius: 16,
    shadowOffset: { width: 0, height: 8 },
    elevation: 10,
  },
  menuHeader: {
    paddingHorizontal: 12,
    paddingVertical: 6,
  },
  menuUserName: {
    color: "#FFFFFF",
    fontWeight: "700",
    fontSize: 15,
  },
  menuUserEmail: {
    color: Palette.textMutedDark,
    fontSize: 12,
    marginTop: 2,
  },
  menuDivider: {
    height: 1,
    backgroundColor: Palette.glassBorder,
    marginVertical: 6,
  },
  menuItem: {
    flexDirection: "row",
    alignItems: "center",
    gap: 10,
    paddingVertical: 10,
    paddingHorizontal: 12,
    borderRadius: 10,
  },
  logoutItem: {
    marginTop: 2,
  },
  menuText: {
    fontSize: 14,
    color: "#F8FAFC",
    fontWeight: "600",
  },
  logoutText: {
    color: Palette.roseLight,
  },
  detailsBackdrop: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    backgroundColor: "rgba(7, 11, 20, 0.8)",
    padding: 20,
  },
  detailsCard: {
    backgroundColor: "#0F172A",
    borderRadius: 24,
    padding: 24,
    width: "100%",
    maxWidth: 380,
    borderWidth: 1,
    borderColor: Palette.glassBorderHighlight,
    shadowColor: Palette.primary,
    shadowOpacity: 0.25,
    shadowRadius: 24,
    elevation: 12,
  },
  profileHeader: {
    alignItems: "center",
    marginBottom: 20,
  },
  modalAvatar: {
    width: 72,
    height: 72,
    borderRadius: 36,
    alignItems: "center",
    justifyContent: "center",
    marginBottom: 12,
    shadowColor: Palette.primary,
    shadowOpacity: 0.4,
    shadowRadius: 14,
    elevation: 8,
  },
  modalAvatarText: {
    fontSize: 30,
    fontWeight: "800",
    color: "#FFFFFF",
  },
  title: {
    fontSize: 22,
    fontWeight: "800",
    color: "#F8FAFC",
    marginBottom: 6,
  },
  badgeRow: {
    backgroundColor: "rgba(99, 102, 241, 0.15)",
    paddingVertical: 4,
    paddingHorizontal: 12,
    borderRadius: 20,
    borderWidth: 1,
    borderColor: "rgba(99, 102, 241, 0.3)",
  },
  badgeText: {
    color: Palette.primaryLight,
    fontSize: 12,
    fontWeight: "700",
  },
  infoSection: {
    backgroundColor: "rgba(255, 255, 255, 0.03)",
    borderRadius: 16,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.glassBorder,
    marginBottom: 20,
    gap: 14,
  },
  infoRow: {
    flexDirection: "row",
    alignItems: "center",
    gap: 12,
  },
  infoContent: {
    flex: 1,
  },
  infoLabel: {
    fontSize: 10,
    fontWeight: "800",
    letterSpacing: 0.8,
    color: Palette.textMutedDark,
    marginBottom: 2,
  },
  detailText: {
    fontSize: 14,
    color: "#F8FAFC",
    fontWeight: "600",
  },
  closeButton: {
    borderRadius: 14,
    overflow: "hidden",
  },
  closeButtonGradient: {
    paddingVertical: 14,
    alignItems: "center",
    justifyContent: "center",
  },
  closeButtonText: {
    color: "#FFFFFF",
    fontWeight: "700",
    fontSize: 15,
  },
});

