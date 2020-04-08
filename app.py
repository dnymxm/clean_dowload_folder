import os
import shutil
from glob import glob

# ~/.../...
home_path = "REPLACE BY YOUR DOWNLOAD PATH"
# Your download folder path
download_folder_path = "REPLACE BY YOUR DOWNLOAD PATH"

# Extensions by folder
extensions = {
    "Documents": [
        ".txt",
        ".pdf",
        ".xls",
        ".xlsx"
    ],
    "Pictures": [
        ".jpg",
        ".jpeg",
        ".png"
    ],
    "Music": [
        ".mp3"
    ],
    "Movies": [
        ".mp4",
        ".mkv",
        ".mov"
    ]
}

# Get currents files in your download folder
files = glob(os.path.join(download_folder_path, "*"))

for f in files:
    # Get extention for each file
    extension = os.path.splitext(f)[-1]
    for key, value in extensions.items():
        # If extension is in one your list of extensions..
        if extension in value:
            # Join folder path
            extension_folder_path = os.path.join(home_path, key)
            # Make new folder directory if it not exists
            os.makedirs(extension_folder_path, exist_ok=True)
            # Move file from your download folder in extension's folder
            shutil.move(f, extension_folder_path)
