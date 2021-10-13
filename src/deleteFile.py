import os
import shutil
from src.globalVariables import *

def deleteFile(absPath):
    for fileFolder in os.listdir(absPath):
        print(f"{blue}{fileFolder}")
    deletedFile = input(f" {purple}Which file would you like do go (you can also go to a directory? {white}>{green} ")
    if os.path.isfile(absPath + r"/" + deletedFile):
        # Were going to be deleting the files using os.remove accompanied with the absolute path of the file
        try:
            os.remove(absPath + r"/" + deletedFile)
        except FileNotFoundError():
            print(f"{white} > You may have mispelled the file name (also inlcude the file extension)")

    # If it is a directory we will list all the files inside the directory. This way we can delete files in sub directories aswell
    elif os.path.isdir(absPath + "/" + deletedFile):
        for file in os.listdir(absPath + "/" + deletedFile):
            print(f"{blue}{file}")
        fileDeleted = input("Enter a file to delete? ")
        try:
            os.remove(absPath + "/" + deletedFile + "/" + fileDeleted)
        except FileNotFoundError():
            print(f"{white} > You may have mispelled the file name (also inlcude the file extension)")
