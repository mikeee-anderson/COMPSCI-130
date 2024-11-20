
def calculate_mean(data):
    total = 0
    for element in data:
        try:
            total += element
        except TypeError:
            print("Error: Invalid number found!")
            return None
    return total / len(data)