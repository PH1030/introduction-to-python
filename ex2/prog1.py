def prog1 (a,b):
	list=[]
	for i in range (a+1,b):
		if i%2==0:
			list.append(i)
	print(list)
a,b=int(input('first number: ')),int(input('second number: '))
prog1 (a,b)
	
