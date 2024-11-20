def correct_errors(data):
    for i in range(len(data)):
        if data[i] < 0:
            data[i] = 0
    return data

print(correct_errors([0, -5, 10, 15, 85, 63, 0, 23]))