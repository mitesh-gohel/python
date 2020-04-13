#Named argument of function in python


def print_info(name = 'unknown', age = None) :
	print("Name : {0}, Age : {1}".format(name, age))


print_info()
print_info('Roy',25)
print_info(33,'Mr.x')
#print_info(name = 'Alex',15)	#This will give error
print_info('Mayank',age = 33)
print_info(name = 'Riya', age = 20)
print_info(age = 21, name = 'kavya')
