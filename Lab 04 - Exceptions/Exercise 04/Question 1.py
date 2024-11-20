
try:
    age = int(input('Enter an age: '))
    print('Your age is', int(age))
except ValueError:
    print("ERROR: Invalid age!")
