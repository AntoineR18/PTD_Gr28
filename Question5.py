# Préparation des données


from lecture_donnees import donnees_athlete_events, donnees_noc_regions
from Question6 import pays_final


entete = donnees_athlete_events[0]
donnees = donnees_athlete_events[1:]

idx_noc = entete.index("NOC")
idx_annee = entete.index("Year")
idx_athlete = entete.index("ID")
idx_sport = entete.index("Sport")


# Pays non médaillé le plus réprésenté sur une année donnée


def pays_non_medaille_max_annee(annee, sortie):
    pays_medaille = {ligne[0]: False for ligne in donnees_noc_regions}
    dico = {}
    athletes = [False for i in range(0, int(donnees[-1][0]) + 1)]
    for ligne in donnees:
        if ligne[idx_annee] != annee:
            continue
        if athletes[int(ligne[idx_athlete])]:
            continue
        athletes[int(ligne[idx_athlete])] = True
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
    pays = max(dico, key=dico.get)
    if sortie == "dico":
        return dico
    elif sortie == "pays":
        return (
            f"En {annee}, le pays non médaillé le plus représenté était"
            f" {pays} avec {dico[pays]} participants."
        )


# print(pays_non_medaille_max_annee("1912", "dico"))


# Liste des années vérifiée


def liste_annees():
    liste = [annee for annee in range(1896, 1993, 4)]
    liste.pop(liste.index(1916))
    liste.pop(liste.index(1940))
    liste.pop(liste.index(1944))
    liste.append(1906)
    liste.extend([annee for annee in range(1994, 2017, 2)])
    liste.sort()
    return liste


annees = liste_annees()

# Dictionnaire des pays par année


def dico_noc_par_annee():
    dico = {annee: [] for annee in annees}
    for noc_annee in pays_final:
        i = len(annees) - 1
        while i >= 0 and annees[i] >= int(noc_annee[1]):
            dico[annees[i]].append(noc_annee[0])
            i -= 1
    return dico


noc_par_annee = dico_noc_par_annee()


# Pays non médaillé le plus représenté dans l'histoire


def pays_non_medaille_max_histoire(sortie):
    dico_statut = {
        ligne[0]: {"participe": False, "medaille": False}
        for ligne in donnees_noc_regions
    }
    dico_pays = pays_non_medaille_max_annee(str(annees[0]), "dico")
    for noc in noc_par_annee[annees[0]]:
        dico_statut[noc]["participe"] = True
        if noc not in dico_pays:
            dico_statut[noc]["medaille"] = True
    i = 1
    while i < len(annees):
        annee = annees[i]
        dico_annee = pays_non_medaille_max_annee(str(annee), "dico")
        for noc in noc_par_annee[annee]:
            if dico_statut[noc]["participe"] and dico_statut[noc]["medaille"]:
                if noc in dico_annee:
                    del dico_annee[noc]
                continue
            if not dico_statut[noc]["participe"]:
                dico_statut[noc]["participe"] = True
                if noc not in dico_annee:
                    dico_statut[noc]["medaille"] = True
        for noc in dico_annee:
            if noc in dico_pays:
                dico_pays[noc] += dico_annee[noc]
            else:
                dico_pays[noc] = dico_annee[noc]
        i += 1
    pays = max(dico_pays, key=dico_pays.get)
    if sortie == "dico statut":
        return dico_statut
    elif sortie == "dico pays":
        return dico_pays
    elif sortie == "pays":
        return (
            f"Dans toute l'histoire, le pays non médaillé le plus représenté"
            f" est {pays} avec {dico_pays[pays]} participants."
        )


print(pays_non_medaille_max_histoire("pays"))
