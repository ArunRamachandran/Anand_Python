class yrange:
	''' Similar to xrange() '''
	def __init__(self,n):
		self.i = 0
		self.n = n

	def __iter__(self):
		return self

	def next(self):
		if self.i < self.n:
			i = self.i
			self.i = self.i + 1
			return i
		else:
			raise StopIteration()

y = yrange(3)
print y.next()
print y.next()
print y.next()

# Many built in fn accept iterators as argument.
z = list(yrange(5))
print z
s = sum(yrange(5))
print s
