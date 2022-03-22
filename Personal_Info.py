class Information:
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
        return '\n' + self.__name + '\n' + self.__address + '\n' + self.__age + '\n' + self.__phone

def main():
    person1 = Information("Samantha", "Germany", "23", "0300512324")
    print(person1)
    print(type(person1))
    
    person2 = Information("Anna", "SwitzerLand", "18", "050324561")
    print(person2)
    
    person3 = Information("Henry", "America", "25", "0345257432")
    print(person3)
    
main()