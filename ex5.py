num = int (input("Saisissez un nombre entre 0 et 10: "))

while (num < 0 or num > 10):
    num = int (input("Saisissez un nombre entre 0 et 10: "))


print("Votre nombre saisi est " + str(num))
