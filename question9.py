#Write a program to display the cube of number up to an integer
i=int(input("Enter count of number that should be cubed from zero  = "))
for i in range (1,i+1):
    cube=i**3
    print("Cube of "+str(i)+" is "+str(cube))