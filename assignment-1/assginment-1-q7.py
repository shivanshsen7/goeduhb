"""
Write a Python program to check whether an alphabet is a vowel or consonant.
"""
letter = input()
vowels = 'aeiouAEIOU'
if letter in vowels:
    print(f'"{letter}" is a Vowel.')
else:
    print(f'"{letter}" is a consonant.')
