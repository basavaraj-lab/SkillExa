import { LinearGradient } from 'expo-linear-gradient';
import React from 'react';
import {
  StyleProp,
  StyleSheet,
  TouchableOpacity,
  View,
  ViewStyle,
} from 'react-native';
import { Gradients, Palette } from '../../constants/theme';

interface GlassCardProps {
  children: React.ReactNode;
  style?: StyleProp<ViewStyle>;
  contentStyle?: StyleProp<ViewStyle>;
  gradientColors?: readonly [string, string, ...string[]];
  borderColor?: string;
  onPress?: () => void;
  activeOpacity?: number;
  glow?: boolean;
}

export function GlassCard({
  children,
  style,
  contentStyle,
  gradientColors = Gradients.darkGlass,
  borderColor = Palette.glassBorder,
  onPress,
  activeOpacity = 0.85,
  glow = false,
}: GlassCardProps) {
  const ContainerComponent = onPress ? TouchableOpacity : View;

  return (
    <ContainerComponent
      activeOpacity={activeOpacity}
      onPress={onPress}
      style={[
        styles.outerContainer,
        { borderColor },
        glow && styles.glowStyle,
        style,
      ]}
    >
      <LinearGradient
        colors={gradientColors as [string, string, ...string[]]}
        start={{ x: 0, y: 0 }}
        end={{ x: 1, y: 1 }}
        style={[styles.gradientLayer, contentStyle]}
      >
        {children}
      </LinearGradient>
    </ContainerComponent>
  );
}

const styles = StyleSheet.create({
  outerContainer: {
    borderRadius: 20,
    borderWidth: 1,
    overflow: 'hidden',
    backgroundColor: 'rgba(15, 23, 42, 0.65)',
  },
  gradientLayer: {
    padding: 16,
    borderRadius: 20,
  },
  glowStyle: {
    shadowColor: Palette.cyan,
    shadowOffset: { width: 0, height: 6 },
    shadowOpacity: 0.25,
    shadowRadius: 16,
    elevation: 8,
    borderColor: Palette.glassBorderCyan,
  },
});
