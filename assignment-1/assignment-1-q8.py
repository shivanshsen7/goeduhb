"""
Write a Python program that reads two integers representing a month and day 
and prints the season for that month and day.
"""
"""
Referece for calender as per year 2020
source: https://www.drikpanchang.com/seasons/season-tropical-timings.html?year=2020
"""

days = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
month_keys = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
 'August', 'September', 'October', 'November', 'December']
month_values = range(1,13)
months = dict(zip(month_keys, month_values))

print('Please Check your input')
print('Months and maximum date must be written as follow:')
for x in range(12):
    print(month_keys[x],"=", month_values[x], "|", "Max. days = ", days[x])

m, day = input().rstrip().split()
m = int(m)
day = int(day)

if (m  == 2 and day >= 19) or (m == 3 and day < 19):
    print('India Spring, "Vasant"')
elif (m == 3 and day >= 19) or (m == 6 and day < 21) or m == 5:
    print('India Summer, "Grishma"')
elif (m  == 6 and day >= 21) or (m == 8 and day < 22) or m == 7:
    print('India Monsoon, "Varsha"')
elif (m  == 8 and day >= 22) or (m == 10 and day < 23) or m == 9:
    print('India Autumn, "Sharad"')
elif (m  == 10 and day >= 23) or (m == 12 and day < 21) or m == 11:
    print('India Prewinter, "Hemant"')
elif (m  == 12 and day >= 21) or (m == 2 and day < 18) or m == 1:
    print('India Winter, "Shishir"')    
else:
    print('\nPlease give input as per instructions.')
