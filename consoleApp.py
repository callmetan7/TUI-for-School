import os
import shutil

from fileOrganiser import fileOrganiserOV
from mkNewFiles import *
from openFile import definePath
from termcolor import colored
from deleteFile import deleteFile

def clear():
    os.system('cls' if os.name=='nt' else 'clear')
    return("   ")
clear()
print("")
running = True
while running:
    userCommand = input(f"\033[1;37;40m> \033[1;49;96m")
    if userCommand.lower() == "movefile":
        source_folder = input("\033[1;37;40m > \033[1;49;95m What is the source folder? \033[1;49;92m")
        if source_folder == "ov":
            fileOrganiserOV()
    elif userCommand.lower() == "newfile":
        userCommand = input("\033[1;37;40m > \033[1;49;95m Where would you like to create the file? \033[1;49;92m")
        if userCommand == "ov":
            userCommand = input("\033[1;37;40m > \033[1;49;95m Which class would like it for?  \033[1;49;96m")
            if userCommand.lower() == "eng":
                engNewFile()
            elif userCommand.lower() == "sci" or userCommand.lower() == "science":
                sciNewFile()
            elif userCommand.lower() == "his" or userCommand.lower() == "history":
                hisNewFile()
    elif userCommand.lower() == "openfile":
        userCommand = input("\033[1;37;40m > \033[1;49;92m")
        if userCommand == "ov":
            definePath()
    elif userCommand == "dlfile" or userCommand == "delete":
        deleteFile()
    elif userCommand == "help":
        print("""
\033[1;37;40m > \033[1;49;92m dlfile --> Delete a file
\033[1;37;40m > \033[1;49;92m movefile --> Organise your files 
\033[1;37;40m > \033[1;49;92m newfile --> Make a new file
\033[1;37;40m > \033[1;49;92m openfile --> Open a file
        """)
    elif userCommand == "clear":
        clear()
    elif userCommand == "quit":
        running = False
        break