e_count=0
o_count=0
i=int(input("Enter a number = "))
j=int(input("Enter a number = "))
for i in range(i,j+1):
    if i%2==0:
        e_count=e_count+1
    else:
        o_count=o_count+1
print("even : ",e_count)
print("odd : ",o_count)