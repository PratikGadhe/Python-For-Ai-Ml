# Write a Python Program to Check Leap Year.
year=int(input("Enter Year : "))
# year % 100 gives 00 remainder then its a century year like 1000,2000..
# therefore year % 400 == 0 then it is leap year 
if(year%400 == 0 and year%100 == 0 ):
    print(f"{year} is a leap year !")
    # if above condition is not true which means above statement is not a century year
elif(year%4 == 0 and year%100 != 0):
    print(f"{year} is a leap year !")
else:
    print(f"{year} is not a leap year !")