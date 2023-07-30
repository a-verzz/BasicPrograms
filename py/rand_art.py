import random

def generate_random_art(width, height):
    art = ""
    characters = ["@", "#", "*", "+", "-", "/", "\\"]
    for _ in range(height):
        row = [random.choice(characters) for _ in range(width)]
        art += "".join(row) + "\n"
    return art

if __name__ == "__main__":
    random_width = 30
    random_height = 10
    print(generate_random_art(random_width, random_height))