# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5 
# 6 6 6 6 6 6 
# 7 7 7 7 7 7 7 
# 8 8 8 8 8 8 8 8 
num=int(input("Enter a value:"))
for i in range(1,num+1):
    for j in range(i):
        print(i ,end=" ")
    print()    