SELECT c.id_client, c.name, c.cpf as CPF,
e.*
FROM extract e
JOIN clients c ON e.id_client = c.id_client
WHERE e.description = 'Solicitação de saque'
ORDER BY e.value;

