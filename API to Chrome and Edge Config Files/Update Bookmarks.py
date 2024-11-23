import json
import os

bookmarks_path = ''
bookmarks_backup_path = ''

# Ensure Chrome is closed
os.system("taskkill /f /im chrome.exe")

def modify_bookmark_names(bookmarks):
    for item in bookmarks:
        if item['type'] == 'folder':
            modify_bookmark_names(item.get('children', []))
        elif item['type'] == 'url':
            # Modify bookmark name if it starts with "(1) "
            if item['name'].startswith("(1) "):
                item['name'] = item['name'][4:]

def update_bookmarks_file(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        bookmarks = data.get('roots', {}).get('bookmark_bar', {}).get('children', [])
        
        # Modify all bookmark names
        modify_bookmark_names(bookmarks)
        
        # Write the modified bookmarks back to the file
        with open(path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        
        print(f"Bookmarks file '{path}' updated successfully.")
            
    except FileNotFoundError:
        print(f"Bookmarks file '{path}' not found. Check the file path.")
    except PermissionError:
        print(f"Permission denied. Make sure Chrome is closed and you have the necessary permissions to modify the file '{path}'.")

# Update both the Bookmarks and Bookmarks.bak files
update_bookmarks_file(bookmarks_path)
update_bookmarks_file(bookmarks_backup_path)