# we create a set using a {} 
# A set is a collection which is unordered, unchangeable*, and unindexed.
a={"hello","hi","Bonjour","Halo","Namaskaram"}
print(a)
print(len(a))   # length of a set

# duplicates are not allowed in sets
b={1,1,2,3,4,3,4,6,4,6,8,6}
print(b)   # this will return a set by eliminating all the duplicates

# a set will take "True" and "1" as the same value and consider them as duplicates
c={1,2,3,4,5,True}
print(c)

# same to "False" and "0" also
d={0,1,2,3,4,5,False}
print(d)

#the set() constructor
e=set(("hello",1,2,3))   # we can also construct a set using set() constructor but should give double brackets
print(e)


#ACCESSING SET ITEMS

# as there are no indexes in sets we can access them through looping
a={"hello","hi","Bonjour","Halo","Namaskaram"}
for i in a:
    print(i)

# by using the "in" and "not in" keywords
a={"hello","hi","Bonjour","Halo","Namaskaram"}
if "hello" in a:
    print("The set is complete")

print("Namaskaram" in a)   
                            # this will just return true or false
print("bonsoir" not in a)

