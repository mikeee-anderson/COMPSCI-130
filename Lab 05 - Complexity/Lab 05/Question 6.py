def rate(n):
    total = 0
    i = 0
    count = 2

    count += 1  # Initial check of while i < n
    while i < n:
        count += 1  # for while i < n check
        j = n
        count += 1  # for j = n
        while j > 0:
            count += 1  # for while j > 0 check
            total += j
            count += 1  # for total += j
            j -= 1
            count += 1  # for j -= 1
        count += 1  # for the while j > 0 check that fails
        i += 1
        count += 1  # for i += 1
    count += 1  # for the while i < n check that fails

    print(f"Number of operations: {count}")
    return total

# Example test
rate(2)  # Should print "Number of operations: 24"
