def input_number_in_range(min_value, max_value):
    while True:
        try:
            number = int(input(f"Enter a number between {min_value} and {max_value}: "))
            if min_value <= number <= max_value:
                return number
        except ValueError:
           print("ERROR: Invalid input!")
           pass

print(input_number_in_range(40, 147))