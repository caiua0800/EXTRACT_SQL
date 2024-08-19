import json
import re

def remove_points_from_cpf(cpf):
    if cpf:
        # Remove pontos e formata o CPF
        return re.sub(r'\.', '', cpf)
    return None

def process_json(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        data = json.load(infile)
    
    for entry in data:
        if 'CPF' in entry and entry['CPF']:
            entry['CPF'] = remove_points_from_cpf(entry['CPF'])
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(data, outfile, indent=4)

if __name__ == "__main__":
    input_file = 'RENDIMENTOS_INPUT_QUASE.json'  # Substitua pelo nome do seu arquivo JSON de entrada
    output_file = 'RENDIMENTOS_OUTPUT.json'  # Nome do arquivo JSON a ser criado
    
    process_json(input_file, output_file)
