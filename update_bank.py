import os
import json

def scan_folders_to_json(output_filename="strudel.json"):
    current_dir = os.getcwd()
    folder_contents = {
        "_base": "https://raw.githubusercontent.com/HoferEmanuel/stbs"
    }
    
    items = os.listdir(current_dir)
    
    folders = [item for item in items if os.path.isdir(os.path.join(current_dir, item)) and not item.startswith('.')]
    
    for folder in folders:
        folder_path = os.path.join(current_dir, folder)
        try:
            files = [f for f in os.listdir(folder_path) 
                    if os.path.isfile(os.path.join(folder_path, f))]
            files_with_path = [f"{folder}/{f.replace(' ', '')}" for f in files]
            folder_contents[folder] = files_with_path
        except PermissionError:
            print(f"Permission denied: {folder}")
            folder_contents[folder] = []
    
    with open(output_filename, 'w', encoding='utf-8') as f:
        json.dump(folder_contents, f, indent=2, ensure_ascii=False)
    
    for folder, files in folder_contents.items():
        print(f"  {folder}: {len(files)} files")
    
    return folder_contents

scan_folders_to_json()
print("strudel.json was refreshed.")