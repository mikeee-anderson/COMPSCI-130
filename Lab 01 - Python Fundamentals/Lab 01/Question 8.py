values = [78, 273, 230, 329]


def create_dictionary(numbers):
    dictionary = {}
    for number in numbers:
        prime = get_smallest_prime_factor(number)
        if prime not in dictionary:
            dictionary[prime] = []
            dictionary[prime].append(number)
        else:
            dictionary[prime].append(number)
    return dictionary

def get_smallest_prime_factor(number):
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19]
    for prime_number in prime_numbers:
        if number % prime_number == 0:
            return prime_number
    return -1

numbers_dictionary = create_dictionary(values)
for key in sorted(numbers_dictionary.keys()):
    print(key, numbers_dictionary[key])