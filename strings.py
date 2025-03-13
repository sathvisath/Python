# like c and c++ strings are just array of unicode charactecrs in python.
#in python we dont have datatype for character so we just access single character using indexing

a="Hello" #strings are defined in double qoutes
print(a[1]) #always remember that indices start with 0 

a="Hello World"   #here the space is also counted as one index 
print(a[5])   #this statement will return "space" cause it is the 5th index
#multiline strings

b = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(b)    #in the result, the line breaks are same as given in the code.

#string length
print(len(a))   #we use "len()" function


#to check if a certain string or word is present in the given text
text="I am very happy today. I started my day peacefully."
print("happy" in text )   #this will result true if the string is present in the text or else false
#using if statement
if "started" in text:
    print("'started' word is there in the given text")



#to check if a certain string or word "is not" present in the given text
txt="Hello my name is Sathvika.Nice to meet you."
print("Sathvi" not in text)   #this will return true if not present in txt or else false
#using if statement
if "." not in txt:
    print('"Sathvi" is not present in the given text')


#slicing strings
 #you can return a range of characters 
a="Hello World"
print(a[2:7])   #this will return characters from 2 index to 6th only, it takes 2:7 means it will print till 6th
 #slicing from start
print(a[:5])    #this will return characters from start to 5th(means till 4th index)
 #similarly slice to the end
print(a[2:])    #this will return characters from 2nd to last index

#negative indexing -- important 
 #here if we have to access from the back we use -1 -2 etc 
 #it goes like !=0,d=-1,l=-2......H=-11
b="Hello World!"
print(b[-10:-2])  #here the ranging limit is reverse it will print only upto 9th




