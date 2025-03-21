import os

chemin_csv1 = os.path.join("donnees_jeux_olympiques", "athlete_events.csv")
chemin_csv2 = os.path.join("donnees_jeux_olympiques", "noc_regions.csv")

donnees_athlete_events = []
donnees_noc_regions = []


with open(chemin_csv1, 'r', encoding='utf-8') as fichier:
    for ligne in fichier:
        ligne = ligne.strip()
        elements = ligne.split(',')
        donnees_athlete_events.append(elements)

with open(chemin_csv2, 'r', encoding='utf-8') as fichier:
    for ligne in fichier:
        ligne = ligne.strip()
        elements = ligne.split(',')
        donnees_noc_regions.append(elements)
