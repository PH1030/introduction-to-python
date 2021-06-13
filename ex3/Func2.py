def func2 (a) :
    res = 0
    value = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    for i in a :
        if i!= '.' :
            res = res * 10 + value[i]
            b=a.index('.')
            c=res/10**b
    return c
print (func2 (a))
