def main():
    print_title()
    regions_file = input("Enter a filename for reading regions: ")
    regions_data = read_file(regions_file)
    regions_dict = create_regions_dictionary(regions_data)
    rainfall_file = input("Enter a filename for reading rainfall data: ")
    rainfall_dict = create_dictionary(rainfall_file)
    regions_dict = merge_data(regions_dict, rainfall_dict)
    min_temp_file = input("Enter a filename for reading minimum temperature data: ")
    min_temp_dict = create_dictionary(min_temp_file)
    regions_dict = merge_data(regions_dict, min_temp_dict)
    max_temp_file = input("Enter a filename for reading maximum temperature data: ")
    max_temp_dict = create_dictionary(max_temp_file)
    regions_dict = merge_data(regions_dict, max_temp_dict)
    sunshine_file = input("Enter a filename for reading sunshine data: ")
    sunshine_dict = create_dictionary(sunshine_file)
    regions_dict = merge_data(regions_dict, sunshine_dict)
    column_names = ['Rainfall(mm)', 'Min.Temperature', 'Max.Temperature', 'Sunshine(hr)']
    print_table(regions_dict, column_names)

# Copy all your functions here

def print_title():
    print("Average Rainfall, temperature and sunshine data for selected locations throughout NZ")
    print("====================================================================================")


def create_regions_dictionary(regions_list):
    regions_dict = {}
    for region in regions_list:
        regions_dict[region] = []
    return regions_dict


def merge_data(regions_dict, data_dict):
    for key in data_dict:
        if key in regions_dict:
            total_data = sum(data_dict[key])
            number_of_points = len(data_dict[key])
            average = round(total_data / number_of_points, 2)
            regions_dict[key].append(average)
    return regions_dict


def read_file(filename):
    with open(filename, "r") as input_file:
        data = input_file.read().strip().split("\n")
    return data


def create_dictionary(filename):
    data = read_file(filename)
    climate_dict = {}
    for line in data:
        if line:
            region, numbers = line.split(':')
            climate_dict[region.strip()] = get_numbers_list(numbers.strip())
    return climate_dict


def get_numbers_list(data):
    return [float(value) for value in data.split(",")]


def print_table(regions_dict, column_names):
    print(f"{'Name':>16}|{column_names[0]:>16}|{column_names[1]:>16}|{column_names[2]:>16}|{column_names[3]:>16}|")
    for key, value in sorted(regions_dict.items()):
        print(f"{key:>16}|{value[0]:>16.2f}|{value[1]:>16.2f}|{value[2]:>16.2f}|{value[3]:>16.2f}|")

