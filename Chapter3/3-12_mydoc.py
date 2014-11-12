def mydoc(name):
	try:
		m = __import__(name)
	except:
		print "%s module not found!" % (name)
		return

	print m.__doc__ # to get the doc string 
	d = dir(m) 	# to get all entries of the module
	for i in d:
		if inspect.isfunction(getattr(m,i,False)):
			print i
			print getattr(m,i).__doc__

import inspect
import sys

if len(sys.argv) != 2:
	print "Need 2 arguments to procees !"
else:
	mydoc(sys.argv[1])
