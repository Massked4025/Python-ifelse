x = int(input("enter the number: "))
y = int(input("total no of digits: "))
sum=0
temp = x
while(temp>0):
    digits = temp%10
    sum += digits**y
    temp = temp//10

if sum == x:
    print("it is an armstrong number")
else:
    print("it is not an armstrong number")