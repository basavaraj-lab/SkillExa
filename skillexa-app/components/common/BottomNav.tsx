import { Feather } from '@expo/vector-icons';
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
  icon: keyof typeof Feather.glyphMap;
  route: string;
}

const NAV_ITEMS: NavItem[] = [
  { id: 'home', label: 'Home', icon: 'home', route: '/home' },
  { id: 'learn', label: 'Learn', icon: 'book-open', route: '/pathselection' },
  { id: 'practice', label: 'Practice', icon: 'check-circle', route: '/coding-problems' },
  { id: 'progress', label: 'Progress', icon: 'bar-chart-2', route: '/progress' },
  { id: 'profile', label: 'Profile', icon: 'user', route: '/profile' },
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
  ];

  if (hiddenRoutes.some(r => pathname === r || pathname.startsWith(r))) {
    return null;
  }

  const getActiveTab = () => {
    if (pathname === '/home' || pathname === '/') return 'home';
    if (pathname.includes('pathselection') || pathname.includes('engineering') || pathname.includes('competitive') || pathname.includes('english') || pathname.includes('mathematics') || pathname.includes('reasoning') || pathname.includes('awareness') || pathname.includes('science') || pathname.includes('fitness') || pathname.includes('topic-learning')) return 'learn';
    if (pathname.includes('coding-problems') || pathname.includes('dsa-practice') || pathname.includes('placement-preparation')) return 'practice';
    if (pathname.includes('progress') || pathname.includes('userdashboard') || pathname.includes('subjectdashboard')) return 'progress';
    if (pathname.includes('profile')) return 'profile';
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
              <Feather
                name={item.icon}
                size={20}
                color={isActive ? Palette.primary : Palette.textMuted}
              />
              <Text
                style={[
                  styles.tabLabel,
                  isActive && styles.tabLabelActive,
                ]}
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
    paddingTop: 8,
    ...Shadows.floating,
  },
  container: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-around',
    paddingHorizontal: 8,
  },
  tabButton: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 4,
  },
  tabLabel: {
    fontSize: 11,
    fontWeight: '500',
    color: Palette.textMuted,
    marginTop: 3,
  },
  tabLabelActive: {
    color: Palette.primary,
    fontWeight: '700',
  },
});
