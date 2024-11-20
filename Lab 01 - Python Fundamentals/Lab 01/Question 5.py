numbers_list = [1, 5, 12, 6, 7]
print(numbers_list)
def square_odds(numbers_list):
    for i in range(len(numbers_list)):
        if numbers_list[i] % 2 != 0:
            numbers_list[i] = numbers_list[i] ** 2
    return numbers_list
square_odds(numbers_list)
print(numbers_list)