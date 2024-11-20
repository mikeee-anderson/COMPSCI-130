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






display_histogram([0, 0, 10, 15, 85, 63, 0, 23])