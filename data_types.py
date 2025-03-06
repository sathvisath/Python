# frozenset
#declaration of frozenset. A frozenset can be declared in set,tuple,list
a=frozenset([1,2,3,4]) #list
b=frozenset((2,3,4,5,6)) #tuple
x=frozenset({"Apple","Banana","Orange"}) #set
#x.add("laddu") this will return an error cause frozenset is immutable
print(x) 
    #operations on frozenset
fs1=({1,2,3,4,5,0,2})
fs2=({9,4,2,6,4,7,8}) #in the output the numbers are sorted automatically in ascending order
print(fs1)
print(fs2)
print(fs1&fs2) #intersection - common element
print(fs1-fs2) 
print(fs1|fs2) #union - combining teo sets 



# range datatype
y=range(5)
print(y)
print(type(y))



#dictionary
nums_fruits={1:"Apple",2:"Banana",3:"Orange"}
print(nums_fruits)
     #operations on dict
nums_fruits[1]="Lichee" #to update a value in the dict
print(nums_fruits)
#to access the elements of a dict
print(nums_fruits[1])
print(nums_fruits.get(3)) #carefully observe the brackets used for these different commands to access the elements



#complex - it is a datatype for numbers
l=3j #complex numbers are only written with "j" 
print(l)
print(type(l))


#converting from one datatype to another

#int to string -  if you want to convert "string to int" the "string" must contain "only numbers"
x=int(input()) #take input from user
y=str(x)
print(y)
print(type(y))
print(type(x))

#int  to complex - but we cannot convert complex to int
xx=int(input())
y=complex(xx)
print(y) 
