''' Write a program wrap.py that takes filename and width as arguments and
wraps the lines longer than the width '''

print "Contents in the file text.txt "
print open('text.txt').read()

def wrap(filename, width):
	for lines in open(filename).readlines():
		l = len(lines)
		count = 0
		if l < width:
			print lines
		else :
			if_list = []
			else_list = []
			for character in lines:
				if count < width:
					print character,
				else :
					print '\n'
					print character,
					count = 0
				count = count + 1
			
				

print " "
wrap('text.txt', 15)
