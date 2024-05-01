age=int(input("Enter your age: "))

salary=int(input("Enter your salary : "))

if age<=25 and salary>=20000:
    loanAmount=int(input("Enter Your Loan Amount : Rs."))
    if loanAmount<=50000:
        print("You are elibible for loan!!")
    else:
        print("Maximum loan amount is Rs.50000")
else:
    print("Sorry you are not eligible :(")
