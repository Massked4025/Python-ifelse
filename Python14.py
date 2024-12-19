class cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"My name is {self.name}, I am {self.age} years old")
    def sound(self):
        print("Meow")

class dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        print(f"My name is {self.name}, I am {self.age} years old")
    def sound(self):
        print("Bark")

ob1=cat("Mittens", 7)
ob2=dog("Sam", 3)

for animal in (ob1, ob2):
    animal.info()
    animal.sound()

#Encapsulation

class computer:
    def __init__(self):
        self.__maxprice=2390
    def sell(self):
        print(f"The selling price is: {self.__maxprice}")
    def setprice(self, price):
        self.__maxprice=price

ob3=computer()
ob3.sell()

ob3.__maxprice=2150
ob3.sell()

ob3.setprice(2050)
ob3.sell()