def read_school_census_data(filename):
    input_file = open(filename, "r")
    lines = input_file.read().split("\n")
    input_file.close()
    final_list = []
    for line in lines:
        updating_list = line.split(",")
        updating_list[1] = int(updating_list[1])
        updating_list[2] = int(updating_list[2])
        updating_list[3] = int(updating_list[3])
        updating_list = tuple(updating_list)
        final_list.append(updating_list)
    return final_list





data = read_school_census_data('data1.txt')
print(data)