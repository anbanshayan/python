#counting particualr no of elements
count=0
i=int(input("Enter a number = "))
j=int(input("Enter a number = "))
for i in range(i+1,j):
    if(i%2==0):
        count=count+1
print(count)
        