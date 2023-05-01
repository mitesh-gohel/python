#unpacking of tuple

a, b, c, d, e = (1, 2, 3, 4, 5)

print (a, b, c, d, e)

a, _, c, _, e = (1, 2, 3, 4, 5) 	#if we don't want some value

print (a, c, e)

a, *_, e = (1, 2, 3, 4, 5)
print (a, e) 

a, *e = (1, 2, 3, 4, 5)
print (type(e))
print (a, e)

*a, e = (1, 2, 3, 4, 5)
print (type(a))
print (a, e)

