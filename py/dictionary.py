# Creating a dictionary
student = {
    "name": "John Doe",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8
}

# Accessing values by keys
print("Name:", student["name"])
print("Age:", student["age"])
print("Major:", student["major"])
print("GPA:", student["gpa"])

# Modifying values
student["age"] = 21
student["gpa"] = 3.9
print("Updated Age:", student["age"])
print("Updated GPA:", student["gpa"])

# Adding a new key-value pair
student["university"] = "ABC University"
print("University:", student["university"])

# Removing a key-value pair
del student["major"]
print("Dictionary after removing 'major':", student)

# Checking if a key exists
if "age" in student:
    print("Age exists in the dictionary")

# Getting all keys and values
keys = student.keys()
values = student.values()
print("Keys:", keys)
print("Values:", values)

# Iterating through keys and values
for key, value in student.items():
    print(key, ":", value)

# Clearing the dictionary
student.clear()
print("Dictionary after clearing:", student)
