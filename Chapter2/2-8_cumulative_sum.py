''' Cumulative sum of a list [a,b,c,...] is defined as [a, a+b, a+b+c, ...].
Write a fn cumulative_sum to compute cumulative sum of a list. '''

def cumulative_sum(x):
	l = len(x)
	res = range(l)
	c_sum = 0
	i = 0
	for element in x:
		c_sum  = c_sum + element	
		res[i] = c_sum	
		i = i + 1
		
	print res


x = [1,2,3,4]
print "List : "
print x
print "Cumulative sum : "
cumulative_sum(x)
