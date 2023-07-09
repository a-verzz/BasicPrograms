# Creating a tuple
student = ("John Doe", 20, "Computer Science", 3.8)

# Accessing elements by index
print("Name:", student[0])
print("Age:", student[1])
print("Major:", student[2])
print("GPA:", student[3])

# Modifying a tuple element (not allowed, tuples are immutable)

# Concatenating tuples
more_info = ("ABC University",)
combined_tuple = student + more_info
print("Combined tuple:", combined_tuple)

# Length of the tuple
length = len(combined_tuple)
print("Length of the tuple:", length)

# Checking if an element exists
if "Computer Science" in combined_tuple:
    print("Computer Science exists in the tuple")

# Counting occurrences of an element
count = combined_tuple.count("John Doe")
print("Number of occurrences of 'John Doe':", count)

# Index of an element
index = combined_tuple.index(3.8)
print("Index of 3.8:", index)

# Converting a tuple to a list
student_list = list(combined_tuple)
print("Converted to list:", student_list)

# Converting a list back to a tuple
student_tuple = tuple(student_list)
print("Converted back to tuple:", student_tuple)
