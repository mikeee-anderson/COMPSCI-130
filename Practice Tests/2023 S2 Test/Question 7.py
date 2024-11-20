def validate(nhi_number):
    if len(nhi_number) != 7:
        raise ValueError(f"ERROR: '{nhi_number}' - Invalid length!")
    elif not nhi_number[:3].isalpha():
        raise ValueError(f"ERROR: '{nhi_number}' - does not start with 3 alphabetical letters!")
    elif not nhi_number[3:].isdigit():
        raise ValueError(f"ERROR: '{nhi_number}' - does not end with 4 digits!")
    else:
        return (nhi_number[:3], int(nhi_number[3:]))

try:
    print(validate('ab12345'))
except ValueError as e:
    print(e)
else:
    print("Well done!")