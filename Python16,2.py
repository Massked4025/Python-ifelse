file = open("Python16.txt", 'r')
file1 = open("Python16updated.txt", 'w')

for line in file.readlines():
    if not (line.startswith("Coding")):
        print(line)
        file1.write(line)

file.close()
file1.close()