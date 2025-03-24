import os
import csv  # Module qui gère mieux les séparations notamment dans le cas

chemin_csv1 = os.path.join("donnees_jeux_olympiques", "athlete_events.csv")
chemin_csv2 = os.path.join("donnees_jeux_olympiques", "noc_regions.csv")

donnees_athlete_events = []
donnees_noc_regions = []

with open(chemin_csv1, "r", encoding="utf-8") as fichier:
    lecteur = csv.reader(fichier)
    for ligne in lecteur:
        donnees_athlete_events.append(ligne)

with open(chemin_csv2, "r", encoding="utf-8") as fichier:
    lecteur = csv.reader(fichier)
    for ligne in lecteur:
        donnees_noc_regions.append(ligne)
