def read_file(filename):
    input_file = open(filename, "r")
    data = input_file.read().split("\n")
    input_file.close()
    return data
def get_numbers_list(data):
    number_list = [float(value) for value in data.split(",")]
    return number_list
def create_dictionary(filename):
    data = read_file(filename)
    climate_dict = {}
    for line in data:
        if line:  # Ensure the line is not empty
            region, numbers = line.split(':')
            climate_dict[region.strip()] = get_numbers_list(numbers.strip())
    return climate_dict

data_dict = create_dictionary('rainfall1.csv')
for key in sorted(data_dict):
    print(key, data_dict [key])





def create_dictionary(filename):
    data = read_file(filename)
    climate_dict = {}
    for line in data:
        if line:  # Ensure the line is not empty
            region, numbers = line.split(':')
            climate_dict[region.strip()] = get_numbers_list(numbers.strip())
    return climate_dict