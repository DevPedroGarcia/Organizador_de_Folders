import json
import shutil
import os
from pathlib import Path

class FileManager:
    def __init__(self, config_path='config.json'):
        self.config = self._load_config(config_path)
        self.source_dir = Path(self.config['source_dir'])
        self.dest_dir = Path(self.config['dest_dir'])
        self._validate_directories()

    def _load_config(self, path):
        with open(path, 'r', encoding='UTF-8') as f:
            return json.load(f)

    def _validate_directories(self):
        if not self.source_dir.exists():
            print(f"Error: Source directory '{self.source_dir}' does not exist.")
            exit(1)

        if not self.dest_dir.exists():
            print(f"Destination directory '{self.dest_dir}' does not exist.")
            response = input("Create destination directory? (y/n): ").strip().lower()
            if response == 'y':
                self.dest_dir.mkdir(parents=True, exist_ok=True)
                print("Directory created successfully.")
            else:
                print("Exiting.")
                exit(1)

    def _clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def _pause(self):
        input("\nPress ENTER to return to the menu...")
        self._clear_screen()    

    def _get_files(self, extension=None):
        """Helper to fetch files, optionally filtered by extension."""
        files = [f for f in self.source_dir.iterdir() if f.is_file()]
        if extension:
            files = [f for f in files if f.suffix.lower() == extension.lower()]
        return files

    def _confirm_operation(self):
        response = input("\nConfirm operation? (y/n): ").strip().lower()
        return response == 'y'
        

    # --- DELETE OPERATIONS ---

    def delete_all_zips(self):
        zip_files = self._get_files(extension='.zip')
        
        if not zip_files:
            print("No .zip files found.")
            return

        if self._confirm_operation():
            for file in zip_files:
                file.unlink()
                print(f"Deleted: {file.name}")
        else:
            print("Operation cancelled.")

    def delete_specific_zips(self):
        zip_files = self._get_files(extension='.zip')
        
        if not zip_files:
            print("No .zip files found.")
            return

        print("\nAvailable .zip files:")
        for file in zip_files:
            print(f"- {file.name}")

        target_names = input("\nEnter file names to delete (comma-separated): ").split(',')
        target_names = [name.strip() for name in target_names]

        files_to_delete = [f for f in zip_files if f.name in target_names]

        self._clear_screen()

        print("\n--- DELETE FILES ---")
        for file in files_to_delete:
            file.unlink()
            print(f"[SIMULATION] Would delete: {file.name}")

    # --- MOVE OPERATIONS ---

    def move_all_pngs(self):
        png_files = self._get_files(extension='.png')
        self._execute_move(png_files)

    def move_specific_files(self):
        all_files = self._get_files()
        
        print("\nAvailable files:")
        for file in all_files:
            print(f"- {file.name}")

        target_names = input("\nEnter file names to move (comma-separated): ").split(',')
        target_names = [name.strip() for name in target_names]
        
        files_to_move = [f for f in all_files if f.name in target_names]
        self._execute_move(files_to_move)

    def _execute_move(self, files):
        if not files:
            print("No files to move.")
            self._clear_screen()
            return

        print("\nFiles ready to move:")
        for file in files:
            print(f"- {file.name}")

        if self._confirm_operation():
            for file in files:
                destination = self.dest_dir / file.name
                shutil.move(file, destination)
                print(f"Moved: {file.name}")
        else:
            print("Operation cancelled.")
        
        self._pause()

    # --- MAIN CONTROLLER ---

    def run(self):
        while True:
            print("\n--- FILE AUTOMATOR ---")
            print("1. Move all PNG files")
            print("2. Move specific files")
            print("3. Delete all ZIP files")
            print("4. Delete specific ZIP files")
            print("5. Exit")
            
            choice = input("Enter your choice (1-5): ").strip()

            if choice == '1':
                self.move_all_pngs()
            elif choice == '2':
                self.move_specific_files()
            elif choice == '3':
                self.delete_all_zips()
            elif choice == '4':
                self.delete_specific_zips()
            elif choice == '5':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")
                print("\nPress ENTER to return to menu...")
                self._clear_screen()

if __name__ == '__main__':
    app = FileManager()
    app.run()