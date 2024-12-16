class Person(object):
    def __init__(self, name, idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)

class employee(Person):
    def __init__(self, name, idnumber, salary, post):
        self.salary=salary
        self.post=post
        Person.__init__(self, name, idnumber)

a = employee("Aryan", 24857301, 15000, "WebDeveloper")
a.display()

#Super Method

class Person():
    def __init__(self, fname, lname):
        self.fname=fname
        self.lname=lname
    def display(self):
        print(self.fname, self.lname)

class student(Person):
    def __init__(self, fname, lname, year):
        self.year=year
        super().__init__(fname, lname)

b = student("Joseph", "Khan", 2021)
b.display()
print(b.year)

#Abstraction

from abc import ABC

class Animal(ABC):
    def move(self):
        pass

class Human(Animal):
    def move(self):
        print("I can walk and run")

class Snake(Animal):
    def move(self):
        print("I can slither")

class Dog(Animal):
    def move(self):
        print("I can bark")

class Lion(Animal):
    def move(self):
        print("I can roar")

H = Human()
H.move()

S = Snake()
S.move()

D = Dog()
D.move()

L = Lion()
L.move()