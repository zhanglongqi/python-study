import os;
import sys;

filePathSrc = "D:\\Books\\"  # Path to the folder with files to convert
for root, dirs, files in os.walk(filePathSrc):
    for fn in files:
        if fn[-4:] == '.txt':  # Specify type of the files
            print(fn)
            notepad.open(root + "\\" + fn)
            console.write(root + "\\" + fn + "\r\n")
            notepad.runMenuCommand("Encoding", "Convert to UTF-8")
            notepad.save()
            notepad.close()
