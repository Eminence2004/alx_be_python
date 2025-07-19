# pattern_drawing.py

# Prompt user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop using while to handle rows
while row < size:
    # Inner loop using for to print asterisks in each row
    for _ in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
