import os
import shutil
from termcolor import colored

def engNewFile():
    fileName = input("\033[1;37;40m  > What is the file name? \033[1;49;96m")
    engFile = r"C:\Users\Tanuj\OneDrive\English\\" + fileName + ".docx"
    with open(engFile, 'w') as fp:
        pass
    os.startfile(Engfile)

def hisNewFile():
    fileName = input("\033[1;37;40m  > What is the file name? \033[1;49;96m")
    hisFile = r"C:\Users\Tanuj\OneDrive\History\\" + fileName + ".docx"
    with open(hisFile, 'w') as fp:
        pass

def sciNewFile():
    fileName = input("\033[1;37;40m  > What is the file name? \033[1;49;96m")
    sciFile = r"C:\Users\Tanuj\OneDrive\Science\\" + fileName + ".docx"
    with open(sciFile, 'w') as fp:
        pass