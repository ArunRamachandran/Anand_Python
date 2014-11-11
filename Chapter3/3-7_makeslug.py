import re
import unidecode

def slug(text):
	text = unidecode.unidecode(text).lower()
	return re.sub(r'\W+', '-', text)



text = 'hello world'
print slug(text)
