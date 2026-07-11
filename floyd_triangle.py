# 1
# 2 3
# 4 5 6
# 7 8 9 10

num=int(input(" Enter a value:"))
number = 1 
for i in range(1, num + 1):
    for j in range(i):
        print(number, end=" ")
        number += 1
    print()    