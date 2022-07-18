# 4. Simple Interest
'''
 - Simple interest is a quick method of calculating the interest charge on a loan.
 - Simple interest is determined by multiplying the daily interest rate by the principal by the number of days that elapse 
   between payments. 
 - Formula :- P*T*R/100
           - P : Amount
             T : Total interest Time
             R : Interest Rate 

'''
print ("Simple Interest")
 
P = int(input("Enter Principal Amount : "))
T = int(input("Enter Time : "))
R = int(input("Enter Rate : "))

interest = P * T * R / 100

print ("Interest : " + str(interest))