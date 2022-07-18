# Maximum of two numbers in Python
Num1 = int(input("Enter Number 1 : "))
Num2 = int(input("Enter Number 2 : "))

if(Num1 >= Num2):
    print("Num 2 : " + str(Num2))
else:
    print("Num 1 : " + str(Num1))

# Using max function
MaxNum = max(Num1, Num2)        
print("Max of two numbers in Python : " + str(MaxNum))

# Using Ternary Operator
print("Using Ternary Operator : " + str(Num1) if Num1 >= Num2 else str(Num2))
