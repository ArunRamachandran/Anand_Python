''' Python provides a built-in-fn map that applies a fn to each element of 
a list. Provide an implementation for map using list comprehensions. '''

def square(x): return x * x

def map(fxy, lst):
	res = [fxy(x) for x in lst]
	print res


map(square, range(5))


