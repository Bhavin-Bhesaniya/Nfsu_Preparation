# 5. Compund Interest

'''

 Amount = principle * (1 + rate / 100)  time)
 Formula : A = P(1 + R/100)
           Compound Interest = A - P 
           A is amount 
           P is principle amount 
           R is the rate and 
           T is the time span
         
 - Compound interest is the addition of interest to the principal sum of a loan or deposit, or in other words, interest on interest.

''' 
print ("Compound Interest")

def compund_interest(P,R,T):
    A = P *(pow((1 + R/100), T)) #TypeError: unsupported operand type(s) for -: 'tuple' and 'int'
    CI = A - P
    return CI


P = int(input("Enter Principal Amount : "))
T = int(input("Enter Time : "))
R = float(input("Enter Rate : "))
print(R)
interest = compund_interest(P,R,T)

print ("Interest : " + str(interest))