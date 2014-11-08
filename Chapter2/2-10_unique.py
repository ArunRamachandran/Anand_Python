''' Write a fn 'unique' to find all the elements of a list. '''

def unique(x):
	res = []
	res.append(x[0])
	for element in x:
		if element in res:
			pass
		else :
			res.append(element)
	print res


x = [1,2,1,3,2,5]
print "List : "
print x
print "List of Unique elements in the list : "
unique(x)
