// index.js (Exemplo de script de inicialização)
const { createUsers } = require('./create_users');

createUsers().then(() => {
  console.log('Todos os usuários foram criados.');
}).catch((error) => {
  console.error('Erro ao criar usuários:', error);
});
