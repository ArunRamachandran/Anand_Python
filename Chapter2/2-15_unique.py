''' Reimplement the unique fn implemented in the earlier examples using 
sets. '''

def unique(x):
	y = set(x)
	print "Unique List : "
	print y

x = [2,1,9,3,2,1]
print "List : "
print x
unique(x)
