''' Write a fn extsort tp sort a list of files based on extension. '''

def extsort(x):	
	res = []	
	final = []
	for element in x:
		(name,ext) = element.split('.')
		res.append([name,ext])
	res.sort(key = lambda x: x[1])
	for element in res:
		a = element[0]
		b = element[1]	
		string = '.'.join([a,b])
		final.append(string)
	print "Sorted list on the basis of Extension : "
	print final

x = ['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']
print "List : "
print x
extsort(x)
