phrase = input("saisissez une phrase : ")

phraseMAJ = phrase.upper()
phraseMIN = phrase.lower()
nombreMots = len(phrase.split())

print("Voici la phrase en majuscule : ", phraseMAJ)
print("Voici la phrase en minuscule : ", phraseMIN)
print("Voici le nombre de mots : ", nombreMots)