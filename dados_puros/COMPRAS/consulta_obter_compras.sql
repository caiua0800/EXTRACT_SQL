
SELECT 
    clients.name AS NAME, 
    clients.cpf AS CPF, 
    quotas.id_quotas AS IDCOMPRA,
    quotas.id_client AS CODCLI,
    quotas.payment_id AS PAYMENT_ID,
    quotas.purchase_date AS PURCHASEDATE,
    quotas.amount AS COINS,
    quotas.value_unit AS COINVALUE,
    quotas.value_total AS TOTALSPENT,
    quotas.total_amount_with_fee AS TOTALSPENTFEE,
    quotas.maximum_quota_yield AS MAXIMUMQUOTAYIELD,
    quotas.total_income AS TOTALINCOME,
    quotas.current_income AS CURRENTINCOME,
    quotas.total_withdrawn AS TOTAL_WITHDRAWN,
    quotas.balance_to_be_withdrawn AS BALANCE_TO_BE_WITHDRAWN,
    quotas.maximum_number_of_days_to_yield AS MAXIMUMNUMBEROFDAYSTOYIELD,
    quotas.yield_term AS YIELDTERM,
    quotas.status_distribute AS STATUSDISTRIBUTE,
    quotas.status_mp AS STATUS_MP,
    quotas.status_detail_mp AS STATUS_DETAIL_MP,
    quotas.external_resource_url AS EXTERNAL_RESOURCE_URL,
    quotas.barcode AS BARCODE,
    quotas.qr_code_base64 AS QR_CODE_BASE64,
    quotas.qr_code AS QR_CODE,
    quotas.status AS STATUS,
    quotas.gateway_payment AS GATEWAY_PAYMENT
FROM 
    quotas
JOIN 
    clients ON quotas.id_client = clients.id_client
ORDER BY 
    clients.name;
