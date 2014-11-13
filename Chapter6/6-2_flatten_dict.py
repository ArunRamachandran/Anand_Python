
def change(x, last):
	res = []
	new_x = []

	for elem in x:
		if isinstance(elem, dict):
			new_x.append(elem)
		else :
			res.append(elem)
			res.append(last)
			elem = '.'.join(res)
			new_x.append(elem)
			res = []
	return new_x

def flatten_dict(a, result = None):
	
	print "a : ",
	print a,
	print "result: ",
	print result
	
	if result is None:
		result = []

	for x in a.values():
		print "In loop : elem : ",
		print x
	  	
		if isinstance(x, dict):
			print "IF : x : ",
			print x
			if last != ' ':
				x = change(x, last)
			flatten_list(x, result)
		else :
			print "Else : ",
			print x	
			result.append(x)
			last = x
	return result

a = {'a': 1, 'b': {'x' : 2, 'y' : 3}, 'c' : 4}
print "DICT : ",
print a
x = flatten_dict(a)
print x
