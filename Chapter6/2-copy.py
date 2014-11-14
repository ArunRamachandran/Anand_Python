def change(d, char):
	l = []
	new_d = dict()
	for keys, values in d.items():
		l.append(char)
		l.append(keys)
		keys = '.'.join(l)
		#print keys
		new_d[keys] = values
		l = []
	return new_d		

def flatten_dict(d, result = None):
	
	if result is None:
		result = {}
		
	for key, value in d.items():
		if isinstance(value, dict):
			new_d = change(value, key)
			flatten_dict(new_d, result)
		else :	
			result[key] = value

	return result


d = {'a' : 1, 'b' : {'x' : 2, 'y' : 3}, 'c' : 4}
print "Dict : ",
print d
new_d = dict()
res = flatten_dict(d, new_d)
print res
#change(d,'zzz')
