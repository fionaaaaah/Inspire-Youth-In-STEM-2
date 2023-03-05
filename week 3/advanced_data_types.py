#Advanced data types

#Mutable vs immutable
#Mutable - Data types that can be changed during programme life cycle
#you can add or remove elements

#Immutable - Data types that cannot be edited during life cycle

#1.list - it is mutable
friends = ["Samara","Joy","David"]
#or friends = []
#add ---> append(),extend()
#remove ---> pop()

students = ["Loreen","Clive"]
friends.extend(students)
friends.append("June")
friends.sort()
friends.reverse()

#2.Tuples - immutable
stationeries = ("pen","glue","eraser","sharpener")

#You can replace the whole tuple
stationeries = ("pencil","clips","highlighter")
for stationery in stationeries:
    print(stationery)


#3.Dictionaries aka dict
#uses key and value pair to store data

student = {"Name" : "Fiona", "Age" : 18, "Gender" : "female", "is_tall" : True}
print(student["Name"])
print(student["Age"])
print(student["Gender"])
print(student["is_tall"])
#name is the key ---> fiona is the value

friend = {"Fav_color" : "Black","Hobby" : "Reading","Course" : "Actuarial Science","Height" : 100,"Food" : "Mchele Njeri"}
print(friend["Fav_color"])
print(friend["Hobby"])
print(friend["Course"])
print(friend["Height"])
print(friend["Food"])

#4.Sets
my_fruits = {"bananas","apples","oranges"}
for fruit in my_fruits:
    print(fruit)

print(type(my_fruits))
print(len(my_fruits))

#ordered - similar data types

#non-ordered - different data types