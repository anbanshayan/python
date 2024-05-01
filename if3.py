marks1=int(input("Enter your first marks = "))

marks2=int(input("Enter your second marks = "))

marks3=int(input("Enter your third marks = "))

total=marks1+marks2+marks3

average=total/3

if average>=75:
    print("Distinction")
elif average>65 and average<75:
    print("Good")
elif average>55 and average<65:
    print("Pass")
else :
    print("Time to re-attempt")
