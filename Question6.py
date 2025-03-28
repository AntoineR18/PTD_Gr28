from lecture_donnees import (
    athletes_medailles,
    donnees_athlete_events,
)

athletes = [donnees_athlete_events[1][1]]
len = len(donnees_athlete_events)
for i in range(2, len):
    ligne = donnees_athlete_events[i]
    if ligne[0] != donnees_athlete_events[i - 1][0]:
        athletes.append(ligne[1])


def test_meilleur(nb_med, plus_medaille_athlete_ID_nb_med):
    if nb_med[0] > plus_medaille_athlete_ID_nb_med[1]:
        plus_medaille_athlete_ID_nb_med[0] = id_avant
        plus_medaille_athlete_ID_nb_med[1] = nb_med[0]
        plus_medaille_athlete_ID_nb_med[2] = nb_med[1]
        plus_medaille_athlete_ID_nb_med[3] = nb_med[2]
    elif nb_med[0] == plus_medaille_athlete_ID_nb_med[1]:
        if nb_med[1] > plus_medaille_athlete_ID_nb_med[2]:
            plus_medaille_athlete_ID_nb_med[0] = id_avant
            plus_medaille_athlete_ID_nb_med[1] = nb_med[0]
            plus_medaille_athlete_ID_nb_med[2] = nb_med[1]
            plus_medaille_athlete_ID_nb_med[3] = nb_med[2]
        elif nb_med[1] == plus_medaille_athlete_ID_nb_med[2]:
            if nb_med[2] == plus_medaille_athlete_ID_nb_med[3]:
                plus_medaille_athlete_ID_nb_med[0] = id_avant
                plus_medaille_athlete_ID_nb_med[1] = nb_med[0]
                plus_medaille_athlete_ID_nb_med[2] = nb_med[1]
                plus_medaille_athlete_ID_nb_med[3] = nb_med[2]


plus_medaille_athlete_ID_nb_med = [0, 0, 0, 0]
id_avant = 0
nb_med = [0, 0, 0]
id = 0
for ligne in athletes_medailles:
    id = ligne[0]
    if id != id_avant:
        if nb_med[0] > plus_medaille_athlete_ID_nb_med[1]:
            plus_medaille_athlete_ID_nb_med[0] = id_avant
            plus_medaille_athlete_ID_nb_med[1] = nb_med[0]
            plus_medaille_athlete_ID_nb_med[2] = nb_med[1]
            plus_medaille_athlete_ID_nb_med[3] = nb_med[2]
        elif nb_med[0] == plus_medaille_athlete_ID_nb_med[1]:
            if nb_med[1] > plus_medaille_athlete_ID_nb_med[2]:
                plus_medaille_athlete_ID_nb_med[0] = id_avant
                plus_medaille_athlete_ID_nb_med[1] = nb_med[0]
                plus_medaille_athlete_ID_nb_med[2] = nb_med[1]
                plus_medaille_athlete_ID_nb_med[3] = nb_med[2]
            elif nb_med[1] == plus_medaille_athlete_ID_nb_med[2]:
                if nb_med[2] == plus_medaille_athlete_ID_nb_med[3]:
                    plus_medaille_athlete_ID_nb_med[0] = id_avant
                    plus_medaille_athlete_ID_nb_med[1] = nb_med[0]
                    plus_medaille_athlete_ID_nb_med[2] = nb_med[1]
                    plus_medaille_athlete_ID_nb_med[3] = nb_med[2]
        nb_med = [0, 0, 0]
    if ligne[14] == "Gold":
        nb_med[0] += 1
    if ligne[14] == "Silver":
        nb_med[1] += 1
    if ligne[14] == "Bronze":
        nb_med[2] += 1
    id_avant = id
id_fin = int(plus_medaille_athlete_ID_nb_med[0])
print(
    athletes[id_fin - 1],
    plus_medaille_athlete_ID_nb_med[1],
    plus_medaille_athlete_ID_nb_med[2],
    plus_medaille_athlete_ID_nb_med[3],
)
