import Pet

#Saving user input in num_of_obj variable
num_of_obj = int(input("How many pets you want to have: "))

#creating empty list for pet objects 
pet_objs = []
QUESTION = "y"
#A for loop that runs the number of times user wanted to enter pets (from abov num_of_obj)
for i in range(num_of_obj):
    #saving pet name,age and type using mutator methods
    Pet.Pets.set_name, Pet.Pets.set_age, Pet.Pets.set_animal_type = input("\nEnter pet name, age and type separated by space ").split()
    #appending empty list with pet details
    pet_objs.append([Pet.Pets.set_name, Pet.Pets.set_age, Pet.Pets.set_animal_type ])

#pet_type varialbe extract pet type from pet_objs lists
pet_type = [col[2]for col in pet_objs]

while(QUESTION == "y"):
    j = 0
    #allowing user to enter his/her choice to view pets details
    user_request = input("Enter type of pet (dog or cat) or type all: ")
    if user_request not in pet_type:
        if user_request != "all":
            print("Sorry your pet is not found")
        else:
            print(pet_objs)
    else:
        for j in range(len(pet_type)):
            if pet_type [j] == user_request:
                print(pet_objs[j])

    QUESTION = input("To continue press y else n: ")