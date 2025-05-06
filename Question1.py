# Question 1 :
# Déterminez le nombre de médailles gagnées par Michael Phelps. Son nom
# complet est Michael Fred Phelps, II.

from lecture_donnees import donnees_athlete_events

nombre_medailles = 0
for ligne in donnees_athlete_events:
    if ligne[1] == "Michael Fred Phelps, II":  # l'id de Michael Phelps dans la bdd
        if ligne[-1] != "NA":
            nombre_medailles += 1


# Afficher le résultat
def afficher_resultat():
    print(f"Michael Phelps a obtenu {nombre_medailles} médailles aux Jeux Olympiques.")
