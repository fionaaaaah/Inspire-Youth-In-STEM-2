#!/usr/bin/env python3

myFavoriteFruits = ["banana","mango","apple","grape","watermelon"]
#accessing elements in a list
for fruit in myFavoriteFruits:
    print(fruit)

print(len(fruit))

my_favorite_fruit = ["banana","mango","apple","grape","watermelon"]
for fruit in my_favorite_fruit:
    print(fruit)

friends = ["Bob","Samara","David","Arif","Buda"]
print(friends)
friends[0] = "Mary"
print(friends)

#append() adds an element to the end of the list
#clear() removes all items in a list
#copy   copies all elements
#inserts   add element at specified position
#pop    specified position
#removes   removes item from a list(specified value)
#count    length
#extend   add elements to the end of the list that exists
#reverse
#pop   removes last item in a list
#index
#sort


new_friends = friends.copy()
print(new_friends)

new_friends.sort()
print(new_friends)
 
new_friends.pop()
print(new_friends)


