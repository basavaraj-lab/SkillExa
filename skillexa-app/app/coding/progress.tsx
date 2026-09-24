import React from 'react';
import {
  StyleSheet,
  Text,
  View,
  ScrollView,
  TouchableOpacity,
  SafeAreaView,
  StatusBar,
} from 'react-native';
import { router } from 'expo-router';
import { Feather } from '@expo/vector-icons';

export default function ProgressDashboardScreen() {
  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      
      {/* Header */}
      <View style={styles.header}>
        <TouchableOpacity style={styles.backBtn} onPress={() => router.back()}>
          <Feather name="arrow-left" size={20} color="#1E293B" />
        </TouchableOpacity>
        <Text style={styles.headerTitle}>Progress Dashboard</Text>
      </View>

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {/* Problems Solved Matrix */}
        <View style={styles.card}>
          <Text style={styles.cardHeading}>Problems Solved</Text>
          
          <View style={styles.statRow}>
            <Text style={styles.statLabel}>Easy</Text>
            <Text style={styles.statValue}>45 / 120</Text>
          </View>
          <View style={styles.barBg}><View style={[styles.barFill, { width: '37%' }]} /></View>

          <View style={styles.statRow}>
            <Text style={styles.statLabel}>Medium</Text>
            <Text style={styles.statValue}>20 / 100</Text>
          </View>
          <View style={styles.barBg}><View style={[styles.barFill, { width: '20%', backgroundColor: '#D97706' }]} /></View>

          <View style={styles.statRow}>
            <Text style={styles.statLabel}>Hard</Text>
            <Text style={styles.statValue}>5 / 80</Text>
          </View>
          <View style={styles.barBg}><View style={[styles.barFill, { width: '6%', backgroundColor: '#DC2626' }]} /></View>
        </View>

        {/* Quick Metrics Grid */}
        <View style={styles.grid}>
          <View style={styles.gridCard}>
            <Feather name="zap" size={22} color="#2563EB" />
            <Text style={styles.gridVal}>7 Days</Text>
            <Text style={styles.gridLbl}>Daily Streak</Text>
          </View>

          <View style={styles.gridCard}>
            <Feather name="award" size={22} color="#2563EB" />
            <Text style={styles.gridVal}>2450</Text>
            <Text style={styles.gridLbl}>Total XP</Text>
          </View>

          <View style={styles.gridCard}>
            <Feather name="shield" size={22} color="#2563EB" />
            <Text style={styles.gridVal}>2</Text>
            <Text style={styles.gridLbl}>Certificates</Text>
          </View>

          <View style={styles.gridCard}>
            <Feather name="star" size={22} color="#2563EB" />
            <Text style={styles.gridVal}>4 Badges</Text>
            <Text style={styles.gridLbl}>Unlocked</Text>
          </View>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#FFFFFF' },
  header: { paddingHorizontal: 24, paddingTop: 12, paddingBottom: 12, flexDirection: 'row', alignItems: 'center', borderBottomWidth: 1, borderBottomColor: '#E2E8F0' },
  backBtn: { marginRight: 12 },
  headerTitle: { fontSize: 20, fontWeight: '800', color: '#1E293B' },
  scrollContent: { padding: 24 },
  card: { backgroundColor: '#FFFFFF', borderRadius: 18, padding: 18, marginBottom: 20, borderWidth: 1, borderColor: '#F1F5F9', elevation: 2 },
  cardHeading: { fontSize: 16, fontWeight: '700', color: '#1E293B', marginBottom: 14 },
  statRow: { flexDirection: 'row', justifyContent: 'space-between', marginTop: 10 },
  statLabel: { fontSize: 13, fontWeight: '600', color: '#64748B' },
  statValue: { fontSize: 13, fontWeight: '700', color: '#1E293B' },
  barBg: { height: 6, backgroundColor: '#F1F5F9', borderRadius: 10, marginTop: 6, overflow: 'hidden' },
  barFill: { height: '100%', backgroundColor: '#16A34A', borderRadius: 10 },
  grid: { flexDirection: 'row', flexWrap: 'wrap', justifyContent: 'space-between' },
  gridCard: { width: '48%', backgroundColor: '#F8FAFC', borderRadius: 16, padding: 16, marginBottom: 14, borderWidth: 1, borderColor: '#E2E8F0', alignItems: 'center' },
  gridVal: { fontSize: 20, fontWeight: '800', color: '#1E293B', marginTop: 8 },
  gridLbl: { fontSize: 12, color: '#64748B', marginTop: 2, fontWeight: '500' },
});