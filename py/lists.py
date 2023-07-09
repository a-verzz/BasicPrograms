# Creating a list
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Accessing elements by index
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Modifying elements
fruits[1] = "grape"
print("Updated list:", fruits)

# Adding elements
fruits.append("fig")
print("List after appending 'fig':", fruits)

# Removing elements
removed_fruit = fruits.pop(2)
print("Removed fruit:", removed_fruit)
print("List after removing element at index 2:", fruits)

# Slicing lists
sliced_list = fruits[1:4]
print("Sliced list:", sliced_list)

# Concatenating lists
more_fruits = ["guava", "honeydew"]
combined_list = fruits + more_fruits
print("Combined list:", combined_list)

# Length of the list
length = len(combined_list)
print("Length of the list:", length)

# Checking if an element exists
if "apple" in combined_list:
    print("Apple exists in the list")

# Counting occurrences of an element
count = combined_list.count("banana")
print("Number of occurrences of 'banana':", count)

# Sorting the list
combined_list.sort()
print("Sorted list:", combined_list)

# Reversing the list
combined_list.reverse()
print("Reversed list:", combined_list)

# Removing all elements
combined_list.clear()
print("List after clearing:", combined_list)
