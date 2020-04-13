#unpacking of dectionary elements

dic = {'a':1, 'b':2, 'c':3, 'd':4}

for x in dic :	#when we iterate over dic, it gives keys
	print(x)

print ("\n")

for item in dic.items() :
	print(type(item))
	print (item)

print ("\n")

for key, val in dic.items() :				#unpacking to key and val variable
	print ("key = {0} value = {1}".format(key,val))
