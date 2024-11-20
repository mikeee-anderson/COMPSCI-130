fruits = ['avocado', 24, 'blackcurrant', 'banana', 'two', 2, 23, 'one']
def create_dictionary(values):
    words_list = []
    numbers_list = []
    for value in values:
        value = str(value)
        if value.isdigit():
            value = int(value)
            numbers_list.append(value)
        else:
            words_list.append(value)
    dictionary = {}
    dictionary['words'] = words_list
    dictionary['numbers'] = numbers_list
    return dictionary





print(create_dictionary(fruits))