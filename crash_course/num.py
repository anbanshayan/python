def oddEven(num):
    if(num % 2 ==0):
        print(num," is an even number")
    else:
        print(num, "is an odd number")

oddEven(52)

n = int(input("Enter a number"))

while(n != 25):
    if(n>25):
        print("Your guess is high")
    elif(n<25):
        print("Your guess is low")
    
    n = int(input("Try again : "))

print("Congrats!! You have guessed the right one")

