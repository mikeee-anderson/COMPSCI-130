def read_countries(filename):
    try:
        input_file = open(filename, "r")
        lines = input_file.read().split("\n")
        input_file.close()
        countries_dict = {}
        for line in lines:
            line = line.strip()
            if not line:  # Skip empty lines
                continue
            try:
                pair = line.split(",")
                countries_dict[pair[0]] = pair[1]
            except IndexError:
                print(f"ERROR: Invalid '{line}'!")
                pass
        return countries_dict
    except FileNotFoundError:
        return f"ERROR: The file '{filename}' does not exist.\n{{}}"


print(read_countries('countries.txt'))