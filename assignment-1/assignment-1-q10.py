"""
Write a Python program to sum of two given integers. 
However, if the sum is between 15 to 20 it will return 20.
"""
ip = list(map(lambda x : int(x), input().rstrip().split()))
sum_ = ip[0] + ip[1]

if sum_ in range(15, 21):
    print(20)
else:
    print(sum_)
