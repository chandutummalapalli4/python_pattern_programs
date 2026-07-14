# * 
# * * 
# *   * 
# *     * 
# * * * * *
rows=int(input("Enter rows value:"))
for i in range(1,rows+1):
    for j in range(1,i+1):
        if(i==1 or i==rows or j==1 or j==i):
            print("*",end=" ")
        else:
            print(" ",end=" ")  
    print()        