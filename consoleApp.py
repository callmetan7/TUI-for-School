import os
import shutil
import webbrowser

from fileOrganiser import fileOrganiserOV
from mkNewFiles import *
from openFile import openedFile
from termcolor import colored
from deleteFile import deleteFile
from colors import colors


def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')
    return("   ")


# Clearing the terminal everytime someone enters the program
clearTerminal()
print("")
running = True

# The core loop of the program that will check for inputs
while running:
    userCommand = input(f"{colors['white']}> {colors['cyan']}")
    if userCommand.lower() == "movefile":
        source_folder = input(
            f"{colors['white']} >  What is the source folder? {colors['green']}")
        if source_folder == "ov":
            fileOrganiserOV()
    elif userCommand.lower() == "newfile":
        userCommand = input(
            f"{colors['white']} > {colors['purple']} Which class would like it for?  {colors['cyan']}")
        if userCommand.lower() == "eng":
            engNewFile()
        elif userCommand.lower() == "sci" or userCommand.lower() == "science":
            sciNewFile()
        elif userCommand.lower() == "his" or userCommand.lower() == "history":
            hisNewFile()
        elif userCommand.lower() == "comp" or userCommand.lower() == "computer":
            compNewFile()
    elif userCommand.lower() == "openfile":
        userCommand = input(f"{colors['white']} > {colors['green']}")
        if userCommand == "ov":
            openedFile()
    elif userCommand == "dlfile" or userCommand == "delete":
        deleteFile()
    elif userCommand == "help":
        print(f"""
{colors['white']} >  dlfile --> Delete a file
{colors['white']} >  movefile --> Organise your files 
{colors['white']} >  newfile --> Make a new file
{colors['white']} >  openfile --> Open a file
        """)
    elif userCommand == "cache":
        try:
            os.remove(r"\__pycache__\\")
            print(f"> Cleared")
        except FileNotFoundError:
            print(colored(f"> File Not Found", 'red'))
    elif userCommand == "clear":
        clear()
    elif userCommand == "quit":
        running = False
        break
    elif userCommand == "search":
        webbrowser.open("https://cn.bing.com/")
