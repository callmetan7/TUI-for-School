import os
import shutil

source_folder = r"C:\Users\Tanuj\Downloads\\"
exeDestination = r"C:\Users\Tanuj\Desktop\Files\Exe\\"
picDestination = r"C:\Users\Tanuj\Desktop\Files\Pictures\\"
# fetch all files
for file_name in os.listdir(source_folder):
    # construct full file path
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