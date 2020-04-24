"""
Write a Python program to print alphabet pattern 'A'
"""
my_str=""
for row in range(0,7):
    for col in range(0,7):
        cnd1 = ((col == 1 or col == 5) and row != 0)
        cnd2 = (row == 0 or row == 3)
        cnd3 = (col > 1 and col < 5)
        if (cnd1 or (cnd2 and cnd3)):
            my_str=my_str+"*"
        else:
            my_str=my_str+" "
    my_str=my_str+"\n"
print(my_str)
