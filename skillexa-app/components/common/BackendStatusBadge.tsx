import { Feather } from '@expo/vector-icons';
import { router } from 'expo-router';
import React from 'react';
import { ActivityIndicator, StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import { Palette, Radii } from '../../constants/theme';
import { useBackendStatus } from '../../services/api';

export function BackendStatusBadge({ compact = false }: { compact?: boolean }) {
  const { isConnected, isChecking, message } = useBackendStatus();

  const handleOpenDiagnostics = () => {
    router.push('/system-status' as any);
  };

  if (compact) {
    return (
      <TouchableOpacity
        onPress={handleOpenDiagnostics}
        style={[
          styles.compactPill,
          isConnected ? styles.pillConnected : isConnected === false ? styles.pillOffline : styles.pillChecking,
        ]}
        activeOpacity={0.7}
      >
        {isChecking ? (
          <ActivityIndicator size={10} color={Palette.primary} />
        ) : (
          <View
            style={[
              styles.dot,
              { backgroundColor: isConnected ? Palette.success : isConnected === false ? Palette.danger : Palette.warning },
            ]}
          />
        )}
        <Text style={styles.compactText}>
          {isConnected ? '🟢 Online' : isConnected === false ? '🔴 Offline' : 'Connecting'}
        </Text>
      </TouchableOpacity>
    );
  }

  return (
    <TouchableOpacity
      onPress={handleOpenDiagnostics}
      style={[
        styles.fullCard,
        isConnected ? styles.cardConnected : isConnected === false ? styles.cardOffline : styles.cardChecking,
      ]}
      activeOpacity={0.8}
    >
      <View style={styles.leftRow}>
        <View
          style={[
            styles.statusDotLarge,
            { backgroundColor: isConnected ? Palette.success : isConnected === false ? Palette.danger : Palette.warning },
          ]}
        />
        <View>
          <Text style={styles.statusTitle}>
            {isConnected ? '🟢 Backend Connected' : isConnected === false ? '🔴 Backend Offline' : 'Connecting to Backend...'}
          </Text>
          <Text style={styles.statusSub}>{message}</Text>
        </View>
      </View>
      <Feather name="chevron-right" size={16} color={Palette.textSecondary} />
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({
  compactPill: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingHorizontal: 8,
    paddingVertical: 4,
    borderRadius: Radii.pill,
    gap: 5,
    borderWidth: 1,
  },
  pillConnected: {
    backgroundColor: '#F0FDF4',
    borderColor: '#BBF7D0',
  },
  pillOffline: {
    backgroundColor: '#FEF2F2',
    borderColor: '#FECACA',
  },
  pillChecking: {
    backgroundColor: '#FFFBEB',
    borderColor: '#FDE68A',
  },
  dot: {
    width: 6,
    height: 6,
    borderRadius: 3,
  },
  compactText: {
    fontSize: 11,
    fontWeight: '700',
    color: Palette.textTitle,
  },
  fullCard: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: 12,
    paddingVertical: 10,
    borderRadius: Radii.card,
    marginHorizontal: 16,
    marginVertical: 6,
    borderWidth: 1,
  },
  cardConnected: {
    backgroundColor: '#F0FDF4',
    borderColor: '#BBF7D0',
  },
  cardOffline: {
    backgroundColor: '#FEF2F2',
    borderColor: '#FECACA',
  },
  cardChecking: {
    backgroundColor: '#FFFBEB',
    borderColor: '#FDE68A',
  },
  leftRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 10,
  },
  statusDotLarge: {
    width: 10,
    height: 10,
    borderRadius: 5,
  },
  statusTitle: {
    fontSize: 12.5,
    fontWeight: '800',
    color: Palette.textTitle,
  },
  statusSub: {
    fontSize: 11,
    color: Palette.textSecondary,
    marginTop: 1,
  },
});
