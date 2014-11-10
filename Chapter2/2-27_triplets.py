''' Write a fn triplets that takes a number n as argument and returns a list
of triplets such that sum of first two elements of the triplet equals the 
third element using numbers below n. Please note that (a,b,c) and (b,a,c) 
represent same triplet '''

def triplet(n):
	res = [(x,y,z) for x in range(1,n) for y in range(x,n) for z in range(y,n) if x + y == z]
	print res


triplet(5)
