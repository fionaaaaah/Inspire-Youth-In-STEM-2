#This is a single line comment
#python program to illustrate conditions
#Name: fiona
#Email: muriithinfiona@gmail.com
#Date : 17th Feb 2023
#File : conditions.py

age = 35
gender = "male"

if(age < 20):
    print(" You are still young")
else:
    print("You should move out")

#compound / multiple conditions

if((age>30) & (gender =="male")):
    print("build a house")
else:
    print("enjoy your youth")

fav_color = "grey"
age = 22
if(fav_color == "grey") | (age <= 20):
    print("Happy birthday to you")
else:
    print("no birthday for you")