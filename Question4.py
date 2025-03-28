# Quelle est la moyenne/médiane d'âge des athlètes, par sport ?
# Quel est le sport avec la plus petite moyenne d'âge ?
# Les gymnastes les plus jeunes obtiennent-ils plus de médailles que les plus vieux ?
# A quel-âge (exact) obtient-on le plus de médailles si l'on pratique le biathlon ?

from collections import Counter
from lecture_donnees import donnees_athlete_events

# réalisation d'un tableau des sports avec effectifs.

# d'abord je créé une liste de tous les sports masculins.
# je prends la colonne 13 de la bdd là où le joueur est masculin.
table_sport_eff_h = []
for ligne in donnees_athlete_events:
    if ligne[2] == "M":
        table_sport_eff_h.append(ligne[12])

# je fais un compteur pour compter le nombre d'athlètes masculins par sport.
compteur_sports = Counter(table_sport_eff_h)
table_sans_doublons = list(compteur_sports.items())
print(table_sans_doublons)


# on fait un dictionnaire des âges par sport.
ages_par_sport = {}
for ligne in donnees_athlete_events[1:]:
    sport = ligne[12]
    age = ligne[3]
    if age == 'NA':
        continue
    age = int(age)
    if sport not in ages_par_sport:
        ages_par_sport[sport] = []
    ages_par_sport[sport].append(age)
# print(ages_par_sport)


somme_ages = sum(ages_par_sport[sport])
