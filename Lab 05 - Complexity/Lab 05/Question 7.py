def rate(n):
    total = 0
    i = 0
    count = 3  # Initialize the counter

    count += 1  # while i < n check
    while i < n:
        j = 8
        count += 1  # Each iteration of the while i < n loo
        count += 1  # while j > 1 check
        while j > 1:
            total += j
            count += 1  # total += j operation
            j //= 2
            count += 1  # j //= 2 operation
            count += 1  # while j > 1 check
        i += 1
        count += 1  # i += 1 operation
        count += 1  # while i < n check

    print(f"Number of operations: {count}")
    return total


# Example test
rate(2)

rate(2)