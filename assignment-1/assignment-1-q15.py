"""
Write a Python program which takes two digits m (row) and n (column) as input 
and generates a two-dimensional array. 
The element value in the i-th row and j-th column 
of the array should be i*j.
"""
m, n = map(lambda x : int(x), input().strip().split())
array = list()
for x in range(1, m+1):
    row = list()
    for y in range(1, n+1):
        row.append(x*y)
    array.append(row)
for x in array:
    print(x)
