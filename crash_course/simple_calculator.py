operator = input("Enter preferred operator + - / * ")

if operator == '+':
    a = int(input("Enter a number to add ="))
    b = int(input("Enter a number to add ="))
    print(a+b)

elif operator == '-':
    a = int(input("Enter a number to subtract ="))
    b = int(input("Enter a number to subtract ="))
    print(a-b)

elif operator == '*':
    a = int(input("Enter a number to multiply ="))
    b = int(input("Enter a number to multiply ="))
    print(a*b)

elif operator == '/':
    a = int(input("Enter a number to divide ="))
    b = int(input("Enter a number to divide ="))
    print(a/b)

else:
    print("Invalid operator!!!")