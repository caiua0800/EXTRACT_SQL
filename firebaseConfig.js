// firebaseConfig.js
const { initializeApp } = require('firebase/app');
const { getFirestore } = require('firebase/firestore');

// Configuração do Firebase Client SDK
const firebaseConfig = {
  apiKey: "AIzaSyBS2YwOCmnJKF4AgnjEqB0Huy2146YitII",
  authDomain: "golden-token-62a99.firebaseapp.com",
  projectId: "golden-token-62a99",
  storageBucket: "golden-token-62a99.appspot.com",
  messagingSenderId: "819750858832",
  appId: "1:819750858832:web:6d331de11d2dc5750a6155",
  measurementId: "G-YY52V2CG6N"
};

// Inicialize o Firebase
const app = initializeApp(firebaseConfig);
const db = getFirestore(app);

module.exports = { db, app }; // Exporta `db` como parte de um objeto
