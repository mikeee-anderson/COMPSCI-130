filename = input("Enter a filename: ")
input_file = open(filename, "r")
lines = input_file.readlines()
input_file.close()
for line in lines:
    words = line.split()
    text = ""
    for word in words:
        text += word[0]
    print(text)






