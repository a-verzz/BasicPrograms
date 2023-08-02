def generate_multiplication_table(number):
    print(f"Multiplication Table for {number}\n")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

if __name__ == "__main__":
    try:
        num = int(input("Enter a number to generate its multiplication table: "))
        generate_multiplication_table(num)
    except ValueError as e:
        print(f"Error: {e}")
