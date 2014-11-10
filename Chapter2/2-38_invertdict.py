''' Write a fn invertdict to intechange keys and values in a dicionary.'''

def invert_dict(d):
	new = {}
	for keys, values in d.items():
		new[values] = keys
	print new


invert_dict({'x': 1, 'y': 2, 'z': 3})
