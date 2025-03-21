import os
# Antoine marie moi

chemin_csv = os.path.join("donnees_jeux_olympiques", "athlete_events.csv")

donnees = []

with open(chemin_csv, 'r', encoding='utf-8') as fichier:
    for ligne in fichier:
        ligne = ligne.strip()
        elements = ligne.split(',')
        donnees.append(elements)

# Afficher les 5 premières lignes
for ligne in donnees[:5]:
    print(ligne)
