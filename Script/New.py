import os

path = "G:\\My Drive\\_Documents\\_Read\\_Paper\\Agricultural and Forest Meteorology"

for (root,dir,file) in os.walk(path):
    for file_S in file:
        if file_S != "desktop.ini":
            print(file_S)