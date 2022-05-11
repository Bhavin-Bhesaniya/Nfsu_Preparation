#Set is unordered and unindexed
set1 = {"Apple","Hello","THIS","is"}
set2 = {"THIS","is","A","Set",1,2.3,True}
set3 = set(("using constructor"))

#Access list :-
print("\nAccess Set Using :")
print(set1)
print("\nThrough For Loop : ")
for A in set2:
    print(A)
#print(set2[6]) #Set is unindexed so this generate error


# Add, join ,Copy Values :-
print("\nAdd Value, Join, Copy Values : ")
set1.add("Add new item")       
set1.update(set2)           # Add Any Iterable With Update Method
print("Set after Update Method :\n",set1)
set4 = set1.union(set3)     # Create new set using uninon    
print("\nUnion set operations :\n",set4)
seCpy = set1.copy()         # Create new set using existing set
print("\nCopy Method :\n",seCpy)


# DIFFERNT SET OPERATION IN SET
print("\nDiffrence Set Operation :\n")
set1.intersection_update(set2)      # return common value
print("Return Common Value :\n",set1)
z = set1.intersection(set2)         # return common value with new set
print("Return Common Value With New Set :\n",z)

sf  = { "set","method","check",1}
sf2 = { "set","method","check",1}
sf3 = sf.difference(sf2)
print("Print Difference Value :\n",sf3)
sf3 = sf.difference_update(sf2)
print(sf3)
sf3 = sf.isdisjoint(sf2)
print(sf3)
sf3 = sf.issubset(sf2)
print("True if both set same value :\n",sf3)
sf3 = sf.issuperset(sf2)
print(sf3)


#Remove value :-
print("\nRemove Value From Set : ")
set1.remove("A")        # Remove specific value if not generate error
set1.discard("A")       # Remove specific value if not than not generate error
set1.pop()              # Remove any value
print(set1)
set1.clear()            
print("Clear list : ",set1)
del set1