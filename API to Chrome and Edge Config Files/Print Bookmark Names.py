import json

def get_chrome_bookmarks():

    # Read the JSON file
    with open('../directory_and_file_path_lib.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Reference the bookmarks_path
    bookmarks_path = data.get('bookmarks_path')
    
    try:
        with open(bookmarks_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        bookmarks = data.get('roots', {}).get('bookmark_bar', {}).get('children', [])
        
        # Recursively fetch bookmark names along with folder path
        def fetch_bookmark_names(bookmarks, path=""):
            bookmark_info = []
            for item in bookmarks:
                if item['type'] == 'folder':
                    # Add folder name to path and recurse
                    folder_path = f"{path}/{item['name']}" if path else item['name']
                    bookmark_info.extend(fetch_bookmark_names(item.get('children', []), folder_path))
                elif item['type'] == 'url':
                    # Append bookmark name with its full folder path
                    if "YouTube Videos - distribute all of this..." in path:
                        bookmark_info.append((f"{path}/{item['name']}" if path else item['name'], item['url']))
            return bookmark_info
        
        # Get all bookmarks with their folder paths
        bookmark_info = fetch_bookmark_names(bookmarks)
        
        # Print each bookmark with its full path
        for name, url in bookmark_info:
            print(f"Path: {name}\nURL: {url}\n")
        
        # Write the filtered bookmarks to a text file
        with open('filtered_bookmarks.txt', 'w', encoding='utf-8') as outfile:
            for name, url in bookmark_info:
                outfile.write(f"Path: {name}\nURL: {url}\n\n")
            
    except FileNotFoundError:
        print("Bookmarks file not found. Check the file path.")

print(get_chrome_bookmarks())
