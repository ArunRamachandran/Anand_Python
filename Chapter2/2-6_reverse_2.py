
def reverse(x):
	l = len(x)
	res = range(1,l + 1)
	l = len(res)
	for element in x:
		res[l - 1] = element
		l = l - 1
	print "Reversed : "
	print res
	

x = [1,2,3,4]
print "List : "
print x
reverse(x)
