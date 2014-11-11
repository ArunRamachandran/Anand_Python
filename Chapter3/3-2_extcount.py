''' Write a program extcount.py to count number of files for each extension
in the given directory. The program should take a directory name as argument
and print count and extension for each file extension. '''

import os

def extcount(direct):
	d = dict()
	for files in os.listdir(direct):
		if os.path.isfile(files):
			name,ext = files.split('.')
			if ext in d:
				d[ext] += 1
			else :
				d[ext] = 1
	print "Count and extension List : "
	for keys, values in d.items():
		print values , keys

direct = os.getcwd()
extcount(direct)
