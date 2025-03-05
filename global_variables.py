"""global variables are the variables that are declared outside the function .
they can be used inside a function or outside also.
"""
x="awesome"

def myfunc():
    x="hello"
    print("Python is "+x) #here the x refers to x="hello".
myfunc() #calling a function

print("Python is "+x) #here x refers to x="awesome".

# we can also use a global variable inside a function
def myfunc2():
    print("I am "+x) #here x refers to the global variable x="awesome"
myfunc2()

# we can also declare a global variable inside a function using the 'GLOBAL' keyword
def myfunc3():
    global x
    x="World" # we have to assign the value in the next line after declaring the variable is global
    print("Hello "+x)
myfunc3()
print("Welcome to my "+x) #here x="World" cause we declared it as global
