#variable number of arguments of function in python

def fun(*argv):
	print((type(argv)))
	print(argv)

fun("a",None, 4,10,"Something",22)
fun(12,78)
fun(12)
fun(12,'K')



