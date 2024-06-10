#built a file organizer using python

import os
import shutil

# Function to create a directory
def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

# Function to move files
def move(folderName, files):
    for file in files:
        shutil.move(file, folderName)
        print(f"Files have been moved to {folderName} successfully")


# List of all files in the current directory
files = os.listdir()
files.remove("fileorganizerr.py")

createIfNotExist('Images')
createIfNotExist('Docs')
createIfNotExist('Media')
createIfNotExist('Others')
createIfNotExist('Torrents')
createIfNotExist('Movies')


imgExts = [".png", ".jpg", ".jpeg"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]

torrentExts = [".torrent"]
torrents = [file for file in files if os.path.splitext(file)[1].lower() in torrentExts]

docExts = [".txt", ".docx", ".doc", ".pdf"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

mediaExts = [".mp4", ".mp3", ".flv"]
medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
        others.append(file)

move("Images", images)
move("Docs", docs)
move("Media", medias)
move("Others", others)


