#This file contains basics of python

# Variables and data types
name = "a-verzz"
age = 22
height = 1.75
life_student = True

# Conditional statements
print("Conditional statements\n")
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Functions
print("\nFuntions\n")
def greet(name):
    print("Hello, " + name + "!")
greet("Mr Developer")

# Functions and loops
print("\nPattern\n")
def pattern(line):
    for i in range(1, line + 1):
        print('*' * i)
line = 5
pattern(line)
    

# List
print("\nList\n")
cities = ["agra", "delhi", "jaipur"]
cities.append("pune")
print(cities[2])

# Dictionaries
print("\nDictionaries\n")
developer = {"name": "A-Verzz", "age": 22, "is_student": False}
print(developer["name"])


# File handling
print("\ncheck example.txt file created\n")
file = open("example.txt", "a+")
file.write("Hello, World!\n")
file.close()
