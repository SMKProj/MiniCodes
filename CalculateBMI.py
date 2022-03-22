# Calculate BMI

try:
    weight = float(input("Enter your weight in (kg) : "))
    height = float(input("Enter your height in (m) : "))
    
    # Defining a max human height in meters
    MAX_HEIGHT = 2.5 
    if weight <= 0 or height <= 0:
        raise ValueError
    elif height > MAX_HEIGHT:
        raise TypeError
except ValueError:
    print("Your weight and height cant be 0. Please try again")
except TypeError:
    print("Please give input in mentioned units")
else:
    BMI = weight / (height * height)
    BMI_str = "{:.2f}".format(BMI)

    if BMI < 18.5:
        print("Your BMI is equal to (", BMI_str,") and therefore you are condidered under weight" )
    elif 18.5 <= BMI < 24.99:
        print("Your BMI is equal to (", BMI_str,")and therefore you are condidered  normal weight" )
    elif 25 <= BMI < 30:
        print("Your BMI is equal to (", BMI_str,")and therefore you are condidered  over weight" )
    elif BMI >= 30:
        print("You BMI is equal to (", BMI_str,") and you are therefore considered obese.")