import time
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def digital_clock():
    print("Welcome to the Digital Clock!\n")
    
    while True:
        current_time = time.strftime("%H:%M:%S")
        print(f"\r{current_time}", end="")
        time.sleep(1)
        clear_console()

if __name__ == "__main__":
    digital_clock()
