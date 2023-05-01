#Result of locals() outside of function

x = 10

print ("Outside of function, locals() :")
print (locals())

print ("globals() :")
print (globals())

def f() :
	a = 1
	print ("Inside function, locals() :")
	print (locals())

f()

'''
Output :
mitesh@mitesh-IdeaPad-3i:~/mitesh_workspace/python$ python3 t21.py 
Outside of function, locals() :
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f8132259b80>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 't21.py', '__cached__': None, 'x': 10}
globals() :
{'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x7f8132259b80>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 't21.py', '__cached__': None, 'x': 10}
Inside function, locals() :
{'a': 1}
mitesh@mitesh-IdeaPad-3i:~/mitesh_workspace/python$


Conclusion :
Results of locals() outside of function is same as globals()
'''
