def get_sum_cubes(numbers):
    if numbers ==  []:
        return 0
    return numbers[0] ** 3 +  get_sum_cubes(numbers[1:])


numbers = [-1, 4, 5, 9, 11]
print(get_sum_cubes(numbers))
