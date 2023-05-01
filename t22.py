#Python is call by value or call by reference ?

#########
num1 = 1
num2 = 1
print (id(num1), id(num2))
print (num1 is num2)


str1 = "string"
str2 = "string"
print (id(str1), id(str2))
print (str1 is str2)

list1 = [1, 2, 3]
list2 = [1, 2, 3]
print (id(list1), id(list2))
print (list1 is list2)
########

print ("\n#############\n")


########
s1 = "old string"

def change_str(s) :
	s = "new string"
	print (s)

print (s1)
change_str(s1)
print (s1)
########

print ("\n#############\n")


########
l1 = [11, 12, 13]

def modify_list(l) :
	l.append(100)
	print (l)

print (l1)
modify_list(l1)
print (l1)
########

print ("\n#############\n")


########
l2 = [50, 60, 70]

def change_list (l) : #ressign list
	print (l)
	l  = [11, 22, 33]
	print (l)

print (l2)
change_list(l2)
print (l2)

########

'''
Output :
mitesh@mitesh-IdeaPad-3i:~/mitesh_workspace/python$ python3 t22.py 
9793088 9793088
True
139938986141168 139938986141168
True
139938986719872 139938985861824
False

#############

old string
new string
old string

#############

[11, 12, 13]
[11, 12, 13, 100]
[11, 12, 13, 100]

#############

[50, 60, 70]
[50, 60, 70]
[11, 22, 33]
[50, 60, 70]
mitesh@mitesh-IdeaPad-3i:~/mitesh_workspace/python$ 



Conclusion :
Python is not call by value nor call by referece.
Python is call by object reference

Means :
It passes reference of object.
If object is immutable (number, string, ...), then it will work like call by value
If object is mutable (list, dictionary, ...), then : 
	(i) if we modifty object, it will work like call by reference. 
	(ii) if we change whole object value then it will work like call by value.
'''
