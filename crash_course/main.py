number = int(input("I'm thinking a number! Try to guess the number I'm thinking of : "))

while(number != 25):
    number = int(input("Enter again any guess "))
    if (number>25):
        print("Your guess is high")
    else:
        print("Your guess is low")
    
print("Your guess is right!!")