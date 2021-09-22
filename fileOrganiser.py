import os
import shutil
from termcolor import colored
from colors import colors

def fileOrganiserOV():
    source_folder = r"C:\Users\Tanuj\Downloads\\"
    # Defining the folder Where the files will go to
    defaultDesitnation = r"C:/Users/Tanuj/Desktop/Files/"
    exeDestination = r"C:\Users\Tanuj\Desktop\Files\Exe\\"
    picDestination = r"C:\Users\Tanuj\Desktop\Files\Pictures\\"
    docDestination = r"C:\Users\Tanuj\Desktop\Files\Documents\\"
    pdfDestination = r"C:\Users\Tanuj\Desktop\Files\PDF\\"
    # Adding all the files in a list using the listdir method from the module os
    folder = os.listdir(source_folder)
    for file_name in folder:
        # Listing the extension for each of the files
        ext = os.path.splitext(file_name)[-1].lower()
        # Making an absolute path for the file 
        source = source_folder + file_name
        # Checking through a list of extensions and moving them to the folder using shutil.move
        if ext == ".exe":
            exeDestination + file_name
            shutil.move(source, exeDestination)   
            print(f"Moved: {file_name} to {exeDestination}")
        elif ext == ".doc" or ext == ".docx" or ext == ".xlsx":
            docDestination + file_name
            shutil.move(source, docDestination)
            print(f"Moved: {file_name} to {docDestination}")
        elif ext == ".png" or ext == ".jfif" or ext == ".jpeg" or ext == ".jpg":
            picDestination + file_name
            shutil.move(source, picDestination)
            print(f"Moved: {file_name} to {picDestination}")
        elif ext == ".pdf":
            pdfDestination + file_name
            shutil.move(source, pdfDestination)
            print(f"Moved: {file_name} to {docDestination}")
        else:
            shutil.move(source, defaultDesitnation)
            print(f"Moved: {file_name} to {defaultDesitnation}")
fileOrganiserOV()