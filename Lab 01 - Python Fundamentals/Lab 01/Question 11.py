integer = int(input("Enter an integer between 1 and 9: "))
while integer < 1 or integer > 9:
    integer = int(input("Enter an integer between 1 and 9: "))

print("EVEN" if integer % 2 == 0 else "ODD")