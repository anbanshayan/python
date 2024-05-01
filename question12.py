# this code output will be 
# 1
# 12
# 123
i=int(input("Enter a number : "))
for i in range(1,i+1):
    print()
    for j in range(1,i+1):
        print(j,end="")
