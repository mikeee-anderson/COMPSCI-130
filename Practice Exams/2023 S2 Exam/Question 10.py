def create_code_dictionary(usernames_list):
    try:
        dictionary = {}

        for username in usernames_list:
            if len(username) >= 3 and username[-3:].isdigit():
                code = sum([int(digit) for digit in username[-3:]])
                if code not in dictionary:
                    dictionary[code] = [username]
                else:
                    dictionary[code].append(username)
            else:
                print(f"ERROR: {username} is invalid.")

            for key in dictionary:
                dictionary[key].sort()

            sorted_dict = dict(sorted(dictionary.items()))
        return sorted_dict
    except ValueError:
        print(f"ERROR: {username} is invalid.")
        pass


values = ['eli923', 'trob', 'brob123', 'agas321', 'aana554', 'nbro495', 'hcho402', 'afin02', 'jchu086']
code_dict = create_code_dictionary(values)
for key in sorted(code_dict):
    print(key, code_dict[key])