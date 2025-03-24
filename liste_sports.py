from lecture_donnees import donnees_athlete_events

sports_par_annee = {}
for ligne in donnees_athlete_events[1:]:
    annee = ligne[7]
    sport = ligne[12]
    epreuve = ligne[13]

    if annee not in sports_par_annee.keys():
        sports_par_annee[annee] = {}

    if epreuve not in details_sports[sport].keys():
        details_sports[sport][epreuve] = 0
    details_sports[sport][epreuve] += 1
print(details_sports)
