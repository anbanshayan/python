#Swap two numbers without using a third variable.

x = int(input("Value 1 = "))
y = int(input("Value 2 ="))


# diff = abs(x-y)

if x >y:
    print("Value 1 after swapping => ",x-abs(x-y))
    print("Value 2 after swapping => ",y+abs(x-y))

else:
    print("Value 1 after swapping => ",x+abs(x-y))
    print("Value 2 after swapping => ",y-abs(x-y))

