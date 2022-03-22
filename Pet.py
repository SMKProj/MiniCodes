#Exercise 2: Pet Class Write a class named Pet, that has the following data attributes:
#name of pet, pets age and its type.write a program that can create objects of the class 
# and prompts the user to enter the name, type, and age of his or her pet. 
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