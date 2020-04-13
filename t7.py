#set and frozen set in python

'''
set is unordered, mutable collection of unique elemets

forezen set is unordered, immutable collection of unique elements
'''

my_set_1 = set()	#declare a set
print (my_set_1)
my_set_1.add(33)
my_set_1.add(33)	#this will not add duplicate element 33 in set and not give error
print (my_set_1)

l1 = [1,2,4,1,4,22,9,20,10]
my_set_2 = set(l1)	#this will make set of unique elements of list l1
print (my_set_2)

my_set_3 = set([10,10,35,80,10])
print (my_set_3)


fset_1 = frozenset(['a', 'f','a','g','m','m'])	#this will make frozen set of unique elements of list
print (fset_1)

