def rate(n):
    total = 0
    i = 1
    count = 2 + 1
    while i < n:
        count +=3
        total += i
        i *= 2
    count += 1
    print(f"Number of operations: {count}")
    return total

rate(2)