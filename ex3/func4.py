def func4(A):
    lst = []
    for i in A:
        (a, b) = i
        while b != 0:
            (a, b) = (b, a % b)
        B = (i[0]/a, i[1]/a)
        lst.append(tuple(B))
    return lst
print(func4(A))
