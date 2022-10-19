# Programme à réaliser
# Saisissez les notes une par une, lorsque l'utilisateur saisit la note -1, la saisie des notes prend fin et votre programme trie toutes les notes de votre tableau puis les affiches.
# Indice
# n = len(tab)
# Traverser tous les éléments du tableau
# for i in range(n):
#     for j in range(0, n-i-1):

inpoute = int(input("Saisissez une note: "))
tab = []
n = len(tab)

# while inpoute != -1:
#     tab.append(inpoute)
#     inpoute = int(input("Saisissez une note: "))

for i in range(n):
    if inpoute == -1:
        inpoute = int(input("Saisissez une note: "))
    else:
        for j in range(0, n-i-1):
            tab.append(inpoute)
            print(tab)