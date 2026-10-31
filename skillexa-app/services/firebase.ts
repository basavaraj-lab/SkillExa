import { initializeApp, getApps, getApp } from "firebase/app";
import * as FirebaseAuth from "firebase/auth";
import { Platform } from "react-native";
import AsyncStorage from "@react-native-async-storage/async-storage";

// SkillExa Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyCUwBIIXRyEX-FMiu8TNU3nx23W0NioBKM",
  authDomain: "skillexa-736b4.firebaseapp.com",
  projectId: "skillexa-736b4",
  storageBucket: "skillexa-736b4.firebasestorage.app",
  messagingSenderId: "741530251369",
  appId: "1:741530251369:web:25f50dc52d76ddfc6d72f8",
  measurementId: "G-WLPVXQNFKS"
};

// Initialize Firebase App singleton
const app = getApps().length === 0 ? initializeApp(firebaseConfig) : getApp();

// Initialize Firebase Auth with React Native AsyncStorage persistence
function getSkillExaAuth(): FirebaseAuth.Auth {
  if (Platform.OS === 'web') {
    return FirebaseAuth.getAuth(app);
  }
  try {
    const getRNPersistence = (FirebaseAuth as any).getReactNativePersistence;
    if (typeof getRNPersistence === 'function') {
      return FirebaseAuth.initializeAuth(app, {
        persistence: getRNPersistence(AsyncStorage),
      });
    }
    return FirebaseAuth.getAuth(app);
  } catch (e: any) {
    // If already initialized or during fast refresh, safely fallback to existing auth
    return FirebaseAuth.getAuth(app);
  }
}

// Initialize Firebase Auth & Google Provider
export const auth: FirebaseAuth.Auth = getSkillExaAuth();
export const googleProvider = new FirebaseAuth.GoogleAuthProvider();

export default app;
