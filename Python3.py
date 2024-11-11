num=int(input("Enter a number to be checked: "))

if num%2==0:
    print("Number is Even")

else:
    print("Number is Odd")


#BMI CALCULATOR
height=float(input("Enter your height, Whole number for foot and decimal for inches: "))
weight=float(input("Enter your weight in kg: "))

BMI=weight/(height/100)**2

if BMI <= 18.4:
    print("You are underweight")
elif BMI <= 24.9:
    print("You are healthy")
elif BMI <= 29.9:
    print("You are overweight")
else:
    print("You are obese")

#Double Check Number
n=int(input("Enter the number to be checked: "))

if n>31:
    print("Number is greater than 31")
    if n%2==0:
        print("Number is Even")
    else:
        print("Number is Odd")

else:
    print("Number is less than 31")

#DATE-TIME-CALENDER-MODULE
import datetime

currenttime=datetime.datetime.now()

print("Current Time:" , currenttime)

import calendar

print(calendar.calendar(2024))