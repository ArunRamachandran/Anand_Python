''' Write a fn dups ton find all duplicates in the list '''

def dups(x):
	unique = []
	unique.append(x[0])
	for element in x:
		if element in unique:
			pass
		else :
			unique.append(element)
	dups = []
	count = 0
	print "Unique : "
	print unique
	for element in unique:
		for number in x:
			if element == number:
				count = count + 1
			else:
				pass
		if count > 1:
			dups.append(element)
			count = 0
		else :
			count = 0
	print dups


x = [1,2,1,3,2,5]
dups(x)
