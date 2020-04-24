"""
Write a Python program to check a string represent an integer or not.
"""
string = input().rstrip()
if string.isdigit():
    print(f"{string} represents integers")
else:
    print(f"{string} does not represent integers")