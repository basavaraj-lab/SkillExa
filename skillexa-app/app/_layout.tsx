import { Stack } from "expo-router";
import React from "react";
import { StyleSheet, View } from "react-native";
import { AuthProvider } from "../components/auth-context";
import { ThemeProvider } from "../components/theme-context";
import { BottomNav } from "../components/common/BottomNav";
import { FloatingSkillExaAI } from "../components/FloatingSkillExaAI";

export default function RootLayout() {
  return (
    <ThemeProvider>
      <AuthProvider>
        <View style={styles.root}>
          <Stack screenOptions={{ headerShown: false }} />
          <BottomNav />
          <FloatingSkillExaAI />
        </View>
      </AuthProvider>
    </ThemeProvider>
  );
}

const styles = StyleSheet.create({
  root: {
    flex: 1,
    backgroundColor: '#F8FAFC',
  },
});
