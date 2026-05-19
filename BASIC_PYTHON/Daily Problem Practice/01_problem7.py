# Write a Python program to display calendar.
import calendar
year=int(input("Enter Year : "))
Month=int(input("Enter Month : "))
cal=calendar.month(year,Month)
print(cal)
