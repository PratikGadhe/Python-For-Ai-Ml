# local variable : which is define inside the function and can be acess inside the function only
# global variable : which is define outside the function and can be access throughout the program
def hello():
    print("Hello world")
    x=0 #this is local variable
    print(a)
    return x;
a=15 #this is global variable
def world():
    # to change the value of global variable we use Global <variable_name>
    global y
    y=10
    return y
y=0
print(world())
hello()