def get_largest_prime_factor(number):
    prime_factors = [19, 17, 13, 11, 7, 5, 3, 2]
    for prime in prime_factors:
        if number % prime == 0:
            break
    return prime
print(get_largest_prime_factor(55))
