import os
import shutil

def deleteFile(absPath):
    for fileFolder in os.listdir(absPath):
        print(fileFolder)
    deletedFile = input("Which file would you like do go (you can also go to a directory? ")
    if os.path.isfile(absPath + r"/" + deletedFile):
        os.remove(absPath + r"/" + deletedFile)
    elif os.path.isdir(absPath + "/" + deletedFile):
        for file in os.listdir(absPath + "/" + deletedFile):
            print(file)
        fileDeleted = input("Enter a file to delete? ")
        os.remove(absPath + "/" + deletedFile + "/" + fileDeleted)
