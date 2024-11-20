def read_file(sensor):
    input_file = open('{}.txt'.format(sensor), "r")
    file_data = input_file.read().split(",")
    input_file.close()
    sensor_data = [int(x) for x in file_data]
    return sensor_data






data = read_file('sensor_a')
print(data)
print(type(data))
print(type(data[0]))