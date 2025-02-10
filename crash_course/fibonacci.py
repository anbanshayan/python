num = int(input("Enter a value :"))

sum = 0


for i in range(1,num):
    prev = i-1
    next = prev-i
    result = prev + next
    print(result)
    result += 1