print(bool(10>9))    #here the condition is true

print(bool(10<9))    #here the condition is false

print(bool("abc"))   
print(bool(123))
print(bool(["apple","banana",1]))  #all of these will be true except number "0"

print(bool(0))   #this will output false ,in boolean we will assume that 0 is false and 1 is true, so does python

#also empty lists,sets,tuples and dictionaries , None, False will be false
print(bool([])) 
print(bool(())) 
print(bool({})) 
print(bool(False))
print(bool(None))
print(bool(""))   

def myfunc():
    return 12        #will only return False if the value is 0
print(bool(myfunc()))

# You can execute code based on the Boolean answer of a function:

def myfunc():
    return 0
if myfunc():
    print("Yes!!")
else:
    print("Oh nooo :)")    #will print the else statement cause 0 returns false

# isinstance() function, which can be used to determine if an object is of a certain data type:

x=212
print(isinstance(x,int))    #will output only true or false
