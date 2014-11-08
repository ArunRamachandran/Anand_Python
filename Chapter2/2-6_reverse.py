''' Write a fn 'reverse' to reverse a list. Can you do this without using
list slicing '''

def reverse(x):
	res = []
	l = len(x)
	i = l
	while i > 0:
		res.append(x[i - 1])
		i = i - 1
	print "Reversed :"
	print res


x = [1,2,3,4]
print "List : "
print x
reverse(x)
