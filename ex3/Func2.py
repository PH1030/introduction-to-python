a = '546'
res = 0
value = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

for digit in a:
    res = res * 10 + value[digit]

print(res)
