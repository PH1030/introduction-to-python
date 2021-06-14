def func3 (a) :
    res = 0
    st="{}".format(a)
    value = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    for i in st :
        if i!= '.' :
            res = res * 10 + value[i]
            b=st.index('.')
            d=(st[ :b])
    return d
print (func3 (a))
