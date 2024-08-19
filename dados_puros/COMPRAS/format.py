import json
import re
import os

def clean_cpf(cpf):
    if cpf:
        # Remove pontos, hífens e espaços
        return re.sub(r'[.\-\s]', '', cpf)
    return None

def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        data = json.load(infile)

    processed_data = []
    for entry in data:
        if entry.get('CPF') not in [None, 'undefined']:
            entry['CPF'] = clean_cpf(entry.get('CPF'))
            processed_data.append(entry)
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(processed_data, outfile, indent=4)

def main():
    # Caminho para o arquivo de entrada
    input_file = 'COMPRAS_INPUT.json'
    
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
    
    # Caminho para o arquivo de saída
    output_file = os.path.join(output_dir, 'COMPRAS_OUTPUT.json')
    
    process_file(input_file, output_file)

if __name__ == "__main__":
    main()
