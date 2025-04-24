# Question 4 :
# 4.1 : Quelle est la moyenne d'âge pour chaque sport ?
# 4.2 : Quel est le sport avec la plus petite moyenne d'âge ?
# 4.3 : Les nageurs les plus jeunes obtiennent-ils plus de médailles que
# les plus vieux ?

# 4.1 : On va d'abord créer un tableau avec la moyenne d'âge pour chaque sport :

from lecture_donnees import donnees_athlete_events

# d'abord je créé une liste de tous les sports masculins.
# je prends la colonne 13 de la bdd là où le joueur est masculin.
table_sport_h = []
for ligne in donnees_athlete_events:
    if ligne[2] == "M":
        table_sport_h.append(ligne[12])
table_sport_h = list(set(table_sport_h))

# on fait un dictionnaire des âges par sport.
ages_par_sport_h = {}
for ligne in donnees_athlete_events[1:]:
    sport = ligne[12]
    age = ligne[3]
    if ligne[2] == "M":
        if sport not in ages_par_sport_h:
            ages_par_sport_h[sport] = []
        if age != "NA":
            age = int(age)
            ages_par_sport_h[sport].append(age)

# On fait un tableau des âges moyens par sport : pour chaque élément de la liste on a
# le sport et la moyenne d'âge de ce sport. On somme ages_par_sport pour chaque sport et
# on divise par la longueur de ages_par_sport[sport].
moy_ages_par_sport = []
for sport in table_sport_h:
    if sport in ages_par_sport_h:
        total_ages = sum(ages_par_sport_h[sport])
        effectif = len(ages_par_sport_h[sport])
        moyenne_age = round(total_ages / effectif, 1)
        moy_ages_par_sport.append([sport, moyenne_age])

# 4.2 : Quel est le sport avec la plus petite moyenne d'âge ?

age_min = moy_ages_par_sport[0][1]
for sport in moy_ages_par_sport:
    if sport[1] < age_min:
        age_min = sport[1]
        sport_min = sport[0]
print(
    f"Le sport avec la plus petite moyenne d'âge est {sport_min} avec une "
    f"moyenne de {age_min} ans."
)

# 4.3 : Déterminer quelques disciplines où les nageurs les plus jeunes obtiennent plus
# de médailles que les plus agés ?


def comp_meda_moy_age(sport: str):
    # On cherche l'indice du sport dans la table des moyennes
    j = -1  # on part du principe que le sport n'est pas trouvé
    for i in range(len(moy_ages_par_sport)):
        if moy_ages_par_sport[i][0] == sport:
            j = i
            break
    if j == -1:
        raise ValueError("Le sport rentré n'est pas dans la liste des sports")

    # On récupère la moyenne d'âge du sport
    age_moyen_sport = moy_ages_par_sport[j][1]

    # On initialise les compteurs de médailles
    nb_med_jeunes = 0
    nb_med_ages = 0

    # On parcourt les données pour ce sport
    for ligne in donnees_athlete_events[1:]:
        age = ligne[3]
        sport_ligne = ligne[12]
        medal = ligne[14]
        sexe = ligne[2]
        if age != 'NA' and sport_ligne == sport and medal != 'NA' and sexe == 'M':
            age = float(age)
            if age < age_moyen_sport:
                nb_med_jeunes += 1
            else:
                nb_med_ages += 1

    # On affiche les résultats
    print(f"Pour le sport {sport} :")
    print(f"Nombre de médailles pour les plus jeunes : {nb_med_jeunes}")
    print(f"Nombre de médailles pour les plus âgés : {nb_med_ages}")


comp_meda_moy_age("Swimming")
comp_meda_moy_age("Trampolining")
comp_meda_moy_age("Gymnastics")
