import datetime

def afficher_date_heure_actuelles():
    date_heure_actuelles = datetime.datetime.now()
    print(f"Date et heure actuelles : {date_heure_actuelles}")

afficher_date_heure_actuelles()
