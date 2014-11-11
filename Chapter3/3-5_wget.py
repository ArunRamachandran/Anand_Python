''' Write a program wget.py to download a given URL. The program should
accept a URL as argument , download it and save the basename of the URL.
If URL ends with a /, consider the basename as index.html '''

import urllib
import os

def wget(url):
	res = urllib.urlopen(url)
	base_name = os.path.basename(url)
	if base_name != ' ':
		page = open(base_name,'w')
	else :
		base_name = 'index.html'
		page = open(base_name, 'w')
	print 'saving %s as %s' % (url,base_name)
	page.write(res)
	page.close()


url = raw_input('Give a URL to download?\n')
wget(url)
