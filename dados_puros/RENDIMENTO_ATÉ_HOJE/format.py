import xml.etree.ElementTree as ET
import json
import os

def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    data = []
    
    for row in root.findall('ROW'):
        ref_number = row.find('ref_number').text
        total_percentual_recompra = row.find('total_percentual_recompra').text
        client_cpf = row.find('client_cpf').text
        
        # Tratar valores nulos ou inválidos
        if client_cpf == 'NULL' or not client_cpf:
            client_cpf = None
        else:
            # Garantir que o CPF é tratado como string e sem formatação incorreta
            client_cpf = str(client_cpf).strip()
        
        entry = {
            'IDCOMPRA': ref_number,
            'CPF': client_cpf,
            'RENDIMENTO_ATUAL': total_percentual_recompra
        }
        
        data.append(entry)
    
    return data

def save_to_json(data, json_file):
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    # Caminho para o arquivo XML
    xml_file = 'RENDIMENTOS_INPUT.xml'  # Substitua pelo nome do seu arquivo XML
    
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
    
    # Caminho para o arquivo JSON
    json_file = os.path.join(output_dir, 'RENDIMENTOS_OUTPUT.json')
    
    data = parse_xml(xml_file)
    save_to_json(data, json_file)
    
    print(f"Dados processados e salvos em {json_file}.")
