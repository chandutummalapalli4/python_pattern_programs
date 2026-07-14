
rows = int(input("Enter rows: "))

# Upper half (including middle row)
for i in range(1, rows + 1):

    # Spaces
    for j in range(rows - i):
        print(" ", end="")

    # Hollow pyramid
    for j in range(1, 2 * i):
        if i == 1 or  j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower half
for i in range(rows - 1, 0, -1):

    # Spaces
    for j in range(rows - i):
        print(" ", end="")

    # Hollow inverted pyramid
    for j in range(1, 2 * i):
        if i == 1 or j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()