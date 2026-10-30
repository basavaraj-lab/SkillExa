import { Feather, Ionicons } from '@expo/vector-icons';
import { router, usePathname } from 'expo-router';
import React from 'react';
import {
  Platform,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from 'react-native';
import { useSafeAreaInsets } from 'react-native-safe-area-context';
import { Palette, Shadows } from '../../constants/theme';

interface NavItem {
  id: string;
  label: string;
  iconName: string;
  iconFamily: 'feather' | 'ionicons';
  route: string;
}

const NAV_ITEMS: NavItem[] = [
  { id: 'home', label: 'Home', iconName: 'home', iconFamily: 'feather', route: '/home' },
  { id: 'engineering', label: 'Engineering', iconName: 'school-outline', iconFamily: 'ionicons', route: '/engineering' },
  { id: 'competitive', label: 'Competitive', iconName: 'target', iconFamily: 'feather', route: '/competitive' },
  { id: 'profile', label: 'Profile', iconName: 'user', iconFamily: 'feather', route: '/profile' },
];

export function BottomNav() {
  const pathname = usePathname();
  const insets = useSafeAreaInsets();

  // Hidden on focused experiences
  const hiddenRoutes = [
    '/',
    '/splash',
    '/login',
    '/register',
    '/register-user',
    '/register-lecturer',
    '/coding/compiler',
    '/quizzpage',
    '/quiz-result',
    '/answer-review',
    '/live-interview',
    '/aptitude-test',
  ];

  if (hiddenRoutes.some(r => pathname === r || pathname.startsWith(r))) {
    return null;
  }

  const getActiveTab = () => {
    if (pathname === '/home' || pathname === '/') return 'home';
    if (pathname.startsWith('/engineering') || pathname.includes('pathselection') || pathname.includes('topic-learning')) return 'engineering';
    if (pathname.startsWith('/competitive') || pathname.includes('aptitude') || pathname.includes('mathematics') || pathname.includes('reasoning') || pathname.includes('english') || pathname.includes('awareness') || pathname.includes('science') || pathname.includes('fitness')) return 'competitive';
    if (pathname.startsWith('/profile') || pathname.includes('settings')) return 'profile';
    return 'home';
  };

  const activeTab = getActiveTab();

  return (
    <View style={[styles.wrapper, { paddingBottom: Math.max(insets.bottom, 8) }]}>
      <View style={styles.container}>
        {NAV_ITEMS.map((item) => {
          const isActive = activeTab === item.id;
          return (
            <TouchableOpacity
              key={item.id}
              style={styles.tabButton}
              onPress={() => router.push(item.route as any)}
              activeOpacity={0.7}
            >
              {item.iconFamily === 'ionicons' ? (
                <Ionicons
                  name={item.iconName as any}
                  size={21}
                  color={isActive ? Palette.primary : Palette.textMuted}
                />
              ) : (
                <Feather
                  name={item.iconName as any}
                  size={19}
                  color={isActive ? Palette.primary : Palette.textMuted}
                />
              )}
              <Text
                style={[
                  styles.tabLabel,
                  isActive && styles.tabLabelActive,
                ]}
                numberOfLines={1}
              >
                {item.label}
              </Text>
            </TouchableOpacity>
          );
        })}
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  wrapper: {
    backgroundColor: '#FFFFFF',
    borderTopWidth: 1,
    borderTopColor: Palette.border,
    paddingTop: 6,
    zIndex: 9999,
    ...(Platform.OS === 'web'
      ? ({
          position: 'fixed' as const,
          bottom: 0,
          left: 0,
          right: 0,
          boxShadow: '0 -4px 16px rgba(0, 0, 0, 0.06)',
        } as any)
      : {
          elevation: 12,
          shadowColor: '#000',
          shadowOffset: { width: 0, height: -3 },
          shadowOpacity: 0.08,
          shadowRadius: 10,
        }),
  },
  container: {
    flexDirection: 'row',
    justifyContent: 'space-around',
    alignItems: 'center',
    maxWidth: 960,
    alignSelf: 'center',
    width: '100%',
    paddingHorizontal: 8,
  },
  tabButton: {
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 4,
    paddingHorizontal: 4,
    flex: 1,
    minHeight: 44,
  },
  tabLabel: {
    fontSize: 11,
    fontWeight: '600',
    color: Palette.textMuted,
    marginTop: 3,
  },
  tabLabelActive: {
    color: Palette.primary,
    fontWeight: '800',
  },
});
