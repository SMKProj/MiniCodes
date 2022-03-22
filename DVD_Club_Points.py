#Video Club Points

#Inpt number of vidoes pruchased this month
num_Vid = input("Enter number of videos purchased this month: ")
#Point System Calculation With Error Handling

try:
    num_Vid = int(num_Vid) # try convert into Integer
    if num_Vid < 0:
        raise ValueError
    else:
        if num_Vid == 0:
            print("Sorry. You get 0 p0ints for this month of purchase")
        elif num_Vid == 1:
            print("You are awarded 5 points for this month of purchase")
        elif num_Vid == 2:
            print("You are awarded 15 points for this month of purchase")
        elif num_Vid == 3:
                print("You are awarded 30 points for this month of purchase")
        elif num_Vid >= 4:
            print("You are awarded 60 points for this month of purchase")
except ValueError:
    print("Wrong input variable type",
          "please supply integer", sep = "\n")