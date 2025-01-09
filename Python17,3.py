outputfile = open("New_file.txt", "w")
inputfile = open("Python16.txt", "r")

lineseen = set()
for line in inputfile:
    if line not in lineseen:
        outputfile.write(line)
    lineseen.add(line)

outputfile.close()
inputfile.close()

#appending two files

with open("Python16.txt", "r") as fp:
    data1 = fp.read()

with open("New_file.txt", "r") as fp:
    data2 = fp.read()

data1 += "\n"
data1 += data2

with open("emptyfile.txt", "w") as fp:
    fp.write(data1)

fp.close()