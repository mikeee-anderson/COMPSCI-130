def read_numbers_list(filename):
    try:
        input_file = open(filename, "r")
        lines = input_file.read().split("\n")
        final_list = []
        for line in lines:
            updated_list = []
            numbers = line.split(",")
            for number in numbers:
                number = number.strip()
                if number != '':
                    updated_list.append(int(number))
            if updated_list != []:
                final_list.append(updated_list)
        return final_list
    except FileNotFoundError:
        print(f"ERROR: The file '{filename}' does not exist.")
        return []


print(read_numbers_list('numbers1.txt'))
print(read_numbers_list('input_unknown.txt'))