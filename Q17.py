#Create a program that checks if a given number is divisible by both 5 and 7 using the modulo operator.
number  = int (input("Enter a Number:"))
if number % 5 == 0 & number % 7 == 0 :
    print(number,"Is divisible by both 5 and 7")
else:
    print(number,"Is not divisible by 5 and 7")
