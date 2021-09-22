import os
from termcolor import colored
from colors import colors

def deleteFile():
    # Defining the root folder of the in wear were going to be deleting our files and printing the sub directories or files
    root = r"C:\Users\Tanuj\OneDrive"
    for dir in os.listdir(root):
        print(colored(dir, 'red'))

    subDir = input(f"{colors['white']} >{colors['purple']} What folder? {colors['cyan']}")

    if subDir == "science" or subDir == "phy":
        # Displaying all the files in a certain sub directory 
        for file in os.listdir(r"C:\Users\Tanuj\OneDrive\Science"):
            print(colored(file, 'blue'))
        
        # Trying to find the file and deleting the file, if the file is not found it will throw an error
        try:
            openedFile = input("{colors['white']}  > {colors['purple']} File Name? {colors['cyan']}")
            openedFile = openedFile + ".docx"
            os.remove(os.path.join(
                r"C:\Users\Tanuj\OneDrive\Science", openedFile))
            print("> File Deleted")
        except FileNotFoundError:
            print("File Not Found")
    elif subDir == "his" or subDir == "history":
        for file in os.listdir(r"C:\Users\Tanuj\OneDrive\History"):
            print(colored(file, 'blue'))
        try:
            openedFile = input("{colors['white']}  > {colors['purple']} File Name? {colors['cyan']}")
            openedFile = openedFile + ".docx"
            os.remove(os.path.join(
                r"C:\Users\Tanuj\OneDrive\History", openedFile))
        except FileNotFoundError:
            print("> File Not Found")
    elif subDir == "eng" or subDir == "english":
        for file in os.listdir(r"C:\Users\Tanuj\OneDrive\English"):
            print(colored(file, 'blue'))
        try:
            openedFile = input("{colors['white']}  > {colors['purple']} File Name? {colors['cyan']}")
            openedFile = openedFile + ".docx"
            os.remove(os.path.join(
                r"C:\Users\Tanuj\OneDrive\English", openedFile))
        except FileNotFoundError:
            print("File Not Found")  