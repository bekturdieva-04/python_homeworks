# string_utils.py
def reverse(s):
    return s[::-1]
def count_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return sum(1 for x in s if x in vowels)