import { router } from 'expo-router';
import React from 'react';
import { SafeAreaView, StatusBar, StyleSheet, Text, TouchableOpacity, View } from 'react-native';

export default function NotesPage() {
  return (
    <SafeAreaView style={styles.container}>
      <StatusBar barStyle="dark-content" backgroundColor="#FFFFFF" />
      <View style={styles.header}>
        <Text style={styles.title}>Notes</Text>
        <Text style={styles.subtitle}>Review study notes and reference materials.</Text>
      </View>
      <View style={styles.body}>
        <Text style={styles.description}>
          This page holds quick notes, cheat sheets, and reference guides.
        </Text>
        <TouchableOpacity style={styles.button} onPress={() => router.back()}>
          <Text style={styles.buttonText}>Back</Text>
        </TouchableOpacity>
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#FFFFFF', padding: 24 },
  header: { marginBottom: 20 },
  title: { fontSize: 28, fontWeight: '800', color: '#2563EB' },
  subtitle: { marginTop: 8, fontSize: 14, color: '#64748B' },
  body: { flex: 1, justifyContent: 'center' },
  description: { fontSize: 16, color: '#334155', lineHeight: 22 },
  button: { marginTop: 24, backgroundColor: '#2563EB', paddingVertical: 14, borderRadius: 12, alignItems: 'center' },
  buttonText: { color: '#FFFFFF', fontSize: 16, fontWeight: '700' },
});
