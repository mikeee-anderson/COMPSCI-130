def swap_space_with_target(string, target_letter):
    space_index = 0
    target_index = 0
    for i in range(len(string)):
        if string[i] == target_letter:
            target_index = i
        if string[i] == " ":
            space_index = i
    string_list = list(string)
    string_list[space_index], string_list[target_index] = string_list[target_index], string_list[space_index]
    return ''.join(string_list)




print(swap_space_with_target("abcde fgh", 'b'))
print(swap_space_with_target("abcde fgh", 'g'))
print(swap_space_with_target("abcde fgh", 'h'))
print(swap_space_with_target("abcde fgh", 'a'))