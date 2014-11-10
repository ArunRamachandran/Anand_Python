''' Write a fn valuesort to sort values of a dictionary based on the key. '''

def valuesort(d):
	import operator
	sorted_d = sorted(d.items(), key = operator.itemgetter(0))
	print "Sorted by keys "
	print [values for keys, values in sorted_d]

d = {'x' : 1, 'y' : 2, 'a' : 3}
print "Dictionary : "
print d
valuesort({'x': 1, 'y' : 2, 'a' : 3})
