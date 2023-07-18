#!/bin/bash

# This script calculates the sum of numbers from 1 to a given positive integer using a loop

# Function to calculate the sum
calculate_sum() {
  local num=$1
  local sum=0

  for ((i = 1; i <= num; i++)); do
    sum=$((sum + i))
  done

  echo "$sum"
}

# Main script starts here
echo "Sum Calculator"
echo "Please enter a positive integer:"
read number

# Validate the input for positive integers
if ! [[ "$number" =~ ^[1-9][0-9]*$ ]]; then
  echo "Invalid input! Please enter a positive integer."
  exit 1
fi

result=$(calculate_sum "$number")

echo "The sum of numbers from 1 to $number is: $result"
