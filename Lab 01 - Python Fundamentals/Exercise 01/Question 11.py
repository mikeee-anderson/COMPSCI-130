filename = input("Enter a filename: ")
input_file = open(filename, "r")
words = input_file.read().split()
text = ""
for word in words:
    text += word[0]
input_file.close()
print(text)