#Write a program to take first particular count of numbers from zero  input and find their sum and average
#time slot 03:2~9:38 video time reference
sum=0
count=0
i=int(input("Enter count of numbers = "))
for i in range(0,i):
    i=i+1
    count=count+1
    sum=sum+i
    avg=sum/count
print(sum)
print(avg)