SELECT clients.name, clients.cpf, extract.*
FROM extract
JOIN clients on extract.id_client = clients.id_client
WHERE description LIKE '%Indique e ganhe%';
