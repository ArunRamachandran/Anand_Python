''' Write a program that takes one or more filenames as arguments and
prints all the lines which are longer than 20 characters. '''

def readfiles(filenames):
	for f in filenames:
		for line in open(f):
			yield line

def match(lines):
	return (line for line in lines if len(line) > 20)

def printlines(lines):
	for line in lines:
		print line,

def main(filenames):
	lines = readfiles(filenames)
	lines = match(lines)
	printlines(lines)

f = ['text.txt']
main(f)
