import { Feather } from '@expo/vector-icons';
import React, { useState } from 'react';
import {
  Alert,
  SafeAreaView,
  ScrollView,
  StatusBar,
  StyleSheet,
  Text,
  TextInput,
  TouchableOpacity,
  View,
} from 'react-native';
import { AppHeader } from '../components/common/AppHeader';
import { Palette, Radii, Shadows } from '../constants/theme';

const WIZARD_STEPS = [
  { id: 1, label: 'Personal', icon: 'user' },
  { id: 2, label: 'Education', icon: 'book' },
  { id: 3, label: 'Skills', icon: 'code' },
  { id: 4, label: 'Projects', icon: 'folder' },
  { id: 5, label: 'Experience', icon: 'briefcase' },
  { id: 6, label: 'Certs', icon: 'award' },
  { id: 7, label: 'Preview', icon: 'eye' },
];

export default function ResumeBuilderPage() {
  const [currentStep, setCurrentStep] = useState(1);
  const [template, setTemplate] = useState<'modern' | 'professional' | 'minimal'>('modern');

  // Form State
  const [personal, setPersonal] = useState({
    fullName: 'Ganesh Kumar',
    title: 'Computer Science Engineer',
    email: 'ganesh@example.edu',
    phone: '+91 98765 43210',
    location: 'Bengaluru, India',
    github: 'github.com/ganesh-code',
  });

  const [education, setEducation] = useState({
    degree: 'B.Tech in Computer Science & Engineering',
    institution: 'National Institute of Technology',
    score: 'CGPA: 8.9 / 10',
    year: '2022 - 2026',
  });

  const [skills, setSkills] = useState({
    languages: 'Java, Python, C++, TypeScript, SQL',
    frameworks: 'React Native, Node.js, Spring Boot, Expo',
    tools: 'Git, Docker, AWS, Postman, Linux',
  });

  const [projects, setProjects] = useState({
    p1Title: 'SkillExa - Mobile Learning Ecosystem',
    p1Tech: 'React Native, Expo, TypeScript',
    p1Desc: 'Engineered an interactive student learning app featuring live code compilers and unit quizzes.',
    p2Title: 'Distributed Cloud Task Scheduler',
    p2Tech: 'Go, Docker, Redis',
    p2Desc: 'Developed high-throughput task worker pool with fault-tolerant heartbeat monitoring.',
  });

  const [experience, setExperience] = useState({
    role: 'Software Engineering Intern',
    company: 'NextGen Tech Solutions',
    duration: 'May 2025 - July 2025',
    desc: 'Optimized API throughput by 28% and built reusable component design tokens.',
  });

  const [certifications, setCertifications] = useState({
    c1: 'AWS Certified Cloud Practitioner',
    c2: 'Meta Certified React Native Specialist',
  });

  const handleNext = () => {
    if (currentStep < 7) {
      setCurrentStep(currentStep + 1);
    }
  };

  const handleBack = () => {
    if (currentStep > 1) {
      setCurrentStep(currentStep - 1);
    }
  };

  return (
    <SafeAreaView style={styles.safeArea}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <AppHeader showBack title="Resume Builder" subtitle={`Step ${currentStep} of 7: ${WIZARD_STEPS[currentStep - 1].label}`} />

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {/* Wizard Step Indicator */}
        <View style={styles.stepIndicatorContainer}>
          <ScrollView horizontal showsHorizontalScrollIndicator={false} contentContainerStyle={styles.stepScroll}>
            {WIZARD_STEPS.map((step) => {
              const isCompleted = step.id < currentStep;
              const isCurrent = step.id === currentStep;
              return (
                <TouchableOpacity
                  key={step.id}
                  style={[
                    styles.stepPill,
                    isCurrent && styles.stepPillCurrent,
                    isCompleted && styles.stepPillCompleted,
                  ]}
                  onPress={() => setCurrentStep(step.id)}
                >
                  <Text style={[styles.stepNumText, isCurrent && styles.stepNumTextCurrent, isCompleted && styles.stepNumTextCompleted]}>
                    {step.id}
                  </Text>
                  <Text style={[styles.stepLabelText, isCurrent && styles.stepLabelTextCurrent]}>
                    {step.label}
                  </Text>
                </TouchableOpacity>
              );
            })}
          </ScrollView>
        </View>

        {/* Step 1: Personal Details */}
        {currentStep === 1 && (
          <View style={styles.formSection}>
            <Text style={styles.sectionHeaderTitle}>1. Personal & Contact Information</Text>
            <Text style={styles.sectionHeaderSub}>Ensure your contact channels are accurate for recruiters.</Text>

            <View style={styles.inputCard}>
              <Text style={styles.inputLabel}>FULL NAME</Text>
              <TextInput
                style={styles.input}
                value={personal.fullName}
                onChangeText={(t) => setPersonal({ ...personal, fullName: t })}
              />

              <Text style={styles.inputLabel}>PROFESSIONAL HEADLINE</Text>
              <TextInput
                style={styles.input}
                value={personal.title}
                onChangeText={(t) => setPersonal({ ...personal, title: t })}
              />

              <Text style={styles.inputLabel}>EMAIL ADDRESS</Text>
              <TextInput
                style={styles.input}
                value={personal.email}
                keyboardType="email-address"
                onChangeText={(t) => setPersonal({ ...personal, email: t })}
              />

              <Text style={styles.inputLabel}>PHONE NUMBER</Text>
              <TextInput
                style={styles.input}
                value={personal.phone}
                keyboardType="phone-pad"
                onChangeText={(t) => setPersonal({ ...personal, phone: t })}
              />

              <Text style={styles.inputLabel}>GITHUB / PORTFOLIO LINK</Text>
              <TextInput
                style={styles.input}
                value={personal.github}
                onChangeText={(t) => setPersonal({ ...personal, github: t })}
              />
            </View>
          </View>
        )}

        {/* Step 2: Education */}
        {currentStep === 2 && (
          <View style={styles.formSection}>
            <Text style={styles.sectionHeaderTitle}>2. Academic Credentials</Text>
            <Text style={styles.sectionHeaderSub}>List your college degree, GPA and expected graduation.</Text>

            <View style={styles.inputCard}>
              <Text style={styles.inputLabel}>DEGREE & MAJOR</Text>
              <TextInput
                style={styles.input}
                value={education.degree}
                onChangeText={(t) => setEducation({ ...education, degree: t })}
              />

              <Text style={styles.inputLabel}>INSTITUTION / UNIVERSITY</Text>
              <TextInput
                style={styles.input}
                value={education.institution}
                onChangeText={(t) => setEducation({ ...education, institution: t })}
              />

              <Text style={styles.inputLabel}>GRADE / CGPA / PERCENTAGE</Text>
              <TextInput
                style={styles.input}
                value={education.score}
                onChangeText={(t) => setEducation({ ...education, score: t })}
              />

              <Text style={styles.inputLabel}>DURATION / GRADUATION YEAR</Text>
              <TextInput
                style={styles.input}
                value={education.year}
                onChangeText={(t) => setEducation({ ...education, year: t })}
              />
            </View>
          </View>
        )}

        {/* Step 3: Technical Skills */}
        {currentStep === 3 && (
          <View style={styles.formSection}>
            <Text style={styles.sectionHeaderTitle}>3. Technical Matrix</Text>
            <Text style={styles.sectionHeaderSub}>Categorize your programming languages and tools.</Text>

            <View style={styles.inputCard}>
              <Text style={styles.inputLabel}>PROGRAMMING LANGUAGES</Text>
              <TextInput
                style={styles.input}
                value={skills.languages}
                onChangeText={(t) => setSkills({ ...skills, languages: t })}
              />

              <Text style={styles.inputLabel}>FRAMEWORKS & LIBRARIES</Text>
              <TextInput
                style={styles.input}
                value={skills.frameworks}
                onChangeText={(t) => setSkills({ ...skills, frameworks: t })}
              />

              <Text style={styles.inputLabel}>DEVELOPER TOOLS & CLOUD</Text>
              <TextInput
                style={styles.input}
                value={skills.tools}
                onChangeText={(t) => setSkills({ ...skills, tools: t })}
              />
            </View>
          </View>
        )}

        {/* Step 4: Projects */}
        {currentStep === 4 && (
          <View style={styles.formSection}>
            <Text style={styles.sectionHeaderTitle}>4. Engineering Projects</Text>
            <Text style={styles.sectionHeaderSub}>Showcase high-impact full-stack and algorithmic projects.</Text>

            <View style={styles.inputCard}>
              <Text style={styles.inputLabel}>PROJECT 1 TITLE</Text>
              <TextInput
                style={styles.input}
                value={projects.p1Title}
                onChangeText={(t) => setProjects({ ...projects, p1Title: t })}
              />
              <Text style={styles.inputLabel}>TECH STACK</Text>
              <TextInput
                style={styles.input}
                value={projects.p1Tech}
                onChangeText={(t) => setProjects({ ...projects, p1Tech: t })}
              />
              <Text style={styles.inputLabel}>BULLET DESCRIPTION</Text>
              <TextInput
                style={[styles.input, styles.textArea]}
                multiline
                value={projects.p1Desc}
                onChangeText={(t) => setProjects({ ...projects, p1Desc: t })}
              />
            </View>

            <View style={[styles.inputCard, { marginTop: 14 }]}>
              <Text style={styles.inputLabel}>PROJECT 2 TITLE</Text>
              <TextInput
                style={styles.input}
                value={projects.p2Title}
                onChangeText={(t) => setProjects({ ...projects, p2Title: t })}
              />
              <Text style={styles.inputLabel}>TECH STACK</Text>
              <TextInput
                style={styles.input}
                value={projects.p2Tech}
                onChangeText={(t) => setProjects({ ...projects, p2Tech: t })}
              />
              <Text style={styles.inputLabel}>BULLET DESCRIPTION</Text>
              <TextInput
                style={[styles.input, styles.textArea]}
                multiline
                value={projects.p2Desc}
                onChangeText={(t) => setProjects({ ...projects, p2Desc: t })}
              />
            </View>
          </View>
        )}

        {/* Step 5: Experience */}
        {currentStep === 5 && (
          <View style={styles.formSection}>
            <Text style={styles.sectionHeaderTitle}>5. Internship & Work Experience</Text>
            <Text style={styles.sectionHeaderSub}>List internships, research fellowships, or open source contributions.</Text>

            <View style={styles.inputCard}>
              <Text style={styles.inputLabel}>ROLE / POSITION</Text>
              <TextInput
                style={styles.input}
                value={experience.role}
                onChangeText={(t) => setExperience({ ...experience, role: t })}
              />
              <Text style={styles.inputLabel}>COMPANY / ORGANIZATION</Text>
              <TextInput
                style={styles.input}
                value={experience.company}
                onChangeText={(t) => setExperience({ ...experience, company: t })}
              />
              <Text style={styles.inputLabel}>TIMELINE</Text>
              <TextInput
                style={styles.input}
                value={experience.duration}
                onChangeText={(t) => setExperience({ ...experience, duration: t })}
              />
              <Text style={styles.inputLabel}>RESPONSIBILITIES & IMPACT</Text>
              <TextInput
                style={[styles.input, styles.textArea]}
                multiline
                value={experience.desc}
                onChangeText={(t) => setExperience({ ...experience, desc: t })}
              />
            </View>
          </View>
        )}

        {/* Step 6: Certifications */}
        {currentStep === 6 && (
          <View style={styles.formSection}>
            <Text style={styles.sectionHeaderTitle}>6. Honors & Certifications</Text>
            <Text style={styles.sectionHeaderSub}>Highlight competitive scores, hackathons, and certifications.</Text>

            <View style={styles.inputCard}>
              <Text style={styles.inputLabel}>PRIMARY CERTIFICATION</Text>
              <TextInput
                style={styles.input}
                value={certifications.c1}
                onChangeText={(t) => setCertifications({ ...certifications, c1: t })}
              />
              <Text style={styles.inputLabel}>SECONDARY CERTIFICATION</Text>
              <TextInput
                style={styles.input}
                value={certifications.c2}
                onChangeText={(t) => setCertifications({ ...certifications, c2: t })}
              />
            </View>
          </View>
        )}

        {/* Step 7: Live Resume Preview */}
        {currentStep === 7 && (
          <View style={styles.previewSection}>
            <View style={styles.templateSelectorRow}>
              <Text style={styles.templateLabel}>Template:</Text>
              {(['modern', 'professional', 'minimal'] as const).map((t) => (
                <TouchableOpacity
                  key={t}
                  style={[styles.templatePill, template === t && styles.templatePillActive]}
                  onPress={() => setTemplate(t)}
                >
                  <Text style={[styles.templateText, template === t && styles.templateTextActive]}>
                    {t.charAt(0).toUpperCase() + t.slice(1)}
                  </Text>
                </TouchableOpacity>
              ))}
            </View>

            {/* Resume Document Canvas */}
            <View style={[styles.resumeDocument, template === 'professional' && styles.resumeDocProfessional]}>
              {/* Header */}
              <View style={styles.docHeader}>
                <Text style={styles.docName}>{personal.fullName}</Text>
                <Text style={styles.docHeadline}>{personal.title}</Text>
                <Text style={styles.docContact}>
                  {personal.email} • {personal.phone} • {personal.location}
                </Text>
                <Text style={styles.docGithub}>{personal.github}</Text>
              </View>

              <View style={styles.docDivider} />

              {/* Education */}
              <View style={styles.docBlock}>
                <Text style={styles.docBlockTitle}>EDUCATION</Text>
                <View style={styles.docRowBetween}>
                  <Text style={styles.docDegree}>{education.degree}</Text>
                  <Text style={styles.docDate}>{education.year}</Text>
                </View>
                <Text style={styles.docInst}>{education.institution} — <Text style={{ fontWeight: '600' }}>{education.score}</Text></Text>
              </View>

              {/* Skills */}
              <View style={styles.docBlock}>
                <Text style={styles.docBlockTitle}>TECHNICAL SKILLS</Text>
                <Text style={styles.docSkillLine}><Text style={styles.boldLabel}>Languages: </Text>{skills.languages}</Text>
                <Text style={styles.docSkillLine}><Text style={styles.boldLabel}>Frameworks: </Text>{skills.frameworks}</Text>
                <Text style={styles.docSkillLine}><Text style={styles.boldLabel}>Tools: </Text>{skills.tools}</Text>
              </View>

              {/* Projects */}
              <View style={styles.docBlock}>
                <Text style={styles.docBlockTitle}>FEATURED PROJECTS</Text>
                <View style={styles.projectItem}>
                  <Text style={styles.docProjectTitle}>{projects.p1Title} <Text style={styles.docTechPill}>({projects.p1Tech})</Text></Text>
                  <Text style={styles.docBullet}>• {projects.p1Desc}</Text>
                </View>
                <View style={styles.projectItem}>
                  <Text style={styles.docProjectTitle}>{projects.p2Title} <Text style={styles.docTechPill}>({projects.p2Tech})</Text></Text>
                  <Text style={styles.docBullet}>• {projects.p2Desc}</Text>
                </View>
              </View>

              {/* Experience */}
              <View style={styles.docBlock}>
                <Text style={styles.docBlockTitle}>EXPERIENCE</Text>
                <View style={styles.docRowBetween}>
                  <Text style={styles.docRole}>{experience.role} — {experience.company}</Text>
                  <Text style={styles.docDate}>{experience.duration}</Text>
                </View>
                <Text style={styles.docBullet}>• {experience.desc}</Text>
              </View>
            </View>

            {/* Action Bar */}
            <View style={styles.downloadRow}>
              <TouchableOpacity
                style={styles.editBtn}
                onPress={() => setCurrentStep(1)}
              >
                <Feather name="edit-2" size={16} color={Palette.primary} />
                <Text style={styles.editBtnText}>Edit Content</Text>
              </TouchableOpacity>

              <TouchableOpacity
                style={styles.downloadBtn}
                onPress={() => Alert.alert("Resume Export", "Your ATS-compliant PDF resume has been compiled successfully!")}
              >
                <Feather name="download" size={16} color="#FFFFFF" />
                <Text style={styles.downloadBtnText}>Download PDF</Text>
              </TouchableOpacity>
            </View>
          </View>
        )}

        {/* Wizard Bottom Controls */}
        <View style={styles.wizardControlRow}>
          {currentStep > 1 && (
            <TouchableOpacity
              style={styles.prevBtn}
              onPress={handleBack}
              activeOpacity={0.8}
            >
              <Feather name="arrow-left" size={16} color={Palette.textTitle} />
              <Text style={styles.prevBtnText}>Previous</Text>
            </TouchableOpacity>
          )}

          {currentStep < 7 ? (
            <TouchableOpacity
              style={styles.nextBtn}
              onPress={handleNext}
              activeOpacity={0.85}
            >
              <Text style={styles.nextBtnText}>Continue to Step {currentStep + 1}</Text>
              <Feather name="arrow-right" size={16} color="#FFFFFF" />
            </TouchableOpacity>
          ) : null}
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  safeArea: { flex: 1, backgroundColor: Palette.background },
  scrollContent: { paddingHorizontal: 16, paddingTop: 14, paddingBottom: 40 },
  stepIndicatorContainer: { marginBottom: 18 },
  stepScroll: { gap: 8, paddingVertical: 4 },
  stepPill: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    paddingHorizontal: 12,
    paddingVertical: 7,
    borderRadius: Radii.pill,
    backgroundColor: '#FFFFFF',
    borderWidth: 1,
    borderColor: Palette.border,
  },
  stepPillCurrent: {
    backgroundColor: Palette.primaryLight,
    borderColor: Palette.primary,
  },
  stepPillCompleted: {
    backgroundColor: Palette.successLight,
    borderColor: Palette.successBorder,
  },
  stepNumText: { fontSize: 11, fontWeight: '700', color: Palette.textSecondary },
  stepNumTextCurrent: { color: Palette.primary },
  stepNumTextCompleted: { color: Palette.success },
  stepLabelText: { fontSize: 12, fontWeight: '600', color: Palette.textSecondary },
  stepLabelTextCurrent: { color: Palette.primary, fontWeight: '700' },
  formSection: { marginBottom: 20 },
  sectionHeaderTitle: { fontSize: 17, fontWeight: '800', color: Palette.textTitle },
  sectionHeaderSub: { fontSize: 12.5, color: Palette.textSecondary, marginTop: 2, marginBottom: 14 },
  inputCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.card,
    padding: 18,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.card,
  },
  inputLabel: {
    fontSize: 10.5,
    fontWeight: '800',
    color: Palette.textTitle,
    letterSpacing: 0.6,
    marginBottom: 4,
    marginTop: 10,
  },
  input: {
    backgroundColor: Palette.backgroundSecondary,
    borderWidth: 1,
    borderColor: Palette.border,
    borderRadius: Radii.input,
    paddingHorizontal: 12,
    paddingVertical: 10,
    fontSize: 14,
    color: Palette.textTitle,
  },
  textArea: {
    height: 60,
    textAlignVertical: 'top',
  },
  previewSection: { marginBottom: 20 },
  templateSelectorRow: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    marginBottom: 14,
  },
  templateLabel: { fontSize: 13, fontWeight: '700', color: Palette.textTitle },
  templatePill: {
    paddingHorizontal: 12,
    paddingVertical: 5,
    borderRadius: 8,
    backgroundColor: '#FFFFFF',
    borderWidth: 1,
    borderColor: Palette.border,
  },
  templatePillActive: { backgroundColor: Palette.primary, borderColor: Palette.primary },
  templateText: { fontSize: 12, fontWeight: '600', color: Palette.textSecondary },
  templateTextActive: { color: '#FFFFFF', fontWeight: '700' },
  resumeDocument: {
    backgroundColor: '#FFFFFF',
    borderRadius: 12,
    padding: 24,
    borderWidth: 1,
    borderColor: Palette.border,
    ...Shadows.floating,
  },
  resumeDocProfessional: {
    borderLeftWidth: 6,
    borderLeftColor: Palette.techNavy,
  },
  docHeader: { alignItems: 'center', marginBottom: 12 },
  docName: { fontSize: 20, fontWeight: '800', color: Palette.techNavy, letterSpacing: -0.4 },
  docHeadline: { fontSize: 13, fontWeight: '600', color: Palette.primary, marginTop: 2 },
  docContact: { fontSize: 11, color: Palette.textSecondary, marginTop: 4 },
  docGithub: { fontSize: 11, color: Palette.primary, marginTop: 2 },
  docDivider: { height: 1, backgroundColor: Palette.border, marginVertical: 12 },
  docBlock: { marginBottom: 12 },
  docBlockTitle: { fontSize: 11, fontWeight: '800', color: Palette.techNavy, letterSpacing: 0.8, marginBottom: 4 },
  docRowBetween: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center' },
  docDegree: { fontSize: 12.5, fontWeight: '700', color: Palette.textTitle },
  docDate: { fontSize: 11, color: Palette.textSecondary },
  docInst: { fontSize: 11.5, color: Palette.textBody, marginTop: 1 },
  docSkillLine: { fontSize: 11.5, color: Palette.textBody, marginTop: 2 },
  boldLabel: { fontWeight: '700', color: Palette.textTitle },
  projectItem: { marginTop: 4 },
  docProjectTitle: { fontSize: 12, fontWeight: '700', color: Palette.textTitle },
  docTechPill: { fontWeight: '500', color: Palette.textSecondary, fontSize: 11 },
  docBullet: { fontSize: 11, color: Palette.textBody, marginTop: 2, lineHeight: 15 },
  docRole: { fontSize: 12.5, fontWeight: '700', color: Palette.textTitle },
  downloadRow: {
    flexDirection: 'row',
    gap: 12,
    marginTop: 18,
  },
  editBtn: {
    flex: 1,
    backgroundColor: '#FFFFFF',
    borderRadius: Radii.button,
    borderWidth: 1,
    borderColor: Palette.border,
    paddingVertical: 12,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 6,
  },
  editBtnText: { fontSize: 14, fontWeight: '700', color: Palette.primary },
  downloadBtn: {
    flex: 1.5,
    backgroundColor: Palette.primary,
    borderRadius: Radii.button,
    paddingVertical: 12,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 6,
    ...Shadows.button,
  },
  downloadBtnText: { fontSize: 14, fontWeight: '700', color: '#FFFFFF' },
  wizardControlRow: {
    flexDirection: 'row',
    gap: 10,
    marginTop: 8,
  },
  prevBtn: {
    backgroundColor: '#FFFFFF',
    borderWidth: 1,
    borderColor: Palette.border,
    borderRadius: Radii.button,
    paddingVertical: 12,
    paddingHorizontal: 16,
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
  },
  prevBtnText: { fontSize: 13.5, fontWeight: '700', color: Palette.textTitle },
  nextBtn: {
    flex: 1,
    backgroundColor: Palette.primary,
    borderRadius: Radii.button,
    paddingVertical: 12,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
    ...Shadows.button,
  },
  nextBtnText: { fontSize: 14, fontWeight: '700', color: '#FFFFFF' },
});
