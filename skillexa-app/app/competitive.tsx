import { Feather } from '@expo/vector-icons';
import { router } from 'expo-router';
import React from 'react';
import {
  Platform,
  SafeAreaView,
  StatusBar,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from 'react-native';
import { AppHeader } from '../components/common/AppHeader';
import { Palette } from '../constants/theme';

export default function CompetitiveDashboard() {
  if (Platform.OS === 'web') {
    return (
      <SafeAreaView style={styles.safeArea}>
        <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
        <AppHeader showBack title="Competitive Exams Suite" subtitle="Powered by SkillExa Competitive Platform" />
        <View style={styles.webContainer}>
          <iframe
            src="http://localhost:5173"
            style={{
              width: '100%',
              height: '100%',
              border: 'none',
              flex: 1,
            } as any}
            title="Competitive Exams Platform"
          />
        </View>
      </SafeAreaView>
    );
  }

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader showBack title="Competitive Exams" subtitle="Aptitude & Govt Exam Suite" />
      <View style={styles.fallbackContainer}>
        <Feather name="award" size={48} color={Palette.primary} />
        <Text style={styles.fallbackTitle}>Competitive Exams Platform</Text>
        <Text style={styles.fallbackSubtitle}>
          Open the Competitive Exam Platform in your web browser.
        </Text>
        <TouchableOpacity
          style={styles.openBtn}
          onPress={() => {
            if (typeof window !== 'undefined') {
              window.open('http://localhost:5173', '_blank');
            }
          }}
        >
          <Text style={styles.openBtnText}>Open Competitive Platform</Text>
          <Feather name="external-link" size={16} color="#FFFFFF" />
        </TouchableOpacity>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: '#0B1120' },
  webContainer: { flex: 1, backgroundColor: '#0B1120' },
  fallbackContainer: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    padding: 24,
    backgroundColor: Palette.background,
  },
  fallbackTitle: {
    fontSize: 20,
    fontWeight: '800',
    color: Palette.textTitle,
    marginTop: 16,
    marginBottom: 8,
  },
  fallbackSubtitle: {
    fontSize: 14,
    color: Palette.textSecondary,
    textAlign: 'center',
    marginBottom: 24,
  },
  openBtn: {
    backgroundColor: Palette.primary,
    paddingVertical: 14,
    paddingHorizontal: 24,
    borderRadius: 12,
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  openBtnText: {
    color: '#FFFFFF',
    fontSize: 15,
    fontWeight: '700',
  },
});