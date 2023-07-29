import random

def dice_rolling_game():
    print("Welcome to the Dice Rolling Game!")
    input("Press Enter to roll the dice...")

    player_roll = random.randint(1, 6)
    computer_roll = random.randint(1, 6)

    print("You rolled:", player_roll)
    print("Computer rolled:", computer_roll)

    if player_roll % 2 == 0:
        print("Congratulations! You win!")
    else:
        print("Sorry, the computer wins. Better luck next time!")

dice_rolling_game()