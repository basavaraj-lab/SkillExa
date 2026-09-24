import { Feather } from "@expo/vector-icons";
import { useRouter } from "expo-router";
import * as SplashScreenExpo from "expo-splash-screen";
import React, { useEffect, useRef } from "react";
import {
  Animated,
  Easing,
  SafeAreaView,
  StatusBar,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from "react-native";
import { useAuth } from "../components/auth-context";
import { Palette, Radii, Shadows } from "../constants/theme";

export default function SplashScreen() {
  const router = useRouter();
  const { profile } = useAuth();

  // Animation values
  const logoScale = useRef(new Animated.Value(0.7)).current;
  const logoOpacity = useRef(new Animated.Value(0)).current;
  const badgeOpacity = useRef(new Animated.Value(0)).current;
  const badgeTranslateY = useRef(new Animated.Value(15)).current;
  const progressAnim = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    // 1. Hide native splash screen safely
    SplashScreenExpo.hideAsync().catch(() => undefined);

    // 2. Start entrance animations
    Animated.parallel([
      Animated.timing(logoScale, {
        toValue: 1,
        duration: 800,
        easing: Easing.out(Easing.back(1.5)),
        useNativeDriver: true,
      }),
      Animated.timing(logoOpacity, {
        toValue: 1,
        duration: 700,
        easing: Easing.out(Easing.ease),
        useNativeDriver: true,
      }),
    ]).start();

    // 3. Subtitle & Badge Animation
    Animated.parallel([
      Animated.timing(badgeOpacity, {
        toValue: 1,
        duration: 600,
        delay: 400,
        easing: Easing.out(Easing.ease),
        useNativeDriver: true,
      }),
      Animated.timing(badgeTranslateY, {
        toValue: 0,
        duration: 600,
        delay: 400,
        easing: Easing.out(Easing.back(1.2)),
        useNativeDriver: true,
      }),
      Animated.timing(progressAnim, {
        toValue: 1,
        duration: 1800,
        delay: 200,
        easing: Easing.inOut(Easing.ease),
        useNativeDriver: false,
      }),
    ]).start();

    // 4. Auto Navigation Timer
    const timer = setTimeout(() => {
      handleNavigate();
    }, 2200);

    return () => clearTimeout(timer);
  }, []);

  const handleNavigate = () => {
    if (profile && profile.name) {
      router.replace("/home" as any);
    } else {
      router.replace("/login" as any);
    }
  };

  const progressWidth = progressAnim.interpolate({
    inputRange: [0, 1],
    outputRange: ["0%", "100%"],
  });

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />

      <View style={styles.centerContent}>
        {/* Animated Brand Icon & Title */}
        <Animated.View
          style={[
            styles.brandGroup,
            {
              opacity: logoOpacity,
              transform: [{ scale: logoScale }],
            },
          ]}
        >
          <View style={styles.iconCircle}>
            <Feather name="book-open" size={38} color="#FFFFFF" />
          </View>

          <Text style={styles.brandTitle}>
            Skill<Text style={styles.brandHighlight}>Exa</Text>
          </Text>
        </Animated.View>

        {/* Tagline & Badges */}
        <Animated.View
          style={[
            styles.subtitleGroup,
            {
              opacity: badgeOpacity,
              transform: [{ translateY: badgeTranslateY }],
            },
          ]}
        >
          <Text style={styles.brandTagline}>
            Engineering & Competitive Preparation
          </Text>

          <View style={styles.badgesRow}>
            <View style={styles.badgePill}>
              <Feather name="cpu" size={12} color={Palette.primary} />
              <Text style={styles.badgeText}>Engineering</Text>
            </View>
            <View style={[styles.badgePill, { backgroundColor: Palette.warningLight, borderColor: Palette.warningBorder }]}>
              <Feather name="award" size={12} color={Palette.warning} />
              <Text style={[styles.badgeText, { color: Palette.warning }]}>Competitive</Text>
            </View>
          </View>
        </Animated.View>
      </View>

      {/* Bottom Loading Progress Bar & Skip */}
      <View style={styles.footer}>
        <View style={styles.progressTrack}>
          <Animated.View style={[styles.progressFill, { width: progressWidth }]} />
        </View>

        <TouchableOpacity
          style={styles.skipBtn}
          onPress={handleNavigate}
          activeOpacity={0.7}
        >
          <Text style={styles.skipText}>Tap to Continue</Text>
          <Feather name="arrow-right" size={13} color={Palette.primary} />
        </TouchableOpacity>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#FFFFFF",
    justifyContent: "space-between",
    alignItems: "center",
    paddingVertical: 40,
    paddingHorizontal: 24,
  },
  centerContent: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    width: "100%",
  },
  brandGroup: {
    alignItems: "center",
  },
  iconCircle: {
    width: 76,
    height: 76,
    borderRadius: 22,
    backgroundColor: Palette.primary,
    alignItems: "center",
    justifyContent: "center",
    marginBottom: 16,
    ...Shadows.button,
  },
  brandTitle: {
    fontSize: 40,
    fontWeight: "900",
    color: Palette.textTitle,
    letterSpacing: -0.8,
  },
  brandHighlight: {
    color: Palette.primary,
  },
  subtitleGroup: {
    alignItems: "center",
    marginTop: 10,
  },
  brandTagline: {
    fontSize: 14.5,
    fontWeight: "600",
    color: Palette.textSecondary,
    textAlign: "center",
    letterSpacing: 0.2,
  },
  badgesRow: {
    flexDirection: "row",
    gap: 10,
    marginTop: 18,
  },
  badgePill: {
    flexDirection: "row",
    alignItems: "center",
    gap: 6,
    backgroundColor: Palette.primaryLight,
    borderWidth: 1,
    borderColor: Palette.primaryBorder,
    paddingHorizontal: 12,
    paddingVertical: 6,
    borderRadius: Radii.pill,
  },
  badgeText: {
    fontSize: 12,
    fontWeight: "700",
    color: Palette.primary,
  },
  footer: {
    width: "100%",
    maxWidth: 260,
    alignItems: "center",
    gap: 12,
  },
  progressTrack: {
    width: "100%",
    height: 4,
    backgroundColor: Palette.border,
    borderRadius: 2,
    overflow: "hidden",
  },
  progressFill: {
    height: "100%",
    backgroundColor: Palette.primary,
    borderRadius: 2,
  },
  skipBtn: {
    flexDirection: "row",
    alignItems: "center",
    gap: 4,
    paddingVertical: 6,
    paddingHorizontal: 12,
  },
  skipText: {
    fontSize: 12.5,
    fontWeight: "700",
    color: Palette.primary,
  },
});