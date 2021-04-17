Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def equation2D (a,b,c):
	delta = (b**2) - (4*a*c)
	print("Δ = {}".format(delta))
	if delta >= 0:
		x1 = (-b+(delta**0.5))/(2*a)
		x2 = (-b-(delta**0.5))/(2*a)
		print ("x1 = {}".format(x1))
		print ("x2 = {}".format(x2))
	elif delta == 0:
		x=(-b)/(2*a)
		print ('there is only one solution which is{}'.format(x))
	elif delta <= 0 :
		print ('this equation has no answer')
a,b,c = int(input("a : ")) , int(input("b : ")) , int(input("c : "))
equation2D (a,b,c)

