def flatten_list(a, result = None):
	print "Now in fn : ",
	print "a : ",
	print a,
	print "    Result : ",
	print result

	if result is None:
		result = []
	for x in a:
		if isinstance(x,list):
			print "If : ",
			print x
			print "Calling Fn"
			flatten_list(x,result)
		else:
			print "Else : x : ",
			print x
			result.append(x)
	print "Result : ",
	print result
	print "Returning to fn call"
	return result

a = [[1,2, [3,4]], [5,6], 7]
print "List : ",
print a
res = flatten_list(a, result = None)

print res
