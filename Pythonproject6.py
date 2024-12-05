class robot:
    species = "robot"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sing(self, song):
        return f"{self.name} sings {song}"

metal = robot("Robotin", 2)

print(f"Robotin is a {metal.species}")

print(f"{metal.name} is {metal.age} years old")

print(metal.sing("Country Road, Take me home."))