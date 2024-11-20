
def get_dice_roll():
    while True:
        try:
            user_input = int(input("Enter a number between 1 and 6 inclusive: "))
            if 1 <= user_input <= 6:
                return user_input
        except (ValueError, TypeError):
            pass




print("Valid input: {}".format(get_dice_roll()))