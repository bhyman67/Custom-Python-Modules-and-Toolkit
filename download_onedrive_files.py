import os

# Path to the OneDrive directory containing the files
one_drive_dir = ''

# Function to force download of OneDrive files
def download_onedrive_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                # Open the file to trigger download
                with open(file_path, 'rb') as f:
                    f.read(1)  # Read the first byte to force download
                print(f"Downloaded: {file_path}")
            except FileNotFoundError:
                # FileNotFoundError occurs if the file is online-only and not yet downloaded
                print(f"File not yet downloaded (triggered download): {file_path}")
            except Exception as e:
                print(f"Error processing {file_path}: {e}")

# Run the function
download_onedrive_files(one_drive_dir)
