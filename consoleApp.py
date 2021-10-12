import os
import shutil

from src.deleteFile import deleteFile
from src.globalVariables import *
from startup import startup
from src.fileOrganiser import fileOrganiser

# Clearing the terminal on the start so there is no clutter in the app
os.system('cls' if os.name == 'nt' else 'clear')
startup()

# Running the mainloop to check for the users inputs and performs actions based on that
isRunning = True
while isRunning:
    userCommand = input("> ")
    
    if userCommand.lower() == "quit":
        os.system('cls' if os.name == 'nt' else 'clear')
        quit()

    elif userCommand.lower() == "ogfile":
        path = input("Please provide the path of the folder (you can use shortcuts like ov for downloads folder?> ")
        if path.lower() == "downloads" or path == "download" or path == "ov":
            path = downloadsFolder
        fileOrganiser(path)
    elif userCommand.lower() == "dlfile":
        absPath = input("Please provide the path of the directory? ")
        if absPath == "ov":
            absPath = downloadsFolder
        deleteFile(absPath)

        # TODO: open, and make a new file features