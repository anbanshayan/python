#Finding whether it's a prime number or not

num = int(input("Enter a number :"))

count = 0

for i in range(1,num+1):
    value = num % i

    if value == 0:
        count += 1

if count ==2:
    print("It's a prime number! :)")
else:
    print("No it's not a prime number :(")
