''' Write a python fn parse_csv to parse csv (comma separated values) files
'''
fp = open('2.csv', 'w')
fp.write('a,b,c \n 1,2,3 \n 2,3,4 \n 3,4,5')
fp.close()

def parse_csv(filename):
	import csv
	res = []
	f = open(filename)
	csv_f = csv.reader(f)

	res = [row for row in csv_f]
	#for row in csv_f:
	#	res.append(row)
	print res


parse_csv('2.csv')

