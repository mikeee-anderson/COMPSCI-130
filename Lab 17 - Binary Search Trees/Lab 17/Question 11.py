import math
def first_vowel(string):
    vowel = "aeiou"
    string = string.lower()
    for char in string:
        if char in vowel:
            break
    return char


string = "apple"
print(first_vowel(string))