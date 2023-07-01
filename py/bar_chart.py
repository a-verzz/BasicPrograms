import matplotlib.pyplot as plt

# Data for the bar chart
people = [' P', 'Q', 'R', 'S']
age = [16, 2, 34, 18]

# Create a bar chart
plt.bar(people,age)

# Add labels and title
plt.xlabel('People')
plt.ylabel('Age')
plt.title('Bar Chart')

# Display the bar chart
plt.show()
