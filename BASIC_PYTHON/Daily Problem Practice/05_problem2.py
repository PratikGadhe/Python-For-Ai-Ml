# Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations.
def addition(x,y):
    return x+y
def subtraction(x,y):
    return x-y
def multiplication(x,y):
    return x*y
def division(x,y):
    return x/y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True : 
    choice =input("Enter Your Choice (1/2/3/4): ")
    if choice in ('1','2','3','4'):
        n1=int(input("Enter number 1 :"))
        n2=int(input("Enter number 2 :"))
        if(choice == '1'):
            print(f"addition {n1}+{n2}={addition(n1,n2)}")
        elif(choice == '2'):
            print(f"Subtraction {n1}-{n2}={subtraction(n1,n2)}")
        elif(choice == '3'):
            print(f"Multiplication {n1}*{n2}={multiplication(n1,n2)}")
        elif(choice == '4'):
            print(f"Division {n1}/{n2}={division(n1,n2)}")
        next_calculation=input("Do You Want to continue ? (yes/no) : ")
        if(next_calculation == 'yes'):
            continue
        elif ( next_calculation == 'no'):
            break
        else:
            print("INVALID SYNTAX")
            break
    else:
        print("INVALID CHOICE")
        print("PLEASE ENTER VALID CHOICE (1/2/3/4)")
