import re
import json
import os

def format_data(data):
    formatted_data = []
    
    for item in data:
        formatted_item = {}
        
        # Formatar CPF: remover espaços, pontos e traços, e renomear para CPF
        cpf_clean = re.sub(r'[.\s-]', '', item.get("cpf", ""))
        formatted_item['CPF'] = cpf_clean
        
        # Processar wallet_btc
        wallet_btc = item.get("wallet_btc", "")
        
        # Criar novos campos com base em wallet_btc
        banco_match = re.search(r'Banco:\s*(.*?)<br>', wallet_btc, re.IGNORECASE)
        if banco_match:
            formatted_item['BANCO'] = banco_match.group(1).strip()
        
        account_type_match = re.search(r'Tipo\s*de\s*conta:\s*(.*?)<br>', wallet_btc, re.IGNORECASE)
        if account_type_match:
            formatted_item['ACCOUNTTYPE'] = account_type_match.group(1).strip()
        
        agency_match = re.search(r'Agência:\s*(.*?)\s*\|\|\|', wallet_btc, re.IGNORECASE)
        if agency_match:
            formatted_item['AGENCY'] = agency_match.group(1).strip()
        
        account_match = re.search(r'Conta:\s*(.*?)($|<br>)', wallet_btc, re.IGNORECASE)
        if account_match:
            formatted_item['ACCOUNT'] = account_match.group(1).strip()
        
        keypix_match = re.search(r'(pix|pixx):?\s*(.*?)($|<br>)', wallet_btc, re.IGNORECASE)
        if keypix_match:
            formatted_item['KEYPIX'] = keypix_match.group(2).strip()
        
        formatted_data.append(formatted_item)
    
    return formatted_data

def main():
    # Ler o JSON de entrada
    with open('CARTEIRA_INPUT.json', 'r', encoding='utf-8') as infile:
        data = json.load(infile)
    
    # Processar os dados
    formatted_data = format_data(data)
    
    # Definir o diretório de saída
    current_dir = os.path.dirname(__file__)  
    parent_dir1 = os.path.dirname(current_dir)  
    parent_dir2 = os.path.dirname(parent_dir1)
    output_dir = os.path.join(parent_dir2, 'dados_formatados')
    
    # Criar o diretório se não existir
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Salvar o resultado no JSON de saída
    output_file_path = os.path.join(output_dir, 'CARTEIRA_OUTPUT.json')
    with open(output_file_path, 'w', encoding='utf-8') as outfile:
        json.dump(formatted_data, outfile, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    main()
