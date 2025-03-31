# ADD ITEMS TO LIST

# add() method
a={"hello","hi","Bonjour","Hallo","Namaskaram"}
a.add("Hola")
print(a)

# To add items from another set into the current set, use the "update()" method.
a={"hello","hi","Bonjour","Hallo","Namaskaram"}
c={1,2,3,4,5,True}
a.update(c)   # we can also say to join both the sets
print(a)

# we can also use update() method using a set and other can be any iterable object (tuples, lists, dictionaries)
a={"hello","hi","Bonjour","Hallo","Namaskaram"}
b=[1,2,3,4]
a.update(b)
print(a)


#REMOVE ITEMS FROM A LIST

# remove() method
a={"hello","hi","Bonjour","Hallo","Namaskaram"}
a.remove("Bonjour")   #If the item to remove does not exist, remove() will raise an error.
print(a)

# discard() method
a={"hello","hi","Bonjour","Hallo","Namaskaram"}
a.discard("hello")    # If the item to remove does not exist, discard() will NOT raise an error.
print(a)

# pop() method
#this method will remove a random item from a list so we don't know what item will be removed.
a={"hello","hi","Bonjour","Hallo","Namaskaram"}
a.pop()
print(a)   # here it popped the item "Bonjour" and if you execute it again it will remove another item 

# clear() method
a={"hello","hi","Bonjour","Hallo","Namaskaram"}
a.clear()
print(a)   # will just return an empty set

# del() method
a={"hello","hi","Bonjour","Hallo","Namaskaram"}
del a
print(a)   # will rise an error as the set is deleted

