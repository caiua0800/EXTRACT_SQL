import subprocess
import os

def run_script(script_path):
    """Executa um script Python e espera até que termine."""
    print(f"Executando {script_path}...")
    result = subprocess.run(['python', script_path], capture_output=True, text=True)
    print(result.stdout)  # Captura a saída padrão do script
    if result.returncode != 0:
        print(f"Erro ao executar {script_path}: {result.stderr}")
    else:
        print(f"{script_path} executado com sucesso.")
    return result

def format_data():
    """Executa format.py (e format2.py se aplicável) em todos os diretórios especificados."""
    directories = [
        'dados_puros/COMPRAS',
        'dados_puros/RENDIMENTO_ATÉ_HOJE',
        'dados_puros/INDICACAO',
        'dados_puros/CLIENTES_INFO'
    ]
    
    for directory in directories:
        format_script = os.path.join(directory, 'format.py')
        if os.path.exists(format_script):
            run_script(format_script)
        else:
            print(f"{format_script} não encontrado.")
    
    # Tratamento especial para 'dados_puros/SAQUES'
    saques_dir = 'dados_puros/SAQUES'
    format_script = os.path.join(saques_dir, 'format.py')
    format2_script = os.path.join(saques_dir, 'format2.py')
    
    if os.path.exists(format_script):
        run_script(format_script)
    else:
        print(f"{format_script} não encontrado.")
    
    if os.path.exists(format2_script):
        run_script(format2_script)
    else:
        print(f"{format2_script} não encontrado.")

def unify_data():
    """Executa unify.py na pasta dados_formatados."""
    unify_script = 'dados_formatados/unify.py'
    if os.path.exists(unify_script):
        run_script(unify_script)
    else:
        print(f"{unify_script} não encontrado.")

def main():
    """Função principal para executar os scripts na ordem correta."""
    print("Iniciando processamento de dados...")
    format_data()
    unify_data()
    print("Processamento concluído.")

if __name__ == "__main__":
    main()
