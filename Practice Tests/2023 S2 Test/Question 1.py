def get_number_and_increment(username):
    number_string = ""
    for char in username:
        if char.isdigit():
            number_string += char
    number = int(number_string)
    number += 1
    return number

print(get_number_and_increment('mgra734'))