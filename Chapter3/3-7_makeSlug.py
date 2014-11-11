def make_slug(text):
	import re
	name = r'\w+'
	print '-'.join(re.findall(name,text))

text = 'hello world'
make_slug(text)
