num = int(input("how many numbers do you want to enter ? "))

lst = []

for i in range(1,num+1):
    no = int(input("Enter a nuber"))
    lst.append(no)
    
#Printing C
print(lst)
print(sum(lst))
print(max(lst))
print(min(lst))