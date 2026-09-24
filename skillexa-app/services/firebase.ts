import { initializeApp, getApps, getApp } from "firebase/app";
import { getAuth } from "firebase/auth";

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

// Initialize Firebase Auth
export const auth = getAuth(app);

export default app;
