#write a program to print the factorial of a number using functions

import math 
def fact(n):
    return(math.factorial(n))
num = int(input("Enter the number"))
f = fact(num)
print("Factorial of ",num, "is" ,f)

#write a program to calculate simple interest
def simple_interest(p,t,r):
    print('The principal is', p)
    print('The time period is', t)
    print('The rate of interest is',r)
     
    si = (p * t * r)/100
     
    print('The Simple Interest is', si)
    return si
     
simple_interest(50000, 6, 8)