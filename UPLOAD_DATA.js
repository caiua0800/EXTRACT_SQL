// upload pro firebase

const fs = require('fs');
const { doc, setDoc } = require('firebase/firestore');
const { db } = require('./firebaseConfig');

const filePath = 'CLIENT_ALL_DATA_OUTPUT.json';

const uploadData = async () => {
  try {
    // Ler o arquivo JSON
    const data = JSON.parse(fs.readFileSync(filePath, 'utf8'));

    // Processar cada cliente
    for (const client of data) {
      const clientId = client.CPF;

      if (!clientId) {
        console.warn(`Cliente sem CPF encontrado e será ignorado.`);
        continue; // Ignorar clientes sem CPF
      }

      // Remove campos com valor `undefined`
      const clientData = {
        CODCLI: client.CODCLI,
        DATACRIACAO: client.DATACRIACAO,
        USERNAME: client.USERNAME,
        NAME: client.NAME,
        CONTACT: client.CONTACT,
        CPF: client.CPF,
        EMAIL: client.EMAIL,
        LAST_PASSWORD_CRYPT: client.LAST_PASSWORD_CRYPT,
        ADRESS: client.ADRESS,
        ADRESS_COMPLEMENT: client.ADRESS_COMPLEMENT,
        NEIGHBORHOOD: client.NEIGHBORHOOD,
        CITY: client.CITY,
        STATE: client.STATE,
        POSTALCODE: client.POSTALCODE,
        COUNTRY: client.COUNTRY,
        STATUS_ACCOUNT_LATE: client.STATUS_ACCOUNT_LATE,
        ACCOUNT_TYPE_LATE: client.ACCOUNT_TYPE_LATE,
        VALORSACADO: client.VALORSACADO,
        SAQUES: client.SAQUES,
        CONTRATOS: client.CONTRATOS,
        DOCSENVIADOS: true,
        DOCSVERIFICADOS: true
      };

      // Remove chaves com valores `undefined`
      for (const key in clientData) {
        if (clientData[key] === undefined) {
          delete clientData[key];
        }
      }

      // Verifica se o clientId está presente
      if (!clientId) {
        console.error('Erro: CPF não encontrado para um cliente.');
        continue; // Ignorar clientes sem CPF
      }

      // Cria ou atualiza o documento na coleção USERS
      await setDoc(doc(db, 'USERS', clientId), clientData);
      console.log(`Dados do cliente com CPF ${clientId} carregados com sucesso.`);
    }

    console.log('Todos os dados foram carregados com sucesso!');
  } catch (error) {
    console.error('Erro ao carregar os dados:', error);
  }
};

// Executar a função
uploadData();
