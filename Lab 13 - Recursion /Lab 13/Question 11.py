def get_fibonacci_count(n):
    if n == 0:
        return (0, 0)
    elif n == 1 or n == 2:
        return (1, 0)
    else:
        fb1, count1 = get_fibonacci_count(n - 1)
        fb2, count2 = get_fibonacci_count(n - 2)
    return (fb1 + fb2, count1 + count2 + 2)


# Test cases
data = get_fibonacci_count(3)
print(type(data))
print(data)
print(get_fibonacci_count(1))
print(get_fibonacci_count(2))