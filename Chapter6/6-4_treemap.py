''' Write a fn treemap to map a fn over nestedd list. '''

def treemap(fxy, lst):
	print "List : ",
	print lst
	new_lst = []
	
	for elem in lst:
		if isinstance(elem, list):
			z = treemap(fxy, elem)
			new_lst.append(z)	
		else :
			x = fxy(elem)
			new_lst.append(x)
	return new_lst

z = treemap(lambda x: x*x, [1,2,[3,4, [5]]])
print z
