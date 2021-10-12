import os
import shutil

def deleteFile(absPath):
    for fileFolder in os.listdir(absPath):
        print(fileFolder)
    deletedFile = input("Which file would you like do go (you can also go to a directory? ")
    if os.path.isfile(absPath + r"/" + deletedFile):
        # Were going to be deleting the files using os.remove accompanied with the absolute path of the file
        os.remove(absPath + r"/" + deletedFile)

    # If it is a directory we will list all the files inside the directory. This way we can delete files in sub directories aswell
    elif os.path.isdir(absPath + "/" + deletedFile):
        for file in os.listdir(absPath + "/" + deletedFile):
            print(file)
        fileDeleted = input("Enter a file to delete? ")
        os.remove(absPath + "/" + deletedFile + "/" + fileDeleted)
