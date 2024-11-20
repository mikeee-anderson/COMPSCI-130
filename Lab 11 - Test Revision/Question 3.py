def remove_multiples_of_2_but_not_7(numbers):
    for i in range(len(numbers)-1,-1,-1):
        if numbers[i] % 2 == 0:
            if numbers[i] % 7 == 0:
                pass
            else:
                numbers.pop(i)
    return numbers


data = [44, 44, 10, 16, 4, 34, 6, 48, 33, 21, 37, 44, 43]
remove_multiples_of_2_but_not_7(data)
print(data)
print(type(data))