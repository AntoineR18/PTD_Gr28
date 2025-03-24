from lecture_donnees import donnees_athlete_events

nombre_medailles = 0
for ligne in donnees_athlete_events:
    if ligne[0] == '"94406"':  # l'id de Michael Phelps dans la bdd
        if ligne[-1] != "NA":
            nombre_medailles += 1

print(nombre_medailles)
# Michael Phelps a obtenu 28 médailles aux Jeux Olympiques.
