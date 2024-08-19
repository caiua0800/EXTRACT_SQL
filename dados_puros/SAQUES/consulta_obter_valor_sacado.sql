

SELECT 
    c.id_client, 
    c.name, 
    CAST(c.cpf AS CHAR) AS cpf, 
    SUM(e.value) AS total_value
FROM extract e
JOIN clients c ON e.id_client = c.id_client
WHERE e.description = 'Solicitação de saque'
GROUP BY c.id_client, c.name, c.cpf
ORDER BY c.name;


