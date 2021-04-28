def prog3 (a):
	list=[]
	for i in range (1,a+1):
		if a%i==0:
			list.append(i)
	if len(list)==2:
		print ('True')
	if len(list)>2:
		print ('False')
a=int(input('enter the number you want: '))
prog3 (a)
