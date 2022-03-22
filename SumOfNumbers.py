#Write a program using a while loop and within the loop asks the user 
# to enter a series of positive numbers. The user should enter a negative 
# number to signal the end of the series. After all the positive numbers 
# have been entered, the program should display their sum.
num = 1
series = []
try:
    while(num >= 0):
        num = int(input("Enter positive number: "))
        if num < 0:
            print("You have entered negative number")
        else:
            series.append(num)
            print("You have entered: ", series, "\t")
            print("To continue enter positive number for (yes) and negative for (no) ")
    else:
        print("The final series contains: ", series)
except ValueError:
    print("Please input integers only")

    
    
