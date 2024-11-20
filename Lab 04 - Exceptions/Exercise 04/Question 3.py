try:
    my_dict = {'test1': 1, 'test2': 2}
    key = input('Enter a key: ')
    print(my_dict[key])
except KeyError:
    print("Enter a key: ERROR: Invalid Key!")
