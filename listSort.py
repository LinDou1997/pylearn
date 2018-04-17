def findMaxMin(list):
	a = list[0]
	for i in list:
		if a<=i:
			a = a
		else:
			a = i
	print('The min number is',a)
	b = list[0]
	for i in list:
		if b>=i:
			b = b
		else:
			b = i
	print('The max number is',b)
findMaxMin([1,3,2,4,5])