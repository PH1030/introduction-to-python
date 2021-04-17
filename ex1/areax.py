def area_rectangle (a,b,c,d,e):
	if d==0:
		s = (a + b + c) / 2
		area_triangle = (s*(s-a)*(s-b)*(s-c)) ** 0.5
		print ('area of triangle is{}'.format(area_triangle))
a,b,c,d,e = int(input("a : ")) , int(input("b : ")) , int(input("c : ")),int(input("d : ")),int(input("e : "))
area_rectangle (a,b,c,d,e)
def areax (a,b,c,d,e):
	if a==0:
		s = (e + c + d) / 2
		area_triangle = (s*(s-e)*(s-c)*(s-d)) ** 0.5
		print ('area of triangle is{}'.format(area_triangle))
	elif b==0:
		s = (e + c + d) / 2
		area_triangle = (s*(s-e)*(s-c)*(s-d)) ** 0.5
		print ('area of triangle is{}'.format(area_triangle))
	elif c==0:
		s = (a + b + e) / 2
		area_triangle1 = (s1*(s1-a)*(s1-b)*(s1-e)) ** 0.5
		print ('area of triangle is{}'.format(area_triangle))
	elif d==0:
		return area_rectangle (a,b,c,d,e)
areax (a,b,c,d,e)
