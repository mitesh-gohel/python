#keyword arguments of function in python

def my_fun(**kwargs):  
	print(type(kwargs))
	'''
	for my_key in kwargs.keys() :
		print("{0} = {1}".format(my_key, kwargs[my_key]))
	'''
	print ("Name = {0}  Age = {1}  Roll No = {2}".format(kwargs['name'], kwargs['age'], kwargs['roll_no']))

my_fun(name = 'Mitesh', age = 20, roll_no = 33)  
my_fun(age = 13, name = 'lakhan', roll_no =42)

'''
conclusion :
Using keyword argument we can give vaiable number of argument in any order to function
'''
