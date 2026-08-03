"""
1. Perimeter Calculation Program
Problem Statement:
Design a program that calculates the perimeter of different geometric shapes: triangle,
rectangle, and circle. The user should select the shape and provide the required dimensions.
Input:
 Choice of shape
 Triangle: three sides (a, b, c)
 Rectangle: length and breadth
 Circle: radius
Output:
 Perimeter of the selected shape
Example:
Input: Rectangle → length = 5, breadth = 3
Output: Perimeter = 16
Constraints:
 All inputs must be positive numbers
"""

def triangle(a,b,c):
    result = a+b+c
    return result
def rectangle(length,breadth):
    result = 2*(length+breadth)
    return result
def circle(radius):
    result = 3.14*(radius**2)
    return result

user = int(input("Enter Your Choice (1/2/3) : "))

match user :
    case 1 :
        a = int(input("Enter A : "))
        b = int(input("Enter B : "))
        c = int(input("Enter C : "))
        result = triangle(a,b,c)
        print("Perimeter of Triangle : ",result)
    case 2 : 
        length = int(input("Enter length : "))
        breadth = int(input("Enter breadth : "))
        result = rectangle(length,breadth)
        print("Perimeter of rectangle : ",result)
    case 3 :
        r = int(input("Enter radius of circle : "))
        result = circle(r)
        print("Perimeter of circle : ",result)
    case _ :
        print("Invalid Choice!!")
