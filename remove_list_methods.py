# remove() method
a=['hello','hi','halo','bonjour','namaskaram']
a.remove('namaskaram')
print(a)

# pop() method
a=['hello','hi','halo','bonjour','namaskaram']
a.pop(1)   #to pop specific element using the index number
print(a)

a.pop()    # to pop the last element 

# clear() method
a=['hello','hi','halo','bonjour','namaskaram']
a.clear()  # this is used to clear all the items in a list and will return and empty list
print(a)

# del() method
a=['hello','hi','halo','bonjour','namaskaram']
del a[3]   # here we declare differntly compared to the above methods
print(a)

del a   # for deleting the entire list 

