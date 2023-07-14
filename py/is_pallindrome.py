def is_palindrome(word):
    # Remove spaces and convert to lowercase for case-insensitive comparison
    word = word.replace(" ", "").lower()
    reversed_word = word[::-1]  # Reverse the word

    if word == reversed_word:
        return True
    else:
        return False

# Check if a word or phrase is a palindrome
word = input("Enter a word or phrase: ")
if is_palindrome(word):
    print(f"{word} is a palindrome!")
else:
    print(f"{word} is not a palindrome.")