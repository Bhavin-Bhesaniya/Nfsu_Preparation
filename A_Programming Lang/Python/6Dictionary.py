# Dictionary :- Store values in key:pairs
# Create dictionary :-
Dict = {"First": "Bhavin",
        "Second": "Bhesaniya", 
        3: "Number", 
        4: 2001,
        "Five": ["add", "list", "add any itrable"]
       }


Dict2 = dict(hello="working")  # Using dict constructor
NestDict = {"firstdict": {"1dictkey": "value",
                          2: "Two"},
            "Secondict": {"2dictkey": "value",
                          2: "second"}}


# Access dictionary :-
print("Accessing dictionary Using Key : " + Dict["First"])
print("\nAccessing dictionary Using get function : ")
print(Dict.get("Five"))
print("\nGet All Keys : ")
print(Dict.keys())
print("\nGet All Values : ")
print(Dict.values())
print("\nGet All keys and Values : ")
print(Dict.items())  # Return all available keys and values in tuple


print("\nAccess dictionary using for loop :- ")
for x in Dict:              # value() | items() | keys() | for i,f in Dict.items():
    print(x, "\t", Dict[x])


# Change dictionary :-
print("\nChanges in dictionary through values or add value :-  ")
Dict[3] = "8989"
Dict.update({4: 1152001})
print(Dict)
# .copy() from exit dict / dict(exit dictionary)


# Method :-
print("\n Extra Method :- ")
thisdict = dict.fromkeys(Dict, Dict2)  # from 1 dict key and another dict value
print(thisdict)
print(Dict.setdefault("First"))  # Default value set


# Remove dictionary :-
print("\nRemove or delete items from dict :- ")
print(Dict.pop(3))     # Remove specific key values
print(Dict.popitem())  # Remove last value
del Dict[4]            # Delete item with specified key
Dict.clear()
print(Dict)
del Dict