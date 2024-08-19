import json

def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def unify_data(clients, purchases, indications, values):
    client_dict = {client['CPF']: client for client in clients}
    
    for purchase in purchases:
        cpf = purchase['CPF']
        if cpf in client_dict:
            client = client_dict[cpf]
            if 'CONTRATOS' not in client:
                client['CONTRATOS'] = []
            client['CONTRATOS'].append(purchase)
    
    for indication in indications:
        cpf = indication['CPF']
        if cpf in client_dict:
            client = client_dict[cpf]
            if 'INDICACAO' not in client:
                client['INDICACAO'] = []
            client['INDICACAO'].append(indication)
    
    for value in values:
        cpf = value['CPF']
        if cpf in client_dict:
            client = client_dict[cpf]
            client['VALORSACADO'] = value['VALORSACADO']
    
    return list(client_dict.values())

def main():
    clients_file = 'CLIENTS_INFO_OUTPUT.json'
    purchases_file = 'COMPRAS_OUTPUT.json'
    indications_file = 'INDICACAO_OUTPUT.json'
    values_file = 'VALOR_SACADO_OUTPUT.json'
    output_file = 'CLIENT_ALL_DATA.json'
    
    clients = load_json(clients_file)
    purchases = load_json(purchases_file)
    indications = load_json(indications_file)
    values = load_json(values_file)
    
    unified_data = unify_data(clients, purchases, indications, values)
    
    save_json(unified_data, output_file)

if __name__ == "__main__":
    main()
