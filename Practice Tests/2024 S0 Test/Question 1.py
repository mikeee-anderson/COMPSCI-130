def get_ascii_value(username):
    first = ord(username[0])
    last = ord(username[-1])
    return first + last


print(get_ascii_value('Akim161'))
print(get_ascii_value('mgra734'))
print(get_ascii_value('dng004'))
print(get_ascii_value('bcar035'))