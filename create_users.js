// create_users.js
const fs = require('fs');
const { getAuth, createUserWithEmailAndPassword, updateProfile } = require('firebase/auth');
const { app } = require('./firebaseConfig');
const clients = require('./CLIENT_ALL_DATA_OUTPUT.json');

const INITIAL_DELAY_MS = 1000; // 1 segundo
const MAX_DELAY_MS = 60000; // 1 minuto

async function createUsers() {
  const auth = getAuth(app);
  const failedEmails = [];
  
  for (const client of clients) {
    let delay = INITIAL_DELAY_MS;
    while (true) {
      try {
        const email = client.EMAIL.toLowerCase();
        const username = client.USERNAME;
        const password = `${username}@${username}123`; // Usar USERNAME@USERNAME123 como senha
        const displayName = username; // Usar USERNAME como nome

        // Criar usuário
        const userCredential = await createUserWithEmailAndPassword(auth, email, password);

        // Atualizar o nome do usuário
        await updateProfile(userCredential.user, {
          displayName: displayName,
        });

        console.log(`Usuário criado com sucesso: ${userCredential.user.uid}`);
        break; // Saia do loop se a criação for bem-sucedida
      } catch (error) {
        console.error(`Erro ao criar usuário para ${client.EMAIL}:`, error);
        failedEmails.push(client.EMAIL); // Adicionar e-mail ao array de falhas
        
        // Aguardar antes de tentar novamente
        await new Promise(resolve => setTimeout(resolve, delay));
        
        // Aumentar o atraso exponencialmente
        delay = Math.min(delay * 2, MAX_DELAY_MS);
      }
    }

    // Aguardar um tempo antes de criar o próximo usuário
    await new Promise(resolve => setTimeout(resolve, DELAY_MS));
  }

  // Salvar e-mails que não foram cadastrados
  if (failedEmails.length > 0) {
    fs.writeFileSync(FAILED_EMAILS_FILE, JSON.stringify(failedEmails, null, 2), 'utf8');
    console.log(`E-mails dos usuários que não foram cadastrados foram salvos em ${FAILED_EMAILS_FILE}`);
  }
}


// Exportar a função createUsers
module.exports = { createUsers };
