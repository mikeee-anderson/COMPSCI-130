def sum_of_multiples_of_5(numbers, start_index, end_index):
    try:
        total = 0
        for i in range(start_index, end_index + 1):
            numbers[i] = int(numbers[i])
            if numbers[i] % 5 == 0:
                total += numbers[i]
        return total
    except IndexError:
        return("ERROR: Out of range!\n0" )
    except ValueError:
        return("ERROR: Invalid number!\n0")

list1 = [1, 5, 9, 2, 8, 5, 10, 6]
print(sum_of_multiples_of_5(list1, 5, 6)) #5+10

list1 = [5, 2, 15]
print(sum_of_multiples_of_5(list1, 2, 6))

list2 = [1, 'A', 5]
print(sum_of_multiples_of_5(list2, 1, 2))





