a=int(input("Enter Your First Number : "))
b=int(input("Enter Your Second Number : "))

operation =input("Add/Sub/Mul/Div :")

if(operation=="Add"):
    print("Sum = ",a+b)
elif(operation == "Sub"):
    print("Difference = ",a-b)
elif(operation =="Mul"):
    print("Mutiplication =",a*b)
else:
    print("Division = ",a/b)

print("Operation done!!")