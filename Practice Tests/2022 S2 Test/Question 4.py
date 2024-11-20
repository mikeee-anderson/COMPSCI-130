def remove_ends_with_vowel(words_list):
    vowels = "AEIOUaeiou"
    new_list = [word for word in words_list if word[-1] not in vowels]
    words_list.clear()
    words_list.extend(new_list)

data = ["Hello", "World", "is", "nice", "weather"]
remove_ends_with_vowel(data)
print(data)