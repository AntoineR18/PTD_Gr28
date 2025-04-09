# Question 5 :
# Quel est le pays avec le plus de participants, n'ayant obtenu aucune
# médaille chaque année ? Dans l'histoire ?

from lecture_donnees import donnees_athlete_events, donnees_noc_regions

entete = donnees_athlete_events[0]
donnees = donnees_athlete_events[1:]

idx_noc = entete.index("NOC")
idx_annee = entete.index("Year")
idx_athlete = entete.index("Name")
idx_sport = entete.index("Sport")


def compte_participants_non_medailles_par_pays_par_annee(annee):
    pays_medaille = {ligne[0]: False for ligne in donnees_noc_regions}
    pays_non_medaille_participants = {}
    for ligne in donnees:
        if ligne[idx_annee] != annee:
            continue
        noc = ligne[idx_noc]
        if noc == "SGP":
            noc = "SIN"
        if ligne[-1] != "NA":
            pays_medaille[noc] = True
        if pays_medaille[noc]:
            if noc in pays_non_medaille_participants:
                del pays_non_medaille_participants[noc]
            continue
        if noc not in pays_non_medaille_participants:
            pays_non_medaille_participants[noc] = 0
        pays_non_medaille_participants[noc] += 1
    return pays_non_medaille_participants


def pays_non_medaille_plus_participants_annee(annee):
    pays_non_medaille_participants_annee = (
        compte_participants_non_medailles_par_pays_par_annee(annee)
    )
    pays_non_medailles = list(pays_non_medaille_participants_annee.keys())
    n = len(pays_non_medaille_participants_annee)
    pays_max = pays_non_medailles[0]
    for i in range(0, n - 1):
        pays = pays_non_medailles[i + 1]
        if (
            pays_non_medaille_participants_annee[pays]
            > pays_non_medaille_participants_annee[pays_max]
        ):
            pays_max = pays
    return pays_max


annees = [annee for annee in range(1896, 1993, 4)]
annees.pop(annees.index(1916))
annees.pop(annees.index(1940))
annees.pop(annees.index(1944))
annees.append(1906)
annees.extend([annee for annee in range(1994, 2017, 2)])
annees.sort()

print([pays_non_medaille_plus_participants_annee(str(annee)) for annee in annees])


def pays_non_medaille_plus_participants_toujours():
    pays_non_medailles_toujours = {ligne[0]: False for ligne in donnees_noc_regions}
    pays_non_medaille_participants_toujours = {}
    for ligne in donnees_athlete_events:
        