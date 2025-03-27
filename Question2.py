# Trouvez des bornes inférieures et supérieures pour le nombre de médailles
# par nation pour les Jeux Olympiques de 2016.

from lecture_donnees import (
    donnees_athlete_events,
    sports_par_annee,
    sport_collectif_par_annee,
)
from compte_medailles import medaille_pays_annee

sports_2016 = sports_par_annee["2016"]
sports_co_2016 = sport_collectif_par_annee["2016"]
# print(sports_2016)
# print(sports_co_2016)

entete = donnees_athlete_events[0]
donnees = donnees_athlete_events[1:]

idx_sport = entete.index("Sport")
idx_event = entete.index("Event")
idx_noc = entete.index("NOC")
idx_medal = entete.index("Medal")
idx_sex = entete.index("Sex")

medailles_2016 = {}
for ligne in donnees_athlete_events:
    sport = ligne[idx_sport]
    event = ligne[idx_event]
    noc = ligne[idx_noc]
    medal = ligne[idx_medal]
    sex = ligne[idx_sex]
    events_co_2016_noc = {event: False for event in sports_co_2016}
    if ligne[-1] != "NA":
        if noc not in medailles_2016:
            medailles_2016[noc] = {"Bronze": 0, "Silver": 0, "Gold": 0, "Total": 0}
        if event not in events_co_2016_noc:
            medailles_2016[noc][medal] += 1
        else:
            if not events_co_2016_noc[event]:
                medailles_2016[noc][medal] += 1
                events_co_2016_noc[event] = True
print(medailles_2016["USA"])
