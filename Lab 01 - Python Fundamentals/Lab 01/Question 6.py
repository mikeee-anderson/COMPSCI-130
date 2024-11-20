values = [36, 19, 29, 42, 15, 15, 6, 15, 48, 48, 23, 31, 18, 2, 35, 24, 7]
def remove_multiples_of_3_but_not_2(numbers):
    for i in range(len(numbers)-1,-1,-1):
        if numbers[i] % 3 == 0 and numbers[i] % 2 != 0:
            numbers.pop(i)
    return numbers
remove_multiples_of_3_but_not_2(values)
print(values)