import os

folder_path = 'PATH_OF_THE_FOLDER'
def traverse_files_from_a_folder(folder_path):
    """Pass the path of the folder. It will
    return a list of all files contains in
    that folder tree."""
    files = []
    path = folder_path
    for item in os.listdir(folder_path):
        
        if os.path.isdir(path +'/'+item):
            print('folder',item)
            files.extend(traverse_files_from_a_folder(path +'/'+item))
        else:
            print('file',item)
            files.append(item)
    return files
        
traverse_files_from_a_folder(folder_path)