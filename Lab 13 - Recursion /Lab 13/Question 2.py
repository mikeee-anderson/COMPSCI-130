def count_multiples_of_2(numbers):
    if len(numbers) == 0:
        return 0
    number = numbers[0]
    if number % 2 == 0:
        return 1 + count_multiples_of_2(numbers[1:])
    else:
        return count_multiples_of_2(numbers[1:])


print(count_multiples_of_2([20, 19, 31, 7, 41, 33, 26, 45, 2, 4, 22, 49, 40, 47]))
