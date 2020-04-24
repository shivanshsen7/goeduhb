"""
Write a Python program which accepts 
a sequence of comma separated 4 digit binary numbers as its input and 
print the numbers that are divisible by 5 in a comma separated sequence.
"""
input_list = list(map(lambda x: int(x), input().split(',')))
out_list = [x for x in input_list if x%5 == 0]
print(out_list)
