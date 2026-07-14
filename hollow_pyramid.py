rows = int(input("Enter rows: "))

for i in range(1, rows + 1):

    # Spaces
    for j in range(rows - i):
        print(" ", end="")

    # Pyramid
    for j in range(1, 2 * i):
        if i == 1 or i == rows or j == 1 or j == 2 * i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()