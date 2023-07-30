import colorama
from colorama import Fore, Style
import time

def print_colorful_rainbow():
    colorama.init()

    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA, Fore.CYAN]
    spaces = " " * 7

    print("Get ready to see a colorful rainbow!\n")
    for color in colors:
        print(f"{spaces}{color}#####{Style.RESET_ALL}")
        time.sleep(0.5)

    colorama.deinit()

if __name__ == "__main__":
    print_colorful_rainbow()