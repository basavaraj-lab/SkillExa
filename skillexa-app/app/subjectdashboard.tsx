import { router } from "expo-router";
import React from "react";
import {
  StyleSheet,
  Text,
  TouchableOpacity,
  View,
} from "react-native";

export default function SubjectDashboard() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Subject Dashboard</Text>

      <TouchableOpacity
        style={styles.button}
        onPress={() => router.push("/quizzpage")}
      >
        <Text style={styles.buttonText}>SDLC Models</Text>
      </TouchableOpacity>

      <TouchableOpacity
        style={styles.button}
        onPress={() => router.push("/quizzpage")}
      >
        <Text style={styles.buttonText}>Pipelining</Text>
      </TouchableOpacity>

      <TouchableOpacity
        style={styles.button}
        onPress={() => router.push("/quizzpage")}
      >
        <Text style={styles.buttonText}>Memory & Cache</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    padding: 20,
    backgroundColor: "#fff",
  },

  title: {
    fontSize: 28,
    fontWeight: "bold",
    textAlign: "center",
    marginBottom: 30,
  },

  button: {
    backgroundColor: "#06b6d4",
    padding: 15,
    borderRadius: 10,
    marginBottom: 15,
  },

  buttonText: {
    color: "#fff",
    textAlign: "center",
    fontSize: 18,
    fontWeight: "bold",
  },
});