def get_first_digit(username):
    for char in username:
        if char.isdigit():
            return int(char)

print(get_first_digit('mgra734'))