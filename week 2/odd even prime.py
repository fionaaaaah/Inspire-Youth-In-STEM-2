#This is a single line comment
#python program to illustrate odd and even numbers
#Name: fiona
#Email: muriithinfiona@gmail.com
#Date : 17th Feb 2023
#File :odd even.py

'''
number = 0
if (number%2 == 0):
    print("even number")
else:
    print("odd number")
'''
'''
num = 0
if (num%2) == 0:
    print("even number")
else:
    print("odd number")
'''
'''
print("***The values below are odd numbers***")
for odd_numbers in range(1,101):
    if(odd_numbers%2 !=0):
        print(odd_numbers)

print("***The values below are even numbers***")
for even_numbers in range(0,102):
    if(even_numbers%2 ==0):
        print(even_numbers)
'''
'''
S = 1 
E = 100
for num in range(S, E+1):
    if num>1:
        for i in range(2,num):
            if(num % i==0):
                break
            else:
                print(num, end=" )
'''

print(" prime numbers from 1 - 100 are ... ")
for x in range(1,100 + 1):
    if x > 0:
        for i in range ( 2,x ):
            if x%i ==0:
                break
        else:
            print(x)