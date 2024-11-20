try:
    filename = input("Enter a filename:")
    input_file = open(filename, 'r')
    data = input_file.read().split()
    print("The first word is:", data[0])
    print("DONE")
except FileNotFoundError:
    print(f"ERROR: The file '{filename}' does not exist.")
    print("DONE")