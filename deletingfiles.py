import os
import shutil

path = "text"

try:
    # os.remove("text")     #deletes a file
    # os.rmdir(path)        #deletes an empty directoy
    shutil.rmtree(path)     #delets a dir containing files


except FileNotFoundError:
    print("File not found")
except OSError:
    print("You cannot delete this der as it contains files")
