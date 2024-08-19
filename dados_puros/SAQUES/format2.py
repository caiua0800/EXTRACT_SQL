import json
import re
import os

def clean_cpf(cpf):
    if cpf:
        # Remove pontos, hífens e espaços, mantendo apenas números
        return re.sub(r'[.\-\s]', '', cpf)
    return None

def format_data(data):
    formatted_data = []
    for entry in data:
        formatted_entry = {
            'CODCLI': entry.get('id_client'),
            'NAME': entry.get('name'),
            'CPF': clean_cpf(entry.get('CPF')),
            'VALORSOLICITADO': entry.get('value'),
            'STATUS': entry.get('status'),
            'DATASOLICITACAO': entry.get('date_created'),
            'DESCRICAO': entry.get('description'),
        }
        formatted_data.append(formatted_entry)
    return formatted_data

def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        data = json.load(infile)

    processed_data = format_data(data)
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(processed_data, outfile, indent=4)

if __name__ == "__main__":
    # Caminho para o arquivo JSON de entrada
    input_file = 'SAQUES_INPUT.json'  # Substitua pelo nome do seu arquivo JSON de entrada
    
    # Caminho para a pasta dados_formatados que está um nível acima de dados_puros
    current_dir = os.path.dirname(__file__)  # Diretório onde o script está
    parent_dir1 = os.path.dirname(current_dir)  # Diretório pai de dados_puros
    parent_dir2 = os.path.dirname(parent_dir1)  # Diretório pai de dados_puros
    output_dir = os.path.join(parent_dir2, 'dados_formatados')
    
    if not os.path.exists(output_dir):
        print(f"Diretório {output_dir} não existe. Criando-o.")
        os.makedirs(output_dir)
    else:
        print(f"Diretório {output_dir} já existe.")
    
    # Caminho para o arquivo JSON de saída
    output_file = os.path.join(output_dir, 'SAQUES_OUTPUT.json')
    
    process_file(input_file, output_file)
    
    print(f"Dados processados e salvos em {output_file}.")
