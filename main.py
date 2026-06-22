import json
from pathlib import Path

def load_config():
    with open('config.json', 'r', encoding='UTF-8') as f:
        return json.load(f)
    
config = load_config()
source_dir = Path(config['source_dir'])
dest_dir = Path(config['dest_dir'])

# --- CHECAGEM DE DIRETÓRIOS ---
if not source_dir.exists():
    print(f"Source directory {source_dir} does not exist.")
    exit(1)

if not dest_dir.exists():
    print(f"Destination directory {dest_dir} does not exist.")
    # CORREÇÃO 1: Salvando a resposta na variável 'response'
    response = input("Do you want to create the destination directory? (y/n): ")
    if response.lower() == 'y':
        dest_dir.mkdir(parents=True, exist_ok=True)
        print("Directory created successfully.")
    else:
        print("Exiting.")
        exit(1)

# --- FUNÇÕES ---
def list_files(directory=source_dir):
    return [f for f in directory.iterdir() if f.is_file()]

def choose_move_option():
    print("\nMove options:")
    print("1. Move all PNG files")
    print("2. Move specific files")
    choice = input("Enter your choice (1/2): ")
    
    if choice == '2':
        print("\n Avaliable files: ")
        for arquivo in list_files(source_dir):
            if arquivo.suffix.lower() != '.png':
             print(f"- {arquivo.name}")
        print("-" * 40)
        file_names = input("Enter file names to move (separated by commas): ")
        return [name.strip() for name in file_names.split(',')]
    return choice

def should_move(choice):
    arquivos_para_mover = []
    
    if choice == '1':
        for arquivo in list_files():
            if arquivo.suffix.lower() == '.png':
                arquivos_para_mover.append(arquivo)
                
    # Adicionei a lógica caso o usuário escolha a opção '2'
    elif isinstance(choice, list): 
        for arquivo in list_files():
            if arquivo.name in choice:
                arquivos_para_mover.append(arquivo)
                
    return arquivos_para_mover 

# --- EXECUÇÃO DO PROGRAMA ---
escolha_usuario = choose_move_option()
arquivos_finais = should_move(escolha_usuario)

print("\nEstes arquivos estão prontos para serem movidos:")
for f in arquivos_finais:
    print(f"- {f.name}")