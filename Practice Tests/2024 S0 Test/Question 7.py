def get_valid_fruit_names(fruit_list, number_required):
    correct_list = []
    while len(correct_list) < number_required:
        fruit = input("Enter a fruit name: ")
        if fruit in fruit_list and fruit not in correct_list:
            correct_list.append(fruit)
    return correct_list

fruit_list = ['orange', 'apple', 'pear', 'lemon', 'kiwifruit']
print(get_valid_fruit_names(fruit_list, 3))