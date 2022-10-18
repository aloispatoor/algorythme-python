inpoute = int(input("Indiquez votre note: "))
# INITIALISER L'ARRAY
num = []

# FINIT LA BOUCLE EN INPUT -1
while inpoute != -1:
    num.append(inpoute)
    inpoute = int(input("Indiquez votre note: "))

print(num)

# FONCTION
def moyenne(table :list[int]):
    i = len(num)
    somme = 0
    for i in table:
        somme = somme + i
    average = somme / len(table)
    return int(average)

result = moyenne(num)
print("la moyenne est de " + str(result))