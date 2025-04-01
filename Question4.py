# Quelle est la moyenne/médiane d'âge des athlètes, par sport ?
# Quel est le sport avec la plus petite moyenne d'âge ?
# Les gymnastes les plus jeunes obtiennent-ils plus de médailles que les plus vieux ?
# A quel-âge (exact) obtient-on le plus de médailles si l'on pratique le biathlon ?

from lecture_donnees import donnees_athlete_events

# réalisation d'un tableau des sports avec effectifs.

# d'abord je créé une liste de tous les sports masculins.
# je prends la colonne 13 de la bdd là où le joueur est masculin.
table_sport_h = []
for ligne in donnees_athlete_events:
    if ligne[2] == "M":
        table_sport_h.append(ligne[12])
table_sport_h = list(set(table_sport_h))


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

# On fait un tableau des âges moyens par sport : pour chaque élément de la liste on a
# le sport et la moyenne d'âge de ce sport. On somme ages_par_sport pour chaque sport et
# on divise par la longueur de ages_par_sport[sport].
moy_ages_par_sport = []
for sport in table_sport_h:
    if sport in ages_par_sport:
        total_ages = sum(ages_par_sport[sport])
        effectif = len(ages_par_sport[sport])
        moyenne_age = round(total_ages / effectif, 1)
        moy_ages_par_sport.append([sport, moyenne_age])
print(moy_ages_par_sport)
