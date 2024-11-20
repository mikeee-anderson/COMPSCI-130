def convert_tuples(list_of_tuples):
    return [sum(x) for x in list_of_tuples]

data = [(2, 3, 4), (25, 50, 75)]
print(convert_tuples(data))