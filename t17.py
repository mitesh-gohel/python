#class attribute and object attribute

class Circle() :
	pi = 3.14	#class attribute
	def __init__(self, radius=1) :
		self.radius = radius	#object attribute
	
	def get_circumference(self) :
		print (2 * Circle.pi * self.radius)

my_circle = Circle()
my_circle.get_circumference()
