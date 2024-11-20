data = [0, 0, 10, 15, 85, 63, 0, 23]
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







display_data('sensor_a', data, 40)
display_histogram(data)