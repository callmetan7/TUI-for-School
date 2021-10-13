import os
from src.globalVariables import *
import shutil


def openFile(absPath):
    for fileFolder in os.listdir(absPath):
        print(f"{blue}{fileFolder}")
    openedFile = input(
        f"{purple} Which file would you like do go (you can also go to a directory? {white}>{green} ")

    # If it is a file we will open it by simply combining the paths 
    if os.path.isfile(absPath + r"/" + openedFile):
        try:
            os.startfile(absPath + r"/" + openedFile)
        except FileNotFoundError():
            print(f"{white} > You may have mispelled the file name (also inlcude the file extension)")

    # We check if its a directory so we have can open it and list the files inside the sub directory
    elif os.path.isdir(absPath + "/" + openedFile):
        for file in os.listdir(absPath + "/" + openedFile):
            print(f"{blue}{file}")
        fileOpened = input(f"{purple}  Enter a file to open? {white}>{green} ")
        try:
            os.startfile(absPath + "/" + openedFile + "/" + fileOpened)
        except FileNotFoundError():
            print(f"{white} > You may have mispelled the file name (also inlcude the file extension)")
