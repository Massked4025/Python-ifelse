file = open('Pythonprojectfile.txt')

print(file.read())

file.close()


file = open('Pythonprojectfile.txt', 'w')
file.write("John: I am John. I come from Colorado, United States of America. I am in Class 8 and my favourite subject is art Richard: I am Richard. I come from Manchester, England. I am in Class 8, and my favourite subject is Social Science Willy: I am Willy. I come from Toronto, Canada. I am in class 9, and my favourite subject is Wood cutting.")
file.close()


file = open('Pythonprojectfile.txt', 'a')
file.write("Abby: I am Abby. I come from Dublin, Ireland. I am in class 8, and my favourite subject is history.")
file.close()