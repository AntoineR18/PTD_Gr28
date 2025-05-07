# Préparation des données


from lecture_donnees import donnees_athlete_events, donnees_noc_regions


entete = donnees_athlete_events[0]
donnees = donnees_athlete_events[1:]

idx_noc = entete.index("NOC")
idx_annee = entete.index("Year")
idx_athlete = entete.index("ID")
idx_sport = entete.index("Sport")

# Dictionnaire code NOC → nom de pays
noc_to_country = {}
for ligne in donnees_noc_regions[1:]:  # on saute l'en-tête
    code_noc = ligne[0]
    nom_pays = ligne[1]
    noc_to_country[code_noc] = nom_pays

# Pays non médaillé le plus réprésenté sur une année donnée


def pays_non_medaille_max_annee(annee):

    # On transforme annee d'un int en une str.
    annee = str(annee)

    # Initialisation du dictionnaire final.
    # Les clés sont les pays issus de noc_regions et les valeurs sont des
    # listes contenant un ensemble qui contiendra les différents athlètes et
    # un booléen qui retient si un pays est médaillé ou non
    pays_medaille = {ligne[0]: [set(), False] for ligne in donnees_noc_regions[1:]}

    for ligne in donnees:

        # On ne s'intéresse qu'à l'année demandée
        if ligne[idx_annee] != annee:
            continue

        noc = ligne[idx_noc]
        if noc == "SGP":
            noc = "SIN"

        # Si l'athlète est médaillé, on actualise son pays.
        if ligne[-1] != "NA":
            pays_medaille[noc][1] = True

        # On ajoute l'athlète à l'ensemble d'athlètes du pays.
        pays_medaille[noc][0].add(ligne[0])

    # On parcourt à nouveau le dictionnaire pour obtenir des couples clés
    # valeurs de la forme noc: nombre d'athlètes.
    for noc in pays_medaille.keys():

        if pays_medaille[noc][1]:
            pays_medaille[noc] = 0

        else:
            pays_medaille[noc] = len(pays_medaille[noc][0])

    noc = max(pays_medaille, key=pays_medaille.get)
    texte = (
        f"En {annee}, avec {pays_medaille[noc]} participants, le pays non médaillé"
        f" le plus représenté était : {noc}."

    )
    print(texte)

    # Sauvegarde dans un fichier texte
    with open("Resultat/Question5.txt", "w", encoding="utf-8") as f:
        f.write(texte + "\n")
    return texte
