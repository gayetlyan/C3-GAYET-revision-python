liste_nombres = [23, 45, 12, 67, 89, 34, 56, 78, 90, 10]
print("Liste de nombres :", liste_nombres)

def trouver_maximum(liste):
    return max(liste)

max = trouver_maximum(liste_nombres)
print("Maximum :", max)


def trouver_minimum(liste):
    return min(liste)

min = trouver_minimum(liste_nombres)
print("Minimum :", min)


def calculer_moyenne(liste):
    return sum(liste) / len(liste)

moyenne = calculer_moyenne(liste_nombres)
print("Moyenne :", moyenne)

