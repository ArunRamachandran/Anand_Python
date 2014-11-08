''' Write a fn 'cumulative_product' to compute product of a list of numbers '''

def cumulative_product(x):
	l = len(x)
	res = []
	i = 0
	c_product = 1

	for element in x:
		c_product = c_product * element
		res.append(c_product)
	print res

x = [1,2,3,4]
cumulative_product(x)
