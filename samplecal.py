#selecting operator in calculator
choices=['+','-','*','/','^','%','#','$']
seperator=','
print(seperator.join(choices))

#As you can see, the join method effectively combines the elements from the choices list into a single string separated by commas, achieving the desired output without square brackets.

sign=input("Choose your operand :")

if sign in choices:
#above lines chcks if entered is available in choices
    num1=int(input("Enter first number : "))
    num2=int(input("Enter second number : "))

else:
    print("Choose valid operand from",choices)

def add(a,b):
    print(a+b)

def subtract(a,b):
    print(a-b)

def multiply(a,b):
    print(a*b)

def divide(a,b):
    if b==0:
        print("Error!! Can't divide by 0")
    else:
        print(a/b)

def power(a,b):
    print(a**b)

def remainder(a,b):
    print(a%b)

def terminate():
    return choices
if sign=='+':
    result = add(num1,num2)

elif sign=='-':
    result = subtract(num1,num2)

elif sign=='*':
    result = multiply(num1,num2)

elif sign=='/':
    result = divide(num1,num2)

elif sign=='^':
    result = power(num1,num2)

elif sign=='/':
    result = remainder(num1,num2)