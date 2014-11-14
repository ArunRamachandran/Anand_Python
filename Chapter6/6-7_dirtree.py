''' Imlement a program dirtree.py that takes a directory as argument and
prints all the files in that directory recursively as a tree. '''

import os


def dirtree(directory):

	for files in os.listdir(directory):
		f_name = os.path.join(directory, files)

		d = 0
		print "|",			
		if os.path.isdir(f_name):
			print "--",
			print files,
			print "/"
			print "|"
			d = 1
			dirtree(f_name)
		else:	
			if d == 1:
				print "|",
				print '\t',
			print "--",
			print files


cwd = os.getcwd()
print cwd
direct = raw_input('Give a directory ? \n')
dirtree(direct)
