import json

# Carregar os dados do arquivo JSON
with open('CLIENT_ALL_DATA_OUTPUT.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Iterar por todos os objetos e adicionar os campos DOCSENVIADOS e DOCSVERIFICADOS
for client in data:
    client['DOCSENVIADOS'] = True
    client['DOCSVERIFICADOS'] = True

# Salvar os dados atualizados em um novo arquivo JSON
with open('backend_data.json', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii=False, indent=4)

print("Dados atualizados e salvos em 'backend_data.json'.")
