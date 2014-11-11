''' Write a program links.py that takes URL of a webpage as argument and
prints all the URLs linked from that webpage.'''

def links(url):
	import urllib2
	import re

	#connenct to URL
	website = urllib2.urlopen(url)
	
	#to read the html code
	html = website.read()

	#use re.findall to get all the links
	for i in re.findall('"https?://.*?"',html):
		print i[1:-1]

	#print links


url = raw_input('Give a URL? \n')
links(url)
