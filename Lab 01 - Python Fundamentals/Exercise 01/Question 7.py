source_list1 = [1,2,3]
print("before", source_list1)
def modify_list(numbers, value):
    numbers.append(value)
    return numbers
modify_list(source_list1, 4)
print("after", source_list1)