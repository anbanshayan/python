#selecting operator in calculator
print("Select your operand : + - * /")

def add(a,b):
    print(a+b)

def subtract(a,b):
    print(a-b)

def multiply(a,b):
    print(a*b)

def divide(a,b):
    if b==0:
        print("Error!! can't divide by 0")
    else:
        print(a/b)

divide(1,0)