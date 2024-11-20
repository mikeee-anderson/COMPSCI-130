def read_file(filename):
    input_file = open(filename, "r")
    data = input_file.read().split("\n")
    input_file.close()
    return data

data = read_file("regions.txt")