liste_nombres = [23, 45, 12, 67, 89, 34, 56, 78, 90, 10]
print("Liste de nombres :", liste_nombres)

def trouver_maximum(liste):
    maximum = liste[0]
    for nombre in liste:
        if nombre > maximum:
            maximum = nombre
    return maximum

max = trouver_maximum(liste_nombres)
print("Maximum :", max)


def trouver_minimum(liste):
    minimum = liste[0]
    for nombre in liste:
        if nombre < minimum:
            minimum = nombre
    return minimum

min = trouver_minimum(liste_nombres)
print("Minimum :", min)


def calculer_moyenne(liste):
    somme = sum(liste)
    moyenne = somme / len(liste)
    return moyenne

moyenne = calculer_moyenne(liste_nombres)
print("Moyenne :", moyenne)

