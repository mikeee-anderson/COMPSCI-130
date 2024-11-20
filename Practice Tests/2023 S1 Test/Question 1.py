def get_greeting(username):
    number = ""
    for char in username:
        if char.isdigit():
            number += char
    return f"Hello agent {number}"

print(get_greeting('mgra734'))
print(get_greeting('dng134'))
print(get_greeting('bcar735'))
print(get_greeting('mand341'))
