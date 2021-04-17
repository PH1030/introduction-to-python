def area_rectangle (a,b,c,d,e):
	if d==0:
		s = (a + b + c) / 2
		area_triangle = (s*(s-a)*(s-b)*(s-c)) ** 0.5
		print ('area of triangle is{}'.format(area_triangle))
	else:
		s1 = (a + b + e) / 2
		area_triangle1 = (s1*(s1-a)*(s1-b)*(s1-e)) ** 0.5
		s2 = (c + d + e) / 2
		area_triangle2 = (s2*(s2-c)*(s2-d)*(s2-e)) ** 0.5
		area_rectangle= area_triangle1 + area_triangle2
		print ('area of rectangle is{}'.format(area_rectangle))
a,b,c,d,e = int(input("a : ")) , int(input("b : ")) , int(input("c : ")),int(input("d : ")),int(input("e : "))
area_rectangle (a,b,c,d,e)


