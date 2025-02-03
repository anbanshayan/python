#My Simple Calculator
count = int(input("No of courses to be calculated = "))

gpa_sum = 0
credits_sum=0

for i in range(1,count+1):
    course = float(input("Enter Allocate GPA =>"))
    credits= int(input("Enter Credits for GPA =>"))
    current_gpa = course*credits

    gpa_sum += current_gpa
    credits_sum += credits

print("Your Average GPA is :",gpa_sum/credits_sum)
