name = input("Enter your full name: ")
full_name = name.split()
letter = full_name[0][0]
output = f"{letter}. {full_name[1]}"
print("=" * len(output))
print(output)
print("=" * len(output))