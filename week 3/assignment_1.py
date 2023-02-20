#create an empty list of favorite musicians
#using a for loop add five new musicians
#copy the list to a new list caled celebs
#sort the list
#pop out two celebs
#count the remaining celebs in the list

favorite_musicians = ["Brent","Miguel","Giveon","Summer","Sza"]
for musician in favorite_musicians:
    print(musician)
favorite_musicians.append("Usher")
favorite_musicians.append("Neyo")
favorite_musicians.append("Lil wayne")
favorite_musicians.append("Normani")
favorite_musicians.append("Tiller")
for musician in favorite_musicians:
    print(musician)

celebs = favorite_musicians.copy()
print(celebs)

celebs.sort()
print(celebs)

celebs.pop()
print(celebs)

celebs.pop()
print(celebs)

print(len(celebs))