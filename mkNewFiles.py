import os
import shutil
from termcolor import colored
from colors import colors

# Since we already defined the sub directories or directories to make the new file we dont need to display. Only make the new file

def engNewFile():
    fileName = input(
        f"{colors['white']}  > {colors['purple']}What is the file name? {colors['cyan']}")
    EngFile = r"C:\Users\Tanuj\OneDrive\English\\" + fileName + ".docx"

    # Creating and opening the file using pythons open method and the module os to open the file in word
    with open(EngFile, 'w') as fp:
        pass
    os.startfile(EngFile)


def hisNewFile():
    fileName = input(
        f"{colors['white']}  > {colors['purple']}What is the file name? {colors['cyan']}")
    hisFile = r"C:\Users\Tanuj\OneDrive\History\\" + fileName + ".docx"
    with open(hisFile, 'w') as fp:
        pass


def sciNewFile():
    fileName = input(
        f"{colors['white']}  > {colors['purple']}What is the file name? {colors['cyan']}")
    sciFile = r"C:\Users\Tanuj\OneDrive\Science\\" + fileName + ".docx"
    with open(sciFile, 'w') as fp:
        pass


def compNewFile():
    fileName = input(
        f"{colors['white']}  > {colors['purple']}What is the file name? {colors['cyan']}")
    compFile = r"C:\Users\Tanuj\OneDrive\Computer\\" + fileName + ".docx"
    with open(compFile, 'w') as fp:
        pass
