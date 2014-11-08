def sum_list(x):
	sum = 0
	for element in x:
		sum = sum + element
		
	return sum	
	
x = [1,2,3]
sum_of_list = sum_list(x)
print "List : ",
print x
print sum_of_list
