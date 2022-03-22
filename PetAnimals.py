class Pets:
    def __init__(self,name, type, age):
        self.__name = name
        self.__age = age
        self.__type = type
    
    #defining mutator methods
    def set_name(self,name):
        self.__name = name
    def set_animal_type(self,type):
        self.__type = type
    def set_age(self,age):
        self.__age = age
        
    #defining accessor methods
    def get_name(self): 
        return self.__name
    def get_animal_type(self): 
        return self.__type
    def get_age(self): 
        return self.__age

def main():
    num_pets = int(input("How many pets you want to have: "))
    list_of_pets = []
    for i in range(num_pets):
        Pets.set_name = input("Enter pet name: ")
        Pets.set_age = input("Enter pet age:")
        Pets.set_animal_type = input("Enter type of pet you have: ")
        list_of_pets.append([Pets.set_name, Pets.set_age, Pets.set_animal_type ])
        
    req = input("Enter type of pet to view: ")
    if req in [col[2]for col in list_of_pets]:
        print(list_of_pets)
    else:
        print("Sorry the pet is not found")

main()
        
