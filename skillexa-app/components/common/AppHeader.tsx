import { Feather } from '@expo/vector-icons';
import { router } from 'expo-router';
import React from 'react';
import {
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from 'react-native';
import { useSafeAreaInsets } from 'react-native-safe-area-context';
import { Palette, Radii } from '../../constants/theme';
import { NotificationBellButton } from '../CollegeNotificationsModal';
import { useAuth } from '../auth-context';
import { BackendStatusBadge } from './BackendStatusBadge';

interface AppHeaderProps {
  title?: string;
  subtitle?: string;
  showBack?: boolean;
  onBack?: () => void;
  rightAction?: React.ReactNode;
}

export function AppHeader({
  title,
  subtitle,
  showBack = false,
  onBack,
  rightAction,
}: AppHeaderProps) {
  const insets = useSafeAreaInsets();
  const { profile } = useAuth();
  const initial = (profile?.name || 'User').charAt(0).toUpperCase();

  const handleBack = () => {
    if (onBack) {
      onBack();
    } else {
      router.back();
    }
  };

  return (
    <View style={[styles.container, { paddingTop: Math.max(insets.top, 12) + 6 }]}>
      <View style={styles.contentRow}>
        {showBack ? (
          <TouchableOpacity
            style={styles.backButton}
            onPress={handleBack}
            activeOpacity={0.7}
          >
            <Feather name="arrow-left" size={20} color={Palette.textTitle} />
            <Text style={styles.backLabel}>Back</Text>
          </TouchableOpacity>
        ) : (
          <View style={styles.brandRow}>
            <View style={styles.brandIconBox}>
              <Feather name="book-open" size={16} color="#FFFFFF" />
            </View>
            <Text style={styles.brandTitle}>
              Skill<Text style={styles.brandHighlight}>Exa</Text>
            </Text>
          </View>
        )}

        {/* Center Title when in inner page */}
        {showBack && title && (
          <View style={styles.centerTitleWrapper}>
            <Text style={styles.centerTitle} numberOfLines={1}>
              {title}
            </Text>
            {subtitle && (
              <Text style={styles.centerSubtitle} numberOfLines={1}>
                {subtitle}
              </Text>
            )}
          </View>
        )}

        {/* Right side Profile / Custom action */}
        <View style={styles.rightGroup}>
          {rightAction ? (
            rightAction
          ) : (
            <View style={{ flexDirection: 'row', alignItems: 'center', gap: 7 }}>
              <BackendStatusBadge compact />
              <NotificationBellButton />
              <TouchableOpacity
                style={styles.avatarButton}
                onPress={() => router.push('/profile' as any)}
                activeOpacity={0.8}
              >
                <Text style={styles.avatarText}>{initial}</Text>
              </TouchableOpacity>
            </View>
          )}
        </View>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: '#FFFFFF',
    borderBottomWidth: 1,
    borderBottomColor: Palette.border,
    paddingHorizontal: 16,
    paddingBottom: 12,
    zIndex: 50,
  },
  contentRow: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    minHeight: 38,
  },
  brandRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  brandIconBox: {
    width: 28,
    height: 28,
    borderRadius: 8,
    backgroundColor: Palette.primary,
    alignItems: 'center',
    justifyContent: 'center',
  },
  brandTitle: {
    fontSize: 20,
    fontWeight: '800',
    color: Palette.textTitle,
    letterSpacing: -0.4,
  },
  brandHighlight: {
    color: Palette.primary,
  },
  backButton: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    paddingVertical: 4,
    paddingRight: 8,
  },
  backLabel: {
    fontSize: 15,
    fontWeight: '600',
    color: Palette.textTitle,
  },
  centerTitleWrapper: {
    flex: 1,
    alignItems: 'center',
    paddingHorizontal: 8,
  },
  centerTitle: {
    fontSize: 16,
    fontWeight: '700',
    color: Palette.textTitle,
  },
  centerSubtitle: {
    fontSize: 11,
    color: Palette.textSecondary,
    marginTop: 1,
  },
  rightGroup: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  avatarButton: {
    width: 34,
    height: 34,
    borderRadius: Radii.pill,
    backgroundColor: Palette.primaryLight,
    borderWidth: 1.5,
    borderColor: Palette.primaryBorder,
    alignItems: 'center',
    justifyContent: 'center',
  },
  avatarText: {
    fontSize: 14,
    fontWeight: '800',
    color: Palette.primary,
  },
});
