import pandas as pd

# Importation et sélection des données utiles

dta = pd.read_csv("donnees_jeux_olympiques/athlete_events.csv")
dta_utile = dta[["ID", "NOC", "Year", "Medal"]]


# Pays non médaillé le plus représenté sur une année donnée.


def pays_non_medaille_max_annee_panda(annee):

    # On initialise le dictionnaire résultat. Il contiendra les couples
    # pays: nombre d'athlètes pour tous les pays non médaillés
    # l'année demandée.
    dico = {}

    # On ne s'intéresse qu'à l'année demandée.
    dta_annee = dta_utile[dta_utile["Year"] == annee]

    # Pour chaque pays, s'il n'a reçu aucune médaille, on compte le nombre
    # d'athlètes qu'il a engagés.
    for noc in dta_annee["NOC"].unique():
        dta_pays = dta_annee[dta_annee["NOC"] == noc]
        if not dta_pays["Medal"].isna().all():
            continue
        dico[noc] = dta_pays["ID"].nunique()

    pays = max(dico, key=dico.get)
    return (
        f"En {annee}, le pays non médaillé le plus représenté était"
        f" {pays} avec {dico[pays]} participants."
    )


# print(pays_non_medaille_max_annee_panda(1912))
