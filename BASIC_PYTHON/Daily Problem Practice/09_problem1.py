#Write a Python Program to calculate your Body Mass Index.
"""
Body Mass Index (BMI) is a measure of body fat based on an individual's weight and height.
It is commonly used as a screening tool to categorize individuals into different weight status categories
such as underweight, normal weight, overweight, and obesity.
"""
weight=float(input("Enter your weight : "))
height=float(input("Enter your height in meter : "))
def bmi(weight,height):
    return round(weight/height**2,2)
BMI=bmi(weight,height)

print(f"Your Body Mass Index is : {BMI}")
if(BMI <= 18.5):
    print("Low Weight")
elif(BMI>=18.5 and BMI <=24.9):
    print("Normal Weight")
elif(BMI>25 and BMI<=29.29):
    print("Over Weight")
else:
    print("Too much weight")
