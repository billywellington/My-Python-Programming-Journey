import os

mypath = "/home/billy-wellington/Desktop/My-Python-Programming-Journey"

if os.path.exists(mypath):
    print("This location exists")
    if os.path.isdir(mypath):
        print("This folder exists")
    else:
        print("This file exists")


