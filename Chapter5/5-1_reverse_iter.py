''' Write an iterator class reverse_iter, that takes a list and iterates
it from the reverse direction. '''

class reverse_iter:
	''' class intended for reverse iteration. '''
	
	def reverse_list(self,lst):
		l = len(lst)
		res = []
		while(l > 0):
			l = l - 1
			res.append(lst[l])
		return res

	def __init__(self, l):
		self.lst = l
		self.lst = self.reverse_list(self.lst)
		self.i = 0
		self.n = 0

	def next_elem(self):
		#self.lst = reverse_list(self.lst)
		l = len(self.lst)	
		if self.i < l:
			i = self.i
			self.i = self.i + 1
			return self.lst[i]
		else:
			raise StopIteration()

lst = reverse_iter([1,2,3,4,5])
print lst.next_elem()		
print lst.next_elem()
print lst.next_elem()

		
