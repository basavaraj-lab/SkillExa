import { Feather } from '@expo/vector-icons';
import { router, useLocalSearchParams } from 'expo-router';
import React from 'react';
import { SafeAreaView, ScrollView, StatusBar, StyleSheet, Text, TouchableOpacity, View } from 'react-native';

const MODULES = [
  { title: 'Introduction', route: '/coding/introduction' },
  { title: 'Theory', route: '/coding/theory' },
  { title: 'Examples', route: '/coding/examples' },
  { title: 'Compiler', route: '/coding/compiler' },
  { title: 'Coding Problems', route: '/coding/problems' },
  { title: 'Quiz', route: '/coding/quiz' },
  { title: 'Progress', route: '/coding/progress' },
];

export default function CodingDashboardScreen() {
  const { langId, langName } = useLocalSearchParams<{ langId: string; langName: string }>();
  const selectedName = langName || 'C Programming';
  const selectedLang = langId || 'c';

  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <View style={styles.header}>
        <TouchableOpacity style={styles.backBtn} onPress={() => router.back()}>
          <Feather name="arrow-left" size={20} color="#1E293B" />
        </TouchableOpacity>
        <Text style={styles.title}>Coding Dashboard</Text>
        <Text style={styles.subtitle}>{selectedName}</Text>
      </View>

      <ScrollView contentContainerStyle={styles.content} showsVerticalScrollIndicator={false}>
        {MODULES.map((item) => (
          <TouchableOpacity
            key={item.title}
            style={styles.card}
            onPress={() =>
              router.push({
                pathname: item.route as any,
                params: { langId: selectedLang, langName: selectedName },
              })
            }
          >
            <Text style={styles.cardTitle}>{item.title}</Text>
            <Feather name="chevron-right" size={18} color="#94A3B8" />
          </TouchableOpacity>
        ))}
      </ScrollView>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#FFFFFF' },
  header: { paddingHorizontal: 24, paddingTop: 16, paddingBottom: 12, borderBottomWidth: 1, borderBottomColor: '#E2E8F0' },
  backBtn: { marginBottom: 12 },
  title: { fontSize: 24, fontWeight: '800', color: '#2563EB' },
  subtitle: { marginTop: 4, fontSize: 14, color: '#64748B' },
  content: { padding: 24 },
  card: { flexDirection: 'row', justifyContent: 'space-between', alignItems: 'center', backgroundColor: '#FFFFFF', borderRadius: 16, padding: 18, marginBottom: 14, borderWidth: 1, borderColor: '#E2E8F0', elevation: 2 },
  cardTitle: { fontSize: 16, fontWeight: '700', color: '#1E293B' },
});
