num = int(input("how many numbers do you want to enter ? "))

lst = []

for i in range(1,num+1):
    no = int(input("Enter a nuber"))
    lst.append(no)
    
#Printing entire list
print(lst)

# Priting sum of numbers with in list
print(sum(lst))

#Printing maximum of list
print(max(lst))

#Printing minimum of list

print(min(lst))