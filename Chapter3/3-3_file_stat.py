''' Write a program to list all the files in the given directory along with
their length and last modification time. The output should contain one line 
for each file containing filename, length, and modification date separated
by tabs. '''

''' using module os.stat '''

import os
import datetime

def get_stat(direct):
	print "File_name- length -last modification_time order " 
	for files in os.listdir(direct):
		print files,
		print '\t',
		print os.stat(files).st_size,
		print '\t',
		print datetime.datetime.fromtimestamp(os.stat(files).st_mtime)
			

direct = os.getcwd()
get_stat(direct)
