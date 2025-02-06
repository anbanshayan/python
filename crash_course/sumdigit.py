#Sum of Digits of a Number

num = int(input("Enter some digits"))
num_list =[]
num_list.append(num)

sum = 0

for i in range(1,len(num_list)):
    sum += num_list[i]

print(sum)