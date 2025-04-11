# Question 5 :
# Quel est le pays avec le plus de participants, n'ayant obtenu aucune
# médaille chaque année ? Dans l'histoire ?

# Préparation des données

from lecture_donnees import donnees_athlete_events, donnees_noc_regions

entete = donnees_athlete_events[0]
donnees = donnees_athlete_events[1:]

idx_noc = entete.index("NOC")
idx_annee = entete.index("Year")
idx_athlete = entete.index("Name")
idx_sport = entete.index("Sport")

# Pays non médaillé le plus réprésenté sur une année donnée


def pays_non_medaille_max_annee(annee, sortie):
    pays_medaille = {ligne[0]: False for ligne in donnees_noc_regions}
    dico = {}
    for ligne in donnees:
        if ligne[idx_annee] != annee:
            continue
        noc = ligne[idx_noc]
        if noc == "SGP":
            noc = "SIN"
        if ligne[-1] != "NA":
            pays_medaille[noc] = True
        if pays_medaille[noc]:
            if noc in dico:
                del dico[noc]
            continue
        if noc not in dico:
            dico[noc] = 0
        dico[noc] += 1
    if sortie == "dico":
        return dico
    elif sortie == "pays":
        return f"En {annee}, le pays non médaillé le plus représenté était : {max(dico, key=dico.get)}."


print(pays_non_medaille_max_annee("2016", "pays"))

# Liste des années vérifiée

annees = [annee for annee in range(1896, 1993, 4)]
annees.pop(annees.index(1916))
annees.pop(annees.index(1940))
annees.pop(annees.index(1944))
annees.append(1906)
annees.extend([annee for annee in range(1994, 2017, 2)])
annees.sort()

# Pays non médaillé le plus représenté dans l'histoire


# def pays_non_medaille_plus_participants_toujours():
#     pays_non_medailles_toujours = compte_participants_non_medailles_par_pays_par_annee(
#         str(annees[0])
#     )
#     for annee in annees[1:]:
#         print(annee)
#         pays_non_medailles_annee = compte_participants_non_medailles_par_pays_par_annee(
#             str(annee)
#         )
#         for noc in pays_non_medailles_toujours.keys():
#             if noc not in pays_non_medailles_annee:
#                 del pays_non_medailles_toujours[noc]
#                 continue
#             pays_non_medailles_toujours[noc] += pays_non_medailles_annee[noc]
#     return pays_non_medailles_toujours


# print(pays_non_medaille_plus_participants_toujours())
