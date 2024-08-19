import json
import os

# Função para formatar o CPF
def format_cpf(cpf):
    if cpf:
        # Remove pontos, traços e espaços
        formatted_cpf = cpf.replace('.', '').replace('-', '').replace(' ', '')
        if formatted_cpf.lower() != "indefinido":
            return formatted_cpf
    return None

def main():
    # Caminho para o arquivo de entrada
    input_file = 'CLIENTS_INFO_INPUT.json'
    
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
    output_file = os.path.join(output_dir, 'CLIENTS_INFO_OUTPUT.json')
    
    # Carregar o arquivo JSON de entrada
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Processar os dados
    output_data = []
    for entry in data:
        formatted_cpf = format_cpf(entry.get("CPF"))
        if formatted_cpf:
            entry["CPF"] = formatted_cpf
        
        # Adicionar os novos campos com valor True
        entry["DOCSENVIADOS"] = True
        entry["DOCSVERIFICADOS"] = True
        
        output_data.append(entry)
    
    # Salvar os dados processados no arquivo de saída
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=4, ensure_ascii=False)
    
    print(f"Arquivo '{output_file}' gerado com sucesso.")

if __name__ == "__main__":
    main()
