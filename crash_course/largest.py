#Write a program that takes three numbers as input and prints the largest of them.

num1 = int(input("Enter num1 "))
num2 = int(input("Enter num2 "))
num3 = int(input("Enter num3 "))

if num1 > num2:
    print(num1,"is greater than ",num2)

elif num2 > num3:
    print(num2,"is greater than ",num3)
elif num3>num2:
    print(num3,"is greater than ",num2)
elif num3>num1:
    print(num3,"is greater than ",num2)
