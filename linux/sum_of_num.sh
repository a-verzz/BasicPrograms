#!/bin/bash

# Prompt the user for numbers
echo "Enter numbers (separated by spaces):"
read -a numbers

# Initialize the sum variable
sum=0

# Calculate the sum
for num in "${numbers[@]}"; do
  sum=$((sum + num))
done

# Display the sum
echo "The sum of the numbers is: $sum"

# End of the script
