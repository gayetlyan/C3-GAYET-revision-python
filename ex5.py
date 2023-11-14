nombreFact = int(input("Entrez un nombre pour calculer son factoriel : "))

def calculer_factoriel(nombre):
    if nombre == 0:
        return 1
    else:
        resultat = 1
        for i in range(1, nombre + 1):
            resultat *= i
        return resultat


resultat_factoriel = calculer_factoriel(nombreFact)
print(f"Le factoriel de {nombreFact} est : {calculer_factoriel(nombreFact)}")
