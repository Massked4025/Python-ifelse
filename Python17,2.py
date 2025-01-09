newfile = open("New_file.txt", "x")
newfile.close()

import os
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("The file does not exist")

myfile = open("myfile.txt", "w")
myfile.write("Hello Pakistan")
myfile.close()

os.remove("Pythonprojectfile.txt")