def read_multiples_of_5(filename):
    try:
        valid_multiples = []
        input_file = open(filename, "r")
        numbers = input_file.read().split()
        input_file.close()
        for number in numbers:
            try:
                if int(number) % 5 == 0:
                    valid_multiples.append(int(number))
            except ValueError:
                pass
        return valid_multiples
    except FileNotFoundError:
        return(f"ERROR: The file '{filename}' does not exist.\n[]")


print(read_multiples_of_5('input.txt'))