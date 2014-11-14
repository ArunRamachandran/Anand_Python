''' Write a fn tree_reverse to reverse elements of a nested-list 
recursively. '''

def tree_reverse(lst):
	print "lst : ",
	print lst
	
	l = len(lst)
	new_lst = range(l)
	i = l - 1

	for elem in lst:
		if isinstance(elem, list):
			temp = tree_reverse(elem)
			print "IsInstance : temp : ",
			print temp
			new_lst[i] = temp
			i -= 1
		else :
			new_lst[i] = elem
			i -= 1
	return new_lst

z = [[1,2], [3, [4,5]], 6]
print "List : ",
print z
x = tree_reverse([[1,2], [3, [4,5]], 6])
print x
