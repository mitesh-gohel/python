#How to handle exception and print exception with line number 

import traceback
x = 6
try :
	x += "Hi"
except Exception :
	traceback.print_exc()	#This will print exception with line number 
print ("End")
