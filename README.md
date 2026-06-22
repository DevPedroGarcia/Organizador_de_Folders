The origin folder is -> pasta de coisas inuteis. 
the second folder is -> Pasta Organizada. 

move only .png files, and delete .zip files. 
if you delete a file, the file go to a QUARENTINE/, dont delete 

the application will be make in dry-run

rename archive(1).png --> excluir 

error scripts - 

no permission to move (alert dont can move this archive)
archive in use (alert, this archive dont can be move or delete because is in use.)
this folder dont exist (announce this folder dont exist if the folder dont exist kkkk)


def list_files(source_dir):
    return [item for item in source_dir.iterdir() if item.is_file()]

def should_move_file(file_path, config):
    return file_path.suffix in config['file_types']
