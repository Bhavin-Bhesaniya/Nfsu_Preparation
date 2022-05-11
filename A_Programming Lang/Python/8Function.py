#Function :- Block of code that run when it is called


# Create Function :-
def run():
    print("Yes it is run")
run()   # Calling function


# Passing Argument Function :-
print("\nPassing Argument Function : ")
def Sname(fname):       # fname is parameter name
    print("My name is " + fname)
Sname("Bhavin")         # Argument passing to function
a = "Bhavin A"          
Sname(a)                # Passing Variable as argument


# Default Argument :-
print("\nDefault Argument Function : ")
def country(name = "India"):
    print("My country name is " + name)
country("USA")
country()


# *ARGS :- Passing no of argument
print("\nPassing No of Arguement *args : ")
def Cname(*fullname):         
    print(fullname[1] + " " + fullname[0])
    print(fullname[0] + " " + fullname[1])
    print(fullname[0] + " " + fullname[0])
Cname("Bhavin","Bhesaniya")


# Keyword argument :-
print("\nKeyword Argument : ")
def Cname(fname,lname):           
    print(fname + " " + lname)
Cname(fname = "Bhavin",lname = "Bhesaniya")


# **kwargs :- Passing no of keyword argument
print("\nPassing No Of Keyword Argument : **kwargs ")
def Cname(**fullname):            
    print(fullname["fname"] + " " + fullname["lname"])
Cname(fname = "Bhavin",lname="Bhesaniya")


# Return Value From Function :-
print("\nReturn Value from the function :")
def sum(a,b):
    return print(a+b)
sum(10,20)


# RECURSION :- Function call itself known as recursion
# tri_recursion is use for recursion


# LAMDA :- Function without name or anonymous function
# Syntax :- lambda arguments : expression
print("\nLamda Function :")
x = lambda p,n: p * n
print(x(5,5))


# First Class Function :-
print("\nFirst Class Function :- \n")

#1)Pass obj in var :-
print("\nPass Object in Function Through Variable")
def fun(txt):
    return txt.upper()
print(fun("hello"))
x  = fun
print(x("pass object"))

#2)Pass function as argument :-
print("\nPassing function as argrument")
def first_fun(txt):
    return txt.upper()
def second_fun(txt):
    return txt.lower()
def third_fun(txt):
    gretty = txt("passing Functions As Argument")
    print(gretty)
third_fun(first_fun)  
third_fun(second_fun)

#3)Function return another function :-
print("\nFunction return another function")
def create_adder(x):
    def adder(y):
        return x+y  
    return adder  
add_15 = create_adder(15)  
print (add_15(10))



#Yield Example :-
print("\nYield Example :")
def sqaure():
    i = 1
    while True:
         yield i * i
         i += 1
for x in sqaure():
    if x > 50:
        break
    print(x)