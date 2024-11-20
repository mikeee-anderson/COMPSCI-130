try:
    my_list = [1, 2, 3]
    index = int(input('Enter an index: '))
    print(my_list[index])
except IndexError:
    print("ERROR: Invalid index!")