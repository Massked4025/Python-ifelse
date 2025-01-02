file = open("Python16.txt", 'r')
file1 = open("Python16updated2.txt", 'w')

Content = file.readlines()
type(Content)
for i in range(1, len(Content)+1):
    if (i % 2 != 0):
        file1.write(Content[i-1])
    else:
        pass

file.close()
file1.close()