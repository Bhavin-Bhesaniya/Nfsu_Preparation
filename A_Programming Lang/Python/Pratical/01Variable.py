print("Hello Print Function") 

# Comment :-
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
a = [50,20,40]  # Declare list
x = y = z = a   # Use list value for multi-variable
print(x)        # Unpack collection of types


# Local And Global Variable :-
A = "Global variable"                 # Global variable declaration outside function
def fun():
  global A   # Make Local variable access outside function use global keyword overwrite global variable value
  A = "Local variable"       # Local variable declaration inside function
  print("This is " + A)
fun()
print("This is " + A)


# Take User values :-
Input_Values = input("ENTER NO :- ")    # Get user value 
print(type(Input_Values))               # All value from input function is string 
print(int(Input_Values))                # Type cast value if value need in int | Either here or At input


# Escape Character
W = '''
    It is \n Newline \t Tab \\ Slash \' Semicolon \" Double Colon 
    \r Carriage Return \b Backspace \f Formfeed \ooo Octal  hexa value''' 
print(W)



''' DATATYPE :-
 Datatype      Type of value store
 String        "" or """ """      
 int           0, 1, -1
 float         1.1, -1.1
 complex       5j
 boolean       True,False
 list          [multi-value] Ex :- ["list","types",1,2.2]
 tuple         (multi-value)       ("tuple",1,2.2)
 dic           {key:value}         {"first" : "dictionary",2 : "second"}
 set           {multi-value}       {"set","type",1}

 Also use Datatype constructor for initalize value 
'''



''' Random module :- Generate random value
 import random
 print(random.randrange(1,9))
'''



''' Array :- Not in python but we can use array module
 import array as ar
 a  = ar.array('i',[1,2,3,4,5])
 print(a)
'''
