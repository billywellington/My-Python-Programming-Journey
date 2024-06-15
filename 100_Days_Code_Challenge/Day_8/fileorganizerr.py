import os
import shutil
from datetime import datetime

# Function to create a directory if it does not exist
def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

# Function to move files to a specified folder and print success message
def move_and_report(folderName, files):
    for file in files:
        # Get the month from the file's last modified time
        month = datetime.fromtimestamp(os.path.getmtime(file)).strftime('%B')
        # Create the month directory if it does not exist
        month_folder = os.path.join(folderName, month)
        createIfNotExist(month_folder)
        # Move the file to the month directory
        shutil.move(file, month_folder)
    print(f"Files have been moved to {folderName} successfully")

# List of all files in the current directory, excluding directories
files = [f for f in os.listdir() if os.path.isfile(f)]
files.remove(os.path.basename(__file__))

# Creating necessary directories
createIfNotExist('Images')
createIfNotExist('Docs')
createIfNotExist('Media')
createIfNotExist('Torrents')
createIfNotExist('Others')

# Categorizing files based on their extensions
imgExts = [".png", ".jpg", ".jpeg", ".gif", ".heic"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

docExts = [".txt", ".docx", ".doc", ".pdf", ".xlsx"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

mediaExts = [".mp4", ".mp3", ".flv"]
medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

torrentExts = [".torrent"]
torrents = [file for file in files if os.path.splitext(file)[1].lower() in torrentExts]

others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and (ext not in torrentExts) and os.path.isfile(file):
        others.append(file)

# Moving categorized files into their respective directories and printing success messages
move_and_report("Images", images)
move_and_report("Docs", docs)
move_and_report("Media", medias)
move_and_report("Torrents", torrents)
move_and_report("Others", others)
