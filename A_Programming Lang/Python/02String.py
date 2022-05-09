#String
a = str("String  Datatype")        # Use str constructor
A = "We check THIS String"         # Normal Write

#Access String :-
print("Print Entier String " + a)                 
print("Access Single Character ",A[0])

print("\nAccess Through Loops : ")
for X in A:                  
   print(X)

print("\nChecking String With Identity Operator : ")
if "S" in a:                 
   print("Yes S in a\n")
if a is A:
   print("Yes Both Are Same\n")
else:
   print("No Both Are Not Same\n")


# Slicing :-
print("\nSlicing in String :- ")
print(a[0:5])       # start : end string
print(a[:5])        
print(a[-5:])       # Negative index start from -1
print(a[::-1])      # Reverse string


# Update :-
print("\nUpdate String :- ")
A = "Update Entier String"
print(A) 
# String is immutable so we can't change single character value we need to change entire string to update it


#Delete :-
print("\nDelete String :- ")
deleteStr = "String is delete"
del deleteStr


#String Methods :-
print("\nString Methods :- ")
print("\nConvert in uppercase : "                 + a.upper())
print("\nConvert in lowercase : "                 + a.lower())
print("\nRemove whitespace begin and end : "      + a.strip())
print("\nOLD values ,Replace with new value : "   + a.replace("String ", "STRING"))
print("\nConvert Whitespace to split ",             a.split(" "))     
print("\nFirst Character each word is capital : " + a.capitalize())
print("\nConvert into lower : "                   + a.casefold())
print("\nAdd Symbol at center : " ,                 a.center(10,"#"))
print("\nCheck Where Word is found in string : "  , a.index("Str")) 
print("\nConvert First Word in Captial : "        , a.title()) 
print("\nFill Space From left with 0 : "          , a.zfill(20))
print("\nReplace each character with given character : ",a.translate("S"))
print("\nCheck String Start With or Endwith Given Character if yes return 1 otherwise 0 : ", a.startswith("hello"), a.endswith("datatype")) 
print("\nConcate two string : First - " + a +" Second - "+ A )
Q = A.count("S") 
print("\nTotal Character in string : ", Q)
S = A.join(a) 
print("\nJoin Two String in New string : ",S)
print("\nEncoding character : ", a.encode(encoding="ascii",errors="ignore"))

'''

 More Methods Are :-
   expandtab / isalpha / isdecimal / isdigit / isidentifier / islower / isnumeric / isprintable / isspace / istitle / issupper / 
   rfind / rjust / rsplit / rstrip 

'''


#String Formating :-
print("\nString Formatting :- ")
A1 = 10

A2 = "How Old You Are. I {} Old"        #IN CURLY BRACKETE VALUE ADD WHICH PASS IN FORMAT
print(A2.format(A1))

A3 = "FIRST {1} VALUE ADD.SECOND {0} VALUE" #You have index in multiple value / {:.2f} for float 
print(A3.format(A1,A2))

A4 = "HERE WE YOU KEYWORD ARGUMENT {first}. WE PASS KEYWORD IN BRACKETE {second}"
print(A4.format(first="A1",second="A2"))

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

txt1 = "My name is {fname}, I'm {age}"#.format(fname = "John", age = 36)
print(txt1.format(fname= "bhavin",age= 21 ))

txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)
