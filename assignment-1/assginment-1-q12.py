"""
Write a Python program to create the multiplication table 
(from 1 to 10) of a number.
"""
n = int(input().strip())
to = range(1, 11)
for mul in to:
    print('{:<d} {}{:^3d} {} {:<4d}'.format(n,'* ', mul, '=', n*mul))
