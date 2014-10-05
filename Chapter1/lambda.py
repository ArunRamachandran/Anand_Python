# attempt to create a function using 
# lambda operator


cube = lambda x: x ** 3

def fxy(f, x, y):
	print f(x) + f(y)

fxy(cube, 2, 3)

