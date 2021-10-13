# This file will be imported to every single file to import the important variables that every other file will use
import os

desktopFolder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
downloadsFolder = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Downloads')

filesFolder = desktopFolder + r"/Files"
exeFolder = filesFolder + r"/EXE"
picFolder = filesFolder + r"/Pictures"
docFolder = filesFolder + r"/Docs"
othFolder = filesFolder + r"/Other files"

schoolFolder = desktopFolder + r"/School"
scienceFolder = schoolFolder + r"/Science"
englishFolder = schoolFolder + r"/English"
historyFolder = schoolFolder + r"/History"

white =  "\033[1;37;40m"
cyan = "\033[1;49;96m"
purple = "\033[1;49;95m"
green = "\033[1;32;40m"
red = "\u001b[31m"
blue = "\u001b[34m"