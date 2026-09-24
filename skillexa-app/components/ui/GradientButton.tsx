import { LinearGradient } from 'expo-linear-gradient';
import React from 'react';
import {
  ActivityIndicator,
  StyleProp,
  StyleSheet,
  Text,
  TextStyle,
  TouchableOpacity,
  ViewStyle,
} from 'react-native';
import { Gradients, Palette } from '../../constants/theme';

interface GradientButtonProps {
  title: string;
  onPress: () => void;
  gradientColors?: readonly [string, string, ...string[]];
  icon?: React.ReactNode;
  loading?: boolean;
  disabled?: boolean;
  style?: StyleProp<ViewStyle>;
  textStyle?: StyleProp<TextStyle>;
  glow?: boolean;
}

export function GradientButton({
  title,
  onPress,
  gradientColors = Gradients.primary,
  icon,
  loading = false,
  disabled = false,
  style,
  textStyle,
  glow = true,
}: GradientButtonProps) {
  return (
    <TouchableOpacity
      activeOpacity={0.85}
      onPress={onPress}
      disabled={disabled || loading}
      style={[
        styles.touchable,
        glow && !disabled && styles.glowStyle,
        disabled && styles.disabledStyle,
        style,
      ]}
    >
      <LinearGradient
        colors={disabled ? ['#334155', '#1e293b'] : (gradientColors as [string, string, ...string[]])}
        start={{ x: 0, y: 0 }}
        end={{ x: 1, y: 0 }}
        style={styles.gradient}
      >
        {loading ? (
          <ActivityIndicator color="#ffffff" size="small" />
        ) : (
          <>
            {icon}
            <Text style={[styles.title, textStyle]}>{title}</Text>
          </>
        )}
      </LinearGradient>
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({
  touchable: {
    borderRadius: 14,
    overflow: 'hidden',
  },
  gradient: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: 14,
    paddingHorizontal: 20,
    gap: 8,
  },
  title: {
    color: '#ffffff',
    fontSize: 16,
    fontWeight: '700',
    letterSpacing: 0.5,
  },
  glowStyle: {
    shadowColor: Palette.primary,
    shadowOffset: { width: 0, height: 6 },
    shadowOpacity: 0.35,
    shadowRadius: 12,
    elevation: 6,
  },
  disabledStyle: {
    opacity: 0.6,
    shadowOpacity: 0,
    elevation: 0,
  },
});
