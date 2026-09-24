import { Platform } from 'react-native';

export const Palette = {
  // Primary Brand
  primary: '#2563EB',          // Vibrant Educational Blue
  primaryHover: '#1D4ED8',
  primaryLight: '#EFF6FF',
  primaryBorder: '#BFDBFE',

  // Status & Semantic Accents
  success: '#10B981',          // Green for success & completed
  successLight: '#ECFDF5',
  successBorder: '#A7F3D0',
  emerald: '#10B981',

  warning: '#F59E0B',          // Orange / Amber for in-progress & streaks
  warningLight: '#FFFBEB',
  warningBorder: '#FDE68A',
  amber: '#F59E0B',
  amberLight: '#FFFBEB',
  amberGlow: '#F59E0B',

  danger: '#EF4444',           // Red for error / incorrect
  dangerLight: '#FEF2F2',
  dangerBorder: '#FECACA',
  rose: '#EF4444',
  roseLight: '#FEF2F2',

  aiPurple: '#8B5CF6',         // Purple used ONLY for AI Mock Interview & AI features
  aiPurpleHover: '#7C3AED',
  aiPurpleLight: '#F5F3FF',
  aiPurpleBorder: '#DDD6FE',
  purpleLight: '#F5F3FF',

  cyan: '#2563EB',
  cyanLight: '#EFF6FF',
  cyanGlow: '#2563EB',

  techNavy: '#0F172A',         // Technical & Code Dark Navy
  techNavyLight: '#1E293B',

  // Surfaces & Backgrounds
  background: '#F8FAFC',       // Clean off-white canvas
  backgroundSecondary: '#F1F5F9',
  bgDark: '#F8FAFC',
  card: '#FFFFFF',             // Pure White Card
  cardElevated: '#FFFFFF',
  
  // Borders & Dividers
  border: '#E2E8F0',           // Very subtle gray
  borderSubtle: '#F1F5F9',
  borderStrong: '#CBD5E1',
  glassBorder: '#E2E8F0',
  glassBorderCyan: '#BFDBFE',
  glassBorderPrimary: '#BFDBFE',
  glassBorderHighlight: '#E2E8F0',

  // Typography Hierarchy
  textTitle: '#0F172A',        // Page & Section Titles
  textBody: '#334155',         // Descriptions & Body
  textSecondary: '#64748B',    // Subtitles & Secondary
  textSecondaryDark: '#64748B',
  textMuted: '#94A3B8',        // Metadata, timestamps, timestamps
  textMutedDark: '#94A3B8',
  textWhite: '#FFFFFF',
};

export const Gradients = {
  primary: ['#2563EB', '#1D4ED8'] as const,
  primarySubtle: ['#EFF6FF', '#DBEAFE'] as const,
  cardGlass: ['#FFFFFF', '#FFFFFF'] as const,
  cardElevated: ['#FFFFFF', '#FFFFFF'] as const,
  darkGlass: ['#FFFFFF', '#FFFFFF'] as const,
  cyanButton: ['#2563EB', '#1D4ED8'] as const,
  cyanBlue: ['#2563EB', '#1D4ED8'] as const,
  purpleButton: ['#8B5CF6', '#7C3AED'] as const,
  purpleIndigo: ['#8B5CF6', '#7C3AED'] as const,
  accentWarm: ['#F59E0B', '#D97706'] as const,
  accentSuccess: ['#10B981', '#059669'] as const,
  glowRing: ['#BFDBFE', 'transparent'] as const,
  meshDark: ['#F8FAFC', '#F1F5F9'] as const,
};

export const Colors = {
  light: {
    text: Palette.textTitle,
    textSecondary: Palette.textSecondary,
    textMuted: Palette.textMuted,
    background: Palette.background,
    surface: Palette.card,
    tint: Palette.primary,
    icon: Palette.textSecondary,
    tabIconDefault: '#94A3B8',
    tabIconSelected: Palette.primary,
    border: Palette.border,
    card: Palette.card,
  },
  dark: {
    text: Palette.textTitle,
    textSecondary: Palette.textSecondary,
    textMuted: Palette.textMuted,
    background: Palette.background,
    surface: Palette.card,
    tint: Palette.primary,
    icon: Palette.textSecondary,
    tabIconDefault: '#94A3B8',
    tabIconSelected: Palette.primary,
    border: Palette.border,
    card: Palette.card,
  },
};

export const Shadows = {
  card: {
    shadowColor: '#0F172A',
    shadowOffset: { width: 0, height: 1 },
    shadowOpacity: 0.04,
    shadowRadius: 6,
    elevation: 2,
  },
  floating: {
    shadowColor: '#0F172A',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.08,
    shadowRadius: 16,
    elevation: 4,
  },
  button: {
    shadowColor: '#2563EB',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.15,
    shadowRadius: 6,
    elevation: 3,
  },
};

export const Radii = {
  button: 12,
  card: 18,
  cardLarge: 20,
  pill: 999,
  input: 12,
};

export const Fonts = Platform.select({
  ios: {
    sans: 'system-ui',
    serif: 'ui-serif',
    rounded: 'ui-rounded',
    mono: 'ui-monospace',
  },
  default: {
    sans: 'normal',
    serif: 'serif',
    rounded: 'normal',
    mono: 'monospace',
  },
  web: {
    sans: "Inter, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
    serif: "Georgia, 'Times New Roman', serif",
    rounded: "'SF Pro Rounded', 'Hiragino Maru Gothic ProN', Meiryo, sans-serif",
    mono: "SFMono-Regular, Menlo, Monaco, Consolas, 'Fira Code', 'Courier New', monospace",
  },
});
