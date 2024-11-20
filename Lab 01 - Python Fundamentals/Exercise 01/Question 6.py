source_list2 = [1,2,3]
print("before", source_list2)
print("after")
def get_appended_list(numbers, value):
    new_list = []
    for numb in numbers:
        new_list.append(numb)
    new_list.append(value)
    return new_list



target_list = get_appended_list(source_list2, 4)
print("source", source_list2)
print("target", target_list)