#globals() and locals()

a = 10

def f() :
	x = 20
	print (x)
	l = locals()	#it gives dictionary of local names
	print ("locals() :")
	print(l)

g = globals()	#it gives dictionary of global names
print("globals() :")
print (g)

f()

'''
Output :
mitesh@mitesh-IdeaPad-3i:~/mitesh_workspace/python$ python3 t20.py 
globals() :
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f800572ab80>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 't20.py', '__cached__': None, 'a': 10, 'f': <function f at 0x7f800578a1f0>, 'g': {...}}
20
locals() :
{'x': 20}
mitesh@mitesh-IdeaPad-3i:~/mitesh_workspace/python$
'''

