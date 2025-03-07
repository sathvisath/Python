#to check if a given number is even or odd 

x=int(input("Give a value: "))

#here we will use if/else condition
if (x%2==0):    #here we used modulud(%) operator which will give us the remainder after division
    print(x,"is even number.")
else:
    print(x,"is odd number.")
