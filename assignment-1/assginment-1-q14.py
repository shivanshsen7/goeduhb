"""
 Write a Python program to get next day of a given date.

Expected Output:
Input a year: 2016                                                      
Input a month [1-12]: 08                                                
Input a day [1-31]: 23                                                  
The next date is [yyyy-mm-dd] 2016-8-24
"""
from datetime import date
print('''Input Format:
Year in format YYYY
Month in format MM
Day in format DD
e.g.: 2016 08 23''')
d = list(map(lambda x: int(x), input().strip().split()))
print(d)

d = date(d[0], d[1], d[2])

d += datetime.timedelta(days=1)
print(d)
