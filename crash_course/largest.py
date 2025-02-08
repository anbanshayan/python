#Write a program that takes three numbers as input and prints the largest of them.

num1 = int(input("Enter num1 "))
num2 = int(input("Enter num2 "))
num3 = int(input("Enter num3 "))

if num1 > num2 and num1 > num3:
    print(num1,"is greatest of all")

elif num2 >num3 and num2 > num1:
    print(num2, "is greatest of all")
    
else:
    print(num3, "is greatest of all")


