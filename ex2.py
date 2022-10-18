var = int (input("Votre age:"))

if(var == 0):
    print("Bizarre votre âge")
elif(var < 18):
    print("Vous êtes mineur")
elif(var == 18):
    print("Vous êtes majeur et vous avez exactement 18 ans")
else:
    print("Vous êtes majeur")
