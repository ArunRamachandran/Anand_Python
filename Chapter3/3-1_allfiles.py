''' Write a program to list all files in the given directory '''

import os

def get_files(cwd):
	print "All files in the DIrectory "
	for files in os.listdir(cwd):
		print files

cwd = os.getcwd()
print "Current Directory : "
print cwd
get_files(cwd)
