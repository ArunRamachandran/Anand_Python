''' Provide an implementation for zip fn using list comprehensions '''

def zip_list(a,b):
	l = len(a)
	res = [(a[x],b[y]) for x in range(len(a)) for y in range(len(b)) if x == y]
	print res

zip_list([1,2,3],["a", "b", "c"])
