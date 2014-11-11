''' Write a program to print directory tree. The program should take path of
a directory as argument and print all the files in it recursively as a 
tree. '''

import os

def dirtree(direct):
	

	for files in os.listdir(direct):
		path = os.path.join(direct,files)

		if os.path.isfile(path):
			print "|-- %s" % (files)
		else:
			print "|",
			print "\t",
			print "|-- %s" % (files)
			dirtree(path)


get = os.getcwd()
print get
direct = raw_input('Give a directory :\n')
dirtree(direct)
