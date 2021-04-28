def prog2 (a,b):
	list=[]
	if a>b:
		a,b=b,a
	for i in range (a+1,b):
		if i%2==0:
			list.append(i)
	print(list)
a,b=int(input('first number: ')),int(input('second number: '))
prog2 (a,b)
