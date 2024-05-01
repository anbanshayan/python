numbers = [3,2,5,7,8]
count = 0
for number in numbers:
    count+=1
    if number==5:
        break
else:
    count=-1
print(count)