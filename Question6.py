from lecture_donnees import (
    donnees_athlete_events,
    donnees_noc_regions,
)


pays = []
pays_final = []
for ligne in donnees_athlete_events[1 : len(donnees_athlete_events)]:
    L = 0
    if ligne[7] == "SGP":
        noc = "SIN"
    elif ligne[7] in ("VNM", "VIE"):
        noc = "VNM"
    else:
        noc = ligne[7]
    for i in range(1, len(pays)):
        if pays[i][0] == noc:
            L = 1
            if ligne[9] not in pays[i]:
                pays[i].append(ligne[9])
    if L == 0:
        pays.append([noc, ligne[9]])


for pays_i in pays:
    pays_final.append([pays_i[0], min(pays_i[1 : len(pays_i)])])


pays_final_toutes_lettres = []
for pays in pays_final:
    val = pays[1]
    noc_a_changer = pays[0]
    for ligne in donnees_noc_regions:
        if ligne[0] == noc_a_changer:
            if ligne[2] == "":
                nom_pays = ligne[1]
            else:
                nom_pays = ligne[2]
            break
    pays_final_toutes_lettres.append([nom_pays, val])


def afficher_annee_adhesion_depuis_tableau(pays_nom: str):
    """
    Affiche l'année de première participation aux JO pour un pays donné,
    à partir du tableau pays_final_toutes_lettres.

    :param pays_nom: Nom du pays (ex: "France")
    """
    pays_nom = pays_nom.strip().title()

    for nom, annee in pays_final_toutes_lettres:
        if nom.strip().title() == pays_nom:
            print(f"Le pay : '{pays_nom}', a participé pour la première fois aux JO en {annee}.")
            return

    print(f"❌ Le pays '{pays_nom}' n’a pas été trouvé dans le tableau.")
