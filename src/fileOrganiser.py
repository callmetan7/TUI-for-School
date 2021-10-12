import os
import shutil
from src.globalVariables import *

def fileOrganiser(path):
    for file in os.listdir(path):
        # Were going to be seperating the file name and the extension in 2 variables for later use
        fileName, fileExt = os.path.splitext(file)
        if fileExt == ".exe":
            shutil.move(path + f"/{file}" , exeFolder)
            print(f"Moved: {fileName} to {exeFolder}")

        elif fileExt == ".png" or fileExt == ".jpeg" or fileExt == ".jpg" or fileExt == ".png":
            shutil.move(path + f"/{file}", picFolder)
            print(f"Moved: {fileName} to {picFolder}")

        elif fileExt == ".doc" or fileExt == ".docx" or fileExt == ".pdf":
            shutil.move(path + f"/{file}" , docFolder)
            print(f"Moved: {fileName} to {docFolder}")

    
