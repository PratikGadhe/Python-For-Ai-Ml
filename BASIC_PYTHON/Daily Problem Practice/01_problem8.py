# Write a Python program to solve quadratic equation
"""
The standard form of a quadratic equation is: (ax^2+bx+c=0)

where
a, b and c are real numbers and
a≠0

The solutions of this quadratic equation is given by:
-b+-(b^2 - 4ac)^2/2a
"""
import math
a=int(input("Enter A : "))
b=int(input("Enter B : "))
c=int(input("Enter C : "))

x=(math.pow(b,2)-(4*a*c))
if(x>0):
    #roots are real and distinct
    root1=(-b-math.sqrt(x))/(2*a)
    root2=(-b+math.sqrt(x))/(2*a)
    print(f"roots are x={root1},y={root2}")

elif(x==0):
    #real and repeated 
    root=-b/(2*a)
    print(f"Roots = {root}")
else:
# Complex roots
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(abs(x)) / (2*a) 
    print(f"Root 1: {real_part} + {imaginary_part}i") 
    print(f"Root 2: {real_part} - {imaginary_part}i")