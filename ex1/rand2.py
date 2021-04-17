import random
def rand2 (x,y):
        for a in range (x,y+1) :
            a = random.randint(x,y)
            if a%2 !=0 and x<a<y :
                print ('num is {}'.format(a+1))
            elif a<=x or a>=y :
                    continue
        if a%2 ==0 :
                print ('num is {}'.format(a))
                
x,y=int(input('first number: ')),int(input('second number: '))
rand2 (x,y)
 
