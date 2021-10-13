import os
import shutil

from src.deleteFile import deleteFile
from src.globalVariables import *
from startup import startup
from src.fileOrganiser import fileOrganiser
from src.openFile import openFile
from src.makeNewFile import makeNewFile

# Clearing the terminal on the start so there is no clutter in the app
os.system('cls' if os.name == 'nt' else 'clear')
startup()

# Running the mainloop to check for the users inputs and performs actions based on that
isRunning = True
while isRunning:
    userCommand = input(f"{white}>{cyan} ")
    
    if userCommand.lower() == "quit":
        os.system('cls' if os.name == 'nt' else 'clear')
        quit()

    elif userCommand.lower() == "ogfile":
        path = input(f"{purple} Please provide the path of the folder (you can use shortcuts like ov for downloads folder?{white} >{green} ")
        if path.lower() == "downloads" or path == "download" or path == "ov":
            path = downloadsFolder
        fileOrganiser(path)

    elif userCommand.lower() == "dlfile":
        absPath = input(f" {purple}Please provide the path of the directory?{white} >{green}")
        if absPath == "ov":
            absPath = schoolFolder
        deleteFile(absPath)
        
    elif userCommand.lower() == "open":
        absPath = input(f"{purple}Please provide the path or directory? {white}>{green}")
        if absPath.lower() == "ov":
            absPath = schoolFolder
        openFile(absPath)
    elif userCommand.lower() == "new":
        absPath = input(f"{purple}Please provide the path or directory? {white}>{green}")
        if absPath == "ov":
            absPath = schoolFolder
        makeNewFile(absPath)


if __name__ == '__main__':
    main()