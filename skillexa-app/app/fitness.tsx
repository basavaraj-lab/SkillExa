// app/fitness.tsx

import { router } from "expo-router";
import React from "react";
import {
    ScrollView,
    StyleSheet,
    Text,
    TouchableOpacity,
    View,
} from "react-native";

const topics = [
  "Physical Endurance",
  "Running Practice",
  "Strength Training",
  "Flexibility & Mobility",
  "Nutrition Basics",
  "Body Mass Index (BMI)",
  "Sports Fitness",
  "Health & Wellness",
];

export default function Fitness() {
  return (
    <ScrollView style={styles.container}>
      {/* Header */}
      <View style={styles.header}>
        <Text style={styles.appName}>SkillExa</Text>

        <Text style={styles.title}>Physical Fitness</Text>

        <Text style={styles.subtitle}>
          Prepare for physical fitness tests and improve overall health.
        </Text>
      </View>

      {/* Topics */}
      {topics.map((topic, index) => (
        <TouchableOpacity
          key={index}
          style={styles.topicCard}
          onPress={() =>
            router.push({
              pathname: "/quizzpage",
              params: { topic },
            })
          }
        >
          <Text style={styles.topic}>{topic}</Text>
          <Text style={styles.arrow}>→</Text>
        </TouchableOpacity>
      ))}

      {/* Quote Card */}
      <View style={styles.quoteCard}>
        <Text style={styles.quote}>
          &quot;A healthy body fuels a focused mind and a successful future.&quot;
        </Text>

        <Text style={styles.quoteAuthor}>
          — Physical Fitness Learning Path
        </Text>
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: "#F8FAFC",
    paddingHorizontal: 20,
  },

  header: {
    marginTop: 40,
    marginBottom: 25,
  },

  appName: {
    fontSize: 30,
    fontWeight: "bold",
    color: "#0F172A",
    textAlign: "center",
    marginBottom: 20,
  },

  title: {
    fontSize: 24,
    fontWeight: "700",
    color: "#0F172A",
  },

  subtitle: {
    fontSize: 14,
    color: "#64748B",
    marginTop: 5,
    lineHeight: 22,
  },

  topicCard: {
    backgroundColor: "#FFFFFF",
    borderRadius: 14,
    padding: 18,
    marginBottom: 12,
    borderWidth: 1,
    borderColor: "#E2E8F0",

    flexDirection: "row",
    justifyContent: "space-between",
    alignItems: "center",

    shadowColor: "#000",
    shadowOffset: {
      width: 0,
      height: 1,
    },
    shadowOpacity: 0.04,
    shadowRadius: 3,
    elevation: 2,
  },

  topic: {
    fontSize: 15,
    fontWeight: "600",
    color: "#1E293B",
  },

  arrow: {
    fontSize: 18,
    color: "#64748B",
    fontWeight: "bold",
  },

  quoteCard: {
    backgroundColor: "#FFFFFF",
    borderRadius: 14,
    padding: 20,
    marginTop: 20,
    marginBottom: 30,
    borderWidth: 1,
    borderColor: "#E2E8F0",

    shadowColor: "#000",
    shadowOffset: {
      width: 0,
      height: 1,
    },
    shadowOpacity: 0.04,
    shadowRadius: 3,
    elevation: 2,
  },

  quote: {
    fontSize: 15,
    color: "#334155",
    textAlign: "center",
    fontStyle: "italic",
    lineHeight: 24,
  },

  quoteAuthor: {
    marginTop: 12,
    textAlign: "center",
    fontSize: 12,
    fontWeight: "600",
    color: "#64748B",
  },
});