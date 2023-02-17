age = 35
gender = "male"

if(age < 20):
    print(" You are still young")
else:
    print("You should move out")

#compound / multiple conditions

if((age>30) & (gender =="male")):
    print("Jenga nyumba")
else:
    print("wacha jokes")

fav_color = "grey"
age = 22
if(fav_color == "grey") | (age <= 20):
    print("Happy birthday to you")
else:
    print("we kauka")