// Importa os módulos necessários
const { initializeApp } = require('firebase/app');
const { getFirestore, doc, setDoc } = require('firebase/firestore');
const fs = require('fs');
const {db} = require('../firebaseConfig')

// Função para processar e importar os dados do arquivo JSON para o Firestore
const importDataToFirestore = async () => {
  try {
    // Lê o arquivo JSON
    const data = JSON.parse(fs.readFileSync('CONTATOS_OUTPUT.json', 'utf8'));

    // Processa cada entrada
    for (const entry of data) {
      const { CPF, CONTACT } = entry;

      // Verifica se CPF é válido
      if (CPF) {
        const clientRef = doc(db, 'USERS', CPF);

        // Define os dados no Firestore
        await setDoc(clientRef, {
          CONTACT: CONTACT || null
        }, { merge: true }); // merge: true permite atualizar os documentos existentes sem apagar os dados anteriores

        console.log(`Dados do cliente com CPF ${CPF} carregados com sucesso.`);
      } else {
        console.warn('CPF não encontrado para um cliente e será ignorado.');
      }
    }

    console.log('Todos os dados foram carregados com sucesso!');
  } catch (error) {
    console.error('Erro ao carregar os dados:', error);
  }
};

// Executa a função de importação
importDataToFirestore();
