def create_dictionary(data):
    number_dict = {}
    for number_list in data:
        number = sum(number_list)
        if number not in number_dict:
            number_dict[number] = []
            number_dict[number].append(number_list)
        else:
            number_dict[number].append(number_list)
    return number_dict

data = [[1, 3, 1], [3, 6, 9], [2, 5, 1], [1, 1, 2, 1]]
dict1 = create_dictionary(data)
print(type(dict1))
for key in sorted(dict1):
    print(key, dict1[key])