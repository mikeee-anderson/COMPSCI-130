def print_lower(word):
    if len(word) == 0:
        print("Go!")
        return
    print(word[0].lower())
    print_lower(word[1:])

print_lower('ABC')
