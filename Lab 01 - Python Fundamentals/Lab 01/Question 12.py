def create_words_list(word):
    words_list = [word[i:] for i in range(len(word))]
    return words_list

word = create_words_list('case')
print(word)
print(create_words_list('cat'))