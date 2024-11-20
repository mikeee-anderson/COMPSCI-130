def calculate_percentage_change(initial, revised):
    change = (revised - initial) / abs(initial) * 100
    return f"{change:.0f}"



print(calculate_percentage_change(60, 71))
print(calculate_percentage_change(71, 60))
print(calculate_percentage_change(-60, -71))
print(calculate_percentage_change(-71, -60))
print(calculate_percentage_change(-7, 1))
print(calculate_percentage_change(2, -5))