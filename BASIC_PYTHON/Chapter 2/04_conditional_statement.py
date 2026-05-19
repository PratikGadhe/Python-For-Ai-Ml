#if elif else
signal=input("Enter signal colour : ")
if(signal=="Red"):
    print("Stop!")
elif(signal == "Yellow"):
    print("Wait!")
elif(signal == "Green"):
    print("Go!")
else:
    print("Light is broken !")

#difference in if and elif is : if condition will check each statement 
# where else : elif statement will check condition if IF statement is False

#example

a=5
if(a>2):
    print("Number is greater than 2")
elif(a>3):
    print("Number is greater than 3")

#here each and every condition is checked 