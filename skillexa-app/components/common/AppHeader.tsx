import { Feather } from '@expo/vector-icons';
import { router, usePathname } from 'expo-router';
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
import { ThemeToggle } from '../theme-context';

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
  const pathname = usePathname();
  const isFac =
    profile?.role === 'FACULTY' ||
    profile?.role === 'ADMIN' ||
    profile?.email?.includes('faculty') ||
    profile?.email === 'dr.ramesh@kvgce.edu.in';

  const initial = (profile?.name || (isFac ? 'Dr. Ramesh' : 'User')).charAt(0).toUpperCase();

  const handleBack = () => {
    if (onBack) {
      onBack();
    } else if (pathname?.startsWith('/faculty/') || (isFac && pathname !== '/faculty-dashboard')) {
      router.replace('/faculty-dashboard' as any);
    } else if (router.canGoBack()) {
      router.back();
    } else {
      if (isFac) {
        router.replace('/faculty-dashboard' as any);
      } else {
        router.replace('/home' as any);
      }
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
              <Feather name="layers" size={16} color="#FFFFFF" />
            </View>
            <View>
              <Text style={styles.brandTitle}>
                Skill<Text style={styles.brandHighlight}>Exa</Text>
              </Text>
              <Text style={styles.brandTagline}>Learn • Practice • Achieve</Text>
            </View>
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
          <ThemeToggle style={{ marginRight: 7 }} />
          {rightAction ? (
            rightAction
          ) : (
            <View style={{ flexDirection: 'row', alignItems: 'center', gap: 7 }}>
              <NotificationBellButton />
              <TouchableOpacity
                style={styles.avatarButton}
                onPress={() => router.push('/profile' as any)}
                activeOpacity={0.8}
              >
                <Feather name="user" size={16} color={Palette.primary} />
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
    minHeight: 40,
    maxWidth: 1240,
    width: '100%',
    alignSelf: 'center',
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
    fontSize: 18,
    fontWeight: '800',
    color: Palette.textTitle,
    letterSpacing: -0.4,
  },
  brandTagline: {
    fontSize: 10,
    fontWeight: '500',
    color: Palette.textSecondary,
    marginTop: -2,
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
