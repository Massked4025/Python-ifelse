file = open("Counter.txt", 'r')
Counter = 0
Content = file.read()
Colist = Content.split("\n")
for i in Colist:
    if i:
        Counter += 1
print(Counter)

file1 = input("Enter the name of the first file")
file2 = input("Enter the name of the second file")

f1 = open(file1, "a")
f2 = open(file2, 'r')

f1.write(f2.read())

f1.close()
f2.close()