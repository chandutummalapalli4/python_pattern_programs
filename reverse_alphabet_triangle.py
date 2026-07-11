num = int(input("Enter N value: "))

for i in range(1, num + 1):
    for j in range(64 + num, 64 + num - i, -1):
        print(chr(j), end=" ")
    print()
    