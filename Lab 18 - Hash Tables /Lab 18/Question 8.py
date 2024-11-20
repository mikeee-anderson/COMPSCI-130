def get_prefix_hash(key, table_size):
    sum = 0
    if len(key) > 5:
        for pos in range(5):
            sum = sum + ord(key[pos])
        return sum % table_size
    else:
        for pos in range(len(key)):
            sum = sum + ord(key[pos])
        return sum % table_size

print(get_prefix_hash('cat', 13))
print(get_prefix_hash('dog', 13))
print(get_prefix_hash('expected', 13))
print(get_prefix_hash('output', 13))