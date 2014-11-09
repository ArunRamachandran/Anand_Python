''' Write a fn lensort to sort a list of strings based on length '''

def lensort(x):
	x.sort(key = lambda x: len(x))
	''' can use either sort or soted to do the same, both will take 
	an optional key fn to sort based on that fn '''
	print "Sorted : "
	print x

x = ['python', 'perl', 'java', 'c', 'haskell', 'ruby']
print "List : "
print x
lensort(x)
