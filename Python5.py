def intro(x):
    print("Good Morning, Afternoon, or Night, my name is ",x)

name=(input("Enter your name: "))
intro(name)

# Factorial
def factorial(n):
    if n==1:
        return n
    else:
        return n*factorial(n-1)
    
num = int(input("Enter the number"))
if num<0:
    print("We can not calculate the factorial of negative numbers")
elif num==0:
    print("The factorial of 0 is 1")
else:
    print("The factorial is: ", factorial(num))

# Calculator
def add(x, y):
    return x+y

def subtract(x, y):
    return x-y

def multiplication(x, y):
    return x*y

def division(x, y):
    return x/y

num1 = int(input("Enter the value of No. 1"))
num2 = int(input("Enter the value of No. 2"))
print("Addition", add(num1, num2))
print("Subtraction", subtract(num1, num2))
print("Multiplication", multiplication(num1, num2))
print("Division", division(num1, num2))