#Implement a function to sort a list of numbers without using built-in sort functions.

num = int(input("How many do you wish to enter = "))

list = []

for i in range(1,num+1):
    digit = int(input("Enter a number "))
    list.append(digit)

print(list)
max = []
for m in range(1,num+1):
    if list[0] < list[m]:
        max.append(list[m])

print(max)