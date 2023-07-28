import random

def word_guessing_game():
    words = ["apple", "banana", "cherry", "grape", "orange", "strawberry", "watermelon"]
    secret_word = random.choice(words)
    guessed_letters = set()
    attempts = 6

    print("Welcome to the Word Guessing Game!")
    print("Guess the secret word. It's a fruit name.")

    while attempts > 0:
        display_word = "".join(letter if letter in guessed_letters else "_" for letter in secret_word)
        print("Word:", display_word)

        if display_word == secret_word:
            print("Congratulations! You guessed the word:", secret_word)
            break

        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        else:
            guessed_letters.add(guess)
            if guess not in secret_word:
                attempts -= 1
                print("Incorrect guess. Attempts remaining:", attempts)

    if attempts == 0:
        print("Sorry, you've run out of attempts. The secret word was:", secret_word)

word_guessing_game()
