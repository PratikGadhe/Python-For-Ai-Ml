# WAF to convert USD to INR.
dollar=int (input("Enter number of dollars : "))
def conversion(dollar):
    INR= dollar*83
    return INR
print(dollar,"$ in Indian Ruppes is",conversion(dollar),"rs")