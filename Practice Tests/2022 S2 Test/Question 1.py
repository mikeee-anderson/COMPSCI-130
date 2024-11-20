def is_multiple_of_3(username):
    if len(username) == 7:
        number = int(username[4:])
    else:
        number = int(username[3:])
    if number % 3 == 0:
        return True
    else:
        return False


print(is_multiple_of_3('mand341'))
print(is_multiple_of_3('mgra734'))
print(is_multiple_of_3('dng134'))
print(is_multiple_of_3('bcar735'))