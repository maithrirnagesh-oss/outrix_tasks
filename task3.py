import os
import shutil

# Define the directory to be organized (e.g., your Downloads folder)
# IMPORTANT: Change this path to the directory you want to organize!
directory_to_organize = "C:\\Users\\DELL\\Downloads" 

# Define a dictionary to map file extensions to folder names
file_types = {
    "Images": [".jpeg", ".jpg", ".png", ".gif", ".bmp", ".tiff", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".rtf", ".odt", ".pptx", ".xlsx", ".csv"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma"],
    "Video": [".mp4", ".mov", ".avi", ".mkv", ".flv", ".wmv"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".html", ".css", ".js", ".java", ".cpp", ".c", ".json"],
    "Executables": [".exe", ".msi"],
    "Other": [] # A catch-all for any uncategorized files
}

# Ensure the specified directory exists
if not os.path.isdir(directory_to_organize):
    print(f"Error: The directory '{directory_to_organize}' does not exist.")
    exit()

# Get a list of all items in the directory
all_items = os.listdir(directory_to_organize)

print(f"Organizing files in: {directory_to_organize}")

for item in all_items:
    item_path = os.path.join(directory_to_organize, item)

    # Skip directories and the script file itself
    if os.path.isdir(item_path) or item == os.path.basename(__file__):
        continue

    # Get the file's extension
    file_name, file_extension = os.path.splitext(item)
    file_extension = file_extension.lower()

    # Find the correct folder for the file
    destination_folder = None
    for folder, extensions in file_types.items():
        if file_extension in extensions:
            destination_folder = folder
            break
    
    # If no category is found, use the 'Other' folder
    if destination_folder is None:
        destination_folder = "Other"

    # Create the destination folder if it doesn't exist
    destination_path = os.path.join(directory_to_organize, destination_folder)
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)
        print(f"Created folder: {destination_folder}")

    # Move the file to the new folder
    try:
        shutil.move(item_path, os.path.join(destination_path, item))
        print(f"Moved '{item}' to '{destination_folder}'")
    except shutil.Error as e:
        print(f"Error moving '{item}': {e}")
    
print("\nFile organization complete!")