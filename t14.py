#zip()

my_list1 = [1,2,3]
my_list2 = ['a','b','c']
my_list3 = [100,200,300]

for item in zip(my_list1, my_list2, my_list3) :
	print (item)

print ("\n")

ziped_list = list(zip(my_list1, my_list2, my_list3))
print (ziped_list)


l1 = [10,20,30,40,50]
l2 = ['A','B']
ziped_list2 = list(zip(l1,l2))
print (ziped_list2)

