USE inovlobf_golden;

SELECT 
    id_client AS CODCLI,
    date_created AS DATACRIACAO, 
    username AS USERNAME, 
    name AS NAME, 
    cpf AS CPF, 
    email AS EMAIL, 
    mobile AS CONTACT, 
    password AS LAST_PASSWORD_CRYPT, 
    CONCAT(address, ', ', address_number) AS ADRESS,
    address_complement AS ADRESS_COMPLEMENT, 
    address_neighborhood AS NEIGHBORHOOD, 
    address_city AS CITY, 
    address_state AS STATE, 
    address_zip_code AS POSTALCODE, 
    address_country AS COUNTRY,
    status AS STATUS_ACCOUNT_LATE, 
    type_account AS ACCOUNT_TYPE_LATE
FROM 
    clients;




