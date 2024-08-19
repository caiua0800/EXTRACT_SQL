import json
import re

# Lista de DDDs brasileiros
BR_DDDs = {'11', '12', '13', '14', '15', '16', '17', '18', '19', '21', '22', '24', '27', '28',
           '31', '32', '33', '34', '35', '37', '38', '41', '42', '43', '44', '45', '46', '47', '48', '49',
           '51', '53', '54', '55', '61', '62', '63', '64', '65', '66', '67', '68', '69',
           '71', '73', '74', '75', '77', '79', '81', '82', '83', '84', '85', '86', '87', '88', '89',
           '91', '92', '93', '94', '95', '96', '97', '98', '99'}

def format_cpf(cpf):
    """Remove espaços, pontuações e traços do CPF e formata como número."""
    if cpf:
        # Remove espaços, pontuações e traços
        cpf = re.sub(r'\D', '', cpf)
        return cpf
    return None

def format_mobile(mobile):
    """Remove código do país, separa o DDD e número, e formata o número conforme especificado."""
    if mobile:
        # Remove todos os caracteres não numéricos
        mobile = re.sub(r'[^\d]', '', mobile)
        
        # Remove o código do país se estiver presente
        if mobile.startswith('55'):
            mobile = mobile[2:]
        
        # Se o número começar com um DDD reconhecido, separa-o do número
        for ddd in BR_DDDs:
            if mobile.startswith(ddd):
                number = mobile[len(ddd):]
                # Se o número tiver 8 dígitos, adiciona um 9
                if len(number) == 8:
                    number = '9' + number
                return f"{ddd} {number}"
        
        # Se não houver DDD reconhecido, retorna o número formatado
        return mobile
    
    return None

def process_data(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile:
        data = json.load(infile)

    cleaned_data = []

    for entry in data:
        cpf = format_cpf(entry.get('cpf'))
        mobile = format_mobile(entry.get('mobile'))

        if mobile:  # Inclui apenas entradas com mobile não nulo
            cleaned_data.append({
                'CPF': cpf,
                'CONTACT': mobile
            })

    with open(output_file, 'w', encoding='utf-8') as outfile:
        json.dump(cleaned_data, outfile, indent=4, ensure_ascii=False)

# Define os caminhos dos arquivos
input_file = 'CONTATOS_INPUT.json'
output_file = 'CONTATOS_OUTPUT.json'

# Processa os dados
process_data(input_file, output_file)
