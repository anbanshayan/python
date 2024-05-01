# question => write a program to read 10 numbers as input from user and find sum and average of them
a=[]
print("Enter 10 numbers")
for i in range(10):
    num=int(input("Enter number "+str(i+1)+" = "))
    a.append(num)
print(a)

sum=0
for i in a:
    sum=sum+i
avg=sum/len(a) #here len(a) is used to get the count of elements inside a
print("Sum = ",sum)
print("Average",avg)