# String concatenation
str1 = "Hello, "
str2 = "world!"
result = str1 + str2
print(result)

# String repetition
str3 = "Python "
repeated_str = str3 * 3
print(repeated_str)

# String length
str4 = "Hello"
length = len(str4)
print("Length:", length)

# Accessing individual characters
str5 = "Python"
print(str5[0])  # Accessing first character
print(str5[-1])  # Accessing last character

# Slicing strings
str6 = "Hello, world!"
slice1 = str6[7:]  # Slicing from index 7 to the end
slice2 = str6[:5]  # Slicing from the start to index 5 (exclusive)
slice3 = str6[7:12]  # Slicing from index 7 to index 12 (exclusive)
print(slice1)
print(slice2)
print(slice3)

# String methods
str7 = "  Python Programming  "
print(str7.strip())  # Remove leading and trailing spaces
print(str7.lower())  # Convert to lowercase
print(str7.upper())  # Convert to uppercase
print(str7.startswith("Python"))  # Check if it starts with "Python"
print(str7.endswith("Programming"))  # Check if it ends with "Programming"
print(str7.replace("Python", "Java"))  # Replace "Python" with "Java"

# String splitting and joining
str8 = "Python,Java,C++,JavaScript"
split_list = str8.split(",")  # Split the string at commas
print(split_list)
joined_str = "-".join(split_list)  # Join the list elements with hyphen
print(joined_str)
