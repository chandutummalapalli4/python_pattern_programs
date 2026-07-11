# * * * *
#   * * *
#     * *
#       *
rows=int(input("Enter row value:"))
for i in range(1,rows+1):
    for j in range(i-1):
        print(" ",end=" ")
    for j in range(rows-i+1):
        print("*",end=" ")   
    print()
            