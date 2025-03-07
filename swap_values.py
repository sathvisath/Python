# swapping values of two variables

x=int(input("Enter a value: "))
y=int(input("Enter a value: "))
print("Before Swapping x value is: ",x)
print("Before Swapping y value is: ",y)

#initialize a temporary variable
temp = x    #now we store the value of 'x' in the 'temp' variable
x=y         #now x is empty so we store y value in x
y= temp     #now y is empty so we store the value of temp in y

print("After Swapping x value is: ",x)
print("After Swapping y value is: ",y)