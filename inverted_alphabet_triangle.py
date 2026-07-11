## for inverted triangle
num = int(input("Enter N value: "))

for i in range(num + 64, 64, -1):
    for j in range(65, i + 1):
        print(chr(j), end=" ")
    print()