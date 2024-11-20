def no_evens_or_multiples_of_3(numbers):
    if numbers == []:
        return True
    if numbers[0] % 2 != 0 and numbers[0] % 3 != 0 and no_evens_or_multiples_of_3(numbers[1:]):
        return True
    else:
        return False

print(no_evens_or_multiples_of_3([1, 5, 7]))
print(no_evens_or_multiples_of_3([1, 15, 5, 2]))
print(no_evens_or_multiples_of_3([1, 4, 6]))
print(no_evens_or_multiples_of_3([]))
print(no_evens_or_multiples_of_3([2, 4, 6]))