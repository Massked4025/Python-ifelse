with open("python17.txt", "w") as file:
    file.write("Hi, I am Aryan Mansoor. I am 13 years old.")
file.close()

with open("python17.txt", "r") as file1:
    data = file1.readlines()
    for line in data:
        word = line.split()
        print(word)

file.close()