from compte_medailles import medaille_pays_annee, noc_to_country


def bornes_medailles_par_nation_v2(annee):
    """
    Calcule la borne inférieure et la borne supérieure du nombre total de médailles
    gagnées par pays pour une année donnée, en parcourant tous les pays possibles.

    :param annee: année des JO (int ou str)
    :return: tuple (min, max)
    """
    annee = str(annee)
    totaux = []

    for code_noc, nom_pays in noc_to_country.items():
        total = medaille_pays_annee(nom_pays, annee, "Total")
        totaux.append(total)

    if not totaux:
        return (0, 0)

    return (min(totaux), max(totaux))


def afficher_bornes_medailles(annee: int):
    """
    Demande à l'utilisateur une année, calcule et affiche les bornes
    du nombre total de médailles gagnées par pays cette année-là.
    """

    try:
        bornes = bornes_medailles_par_nation_v2(annee)
        print(f"En {annee}, le nombre de médailles par pays varie de {bornes[0]}"
              f" à {bornes[1]}.")
    except Exception as e:
        print(f"Erreur lors du calcul des bornes : {e}")
