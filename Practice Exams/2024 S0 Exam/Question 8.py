def contains_letter(a_word, a_letter):
    # Base case: if the word is empty, the letter was not found
    if not a_word:
        return False, -1
    # Check if the first character matches the letter we're looking for
    if a_word[0] == a_letter:
        return True, 0

    found, position = contains_letter(a_word[1:], a_letter)
    return (found, position + 1) if found else (False, -1)