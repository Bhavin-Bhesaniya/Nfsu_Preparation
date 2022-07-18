#Tuple :-
#Create a new Tuple
Tup1 = ("THIS","is","First","TuPle")        #Simple tuple
Tup2 = ("THIS","is","Mix",1,2.2,True)       #Tuple with multi-value
Tup3 = tuple(("Using constructor",))        #Tuple using constructor /for single value use , at end


#Access Value/ Slice :-
print("\nAccessing Value in Tuple :\n",Tup1[0] + " " +Tup1[-1])
print("\nAccessing Value in Tuple Using For Loop :")
for x in Tup1:  #for i in range(len(Tup1)):
    print(x)


#Slice in tuple :-
print("\nSliceing in Tuple :")
print(Tup1[0:2])
print(Tup1[-1:])
print(Tup1[::-1])


#Change value :- but tuple immutable so first change in list than convert 
print("\nChange Value Using Type Casting :")
x = list(Tup1)
x[1] = "Is"
x.append("Using list method")
Tup1 = tuple(x)
print(Tup1)


#Unpacking :- Assign value to tuple called packing but extract the values back into variable called unpacking
print("\nUnpacking used :")
fruits = ("apple", "banana","cherry", "apple","strawberry", "raspberry")     #Packing
(green, *yellow, red) = fruits      #if no howmany value use * at last name  #UnPacking
print("\nUnpacking Values Using Index :",green)
print(yellow)
print(red,"\n")


#Method :-
print("Return Item Index No :   ",Tup1.index("First"))
print("Return 1 If Item Found : ",Tup1.count("THIS"))


#Joining Tuple :-
tup2 = (2,)
tup3 = Tup1 + tup2
print(tup3)
tup3 =  tup2 * 2
print(tup3)


#delete tuple
del Tup1
