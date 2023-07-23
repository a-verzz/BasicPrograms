def is_prime(number):
    if number <= 1:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False

    return True

# Take user input
try:
    num_to_check = int(input("Enter a number to check if it's prime: "))
    if is_prime(num_to_check):
        print(f"{num_to_check} is a prime number.")
    else:
        print(f"{num_to_check} is not a prime number.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
