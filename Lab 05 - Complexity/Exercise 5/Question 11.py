
def rate(n):
    total = 0
    i = 0
    count = 4
    while i < n:
        j = 0
        while j < n:
            total += j
            j += 1
            count += 3
        i += 1
        count += 4
    print(f"Number of operations: {count}")
    return total


rate(2)