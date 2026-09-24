import { Feather } from '@expo/vector-icons';
import React, { useState } from 'react';
import {
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from 'react-native';
import { Palette, Radii, Shadows } from '../../constants/theme';

// --- Note Card (📖 Note cards) ---
export function NoteCard({ title, children }: { title?: string; children: React.ReactNode }) {
  return (
    <View style={styles.noteContainer}>
      <View style={styles.cardHeaderRow}>
        <Feather name="book-open" size={16} color={Palette.primary} />
        <Text style={styles.noteTitle}>{title || 'Concept Summary'}</Text>
      </View>
      <View style={styles.cardBody}>{typeof children === 'string' ? <Text style={styles.cardText}>{children}</Text> : children}</View>
    </View>
  );
}

// --- Example Card (💡 Example cards) ---
export function ExampleCard({ title, example, explanation }: { title?: string; example: string; explanation?: string }) {
  return (
    <View style={styles.exampleContainer}>
      <View style={styles.cardHeaderRow}>
        <Feather name="zap" size={16} color={Palette.warning} />
        <Text style={styles.exampleTitle}>{title || 'Practical Example'}</Text>
      </View>
      <View style={styles.exampleBox}>
        <Text style={styles.exampleCodeText}>{example}</Text>
      </View>
      {explanation && <Text style={styles.exampleExplanation}>{explanation}</Text>}
    </View>
  );
}

// --- Important Rule Card (⚠️ Important rule cards) ---
export function RuleCard({ title, rules }: { title?: string; rules: string[] }) {
  return (
    <View style={styles.ruleContainer}>
      <View style={styles.cardHeaderRow}>
        <Feather name="alert-circle" size={16} color={Palette.danger} />
        <Text style={styles.ruleTitle}>{title || 'Crucial Grammar & Exam Rules'}</Text>
      </View>
      <View style={styles.rulesList}>
        {rules.map((rule, idx) => (
          <View key={idx} style={styles.ruleItemRow}>
            <Text style={styles.ruleBullet}>•</Text>
            <Text style={styles.ruleItemText}>{rule}</Text>
          </View>
        ))}
      </View>
    </View>
  );
}

// --- Exam Tip Card (⭐ Exam tip cards) ---
export function ExamTipCard({ tip, exam }: { tip: string; exam?: string }) {
  return (
    <View style={styles.tipContainer}>
      <View style={styles.cardHeaderRow}>
        <Feather name="award" size={16} color={Palette.success} />
        <Text style={styles.tipTitle}>Exam Strategy Tip {exam ? `(${exam})` : ''}</Text>
      </View>
      <Text style={styles.tipText}>{tip}</Text>
    </View>
  );
}

// --- Collapsible Section (+ Simple Present, etc.) ---
export function CollapsibleSection({
  title,
  subtitle,
  children,
  defaultExpanded = false,
}: {
  title: string;
  subtitle?: string;
  children: React.ReactNode;
  defaultExpanded?: boolean;
}) {
  const [expanded, setExpanded] = useState(defaultExpanded);

  return (
    <View style={styles.collapsibleWrapper}>
      <TouchableOpacity
        style={styles.collapsibleHeader}
        onPress={() => setExpanded(!expanded)}
        activeOpacity={0.7}
      >
        <View style={styles.collapsibleTitleGroup}>
          <Text style={styles.collapsibleTitle}>{title}</Text>
          {subtitle && <Text style={styles.collapsibleSubtitle}>{subtitle}</Text>}
        </View>
        <View style={styles.expandIconCircle}>
          <Feather name={expanded ? 'minus' : 'plus'} size={16} color={Palette.primary} />
        </View>
      </TouchableOpacity>
      {expanded && <View style={styles.collapsibleContent}>{children}</View>}
    </View>
  );
}

// --- Progress Bar Component ---
export function ProgressBar({ progress, color = Palette.primary }: { progress: number; color?: string }) {
  const clamped = Math.min(Math.max(progress, 0), 1);
  return (
    <View style={styles.progressTrack}>
      <View style={[styles.progressFill, { width: `${clamped * 100}%`, backgroundColor: color }]} />
    </View>
  );
}

const styles = StyleSheet.create({
  cardHeaderRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    marginBottom: 8,
  },
  cardBody: {
    marginTop: 2,
  },
  cardText: {
    fontSize: 14,
    color: Palette.textBody,
    lineHeight: 21,
  },
  noteContainer: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.border,
    marginBottom: 14,
    borderLeftWidth: 4,
    borderLeftColor: Palette.primary,
    ...Shadows.card,
  },
  noteTitle: {
    fontSize: 15,
    fontWeight: '700',
    color: Palette.textTitle,
  },
  exampleContainer: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.border,
    marginBottom: 14,
    borderLeftWidth: 4,
    borderLeftColor: Palette.warning,
    ...Shadows.card,
  },
  exampleTitle: {
    fontSize: 15,
    fontWeight: '700',
    color: Palette.textTitle,
  },
  exampleBox: {
    backgroundColor: Palette.backgroundSecondary,
    padding: 12,
    borderRadius: 8,
    marginVertical: 6,
    borderWidth: 1,
    borderColor: Palette.border,
  },
  exampleCodeText: {
    fontFamily: 'monospace',
    fontSize: 13,
    color: Palette.techNavy,
  },
  exampleExplanation: {
    fontSize: 13,
    color: Palette.textSecondary,
    lineHeight: 19,
    marginTop: 4,
  },
  ruleContainer: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.border,
    marginBottom: 14,
    borderLeftWidth: 4,
    borderLeftColor: Palette.danger,
    ...Shadows.card,
  },
  ruleTitle: {
    fontSize: 15,
    fontWeight: '700',
    color: Palette.textTitle,
  },
  rulesList: {
    gap: 6,
    marginTop: 4,
  },
  ruleItemRow: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    gap: 6,
  },
  ruleBullet: {
    fontSize: 14,
    color: Palette.danger,
    lineHeight: 20,
  },
  ruleItemText: {
    flex: 1,
    fontSize: 13.5,
    color: Palette.textBody,
    lineHeight: 20,
  },
  tipContainer: {
    backgroundColor: Palette.successLight,
    borderRadius: Radii.card,
    padding: 16,
    borderWidth: 1,
    borderColor: Palette.successBorder,
    marginBottom: 14,
  },
  tipTitle: {
    fontSize: 15,
    fontWeight: '700',
    color: Palette.success,
  },
  tipText: {
    fontSize: 13.5,
    color: Palette.textBody,
    lineHeight: 20,
  },
  collapsibleWrapper: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    borderWidth: 1,
    borderColor: Palette.border,
    marginBottom: 12,
    overflow: 'hidden',
    ...Shadows.card,
  },
  collapsibleHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    padding: 16,
  },
  collapsibleTitleGroup: {
    flex: 1,
    marginRight: 10,
  },
  collapsibleTitle: {
    fontSize: 15,
    fontWeight: '700',
    color: Palette.textTitle,
  },
  collapsibleSubtitle: {
    fontSize: 12,
    color: Palette.textSecondary,
    marginTop: 2,
  },
  expandIconCircle: {
    width: 28,
    height: 28,
    borderRadius: 14,
    backgroundColor: Palette.primaryLight,
    alignItems: 'center',
    justifyContent: 'center',
  },
  collapsibleContent: {
    paddingHorizontal: 16,
    paddingBottom: 16,
    borderTopWidth: 1,
    borderTopColor: Palette.borderSubtle,
    paddingTop: 12,
  },
  progressTrack: {
    height: 6,
    backgroundColor: Palette.border,
    borderRadius: 3,
    overflow: 'hidden',
  },
  progressFill: {
    height: '100%',
    borderRadius: 3,
  },
});
