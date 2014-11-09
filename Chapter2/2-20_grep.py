''' Implement unix command grep. The grep command takes a string and a 
file as arguments and prints all lines in the file which contain the specified string '''

fp = open('text.txt')
print "Elements in the file : "
print open('text.txt').read()
fp.close()

def grep(string, filename):
	fp = open(filename)
	found = 0
	print "Lines with given string : "
	for lines in open(filename).readlines():
		if string in lines:
			print lines
			found = found + 1
		else :
			pass
	if found == 0:
		print "Sorry..!! Couldn't locate any Lines "

print "Calling Grep() : grep(%s, %s) " % ('she', 'text.txt')
print " "
grep('she', 'text.txt')
