size = int(input("Enter the size of the pattern: "))

row = 0

# While loop for each row
while row < size:
    # For loop for printing asterisks in one row
    for _ in range(size):
        print("*", end="")
    print()  # Move to the next line
    row += 1