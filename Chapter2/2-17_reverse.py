''' Write a program reverse.py to print lines of a file in reverse order '''

fp = open('17.txt', 'w')
fp.write('She sells seashells on the seashore: \n The shells sre seashells Im sure. \n So if she sells seashells on the seashore, \n Im sure that the shells are seashore shells.')
fp.close()


def reverse(filename):
	res = []

	fp = open(filename)
	for lines in (open(filename).readlines()):
		res.append(lines)
	res = res[::-1]
	fp.close()

	fp = open(filename, 'w')
	for lines in res:
		fp.write(lines)
		
	fp.close()

print "FIle name : 17.txt"
print "Initial contents : "
f = open('17.txt')
print f.readlines()
f.close()
reverse('17.txt')

print "Final, reversed contents : "
f = open('17.txt')
print f.readlines()
f.close()
