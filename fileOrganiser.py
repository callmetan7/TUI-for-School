import os
import shutil
from termcolor import colored

def fileOrganiserOV():
    source_folder = r"C:\Users\Tanuj\Downloads\\"

    # Defining the folder Where the files will go to
    defaultDesitnation = colored(r"C:\Users\Tanuj\Desktop\Files\\", 'red')
    exeDestination = colored(r"C:\Users\Tanuj\Desktop\Files\Exe\\", 'red')
    picDestination = colored(r"C:\Users\Tanuj\Desktop\Files\Pictures\\", 'red')
    docDestination = colored(r"C:\Users\Tanuj\Desktop\Files\Word Documents\\", 'red')
    print(defaultDesitnation, exeDestination, picDestination, docDestination)
    # Adding all the files in a list using the listdir method from the module os
    folder = os.listdir(source_folder)
    for file_name in folder:
        # Listing the extension for each of the files
        ext = os.path.splitext(file_name)[-1].lower()
        source = source_folder + file_name
        if ext == ".exe":
            exeDestination + file_name
            shutil.move(source, exeDestination)
            print(f"Moved: {colored(file_name, 'blue')} to {exeDestination}")
        elif ext == ".png" or ext == ".jpg" or ext == ".jpeg" or ext == ".jfif":
            picDestination + file_name
            shutil.move(source, picDestination)
            print(f"Moved: {colored(file_name, 'blue')} to {picDestination}")
        elif ext == ".doc" or ext == ".docx":
            docDestination + file_name
            shutil.move(source, docDestination)
            print(f"Moved: {colored(file_name, 'blue')} to {docDestination}") 
        else:
            shutil.move(source, defaultDesitnation)
            print(f"Moved: {colored(file_name, 'blue')} to {defaultDesitnation}")