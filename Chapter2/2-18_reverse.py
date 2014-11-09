''' Write a program to print each line of a file in reverse order '''

fp = open('she.txt', 'w')
fp.write('she sells seashells on the sea shore ! \n')
fp.close()

def line_reverse(filename):
	res = []
	new_list = []
	fp = open(filename)
	for lines in (fp.readlines()):
		res.append(lines)
	fp.close()
	fp = open(filename, 'w')
	for elements in res:
		a = elements
		a = a[::-1]
		fp.write(a)
	fp.close()		

print "Initial File : "
fp = open('she.txt')
print (fp.readlines())
fp.close()
line_reverse('she.txt')
print "Final contents : "
print (open('she.txt').readlines())
