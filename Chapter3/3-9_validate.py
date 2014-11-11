def validate(num):
	pat=r'^([+]?\d{1,2})?(\d{10})$'
	if re.search(pat,num):
		print '\n\n%s is a valide mobile number!!\n\n'%num
	else:
		print '\n\n%s is not a valide mobile number!!\n\n'%num

import re,sys

num = raw_input('Give a Phone number ? \n')
validate(num)
