''' Implement a fn product to multiply 2 numbers recursively using + and 
- operators only. '''

def product(x,n):
	if  n == 0:
		return 0
	else :
		return x + product(x, n - 1)

p = product(2,3)
print "%d * %d = " % (2,3), 
print p
