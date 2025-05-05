# Préparation des données


from lecture_donnees import donnees_athlete_events, donnees_noc_regions

# import Question5_panda as Q5


entete = donnees_athlete_events[0]
donnees = donnees_athlete_events[1:]

idx_noc = entete.index("NOC")
idx_annee = entete.index("Year")
idx_athlete = entete.index("ID")
idx_sport = entete.index("Sport")


# Liste des années vérifiée


# def liste_annees():
#     liste = [annee for annee in range(1896, 1993, 4)]
#     liste.pop(liste.index(1916))
#     liste.pop(liste.index(1940))
#     liste.pop(liste.index(1944))
#     liste.append(1906)
#     liste.extend([annee for annee in range(1994, 2017, 2)])
#     liste.sort()
#     return liste


# annees = liste_annees()
# print(annees)

# Pays non médaillé le plus réprésenté sur une année donnée


def pays_non_medaille_max_annee(annee):

    # On transforme annee d'un int en une str.
    annee = str(annee)

    # On initialise un dictionnaire des pays pour marquer s'ils
    # sont médaillés ou non.
    pays_medaille = {ligne[0]: False for ligne in donnees_noc_regions}

    # On utilise une liste pour marquer si un athlète a déjà été vu ou non.
    athletes = [False for i in range(0, int(donnees[-1][0]) + 1)]

    # On initialise le dictionnaire résultat. Il contiendra les couples
    # pays: nombre d'athlètes pour tous les pays non médaillés
    # l'année demandée.
    dico = {}

    for ligne in donnees:

        # On ne s'intéresse qu'à l'année demandée
        if ligne[idx_annee] != annee:
            continue

        # On ne compte pas deux fois le même athlète
        if athletes[int(ligne[idx_athlete])]:
            continue
        athletes[int(ligne[idx_athlete])] = True

        noc = ligne[idx_noc]
        if noc == "SGP":
            noc = "SIN"

        # Si l'athlète est médaillé, on actualise son pays.
        if ligne[-1] != "NA":
            pays_medaille[noc] = True

        # Si le pays est médaillé et s'il est dans le dictionnaire final,
        # on le supprime.
        if pays_medaille[noc]:
            if noc in dico:
                del dico[noc]

        # Si le pays n'est pas médaillé, on initialise son nombre d'athlètes
        # à 0 s'il n'est pas déjà dans le dictionnaire final, puis on
        # incrémente le nombre d'athlètes.
        else:
            if noc not in dico:
                dico[noc] = 0
            dico[noc] += 1

    pays = max(dico, key=dico.get)
    return (
        f"En {annee}, le pays non médaillé le plus représenté était"
        f" {pays} avec {dico[pays]} participants."
    )


# print(pays_non_medaille_max_annee(1912))

# for annee in annees:
#     if (pays_non_medaille_max_annee(annee) !=
#           Q5.pays_non_medaille_max_annee_panda(annee)):
#         print(pays_non_medaille_max_annee(annee))
#         print(Q5.pays_non_medaille_max_annee_panda(annee))
