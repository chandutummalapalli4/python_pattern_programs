## for contionus alphabets
num=int(input("Enter N value:"))
for i in range(65,num+65):
    for j in range(65,i+1):
        print(chr(i),end=" ")
    print()