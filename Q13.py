#Write a Python program to find the largest among three numbers using boolean expressions.
num1 = int(input("Enter first number:"))
num2 = int(input("Enetr second number:"))
num3 = int(input("Enter third number:"))
if(num1 > num2):
    print(num1,"is Largest")
elif(num2 > num3):
    print(num2,"is Largest")
else:
    print(num3,"is Largest")