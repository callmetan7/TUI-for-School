import os
import shutil


def fileOrganiserOV():
    source_folder = r"C:\Users\Tanuj\Downloads\\"

    # Defining the folder Where the files will go to
    exeDestination = r"C:\Users\Tanuj\Desktop\Files\Exe\\"
    picDestination = r"C:\Users\Tanuj\Desktop\Files\Pictures\\"
    docDestination = r"C:\Users\Tanuj\Desktop\Files\Word Documents\\"

    # Adding all the files in a list using the listdir method from the module os
    folder = os.listdir(source_folder) 
    for file_name in folder:
        # Listing the extension for each of the files
        ext = os.path.splitext(file_name)[-1].lower()
        source = source_folder + file_name
        if len(folder) == 0:
            print("> No files in specified directory")
        if ext == ".exe":
            exeDestination + file_name
            shutil.move(source, exeDestination)
            print(f"Moved: {file_name} to {exeDestination}")
        elif ext == ".png" or ".jpg" or ".jpeg" or ".jfif":
            picDestination + file_name
            shutil.move(source, picDestination)
            print(f"Moved: {file_name} to {picDestination}")
