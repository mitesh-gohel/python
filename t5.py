#get() in dictionary

student = {"first name":"Mitesh", "last name":"Gohel", "ID number":33}



print ("first name = {0}".format(student['first name']))
print ("last name = {0}".format(student['last name']))


print ("class = {0}".format(student.get("class")))	#Find value of "class" key
							#if key will not found, instead of giving KeyError, It will give None value
print ("college = {0}".format(student.get("college", "CSPIT")))	#find value of "college" key
								#if key will not found, it will give default "CSPIT" value for key "college"


