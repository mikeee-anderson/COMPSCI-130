def get_last_letter(username):
    for char in username[::-1]:
        if char.isalpha():
            break
    return char



print(get_last_letter('Akim161'))
print(get_last_letter('mgra734'))
print(get_last_letter('dng004'))
print(get_last_letter('bcar035'))

print(get_last_letter('brob123'))
print(get_last_letter('eli923'))
print(get_last_letter('trob264'))