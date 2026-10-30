import { Feather } from '@expo/vector-icons';
import React, { createContext, useContext, useEffect, useState } from 'react';
import { Platform, StyleSheet, TouchableOpacity, View } from 'react-native';

type ThemeMode = 'light' | 'dark';

interface ThemeContextType {
  theme: ThemeMode;
  isDark: boolean;
  toggleTheme: () => void;
  setTheme: (mode: ThemeMode) => void;
}

const ThemeContext = createContext<ThemeContextType>({
  theme: 'light',
  isDark: false,
  toggleTheme: () => {},
  setTheme: () => {},
});

const DARK_STYLES_CSS = `
  html, body, #root {
    background-color: #0B0F19 !important;
    color: #F8FAFC !important;
  }
  [data-theme="dark"] {
    color-scheme: dark;
    background-color: #0B0F19 !important;
  }
  /* App Root and SafeAreaViews */
  [data-theme="dark"] div[style*="background-color: rgb(248, 250, 252)"],
  [data-theme="dark"] div[style*="background-color: #F8FAFC"],
  [data-theme="dark"] div[style*="background-color: #f8fafc"],
  [data-theme="dark"] div[style*="background-color: rgb(240, 244, 250)"],
  [data-theme="dark"] div[style*="background-color: #F0F4FA"],
  [data-theme="dark"] div[style*="background-color: rgba(242, 242, 242"] {
    background-color: #0B0F19 !important;
  }
  /* Cards and Surfaces */
  [data-theme="dark"] div[style*="background-color: rgb(255, 255, 255)"],
  [data-theme="dark"] div[style*="background-color: #FFFFFF"],
  [data-theme="dark"] div[style*="background-color: #ffffff"],
  [data-theme="dark"] .r-backgroundColor-14lw9ot {
    background-color: #131B2E !important;
    border-color: #1E293B !important;
  }
  /* Secondary Surfaces & pill tracks */
  [data-theme="dark"] div[style*="background-color: rgb(241, 245, 249)"],
  [data-theme="dark"] div[style*="background-color: #F1F5F9"],
  [data-theme="dark"] div[style*="background-color: #DDE7F3"],
  [data-theme="dark"] .r-backgroundColor-1jh0li6 {
    background-color: #192238 !important;
    border-color: #243049 !important;
  }
  /* Headings & Title Texts */
  [data-theme="dark"] div[style*="color: rgb(15, 23, 42)"],
  [data-theme="dark"] div[style*="color: #0F172A"],
  [data-theme="dark"] span[style*="color: #0F172A"],
  [data-theme="dark"] .r-color-15ijx5m {
    color: #F8FAFC !important;
  }
  /* Body and Secondary Texts */
  [data-theme="dark"] div[style*="color: rgb(51, 65, 85)"],
  [data-theme="dark"] div[style*="color: #334155"],
  [data-theme="dark"] div[style*="color: rgb(100, 116, 139)"],
  [data-theme="dark"] div[style*="color: #64748B"],
  [data-theme="dark"] .r-color-1s7ct43,
  [data-theme="dark"] .r-color-dz6k1 {
    color: #94A3B8 !important;
  }
  /* Borders */
  [data-theme="dark"] div[style*="border-color: rgb(226, 232, 240)"],
  [data-theme="dark"] div[style*="border-color: #E2E8F0"],
  [data-theme="dark"] div[style*="border-bottom-color: #E2E8F0"],
  [data-theme="dark"] .r-borderColor-1wr2p1e,
  [data-theme="dark"] .r-borderBottomColor-eaxd7d {
    border-color: #1E293B !important;
  }
  /* Form Inputs */
  [data-theme="dark"] input,
  [data-theme="dark"] textarea {
    background-color: #131B2E !important;
    color: #F8FAFC !important;
    border-color: #243049 !important;
  }
  /* Bottom Nav and App Headers */
  [data-theme="dark"] div[style*="background-color: rgb(255, 255, 255)"][style*="border-top-width"],
  [data-theme="dark"] div[style*="background-color: #FFFFFF"][style*="border-bottom-width"] {
    background-color: #0F172A !important;
    border-color: #1E293B !important;
  }
`;

export function ThemeProvider({ children }: { children: React.ReactNode }) {
  const [theme, setThemeState] = useState<ThemeMode>(() => {
    if (Platform.OS === 'web' && typeof window !== 'undefined' && window.localStorage) {
      const saved = window.localStorage.getItem('skillexa_theme');
      if (saved === 'dark' || saved === 'light') return saved;
    }
    return 'light';
  });

  const setTheme = (mode: ThemeMode) => {
    setThemeState(mode);
    if (Platform.OS === 'web' && typeof window !== 'undefined' && window.localStorage) {
      try {
        window.localStorage.setItem('skillexa_theme', mode);
      } catch (e) {}
    }
  };

  const toggleTheme = () => {
    setTheme(theme === 'light' ? 'dark' : 'light');
  };

  useEffect(() => {
    if (Platform.OS === 'web' && typeof document !== 'undefined') {
      document.documentElement.setAttribute('data-theme', theme);

      let styleEl = document.getElementById('skillexa-dark-mode-styles');
      if (theme === 'dark') {
        if (!styleEl) {
          styleEl = document.createElement('style');
          styleEl.id = 'skillexa-dark-mode-styles';
          document.head.appendChild(styleEl);
        }
        styleEl.innerHTML = DARK_STYLES_CSS;
      } else {
        if (styleEl) {
          styleEl.innerHTML = '';
        }
      }
    }
  }, [theme]);

  const value = {
    theme,
    isDark: theme === 'dark',
    toggleTheme,
    setTheme,
  };

  return <ThemeContext.Provider value={value}>{children}</ThemeContext.Provider>;
}

export function useTheme() {
  return useContext(ThemeContext);
}

export function ThemeToggle({ style }: { style?: any }) {
  const { isDark, toggleTheme } = useTheme();

  return (
    <TouchableOpacity
      onPress={toggleTheme}
      activeOpacity={0.75}
      style={[
        styles.toggleBtn,
        isDark ? styles.toggleBtnDark : styles.toggleBtnLight,
        style,
      ]}
      accessibilityLabel={isDark ? 'Switch to light mode' : 'Switch to dark mode'}
      accessibilityRole="button"
    >
      <Feather
        name={isDark ? 'sun' : 'moon'}
        size={16}
        color={isDark ? '#F59E0B' : '#4F46E5'}
      />
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({
  toggleBtn: {
    width: 34,
    height: 34,
    borderRadius: 10,
    alignItems: 'center',
    justifyContent: 'center',
    borderWidth: 1,
  },
  toggleBtnLight: {
    backgroundColor: '#F1F5F9',
    borderColor: '#E2E8F0',
  },
  toggleBtnDark: {
    backgroundColor: '#1E293B',
    borderColor: '#334155',
  },
});

