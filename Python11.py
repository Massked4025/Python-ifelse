class student:
    grade = 8
    name = "Aryan"
    def intro(self):
        print("Hi, I am a student")
    def details(self):
        print("My name is ", self.name)
        print("I am in grade ", self.grade)

ob = student()
ob.intro()
ob.details()

#Parrot

class parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sing(self, song):
        return f"{self.name} sings {song}"
    def dance(self, dance):
        return f"{self.name} dancing {dance}"

blue = parrot("Rio", 9)
red = parrot("Rico", 10)

print(f"Rio is a {blue.species}")
print(f"Rico is also a {red.species}")

print(f"{blue.name} is {blue.age} years old")
print(f"{red.name} is {red.age} years old")

print(blue.sing("Happy"))
print(red.dance("Joy"))