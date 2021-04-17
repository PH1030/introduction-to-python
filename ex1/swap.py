def swap (a,b):
	a,b=b,a
	print ('{} is a and {} is b now!'.format(a,b))
a,b = int(input("a : ")) , int(input("b : "))
swap (a,b)
