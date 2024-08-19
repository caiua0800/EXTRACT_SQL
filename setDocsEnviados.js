
//setar como verificados no firebase

const { getFirestore, collection, getDocs, doc, updateDoc, writeBatch } = require('firebase/firestore');
const { initializeApp } = require('firebase/app');
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

const updateDocuments = async () => {
  try {
    // Obtém todos os documentos na coleção USERS
    const usersCollectionRef = collection(db, 'USERS');
    const usersSnapshot = await getDocs(usersCollectionRef);

    if (usersSnapshot.empty) {
      console.log('Nenhum documento encontrado.');
      return;
    }

    // Atualiza cada documento com os campos DOCSENVIADOS e DOCSVERIFICADOS
    const batch = writeBatch(db);
    usersSnapshot.forEach(docSnap => {
      const docRef = doc(db, 'USERS', docSnap.id);
      batch.set(docRef, {
        DOCSENVIADOS: true,
        DOCSVERIFICADOS: true
      }, { merge: true });

      // Log do ID do documento
      console.log(`Atualizando documento ID: ${docSnap.id}`);
    });

    // Commit as atualizações em lote
    await batch.commit();
    console.log('Todos os documentos foram atualizados com sucesso.');
  } catch (error) {
    console.error('Erro ao atualizar documentos:', error);
  }
};

updateDocuments();
