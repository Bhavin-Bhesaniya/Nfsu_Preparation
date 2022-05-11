# OOPS
'''
 - Object-oriented programming implement real-world entities like inheritance, hiding, polymorphism etc in programming 
 - Main aim of OOP is to bind data and function together so that no other part of ode can access this data except 
   that function
'''

class MyClass:
    x = "My Method"  # assign value or say attribute
    y = "Second Attributes"

    def first_method(self):  # First Method create
        print("first is ", self.x)
        print("Second is ", self.y)

CreateObject = MyClass()   # Create object and initialize to MyClass or share attr and behviour
print(CreateObject.x, "\n") # Accessing class attribute by object
CreateObject.first_method() # Accessing class methods by object



class Init_class:
    NAME = "BHAVIN"  # Class variable
    def __init__(self, name, lname):
        self.name = name  # Instance variable
        self.lname = lname
    def first_method(self):
        print("first is metod here", self.name)
        print("second variable accesss", self.lname)
P = Init_class("bhavin", "bhasaniya")
print("here : ", P.name)
print("class : ", P.NAME)  # access by object
print("last", P.lname)  # access instance variable
print(Init_class.NAME)  # access class variable with class name


# Accessing class
class method_use:
    NAME = "BHAVIN"
    def __init__(self, name):
        self.name = name
    def setColor(self, color):
        self.color = color
    def getColor(self):
        return self.color

c1 = method_use("Cyber")
c1.setColor("Black")  # set the object
print(c1.getColor())
del c1.setColor  # delete obj
# print(c1.setColor())