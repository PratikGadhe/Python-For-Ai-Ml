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
    result = a + b + c
    return result
def rectangle(l1,b):
    result = 2 * (l1 + b)
    return result
def circle(r):
    result = 2 * 3.14 * r
    return result

user = int(input("Enter Your Choice (1 = Triangle /2 = Rectangle /3 = Circle) : "))
match user :
    case 1 :
        a = int(input("Enter Side A : "))
        b = int(input("Enter Side B : "))
        c = int(input("Enter Side C : "))
        result = triangle(a,b,c)
        print("Perimeter of triangle : ",result)
    case 2 :
        length = int(input("Enter length : "))
        breadth = int(input("Enter breadth : "))
        result = rectangle(length,breadth)
        print("Perimeter of triangle : ",result)
    case 3 :
        radius = int(input("Enter radius of circle : "))
        result = circle(radius)
        print("Perimeter of Circle : ",result)
    case _:
        print("User Enteres wrong choice!!")
        