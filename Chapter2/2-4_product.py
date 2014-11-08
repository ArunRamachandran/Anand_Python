''' Implement a fn 'product' to compute product of a list '''

def product(x):
	prdct = 1
	for element in x:
		prdct = prdct * element
 
	print "Product : ",
	print prdct


x = [1,2,3]
print "List : "
print x
product(x)
