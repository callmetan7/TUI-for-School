import os
import shutil


def NewFile():
    fileName = input("  > What is the file name? ")

    # The first variable should be the absolute path of the file you want to create. The second variable should be the extension eg. ".docx"
    file = r"#" + fileName + "#"
    with open(file, 'w') as fp:
        pass
