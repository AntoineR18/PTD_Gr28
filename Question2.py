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
    Calcule et affiche les bornes du nombre total de médailles gagnées
    par pays pour une année donnée, et sauvegarde le résultat dans un fichier.
    """
    try:
        borne_min, borne_max = bornes_medailles_par_nation_v2(annee)
        texte = (f"En {annee}, le nombre de médailles par pays varie de "
                 f"{borne_min} à {borne_max}.")
        print(texte)

        # Sauvegarde dans un fichier résultat spécifique
        with open("Resultat/Questions2.txt", "w", encoding="utf-8") as f:
            f.write(texte + "\n")

    except Exception as e:
        message_erreur = f"Erreur lors du calcul des bornes pour l'année {annee} : {e}"
        print(message_erreur)

        with open("Resultat/Question2.txt", "w", encoding="utf-8") as f:
            f.write(message_erreur + "\n")
