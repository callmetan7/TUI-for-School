import os
import shutil
import json

desktopFolder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
downloadsFolder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')

filesFolder = desktopFolder + r"/Files"
schoolFolder = desktopFolder + r"/School"

scienceFolder = schoolFolder + r"/Science"
englishFolder = schoolFolder + r"/English"
historyFolder = schoolFolder + r"/History"

exeFolder = filesFolder + r"/EXE"
picFolder = filesFolder + r"/Pictures"
docFolder = filesFolder + r"/Docs"
othFolder = filesFolder + r"/Other files"

def startup():
    foldersToMake = [
        schoolFolder,
        scienceFolder,
        englishFolder,
        historyFolder,
        filesFolder,
        exeFolder,
        picFolder,
        docFolder,
        othFolder,
    ]

# This will make the folders but also check if the folders have already been made. If they havent been made it will make them. Since the entire app dependeds
# on these folders existing it's very hard to operate without them.
    try:
        for folder in foldersToMake:
            os.makedirs(folder)
    except Exception as check:
        pass

