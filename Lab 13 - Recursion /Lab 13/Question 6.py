def get_fibonacci_term(n):
    if n == 0 or n == 1:
        return n
    return get_fibonacci_term(n - 1) + get_fibonacci_term(n - 2)

print(get_fibonacci_term(1))
print(get_fibonacci_term(2))
print(get_fibonacci_term(3))
print(get_fibonacci_term(4))