import os
import shutil

from fileOrganiser import fileOrganiserOV
from oneDriveOV.makeNew.engNewFile import engNewFile

running = True
while running:
    userCommand = input("> ")
    if userCommand == "moveFile":
        source_folder = input(" > What is the source folder? ")
        if source_folder == "ovFileMove":
            fileOrganiserOV()
    if userCommand == "quit":
        running = False
        break
