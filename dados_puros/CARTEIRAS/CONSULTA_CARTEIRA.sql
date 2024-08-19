SELECT  c.cpf, w.wallet_btc 
FROM withdrawals w
JOIN clients c ON w.id_client = c.id_client;
