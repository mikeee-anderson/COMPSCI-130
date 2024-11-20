line1 = '73.3, 66.1, 87.3, 99.4, 112.6, 126.4, 145.1, 118.4, 105.1, 100.2, 85.8, 92.8'
line2 = '76.3, 68.7, 79.4, 80.3, 99.7, 113.2, 118.2, 103.4, 91.5, 91.9, 85.0, 100.7'
def get_numbers_list(data):
    number_list = [float(value) for value in data.split(",")]
    return number_list


list1 = get_numbers_list(line1)
print(list1)
print(get_numbers_list(line2))
print(type(list1[0]))