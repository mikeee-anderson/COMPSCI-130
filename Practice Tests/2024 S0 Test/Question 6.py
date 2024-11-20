def read_fruit_names(filename):
    try:
        fruit_list = []
        input_file = open(filename, "r")
        fruits = input_file.read().split("\n")
        input_file.close()
        for fruit in fruits:
            fruit = fruit.lower()
            fruit_list.append(fruit)
        return fruit_list
    except FileNotFoundError:
        print(f"ERROR: The file '{filename}' does not exist.")
        return []







print(read_fruit_names('fruit_small.txt'))
print(read_fruit_names('input_unknown.txt'))

