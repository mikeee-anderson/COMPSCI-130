number = int(input("Enter an integer: "))
series = 0
counter = 0
for i in range(number + 1):
    if i != 0:
        series += 1 / i
series = round(series, 1)
print(f"The sum is {series}")