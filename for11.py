t_count=0
f_count=0
i=int(input("Enter a number = " ))
j=int(input("Enter a number = " ))
for i in range(i,j):
    if i%3==0 and i%5==0:
        t_count=t_count+1
        f_count=f_count+1
print("Count of numbers divisile by 3 between 1 and 100 = ",t_count)
print("Count of numbers divisile by 5 between 1 and 100 = ",f_count)