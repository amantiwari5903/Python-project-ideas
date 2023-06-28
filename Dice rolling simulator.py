import random

def roll_dice():
    return random.randint(1, 6)

def print_dice(dice_value):
    print("---------")
    print("|       |")
    print("|   {}   |".format(dice_value))
    print("|       |")
    print("---------")

def play_game():
    print("Welcome to the Dice Rolling Simulator Game!")

    while True:
        print("\nPress Enter to roll the dice or 'Q' to quit.")
        choice = input().lower()

        if choice == 'q':
            break

        dice_value = roll_dice()
        print_dice(dice_value)

    print("Thank you for playing!")

play_game()
