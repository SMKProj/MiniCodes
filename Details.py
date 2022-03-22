#importing Data.py file
import Data

#Creating an intances of class using filename.classname
d1 = Data.Records('John', 'Borlange', '22', '12345')
d2 = Data.Records('Alice', 'Stockholm', '20', '11123')
d3 = Data.Records('Mia', 'Gotheborg', '18', '56432')

print(type(d1))
#I have decided to print above objects in two ways:

#By calling accessor functions for each object in print
print("\n Hello! My name is:", d1.get_name(),". I live in ", d1.get_address(),". I am ", d1.get_age(), "years old and my phone number is ", d1.get_phone() )
print("\n Hi! My name is:", d2.get_name(),". I am ", d1.get_name(), "friend. I live in ", d2.get_address(),"." "I am ", d2.get_age(), "years old and my phone number is ", d2.get_phone() )
print("\n Hej! Mitt namn är:", d3.get_name(),". Jag bor i ", d3.get_address(),". Jag är ", d3.get_age(), "år gammal och mitt telefonnummer är ", d3.get_phone() )

print("-----------------------------------------------------------")

#By passing list of objects to __str__ function in main class for printing
d = [d1,d2,d3]
for index in d:
    print(index, '\n')
    
