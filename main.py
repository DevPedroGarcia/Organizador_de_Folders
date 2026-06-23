import json
import shutil
import os
from pathlib import Path

# --- FUNÇÕES DE CONFIGURAÇÃO ---
def load_config():
    with open('config.json', 'r', encoding='UTF-8') as f:
        return json.load(f)

def check_directories(source_dir, dest_dir):
    if not source_dir.exists():
        print(f"Source directory {source_dir} does not exist.")
        exit(1)

    if not dest_dir.exists():
        print(f"Destination directory {dest_dir} does not exist.")
        response = input("Do you want to create the destination directory? (y/n): ")
        if response.lower() == 'y':
            dest_dir.mkdir(parents=True, exist_ok=True)
            print("Directory created successfully.")
        else:
            print("Exiting.")
            exit(1)

def clean_screen(): 
    # Correção: 'nt' e 'clear' precisavam estar entre aspas (como strings)
    os.system('cls' if os.name == 'nt' else 'clear')

# --- FUNÇÕES DE LÓGICA ---
def list_files(directory):
    return [f for f in directory.iterdir() if f.is_file()]

def choose_move_option(source_dir):
    print("\nMove options:")
    print("1. Move all PNG files")
    print("2. Move specific files")
    choice = input("Enter your choice (1/2): ")
    
    clean_screen()

    if choice == '2':
        print("\nAvaliable files:")
        for arquivo in list_files(source_dir):
            if arquivo.suffix.lower() != '.png':
                print(f"- {arquivo.name}")
        print("-" * 40)
        
        file_names = input("Enter file names to move (separated by commas): ")
        clean_screen()
        return [name.strip() for name in file_names.split(',')]
        
    return choice

def should_move(choice, source_dir):
    arquivos_para_mover = []
    
    if choice == '1':
        for arquivo in list_files(source_dir):
            if arquivo.suffix.lower() == '.png':
                arquivos_para_mover.append(arquivo)
                
    elif isinstance(choice, list): 
        for arquivo in list_files(source_dir):
            if arquivo.name in choice:
                arquivos_para_mover.append(arquivo)
                
    return arquivos_para_mover 

def move_folder(arquivos_finais, dest_dir):
    for archive in arquivos_finais: 
        dest_way = dest_dir / archive.name
        shutil.move(archive, dest_way)
        print(f"Success: {archive.name} was moved!")

def confirm_moved_archives():
    print("\nDo you confirm this operation?")
    confirmChoice = input("Enter the choice (Y/N): ").upper()
    
    if confirmChoice == "Y": 
        return True
    elif confirmChoice == "N":
        return False
    else:
        print("This option doesn't exist.")
        exit(1)

# --- O MAESTRO (Função Principal) ---
def main():
    # 1. Carrega as configurações
    config = load_config()
    source_dir = Path(config['source_dir'])
    dest_dir = Path(config['dest_dir'])

    # 2. Verifica se as pastas existem
    check_directories(source_dir, dest_dir)
    
    # 3. O Loop Principal do Programa
    while True:
        escolha_usuario = choose_move_option(source_dir)
        arquivos_finais = should_move(escolha_usuario, source_dir)

        if not arquivos_finais:
            print("No files to move. Exiting.")
            break

        print("\nThese archives are ready to be moved:")
        for f in arquivos_finais:
            print(f"- {f.name}")

        # 4. Confirmação
        if confirm_moved_archives():
            move_folder(arquivos_finais, dest_dir)
            break # Encerra o loop e o programa após mover
        else:
            clean_screen()
            print("Operation cancelled. Let's try again...\n")
            # Como não tem 'break' aqui, o 'while True' faz o programa voltar para o menu!

# Isso garante que o script só rode se for executado diretamente
if __name__ == '__main__':
    main()