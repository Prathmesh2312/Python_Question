#Write a Python program to swap the values of two variables without using a temporary variable.

#Method 1 :- Using simple built-in method 

x = 5
y = 3
print("Before swapping")
print("value of X:",x,"Value of Y:",y)
x, y = y ,x
print("After swapping")
print("Value of X:",x,"Value of Y:",y)

#Method 2 :- Using Bitwise XOR operator 
#This method only works for integers

p = 5
q = 10
print("Before Swapping")
print("value of P:",p,"value of Q:",q)
p ^= q
q ^= p
p ^= q
print("After Swapping")
print("Value of P:",p,"Value of Q:",q)
