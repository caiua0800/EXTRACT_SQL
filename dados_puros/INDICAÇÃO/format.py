import json
import os

# Função para formatar o CPF
def format_cpf(cpf):
    if cpf:
        # Remove pontos, traços e espaços
        formatted_cpf = cpf.replace('.', '').replace('-', '').replace(' ', '')
        if formatted_cpf and formatted_cpf.lower() != "indefinido":
            return formatted_cpf
    return None

def main():
    # Caminho para o arquivo de entrada
    input_file = 'INDICACAO_INPUT.json'
    
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
    output_file = os.path.join(output_dir, 'INDICACAO_OUTPUT.json')
    
    # Carregar o arquivo JSON de entrada
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Processar os dados
    output_data = []
    for entry in data:
        formatted_cpf = format_cpf(entry.get("cpf"))
        if formatted_cpf:
            new_entry = {
                "NAME": entry.get("name"),
                "CPF": formatted_cpf,
                "ID_EXTRACT": entry.get("id_extract"),
                "CODCLI": entry.get("id_client"),
                "DATACRIACAO": entry.get("date_created"),
                "DESCRIPTION": entry.get("description"),
                "VALUE": entry.get("value")
            }
            output_data.append(new_entry)

    # Escrever o output em um novo arquivo JSON
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=4)

    print(f"Dados processados e salvos em {output_file}.")

if __name__ == "__main__":
    main()
