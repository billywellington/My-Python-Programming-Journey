import os

source = "copy-text"
dest = "/home/billy-wellington/Desktop/My-Python-Programming-Journey/copy-text"


try:
    if os.path.exists(dest):
        print("There is already a file there")
    else:
        os.replace(source, dest)
        print("File was successfully moved")

except FileNotFoundError:
    print(source + "was not found")


