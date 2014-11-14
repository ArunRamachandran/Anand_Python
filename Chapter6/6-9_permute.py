''' Write a fn permute ti compute all possible permutations of elements
of a given list. '''

def foo(res):

	new = []
	sub = []
	for lst in res:
		l = len(lst)
		l = l - 1
		new.append(lst[0])
		while l > 0:
			new.append(lst[l])
			l = l - 1
		for elem in new:
			sub.append(elem)

		print sub
		if sub in res:
			pass
		else:
			res.append(sub)
		new = []
		sub = []
	print res
			
def permute(lst):
	copy = []
	for elem in lst:
		copy.append(elem)

	print "Orig : ",
	print lst

	print "Copy : ",
	print copy

	l = len(copy)
	i = 0
	x = 0
	res = []
	sub = []


	while i < l:
			
		for elem in copy:
			sub.append(elem)
			for each in copy:
				if each == elem:
					pass
				else:
					sub.append(each)
			if sub in res:
				pass
			else:
				res.append(sub)
			sub = []
		i += 1

	print res
	foo(res)	


x = [1,2,3]
print "List : ",
print x

permute([1,2,3])
