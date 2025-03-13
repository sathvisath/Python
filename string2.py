#modifying strings


a="Hello World"
print(a.upper())   #returns the string in uppercase
print(a.lower())   #returns the string in lowercase
print(a.capitalize())   #returns the string with only 1st letter  as capital letter
print(a.casefold())     #returns the string in lowercase(same as lower())

#remove white space
x=" Happy Birthday! "
print(x.strip())      #will remove whitespace at the beginning and the end 


#replace string
b="Thank you"
print(b.replace("T","K"))   #here T is replaced with K


#split string
y="No Thank You"
print(y.split())
