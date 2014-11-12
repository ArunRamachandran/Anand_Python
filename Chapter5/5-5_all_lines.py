''' Write a fn to compute the total no.of lines of code in all python
files in the specified directory recursively. '''

import os

def extract(d):
	for files in os.listdir(d):
		yield os.path.join(files)

def main(direct):
	for path in extract(direct):
		if os.path.isfile(path):
			tot_len = len(open(path).readlines())
			print "%s : No.of Lines  %d" % (path,tot_len)
		else:
			main(path)


directory = "/home/user/Anand_Python/Chapter5/"
main(directory)
