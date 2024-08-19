import json

def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def unify_data(clients, purchases, indications, values, saques, rendimentos, carteiras):
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
    
    for saque in saques:
        cpf = saque['CPF']
        if cpf in client_dict:
            client = client_dict[cpf]
            if 'SAQUES' not in client:
                client['SAQUES'] = []
            client['SAQUES'].append({
                'CODCLI': saque['CODCLI'],
                'VALORSOLICITADO': saque['VALORSOLICITADO'],
                'STATUS': saque['STATUS'],
                'DATASOLICITACAO': saque['DATASOLICITACAO']
            })
    
    for rendimento in rendimentos:
        cpf = rendimento['CPF']
        id_compra = str(rendimento['IDCOMPRA'])  # Converter para string
        rendimento_atual = float(rendimento['RENDIMENTO_ATUAL'])
        if cpf in client_dict:
            client = client_dict[cpf]
            if 'CONTRATOS' in client:
                for contrato in client['CONTRATOS']:
                    if str(contrato['IDCOMPRA']) == id_compra:  # Converter para string
                        if 'RENDIMENTO_ATUAL' not in contrato:
                            contrato['RENDIMENTO_ATUAL'] = rendimento_atual
                            print(f"Rendimento {rendimento_atual} adicionado ao contrato {id_compra}")
    
    for carteira in carteiras:
        cpf = carteira['CPF']
        if cpf in client_dict:
            client = client_dict[cpf]
            client.update(carteira)
    
    return list(client_dict.values())

def main():
    clients_file = 'CLIENTS_INFO_OUTPUT.json'
    purchases_file = 'COMPRAS_OUTPUT.json'
    indications_file = 'INDICACAO_OUTPUT.json'
    values_file = 'VALOR_SACADO_OUTPUT.json'
    saques_file = 'SAQUES_OUTPUT.json'
    rendimentos_file = 'RENDIMENTOS_OUTPUT.json'
    carteiras_file = 'CARTEIRA_OUTPUT.json'
    output_file = 'CLIENT_ALL_DATA_INPUT.json'
    
    clients = load_json(clients_file)
    purchases = load_json(purchases_file)
    indications = load_json(indications_file)
    values = load_json(values_file)
    saques = load_json(saques_file)
    rendimentos = load_json(rendimentos_file)
    carteiras = load_json(carteiras_file)
    
    unified_data = unify_data(clients, purchases, indications, values, saques, rendimentos, carteiras)
    
    save_json(unified_data, output_file)

if __name__ == "__main__":
    main()
