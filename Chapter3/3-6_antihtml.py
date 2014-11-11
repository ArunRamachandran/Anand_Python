''' Write a program antihtml.py that takes a URL as argument, 
	downloads the html from web and print it after strippig html tags. '''

import urllib
import re

def antihtml(url):
	page = urllib.urlopen(url)
	no_tag = re.sub("<.*?>",'',page)
	print "Without tags..\n"
	print no_tag




url = raw_input('Give a URL:?\n')
antihtml(url)
