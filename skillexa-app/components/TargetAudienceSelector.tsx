import { Feather } from '@expo/vector-icons';
import React from 'react';
import {
  ScrollView,
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from 'react-native';
import { Palette, Radii } from '../constants/theme';
import { TargetAudience, TargetAudienceType } from '../data/collegeData';

interface Props {
  visibility?: 'college' | 'community';
  onChangeVisibility?: (v: 'college' | 'community') => void;
  target: TargetAudience;
  onChangeTarget: (newTarget: TargetAudience) => void;
  collegeName?: string;
}

const TARGET_TYPES: { type: TargetAudienceType; label: string; icon: string }[] = [
  { type: 'ENTIRE_COLLEGE', label: 'Entire College', icon: 'globe' },
  { type: 'DEPARTMENT', label: 'Department', icon: 'layers' },
  { type: 'YEAR', label: 'Academic Year', icon: 'calendar' },
  { type: 'SECTION', label: 'Specific Section', icon: 'users' },
];

const DEPARTMENTS = ['ECE', 'CSE', 'AIML', 'MECH', 'ISE'];
const YEARS = ['1st Year', '2nd Year', '3rd Year', '4th Year'];
const SECTIONS = ['A', 'B', 'C'];

export function TargetAudienceSelector({
  visibility = 'college',
  onChangeVisibility,
  target,
  onChangeTarget,
  collegeName = 'KVG College of Engineering',
}: Props) {
  const setType = (type: TargetAudienceType) => {
    onChangeTarget({
      ...target,
      targetType: type,
    });
  };

  const setDept = (dept: string) => {
    onChangeTarget({
      ...target,
      department: dept,
    });
  };

  const setYear = (year: string) => {
    onChangeTarget({
      ...target,
      academicYear: year,
    });
  };

  const setSection = (sec: string) => {
    onChangeTarget({
      ...target,
      section: sec,
    });
  };

  return (
    <View style={styles.container}>
      {/* 1. Visibility Switch (My College vs SkillExa Community) */}
      <View style={styles.headerRow}>
        <Feather name="globe" size={16} color={Palette.primary} />
        <Text style={styles.title}>Publication Scope & Visibility</Text>
      </View>

      <View style={styles.visibilityRow}>
        <TouchableOpacity
          style={[
            styles.visibilityBtn,
            visibility === 'college' && styles.visibilityBtnActive,
          ]}
          onPress={() => onChangeVisibility && onChangeVisibility('college')}
          activeOpacity={0.8}
        >
          <Feather
            name="home"
            size={14}
            color={visibility === 'college' ? '#FFFFFF' : Palette.textSecondary}
          />
          <Text
            style={[
              styles.visibilityBtnText,
              visibility === 'college' && styles.visibilityBtnTextActive,
            ]}
          >
            🏫 My College
          </Text>
        </TouchableOpacity>

        <TouchableOpacity
          style={[
            styles.visibilityBtn,
            visibility === 'community' && styles.visibilityBtnCommunityActive,
          ]}
          onPress={() => onChangeVisibility && onChangeVisibility('community')}
          activeOpacity={0.8}
        >
          <Feather
            name="globe"
            size={14}
            color={visibility === 'community' ? '#FFFFFF' : Palette.textSecondary}
          />
          <Text
            style={[
              styles.visibilityBtnText,
              visibility === 'community' && styles.visibilityBtnTextActive,
            ]}
          >
            🌍 SkillExa Community
          </Text>
        </TouchableOpacity>
      </View>

      {/* When Community is Selected */}
      {visibility === 'community' ? (
        <View style={styles.communityBanner}>
          <View style={styles.commIconBox}>
            <Feather name="share-2" size={18} color={Palette.aiPurple} />
          </View>
          <View style={{ flex: 1 }}>
            <Text style={styles.commBannerTitle}>Public Community Publication</Text>
            <Text style={styles.commBannerDesc}>
              This content will be published to the **SkillExa Community** and publicly discoverable by students across all colleges under your verified educator profile.
            </Text>
          </View>
        </View>
      ) : (
        /* When College is Selected */
        <>
          <Text style={styles.subtitle}>
            Target specific student batches within {collegeName}.
          </Text>

          {/* Target Level Pills */}
          <View style={styles.pillsRow}>
            {TARGET_TYPES.map((t) => {
              const isActive = target.targetType === t.type;
              return (
                <TouchableOpacity
                  key={t.type}
                  style={[styles.pill, isActive && styles.pillActive]}
                  onPress={() => setType(t.type)}
                >
                  <Feather
                    name={t.icon as any}
                    size={13}
                    color={isActive ? '#FFFFFF' : Palette.textSecondary}
                  />
                  <Text style={[styles.pillText, isActive && styles.pillTextActive]}>{t.label}</Text>
                </TouchableOpacity>
              );
            })}
          </View>

          {/* Sub-Filters based on selection */}
          {target.targetType !== 'ENTIRE_COLLEGE' && (
            <View style={styles.subFiltersBox}>
              {/* Department Row */}
              <Text style={styles.filterLabel}>DEPARTMENT / BRANCH</Text>
              <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={styles.chipsScroll}>
                {DEPARTMENTS.map((d) => (
                  <TouchableOpacity
                    key={d}
                    style={[styles.chip, target.department === d && styles.chipActive]}
                    onPress={() => setDept(d)}
                  >
                    <Text style={[styles.chipText, target.department === d && styles.chipTextActive]}>
                      {d}
                    </Text>
                  </TouchableOpacity>
                ))}
              </ScrollView>

              {/* Year Row */}
              {(target.targetType === 'YEAR' || target.targetType === 'SECTION') && (
                <View style={{ marginTop: 8 }}>
                  <Text style={styles.filterLabel}>ACADEMIC YEAR</Text>
                  <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={styles.chipsScroll}>
                    {YEARS.map((y) => (
                      <TouchableOpacity
                        key={y}
                        style={[styles.chip, target.academicYear === y && styles.chipActive]}
                        onPress={() => setYear(y)}
                      >
                        <Text style={[styles.chipText, target.academicYear === y && styles.chipTextActive]}>
                          {y}
                        </Text>
                      </TouchableOpacity>
                    ))}
                  </ScrollView>
                </View>
              )}

              {/* Section Row */}
              {target.targetType === 'SECTION' && (
                <View style={{ marginTop: 8 }}>
                  <Text style={styles.filterLabel}>SECTION</Text>
                  <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={styles.chipsScroll}>
                    {SECTIONS.map((s) => (
                      <TouchableOpacity
                        key={s}
                        style={[styles.chip, target.section === s && styles.chipActive]}
                        onPress={() => setSection(s)}
                      >
                        <Text style={[styles.chipText, target.section === s && styles.chipTextActive]}>
                          Section {s}
                        </Text>
                      </TouchableOpacity>
                    ))}
                  </ScrollView>
                </View>
              )}
            </View>
          )}
        </>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: Palette.backgroundSecondary,
    borderRadius: Radii.card,
    padding: 12,
    borderWidth: 1,
    borderColor: Palette.border,
    marginBottom: 12,
  },
  headerRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    marginBottom: 4,
  },
  title: {
    fontSize: 13,
    fontWeight: '800',
    color: Palette.textTitle,
  },
  visibilityRow: {
    flexDirection: 'row',
    gap: 8,
    marginVertical: 8,
  },
  visibilityBtn: {
    flex: 1,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 6,
    paddingVertical: 8,
    borderRadius: Radii.button,
    backgroundColor: '#FFFFFF',
    borderWidth: 1,
    borderColor: Palette.border,
  },
  visibilityBtnActive: {
    backgroundColor: Palette.primary,
    borderColor: Palette.primary,
  },
  visibilityBtnCommunityActive: {
    backgroundColor: Palette.aiPurple,
    borderColor: Palette.aiPurple,
  },
  visibilityBtnText: {
    fontSize: 12,
    fontWeight: '700',
    color: Palette.textSecondary,
  },
  visibilityBtnTextActive: {
    color: '#FFFFFF',
  },
  communityBanner: {
    backgroundColor: Palette.aiPurpleLight,
    borderRadius: 8,
    padding: 10,
    borderWidth: 1,
    borderColor: Palette.aiPurpleBorder,
    flexDirection: 'row',
    alignItems: 'flex-start',
    gap: 10,
    marginTop: 4,
  },
  commIconBox: {
    width: 32,
    height: 32,
    borderRadius: 8,
    backgroundColor: '#FFFFFF',
    alignItems: 'center',
    justifyContent: 'center',
    marginTop: 2,
  },
  commBannerTitle: {
    fontSize: 12.5,
    fontWeight: '800',
    color: Palette.aiPurple,
    marginBottom: 2,
  },
  commBannerDesc: {
    fontSize: 11,
    color: Palette.textTitle,
    lineHeight: 15,
  },
  subtitle: {
    fontSize: 11,
    color: Palette.textSecondary,
    marginBottom: 8,
  },
  pillsRow: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    gap: 6,
    marginBottom: 8,
  },
  pill: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 5,
    paddingHorizontal: 9,
    paddingVertical: 5,
    borderRadius: Radii.pill,
    backgroundColor: '#FFFFFF',
    borderWidth: 1,
    borderColor: Palette.border,
  },
  pillActive: {
    backgroundColor: Palette.primary,
    borderColor: Palette.primary,
  },
  pillText: {
    fontSize: 11,
    fontWeight: '600',
    color: Palette.textSecondary,
  },
  pillTextActive: {
    color: '#FFFFFF',
    fontWeight: '700',
  },
  subFiltersBox: {
    backgroundColor: '#FFFFFF',
    borderRadius: 8,
    padding: 10,
    borderWidth: 1,
    borderColor: Palette.borderSubtle,
    marginTop: 4,
  },
  filterLabel: {
    fontSize: 9,
    fontWeight: '800',
    color: Palette.textSecondary,
    letterSpacing: 0.6,
    marginBottom: 5,
  },
  chipsScroll: {
    gap: 6,
  },
  chip: {
    paddingHorizontal: 10,
    paddingVertical: 4,
    borderRadius: 6,
    backgroundColor: Palette.backgroundSecondary,
    borderWidth: 1,
    borderColor: Palette.border,
  },
  chipActive: {
    backgroundColor: Palette.primaryLight,
    borderColor: Palette.primary,
  },
  chipText: {
    fontSize: 11,
    fontWeight: '600',
    color: Palette.textBody,
  },
  chipTextActive: {
    color: Palette.primary,
    fontWeight: '700',
  },
});
