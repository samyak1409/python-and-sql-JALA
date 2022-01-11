# script to move the files to the folders

from os import chdir, listdir, mkdir
from shutil import move

chdir('Python PDFS')

for file in listdir():
    print(file)
    folder = file.split('.', maxsplit=1)[0]
    print(folder)

    mkdir(folder)
    move(src=file, dst=f"{folder}\\{file}")
