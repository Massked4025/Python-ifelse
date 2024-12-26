file = open('Python15.txt')

print(file.read())

file.close()

#Write mode

file = open('Python15.txt', 'w')
file.write("Hello!")
file.close()

#Append Mode

file = open('Python15.txt', 'a')
file.write("Goodbye!")
file.close()