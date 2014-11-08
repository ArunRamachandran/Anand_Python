''' Python has a built in fn min and max to compute minimum and maximum 
of a given list. Provide an implementation for these functions. '''

def min_list(x):
	minimum = x[0]
	for element in x:
		if element < minimum:
			minimum = element
		else :
			pass
	print minimum

def max_list(x):
	maximum = x[0]
	for element in x:
		if element > maximum:
			maximum = element
		else :
			pass
	print maximum
	
x = [1,2,3,4]
print "List : "
print x
print "min() : "
min_list(x)
print "max() : "
max_list(x)
