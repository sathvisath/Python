# Accessing list items
x=[1,"apple",2,"banana",3,"cherry"]
print(x,"\n")

#we access the list items using indexing
print(x[3])
print(x[-1])  #this is known as reverse indexing
print(x[2:5]) #indexing or accessing the items b/w this range
print(x[-2:-5])   #this will result an empty list "[]". 
# If "start" comes after "end" in the list (left to right), the result is an empty list unless a negative step is used.

#so we have to write it like this 
print(x[-2:-5:-1])  #This tells Python to move backward while slicing.

print(x[-5:-2])  #we can also write like this , but will a different output from the above

#check if item exist
b=["house","car","money","fame"]
if "money" in b:
    print("Yes, you are successful now")
if "defame" in b:
    print("You are not successful")


