# Define a function called hypotenuse that calculate the length of hypotenuse of right triangle when the other two slide are given . Use this function in a program to length of the hypotenuse for each of the following triangle
import math
def hyp(a,b):
    c=a**2+b**2
    return math.sqrt(c)
for i in range (1,4):
b=int(input("Enter the slide of triangle"))
a=int(a)
b=int(b)
x=hyp(a,b)
print("hyptonuse of triangle is ",x)