import json

def load_and_decode_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def save_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def format_all(data):
    # Filtra os dados para incluir apenas os objetos com CPF não nulo
    filtered_data = [entry for entry in data if entry.get("CPF") is not None]
    return filtered_data

def main():
    input_file = 'CLIENT_ALL_DATA_INPUT.json'
    output_file = 'CLIENT_ALL_DATA_OUTPUT.json'
    
    # Load and decode the JSON
    data = load_and_decode_json(input_file)
    
    # Format the data
    formatted_data = format_all(data)
    
    # Save the formatted data to a file
    save_json(formatted_data, output_file)

if __name__ == "__main__":
    main()
