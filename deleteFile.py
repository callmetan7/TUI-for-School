import os
from termcolor import colored
def deleteFile():
    root = r"C:\Users\Tanuj\OneDrive"
    for dir in os.listdir(root):
        print(colored(dir, 'red'))

    subDir = input("\033[1;37;40m >\033[1;49;95m What folder? \033[1;49;96m")

    if subDir == "science" or subDir == "phy":
        for file in os.listdir(r"C:\Users\Tanuj\OneDrive\Science"):
            print(colored(file, 'blue'))
        try:
            openedFile = input("\033[1;37;40m  > \033[1;49;95m File Name? \033[1;49;96m")
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
            openedFile = input("\033[1;37;40m  > \033[1;49;95m File Name? \033[1;49;96m")
            openedFile = openedFile + ".docx"
            os.remove(os.path.join(
                r"C:\Users\Tanuj\OneDrive\History", openedFile))
        except FileNotFoundError:
            print("> File Not Found")
    elif subDir == "eng" or subDir == "english":
        for file in os.listdir(r"C:\Users\Tanuj\OneDrive\English"):
            print(colored(file, 'blue'))
        try:
            openedFile = input("\033[1;37;40m  > \033[1;49;95m File Name? \033[1;49;96m")
            openedFile = openedFile + ".docx"
            os.remove(os.path.join(
                r"C:\Users\Tanuj\OneDrive\English", openedFile))
        except FileNotFoundError:
            print("File Not Found")  