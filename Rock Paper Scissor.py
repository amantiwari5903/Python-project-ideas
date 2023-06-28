import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"

    if (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!"

    return "Computer wins!"

def play_game():
    print("Welcome to the Rock, Paper, Scissors Game!")

    choices = ['rock', 'paper', 'scissors']

    while True:
        print("\nChoose your move: Rock, Paper, or Scissors (or 'Q' to quit)")
        user_choice = input().lower()

        if user_choice == 'q':
            break

        if user_choice not in choices:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(choices)

        print("You chose:", user_choice)
        print("Computer chose:", computer_choice)

        result = determine_winner(user_choice, computer_choice)
        print(result)

    print("Thank you for playing!")

play_game()
