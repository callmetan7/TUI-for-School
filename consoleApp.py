import os
import shutil

from fileOrganiser import fileOrganiserOV
from NewFile import *

running = True
while running:
    userCommand = input("> ")
    if userCommand == "moveFile":
        source_folder = input(" > What is the source folder? ")
        if source_folder == "ovFileMove":
            fileOrganiserOV()
    if userCommand == "newFile":
        userCommand = input(" > Where would you like to create the file? ")

        # This is a command that will run the function from the newFile.py file
        if userCommand == "ovOneDrive":
                NewFile()
    if userCommand == "quit":
        running = False
        break
