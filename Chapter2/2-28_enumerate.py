''' Write a fn enumerate that takes a list and returns a list of tuplets
containing (index,item) for each item in the list '''

def enumerate(lst):
	res = [(lst[x],x) for x in range(len(lst)) for y in range(len(lst)) if x == y]
	print res

enumerate(["a", "b", "c"])
