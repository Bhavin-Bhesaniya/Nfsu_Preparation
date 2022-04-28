#OOPS
'''
- Object-oriented programming aims to implement real-world entities like inheritance, hiding, polymorphism, etc in programming. The main aim of OOP is to bind together the data and the functions that operate on them so that no other part of the code can access this data except that function.

'''


'''

What is class
A Class is like an object constructor, or a "blueprint" for creating objects.
Classes provide a means of bundling data and functionality together.
Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. 
Class instances can also have methods (defined by their class) for modifying their state.
Class creates a user-defined data structure, which holds its own data members and member functions, which can be accessed and used by creating an instance of that class.

Note:-
Attributes are the variables that belong to a class.
Attributes are always public and can be accessed using the dot (.) operator

What is Objects
Instance of a class

class is a blueprint while instance is a copy of the class with actual values

state - attribute of an object
behaviout - methods of object
identity - unique name
'''


'''
class MyClass:
    x = "My Method"         #assign value or say attribute
    y = "Second Attributes"

    def first_method(self):         #First Method create
        print("first is ",self.x)
        print("Second is ",self.y)
        
CreateObject = MyClass() #Create object and initialize to MyClass or share attr and behviour

#Accessing class attribute by object
print(CreateObject.x,"\n")

#Accessing class methods by object
CreateObject.first_method()
'''


''' 
THE SELF
- Class methods must have an extra first parameter in the method definition. We do not give a value for this parameter when we call the method, Python provides it.
ex :- When we call a method of this object as myobject.method(arg1, arg2), this is automatically converted by Python into MyClass.method(myobject, arg1, arg2) – this is all the special self is about.
'''



''' 
__init__ function 
  All classes have a function called __init__(), which is always executed when the class is being initiated.
  Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
  Similar to constructor their used to initallizing the object state
  useful to do any initallizing
'''

class Init_class:
    def __init__(self,name):
        self.name = name        #instance variable
    def first_method(self):
        print("first is metod here",self.name)
P = Init_class("bhavin")
P.first_method()

#Instance variables are variables whose value is assigned inside a constructor or method with self whereas class variables are variables whose value is assigned in the class
class Init_class:
    NAME = "BHAVIN"             #Class variable
    def __init__(self,name,lname):
        self.name = name        #instance variable
        self.lname = lname
    def first_method(self):
        print("first is metod here",self.name)
        print("second variable accesss",self.lname)
P = Init_class("bhavin","bhasaniya")
print("here : ",P.name)
print("class : ",P.NAME) #access by object 
print("last" , P.lname) #access instance variable
print(Init_class.NAME)  #access class variable with class name

#Accessing class
class method_use:
     NAME = "BHAVIN"

     def __init__(self,name):
         self.name = name

     def setColor(self,color):
         self.color = color

     def getColor(self):
         return self.color

c1 = method_use("Cyber")
c1.setColor("Black")    #set the object
print(c1.getColor())
del c1.setColor         #delete obj
#print(c1.setColor())