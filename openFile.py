import os
import shutil
from termcolor import colored
from colors import colors

def openedFile():
    # Defining the root folder and listing all the sub directories with in it 
    root = r"C:\Users\Tanuj\OneDrive"
    for dir in os.listdir(root):
        print(colored(dir, 'red'))

    subDir = input("\033[1;37;40m >\033[1;49;95m What folder? \033[1;49;96m")

    if subDir == "science" or subDir == "phy":
        # Printing all the files in a sub directory
        for file in os.listdir(r"C:\Users\Tanuj\OneDrive\Science"):
            print(colored(file, 'blue'))
        # Opening the file by using the absolute path and os.startfile to open it. If not it will throw an error of file not found
        try:
            openedFile = input(f"{colors['white']}  > {colors['purple']} File Name? {colors['cyan']}")
            openedFile = openedFile + ".docx"
            os.startfile(os.path.join(
                r"C:\Users\Tanuj\OneDrive\Science", openedFile))
        except FileNotFoundError:
            print("File Not Found")
    elif subDir == "his" or subDir == "history":
        for file in os.listdir(r"C:\Users\Tanuj\OneDrive\History"):
            print(colored(file, 'blue'))
        try:
            openedFile = input(f"{colors['white']}  > {colors['purple']} File Name? {colors['cyan']}")
            openedFile = openedFile + ".docx"
            os.startfile(os.path.join(
                r"C:\Users\Tanuj\OneDrive\History", openedFile))
        except FileNotFoundError:
            print("> File Not Found")
    elif subDir == "eng" or subDir == "english":
        for file in os.listdir(r"C:\Users\Tanuj\OneDrive\English"):
            print(colored(file, 'blue'))
        try:
            openedFile = input(f"{colors['white']}  > {colors['purple']} File Name? {colors['cyan']}")
            openedFile = openedFile + ".docx"
            os.startfile(os.path.join(
                r"C:\Users\Tanuj\OneDrive\English", openedFile))
        except FileNotFoundError:
            print("File Not Found") 
    elif subDir == "comp":
        for file in os.listdir(r"C:\Users\Tanuj\OneDrive\Computer"):
            print(colored(file, 'blue'))
        try:
            openedFile = input(f"{colors['white']}  > {colors['purple']} File Name? {colors['cyan']}")
            openedFile = openedFile + ".docx"
            os.startfile(os.path.join(
                r"C:\Users\Tanuj\OneDrive\Computers", openedFile))
        except FileNotFoundError:
            print("File Not Found") 
      
