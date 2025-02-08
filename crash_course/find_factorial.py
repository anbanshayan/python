#Find the factorial of a number.
num = int(input(("Enter a number to find its factorial = ")))
pdt = 1
for i in range(1,num+1):
    pdt *= i
print(pdt)