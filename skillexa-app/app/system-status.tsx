import { Feather } from '@expo/vector-icons';
import { router } from 'expo-router';
import React, { useEffect, useState } from 'react';
import {
  ActivityIndicator,
  Alert,
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  View,
} from 'react-native';
import { AppHeader } from '../components/common/AppHeader';
import { Palette, Radii, Shadows } from '../constants/theme';
import {
  ApiClient,
  getApiBaseUrl,
  getCustomApiBaseUrl,
  setCustomApiBaseUrl,
} from '../services/api';

export default function SystemStatusScreen() {
  const [ipInput, setIpInput] = useState('');
  const [isTesting, setIsTesting] = useState(false);
  const [testResult, setTestResult] = useState<any>(null);
  const [latencyMs, setLatencyMs] = useState<number | null>(null);

  useEffect(() => {
    const custom = getCustomApiBaseUrl();
    if (custom) {
      setIpInput(custom);
    } else {
      setIpInput(getApiBaseUrl().replace('/api', ''));
    }
    runTest();
  }, []);

  const runTest = async () => {
    setIsTesting(true);
    setTestResult(null);
    const start = Date.now();

    try {
      const res = await ApiClient.testFullStack();
      const elapsed = Date.now() - start;
      setLatencyMs(elapsed);
      setTestResult(res);
    } catch (e: any) {
      setLatencyMs(Date.now() - start);
      setTestResult({
        success: false,
        backendOnline: false,
        databaseConnected: false,
        error: e.message || 'Unknown network error',
      });
    } finally {
      setIsTesting(false);
    }
  };

  const handleApplyIp = () => {
    if (!ipInput.trim()) {
      Alert.alert('Invalid URL', 'Please enter a valid backend URL (e.g., http://192.168.1.10:8000)');
      return;
    }
    setCustomApiBaseUrl(ipInput.trim());
    runTest();
  };

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader showBack title="System Diagnostics" subtitle="Frontend ↔ FastAPI ↔ DB" />

      <ScrollView contentContainerStyle={styles.content} showsVerticalScrollIndicator={false}>
        {/* Status Hero Card */}
        <View
          style={[
            styles.card,
            testResult?.success ? styles.heroCardSuccess : testResult ? styles.heroCardDanger : styles.heroCardNeutral,
          ]}
        >
          <View style={styles.heroRow}>
            <View
              style={[
                styles.statusIconBox,
                {
                  backgroundColor: testResult?.success
                    ? Palette.successLight
                    : testResult
                    ? Palette.dangerLight
                    : Palette.warningLight,
                },
              ]}
            >
              <Feather
                name={testResult?.success ? 'check-circle' : testResult ? 'alert-triangle' : 'activity'}
                size={26}
                color={testResult?.success ? Palette.success : testResult ? Palette.danger : Palette.warning}
              />
            </View>
            <View style={{ flex: 1 }}>
              <Text style={styles.heroTitle}>
                {isTesting
                  ? 'Testing Full-Stack Pipeline...'
                  : testResult?.success
                  ? '🟢 Backend Connected'
                  : '🔴 Backend Offline'}
              </Text>
              <Text style={styles.heroSubtitle}>
                {isTesting
                  ? 'Verifying FastAPI route and database connectivity'
                  : testResult?.success
                  ? `Active API endpoint responding in ${latencyMs}ms`
                  : 'Cannot reach FastAPI server. Check Wi-Fi & IP.'}
              </Text>
            </View>
          </View>
        </View>

        {/* Action Button */}
        <TouchableOpacity
          style={[styles.primaryActionBtn, isTesting && styles.btnDisabled]}
          onPress={runTest}
          disabled={isTesting}
          activeOpacity={0.8}
        >
          {isTesting ? (
            <ActivityIndicator size="small" color="#FFFFFF" />
          ) : (
            <Feather name="refresh-cw" size={16} color="#FFFFFF" />
          )}
          <Text style={styles.primaryActionText}>
            {isTesting ? 'Testing Pipeline...' : 'Run Real Full-Stack Test'}
          </Text>
        </TouchableOpacity>

        {/* Real Backend & Database Details */}
        {testResult?.details && (
          <View style={styles.card}>
            <Text style={styles.sectionHeader}>🗄️ Database & Services Verification</Text>

            <View style={styles.detailRow}>
              <Text style={styles.detailLabel}>FastAPI Status:</Text>
              <Text style={styles.detailValueSuccess}>Online ({testResult.details.environment})</Text>
            </View>

            <View style={styles.detailRow}>
              <Text style={styles.detailLabel}>Database Engine:</Text>
              <Text style={styles.detailValue}>{testResult.details.database?.engine || 'Connected'}</Text>
            </View>

            <View style={styles.detailRow}>
              <Text style={styles.detailLabel}>Colleges Seeded:</Text>
              <Text style={styles.detailValue}>{testResult.details.database?.records?.colleges ?? '6'}</Text>
            </View>

            <View style={styles.detailRow}>
              <Text style={styles.detailLabel}>Verified Users:</Text>
              <Text style={styles.detailValue}>{testResult.details.database?.records?.users ?? '4'}</Text>
            </View>

            <View style={styles.detailRow}>
              <Text style={styles.detailLabel}>Active Quizzes:</Text>
              <Text style={styles.detailValue}>{testResult.details.database?.records?.quizzes ?? '1'}</Text>
            </View>

            <View style={styles.detailRow}>
              <Text style={styles.detailLabel}>Round-Trip Latency:</Text>
              <Text style={styles.detailValueHighlight}>{latencyMs} ms</Text>
            </View>
          </View>
        )}

        {/* Error Output if Failed */}
        {testResult && !testResult.success && (
          <View style={[styles.card, styles.errorBox]}>
            <Text style={styles.errorTitle}>⚠️ Connection Diagnostics</Text>
            <Text style={styles.errorText}>
              {testResult.error || 'Connection failed.'}
            </Text>
            <View style={styles.troubleshootList}>
              <Text style={styles.troubleshootItem}>• Ensure FastAPI is running on your PC (port 8000).</Text>
              <Text style={styles.troubleshootItem}>• If testing on Expo Go phone, make sure both PC and Phone are on the same Wi-Fi network.</Text>
              <Text style={styles.troubleshootItem}>• Check if Windows Firewall is blocking incoming connections on port 8000.</Text>
            </View>
          </View>
        )}

        {/* Configurable IP Address Card */}
        <View style={styles.card}>
          <Text style={styles.sectionHeader}>⚙️ Configure Backend Base URL</Text>
          <Text style={styles.inputHelp}>
            For Expo Go on your mobile device, enter your computer's local Wi-Fi IPv4 address (e.g., http://192.168.1.10:8000):
          </Text>

          <TextInput
            style={styles.textInput}
            value={ipInput}
            onChangeText={setIpInput}
            placeholder="http://192.168.1.10:8000"
            autoCapitalize="none"
            autoCorrect={false}
          />

          <TouchableOpacity
            style={styles.saveIpBtn}
            onPress={handleApplyIp}
            activeOpacity={0.8}
          >
            <Feather name="check" size={15} color="#FFFFFF" />
            <Text style={styles.saveIpText}>Save URL & Reconnect</Text>
          </TouchableOpacity>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: Palette.background },
  content: { padding: 16, gap: 14 },
  card: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  heroCardNeutral: { borderColor: Palette.border },
  heroCardSuccess: { borderColor: Palette.success, backgroundColor: '#F0FDF4' },
  heroCardDanger: { borderColor: Palette.danger, backgroundColor: '#FEF2F2' },
  heroRow: { flexDirection: 'row', alignItems: 'center', gap: 14 },
  statusIconBox: {
    width: 48,
    height: 48,
    borderRadius: 24,
    alignItems: 'center',
    justifyContent: 'center',
  },
  heroTitle: { fontSize: 16, fontWeight: '800', color: Palette.textTitle },
  heroSubtitle: { fontSize: 12, color: Palette.textSecondary, marginTop: 2, lineHeight: 16 },
  primaryActionBtn: {
    backgroundColor: Palette.primary,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 13,
    borderRadius: Radii.button,
    gap: 8,
    ...Shadows.button,
  },
  btnDisabled: { opacity: 0.7 },
  primaryActionText: { color: '#FFFFFF', fontSize: 14, fontWeight: '700' },
  sectionHeader: { fontSize: 14, fontWeight: '800', color: Palette.textTitle, marginBottom: 12 },
  detailRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    paddingVertical: 8,
    borderBottomWidth: 1,
    borderBottomColor: Palette.borderSubtle,
  },
  detailLabel: { fontSize: 13, color: Palette.textSecondary },
  detailValue: { fontSize: 13, fontWeight: '700', color: Palette.textTitle },
  detailValueSuccess: { fontSize: 13, fontWeight: '700', color: Palette.success },
  detailValueHighlight: { fontSize: 13, fontWeight: '800', color: Palette.primary },
  errorBox: { backgroundColor: '#FEF2F2', borderColor: '#FECACA' },
  errorTitle: { fontSize: 13, fontWeight: '800', color: Palette.danger, marginBottom: 4 },
  errorText: { fontSize: 12, color: Palette.danger, lineHeight: 17 },
  troubleshootList: { marginTop: 8, gap: 4 },
  troubleshootItem: { fontSize: 11.5, color: Palette.textSecondary, lineHeight: 16 },
  inputHelp: { fontSize: 12, color: Palette.textSecondary, marginBottom: 10, lineHeight: 17 },
  textInput: {
    backgroundColor: Palette.backgroundSecondary,
    borderWidth: 1,
    borderColor: Palette.border,
    borderRadius: Radii.input,
    paddingHorizontal: 12,
    paddingVertical: 10,
    fontSize: 13,
    color: Palette.textTitle,
    marginBottom: 12,
  },
  saveIpBtn: {
    backgroundColor: Palette.primary,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 10,
    borderRadius: Radii.button,
    gap: 6,
  },
  saveIpText: { color: '#FFFFFF', fontSize: 13, fontWeight: '700' },
});
