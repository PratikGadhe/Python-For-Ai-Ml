"""
wap to calculate the area of triangle , rectangle , circle
"""

def triangle(base , height):
    area = 0.5 * base * height
    return area
def circle(radius):
    area = 3.14 * radius * radius
    return area
def rectangle(length , breadth):
    area = length * breadth
    return area

n = int(input("Enter Your Choice (1:traingle / 2:Rectangle / 3:Circle) : "))

if(n == 1):
    base = int(input("Enter base of triangle : "))
    height = int(input("Enter height of triangle : "))
    result = triangle(base , height)
    print("Area of triangle : ",result)
elif(n == 2):
    length = int(input("Enter length : "))
    breadth = int(input("Enter Breadth : "))
    result = rectangle(length , breadth)
    print("Area of Rectangle : ",result)
elif(n == 3):
    radius = int(input("Enter Radius of Circle : "))
    result = circle(radius)
    print("Enter Radius of Circle : ")
    print("Area of Circle : ",result)
else :
    print("User Entered Wrong Choice!!!")
    