def get_vowels(word):
    vowels = "AEIOUaeiou"
    list1 = [char for char in word if char in vowels]
    return list1

print(get_vowels('solidarity'))
