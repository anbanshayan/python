#Check palindrome

txt = input("Enter something: ")

rev_txt = txt[::-1]

if (txt == rev_txt):
    print("This is palindrome!!")
else:
    print("This is not palindrome")