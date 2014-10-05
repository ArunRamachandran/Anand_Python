# attempt to implement a fxy() func.
# fxy(f, x, y) --> where, f is a function
# and both x and y are variables.

def f(x):
	return x * x

def fxy(f, x, y):
	print f(x) + f(y)

fxy(f, 2, 3)
