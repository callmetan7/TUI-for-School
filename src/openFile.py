import os
from src.globalVariables import *
import shutil


def openFile(absPath):
    for fileFolder in os.listdir(absPath):
        print(fileFolder)
    openedFile = input(
        "Which file would you like do go (you can also go to a directory? ")

    # If it is a file we will open it by simply combining the paths 
    if os.path.isfile(absPath + r"/" + openedFile):
        os.startfile(absPath + r"/" + openedFile)

    # We check if its a directory so we have can open it and list the files inside the sub directory
    elif os.path.isdir(absPath + "/" + openedFile):
        for file in os.listdir(absPath + "/" + openedFile):
            print(file)
        fileOpened = input("Enter a file to open? ")
        os.startfile(absPath + "/" + openedFile + "/" + fileOpened)
