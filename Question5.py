# Préparation des données


from lecture_donnees import donnees_athlete_events, donnees_noc_regions
from Question6 import pays_final


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
        return (f"En {annee}, le pays non médaillé le plus représenté était :"
                f" {max(dico, key=dico.get)}.")

# print(pays_non_medaille_max_annee("2016", "pays"))


# Liste des années vérifiée

annees = [annee for annee in range(1896, 1993, 4)]
annees.pop(annees.index(1916))
annees.pop(annees.index(1940))
annees.pop(annees.index(1944))
annees.append(1906)
annees.extend([annee for annee in range(1994, 2017, 2)])
annees.sort()


# Dictionnaire des pays par année

noc_par_annee = {annee: [] for annee in annees}
for noc_annee in pays_final:
    i = len(annees) - 1
    while i >= 0 and annees[i] >= int(noc_annee[1]):
        noc_par_annee[annees[i]].append(noc_annee[0])
        i -= 1
print(noc_par_annee)



# Pays non médaillé le plus représenté dans l'histoire


# def pays_non_medaille_plus_participants_toujours():
#     pays_non_medailles_toujours = pays_non_medaille_max_annee(
#         str(annees[0]),
#         "dico"
#     )
#     for annee in annees[1:]:
#         print(annee)
#         pays_non_medailles_annee = pays_non_medaille_max_annee(
#             str(annee)
#         )
#         for noc in pays_non_medailles_toujours.keys():
#             if noc not in pays_non_medailles_annee:
#                 del pays_non_medailles_toujours[noc]
#                 continue
#             pays_non_medailles_toujours[noc] += pays_non_medailles_annee[noc]
#     return pays_non_medailles_toujours


# print(pays_non_medaille_plus_participants_toujours())
