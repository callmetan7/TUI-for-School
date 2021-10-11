# This file will be imported to every single file to import the important variables that every other file will use
import os

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