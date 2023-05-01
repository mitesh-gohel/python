#type() of class

class Dog() :
	def __init__(self, breed) :	#constuctor
		self.breed = breed #attribute

my_dog = Dog("Lab")
print(type(my_dog))

'''
Output :
mitesh@mitesh-IdeaPad-3i:~/mitesh_workspace/python$ python3 t16.py 
<class '__main__.Dog'>
mitesh@mitesh-IdeaPad-3i:~/mitesh_workspace/python$
'''
