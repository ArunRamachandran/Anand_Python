def word_freq(words):
	freq = {}
	for w in words:
		freq[w] = freq.get(w,0) + 1
	return freq

def read_words(filename):
	return open(filename).read().split()

def main(filename):
	frq = word_freq(read_words(filename))
	#for word,count in frq.items():
	#	print word, count
	#sorted_frq = {}
	import operator
	sorted_frq = sorted(frq.items(), key = operator.itemgetter(1))
	#sorted_frq.reverse()
	for word, count in sorted_frq:
		print word, count

if __name__ == "__main__" :
	import sys
	main(sys.argv[1])	
