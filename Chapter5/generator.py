''' Generators simplifies creation of iterators. A generator is a fn
that produces a sequence of results instead of a single value. '''

def yrange(n):
	i = 0
	while i < n:
		yield i
		i += 1

x = yrange(4)
print x.next()
