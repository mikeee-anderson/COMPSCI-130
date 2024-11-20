def prompt_odd_larger(limit):
    while True:
        try:
            number = int(input(f"Enter an odd integer larger than {limit}: "))
            if number % 2 == 0:
                continue
            if number <= limit:
                continue
            else:
                return number
        except ValueError:
            print("Invalid input!")

value = prompt_odd_larger(29)
print(value)