''' Write a fn group(list,size) that take a list and splits into smaller 
list of  given size '''

def group(x,n):
	count = 0
	l = len(x)
	tot_len = 0
	main_list = []
	sub_list  = []
	for element in x:
		count = count + 1
		tot_len = tot_len + 1
		if count <= n:
			sub_list.append(element)
		if count > n :
			main_list.append(sub_list)
			count = 1
			sub_list = []
			sub_list.append(element)
		if tot_len == l:
			main_list.append(sub_list)
			
	print "Result : "
	print main_list					


x = [1,2,3,4,5,6,7,8,9]
n = 4
print "List : "
print x
print "Case : %d" % (n)
group([1,2,3,4,5,6,7,8,9],4)
