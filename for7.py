#printing even numbers between particular range.

i=int(input("Enter a number"))
j=int(input("Enter a number"))

for i in range(i+1,j):
    if i%2==0:
        print(i)