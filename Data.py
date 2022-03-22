#Exercise 1: Personal Information Class 
# Design a class that holds the following personal data: name, address, age 
# and phonenumber. Write appropriate accessor and mutator methods. 
# Also, create a program that creates three instances of the class. 
# One instance should hold your information, and the other two should 
# hold your friends’ or family members’ information
class Records:
    def __init__(self,name, address, age, phone ):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone
    
    #defining mutator methods
    def set_name(self,name):
        self.__name = name
    def set_address(self,address):
        self.__address = address
    def set_age(self,age):
        self.__age = age
    def set_phone(self,phone):
        self.__phone = phone
        
    #defining accessor methods
    
    def get_name(self): 
        return self.__name
    def get_address(self): 
        return self.__address
    def get_age(self): 
        return self.__age
    def get_phone(self): 
        return self.__phone
    
    def __str__(self):
        return '\n' + "Hej! Mitt namn är:" + self.__name + ". Jag bor i " + self.__address + ". Jag är " + self.__age + " år gammal och mitt telefonnummer är " + self.__phone
    