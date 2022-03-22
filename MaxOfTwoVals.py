#Exercise 5: Maximum of Two Values 
# Write a function named my_max
# that accepts two integer values as arguments and returns the 
# value that is the greater of the two. For example, if 12 and 19 
# are passed as arguments to the function, the function should return 19. 
# Use the function in a program that prompts the user to enter two integer values. 
# The program should display the value that is the greater of the two.

def my_max(x,y):
    if x>y:
        return x
    else:
        return y

try:
    x = int(input("Enter first value: "))
    y = int(input("Enter second value: "))

except ValueError:
    print("You are requested to input integer values only")

else:
    greater_val = my_max(x,y)
    print("The ", greater_val, "is the greater value out of two entered values")