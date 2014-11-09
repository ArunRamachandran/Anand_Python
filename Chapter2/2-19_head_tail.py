''' Implement unix commands head and tail. The head and tail commands take a
file as argument and prints its first and last 10 lines of the file respectively. '''

fp = open('text.txt', 'w')
fp.write('She sells seashells on the seashore;\n The shells that she sells are seashells Im sure.')
fp.close()

print "Contents in the file : "
fp = open('text.txt')
print fp.read()

def head(filename):
	fp = open(filename)
	l = len(open(filename).read())	
	count = 0
	res = []
	fp.close()
	for elements in ( open(filename).read()):
		if count > 11:
			break
		else:
			print elements,
		count = count + 1
	fp.close()
	
def tail(filename):
	fp = open(filename)
	l = len(open(filename).read())
	count = l - 10
	val = 0
	for elements in (open(filename).read()):
		val = val + 1
		if val < count - 1:
			pass
		else :
			print elements,
print " "
print " "
print "Calling Head(): The first 10 characters are : "	
head('text.txt')
print ' '
print ' '
print "Calling Tail(): The last 10 characters are : "
tail('text.txt')

