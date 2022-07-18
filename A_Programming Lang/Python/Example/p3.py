# find n factorial number
# Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n.

import math


def factorial(no):
    if(no < 0):
        return 0
    elif(no == 0 or no == 1):
        return 1
    else:
        fact = 1
        while(no > 1):
            fact *= no
            no -= 1
        return fact


def factorial2(n):
    return 1 if (n == 1 or n == 0) else n * factorial2(n - 1)


def factorial3(n):
    return (math.factorial(n))


def factorial4(n):
    res = 1
    for i in range(2, n+1):
        res *= i
    return res


def factorial5(n):
    if (n == 0):
        return 1
    i = n
    fact = 1
    while(n / i != n):
        fact = fact * i
        i -= 1
    return fact


number = int(input('Enter a number : '))
no = factorial(number)
n = factorial2(number)
n2 = factorial3(number)
n3 = factorial4(number)
n4 = factorial5(number)

print('Factorial Of No : ' + str(no) + "\nTernary Function : " +
      str(n) + "\nBuilt-in Function : " + str(n2) + "\nFor-loop Function : " + str(n3) + "\nWhile-loop Function : " + str(n4))
