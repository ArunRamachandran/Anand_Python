''' Write a python program zip.py to create a zip file. The program should
take name of zip file as first argument and files to add as rest of the 
arguments. '''

import zipfile
import sys
'''
f = open('arun.txt', 'w')
f.write('If you are reading this file')
f.close()
'''


def zip_file(file_name, add_file1, add_file2):
	z = zipfile.ZipFile(file_name,'w')
	z.write(add_file1)
	z.write(add_file2)
	z.close()

if len(sys.argv) != 4:
	print "Need 4 arguments to proceed..!!"
else:
	zip_file(sys.argv[1], sys.argv[2], sys.argv[3])

