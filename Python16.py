file = open("Python16.txt", 'r')
print(file.read(8))
file.close()

file = open("Python16.txt", 'r')
print(file.readline())
file.close()

file = open("Python16.txt", 'r')
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file = open("Python16.txt", 'r')
for line in file:
    print(line)
file.close()