# Question 1 :
# Déterminez le nombre de médailles gagnées par Michael Phelps. Son nom
# complet est Michael Fred Phelps, II.
import os
from lecture_donnees import donnees_athlete_events

nombre_medailles = 0
for ligne in donnees_athlete_events:
    if ligne[1] == "Michael Fred Phelps, II":  # l'id de Michael Phelps dans la bdd
        if ligne[-1] != "NA":
            nombre_medailles += 1


# Afficher et sauvegarder le résultat
def afficher_resultat():
    texte = f"Michael Phelps a obtenu {nombre_medailles} médailles aux Jeux Olympiques."

    # Affichage dans le terminal (optionnel)
    print(texte)

    # Chemin vers le fichier à créer dans le sous-dossier
    chemin_fichier = os.path.join("Resultat", "Q1.txt")

    # Écriture dans le fichier
    with open(chemin_fichier, "w", encoding="utf-8") as fichier:
        fichier.write(texte + "\n")
