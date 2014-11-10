''' Write a fn array to create an 2-dimensional array. The fn should take
both dimensions are arguments. Value of each element can be initialized to
None: '''

def  array(i,j):
	res = []
	res = [[None] * j for element in range(i)]
	return res



a = array(2,3)
print a
