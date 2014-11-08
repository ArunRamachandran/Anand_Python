''' Write a f. 'factorial' to compute factorial of a number. Can you use the
'product' fn defined in the previous example to compute factorial '''

def product(x):
	prdct = 1
	for element in x:
		prdct = prdct * element

	return prdct

def factorial(n):
	x = range(1,n+1)
	fact = product(x)
	return fact

n = input('Give a number to find Factorial ?\n')
x = factorial(n)
print "Factorial of %d : %d " % (n,x)
