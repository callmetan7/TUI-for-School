import os
import shutil

# Defininf the folder in which we move the files from
source_folder = r"C:\Users\Tanuj\Downloads\\"

#Defininf the folders where he files will go to
exeDestination = r"C:\Users\Tanuj\Desktop\Files\Exe\\"
picDestination = r"C:\Users\Tanuj\Desktop\Files\Pictures\\"

# Adding all the files in a list using the listdir method from the module os
for file_name in os.listdir(source_folder):
    # Listing the extension for each of the files
    ext = os.path.splitext(file_name)[-1].lower()
    source = source_folder + file_name
    if ext == ".exe":
        exeDestination + file_name
        shutil.move(source, exeDestination)    
        print(f"Moved: {file_name} to {exeDestination}")
    elif ext == ".png" or ".jpg" or ".jpeg" or ".jfif":
        picDestination + file_name
        shutil.move(source, picDestination)
        print(f"Moved: {file_name} to {picDestination}")