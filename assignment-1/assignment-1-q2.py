"""
Write a Python program to construct the following pattern,
using a nested for loop.

*

* *

* * *

* * * *

* * * * *

* * * *

* * *

* *

*

"""

# i = int(input().rstrip())
for x in range(1,i+1):
    print(x*"*")
for x in range(i-1,0,-1):
    print(x*"*")
