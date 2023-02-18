#This is a single line comment
#python program to illustrate lists
#Name: fiona
#Email: muriithinfiona@gmail.com
#Date : 14th Feb 2023
#File : list.py

names=("Samara","Fiona","David")
#accessing names on a list
print(names)
print(names[0])
print(names[0:2])
fruits = ("mangoes","bananas","melon","grapes","apples")
print(fruits[0:-1])
print("My favorite fruit is",fruits[1].upper())
#adding two lists
vegetables=("spinach","cabbage","broccoli","cauliflower","mushrooms")
stationery=("pen","pencils","ruler","glue","sharpener")
shoppings = vegetables + stationery
print(shoppings[5])
for vegetable in vegetables:
    print(vegetable)
for shopping in shoppings:
    print(shopping)
print("My name is " + names[1]+ " and my favorite fruit is " + fruits[3])