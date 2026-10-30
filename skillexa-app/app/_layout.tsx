import { Stack } from "expo-router";
import React from "react";
import { StyleSheet, View } from "react-native";
import { AuthProvider } from "../components/auth-context";
import { BottomNav } from "../components/common/BottomNav";
import { FloatingSkillExaAI } from "../components/FloatingSkillExaAI";

export default function RootLayout() {
  return (
    <AuthProvider>
      <View style={styles.root}>
        <Stack screenOptions={{ headerShown: false }} />
        <BottomNav />
        <FloatingSkillExaAI />
      </View>
    </AuthProvider>
  );
}

const styles = StyleSheet.create({
  root: {
    flex: 1,
    backgroundColor: '#F8FAFC',
  },
});
