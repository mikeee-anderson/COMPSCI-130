fruits = ['avocado', 'apple', 'blackcurrant', 'banana']
def create_string_lengths_dictionary(fruits):
    dictionary = {}
    for fruit in fruits:
        dictionary[fruit] = len(fruit)
    return dictionary

print(create_string_lengths_dictionary(fruits))
