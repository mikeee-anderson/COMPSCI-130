def read_file(sensor):
    input_file = open('{}.txt'.format(sensor), "r")
    file_data = input_file.read().split(",")
    input_file.close()
    sensor_data = [int(x) for x in file_data]
    return sensor_data
def correct_errors(data):
    for i in range(len(data)):
        if data[i] < 0:
            data[i] = 0
    return data
def display_histogram(data, width=20):
    print("Day|Rainfall Data")
    max_value = max(data)
    scale_factor = width / max_value
    number = 0
    for value in data:
        number += 1
        multiplier = round(value * scale_factor)
        bar_width = "*" * multiplier
        print("{:>3}|{}".format(number, bar_width))
def display_data(name, data, width=30):
    print(f"Data From: '{name}'")
    number = 0
    total = 0
    for value in data:
        number += 1
        total += value
    average = round(total / number, 2)
    print(f"Mean Rainfall: {average:.2f}")
    display_histogram(data, width)
    print("=" * (width + 4))
def main(sensor_names):
    for sensor in sensor_names:
        sensor_data = read_file(sensor)
        corrected_data = correct_errors(sensor_data)
        display_data(sensor, corrected_data, width=20)