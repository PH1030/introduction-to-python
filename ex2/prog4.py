def prog4 (a):
	list=[]
	for i in range (1,a+1):
		if a%i==0 :
			list.append(i)
	print (list)

a=int(input('enter the number you want: '))
prog4 (a)
