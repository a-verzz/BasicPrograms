def print_triangle_star(height):
    for i in range(1, height + 1):
        # Print spaces before the stars
        for j in range(height - i):
            print(" ", end="")
        
        # Print stars
        for k in range(2 * i - 1):
            print("*", end="")
        
        # Move to the next line
        print()

# Example usage:
print_triangle_star(5)
