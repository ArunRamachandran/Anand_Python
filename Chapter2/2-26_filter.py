''' Python provides a built-in-fn filter(f, a) that returns items of the
list a for which f(item) returns true. Provide an implementation for filter 
using list comprehensions. '''

def even(x): return x % 2 == 0

def filter(fxy, lst):
	res = [x for x in lst if fxy(x) == True]
	print res

filter(even, range(10))
