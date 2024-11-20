

def remove_strings_by_len(words, target_length):
    return [word for word in words if len(word) != target_length]


words = ['hot', 'cat', 'over', 'index', 'own', 'are', 'and']
remove_strings_by_len(words, 3)
print(words)
remove_strings_by_len(words, 4)
print(words)
data = ['hot', 'cat', 'over', 'index', 'own', 'are', 'and']
remove_strings_by_len(data, 7)
print(data)