import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Enter your choice: rock, paper, or scissors.")

    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    user_choice = input("Your choice: ").lower()

    print(f"Computer chose: {computer_choice}")

    if user_choice in choices:
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'paper' and computer_choice == 'rock') or
            (user_choice == 'scissors' and computer_choice == 'paper')
        ):
            print("Congratulations! You win!")
        else:
            print("Oops! Computer wins!")
    else:
        print("Invalid choice. Please choose rock, paper, or scissors.")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == 'yes':
        play_game()
    else:
        print("Thank you for playing!")

play_game()