''' Generalize the above implementation of csv parser to support any
delimeter and comments. '''

f = open('a.txt', 'w')
f.write("# Elements are separated by ! and comment indicator is # \n a!b!c! \n 1!2!3! \n 2!3!4! \n 3!4!5")
f.close()

def parse(filename, sym1, sym2):
	res = []
	res = [[lines] for lines in open(filename).readlines() if lines[0] != sym2]

	index = 0
	for element in res:
		for each in element:
			for numb in each:
				if numb == sym1:
					numb = ','
						
	print res

parse('a.txt', '!', '#')
