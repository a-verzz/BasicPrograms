import random
import string

def generate_random_password(length=12, include_digits=True, include_special_chars=True):
    chars = string.ascii_letters
    if include_digits:
        chars += string.digits
    if include_special_chars:
        chars += string.punctuation

    if length < 6:
        raise ValueError("Password length should be at least 6 characters.")

    return "".join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
    try:
        password_length = int(input("Enter the desired password length: "))
        include_digits = input("Include digits (y/n): ").lower() == 'y'
        include_special_chars = input("Include special characters (y/n): ").lower() == 'y'

        password = generate_random_password(password_length, include_digits, include_special_chars)
        print(f"\nYour random password: {password}")
    except ValueError as e:
        print(f"Error: {e}")
