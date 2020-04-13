#_ variable in python
import re
name = "mitesh_gohel"
first_name, _ = re.split("_gohel",name)		#store redundant string in _ variable
print (first_name)

for _ in range(5) :
	print ("Hello")

