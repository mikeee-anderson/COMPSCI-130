def print_names_and_weights(names, weights):
    print("{:10}{}".format("Name", "Weight"))
    print("-"*16)
    for i in range(len(names)):
        spacer = 10 - len(names[i])
        seperator = " " * spacer
        print(f"{names[i]}{seperator}{round(weights[i], 2)}")


print_names_and_weights(['Bill', 'Helen', 'Michael'], [76.27, 54.61, 67.92])