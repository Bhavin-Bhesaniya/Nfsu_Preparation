print("Hello Print Function") 

#Comment :-
# Single Line comments
    
"""
  Multi-line 
  Comments
"""

#Variable :- ---------------------------------------------------------------------------------------
a = 10   
print(a) 
print(type(a))      # Type function use to define which type variable
# print(len(a))     # Howmany characters are there
a = b = c = 10      # Declare multi-variable with same value
print(a,b,c)
a = b = c = 10 ,20 ,30   #Declare multi-variable with multivalue
print(a)


#Unpacking :-
a = [50,20,40]  #Declare list
x = y = z = a   #Use list value for multi-variable
print(x)        #Unpack collection of types


#Local And Global Variable :-
A = "Global"                           #Global variable declaration outside the function
def fun():
    global A                           #Make Local variable access outside function use global keyword overite the value of global vaiable
    A = "Local variable"               #Local variable declaration inside the function
    print("this is variables " + A)
fun()
print("this is variables " + A)


#Take user values in variables  :-
Input_Values = input("ENTER NO :- ")    #we can get user value from input function
print(type(Input_Values))               #all value from input function is string 
print(int(Input_Values))                #we need to type cast value if need int either here or at input


#Escape Character
# W = "here \n newline \t tab \\ forslash \' semicolon \"double colon \r carriage return \b backspace \f formfeed \ooo Octal \xhh hexa value"  
# print(W)

'''
DATATYPE

Datatype       Which Type value store
String        " " or """ """      
int           0,1,-1
float         1.1,-1.1
complex       5j
boolean       True,False
list          [multi-value] Ex :- ["list","types",1,2.2]
tuple         (multi-value)       ("tuple",1,2.2)
dic           {key:value}         {"first" : "dictionary",2 : "second"}
set           {multi-value}       {"set","type",1}

U can use datatype name constructor for initalizze value 
'''


'''
Random module :-
import random
print(random.randrange(1,9)) #random no between range 1 to 9 randrnage(method)

Array :-
#Array is not in python we use array module
import array as ar
a  = ar.array('i',[1,2,3,4,5])
print(a)

'''