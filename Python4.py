num=17
print("TABLE OF 17")
for i in range(1,11):
    mult = num*i
    print(f"17 x {i} = {mult}")

# Star Patterns
rows=int(input("Enter the number of rows :"))
for i in range(0, rows):
    for j in range(0, i+1):
        print("*", end=" ")

    print("\n")

# While loop
num=1
sum=0
while(num<=10):
    sum=sum+num
    num=num+1

print("Total sum is :", sum)

# Checking prime numbers
num=int(input("Enter the number to be checked :"))
flag=False
if num>1:
    for i in range(2, num):
        if num %i ==0:
            flag=True
            break
if flag:
    print("The number is not prime")

else:
    print("Number is prime")