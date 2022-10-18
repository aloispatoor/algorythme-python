a = input("Entrez un chiffre:")
b = input("Entrez un autre chiffre:")

addition = int(a) + int(b)
print(f"Le resultat est {addition}")
# Avec le f format

soustraction = int(a) - int(b)
print(str(soustraction))

multiplication = int(a) * int(b)
print(str(multiplication))

if (int(b) == 0 ):
    print("Division impossible par 0")
else: 
    division = int(a) / int(b)
    print(str(division))
