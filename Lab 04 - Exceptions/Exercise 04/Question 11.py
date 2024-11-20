
def calculate_mean(data):
    total = 0
    number = 0
    for element in data:
        try:
            total += element
            number += 1
        except TypeError:
            pass
    return total / number


print(calculate_mean([1,3,'a',4,5]))