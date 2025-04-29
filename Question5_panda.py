import pandas as pd

# Importation et sélection des données utiles

dta = pd.read_csv("donnees_jeux_olympiques/athlete_events.csv")
dta_utile = dta[["ID", "NOC", "Year", "Medal"]]


# Pays non médaillé le plus représenté sur une année donnée.


def pays_non_medailles_max_annee(annee):
    dico = {}
    dta_annee = dta_utile[dta_utile["Year"] == annee]
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


print(pays_non_medailles_max_annee(2016))


# Pays non médaillé le plus représenté dans l'histoire.


def pays_non_medailles_max_histoire():
    dico = {}
    for noc in dta_utile["NOC"].unique():
        dta_pays = dta_utile[dta_utile["NOC"] == noc]
        if not dta_pays["Medal"].isna().all():
            continue
        else:
            dico[noc] = dta_pays[["ID", "Year"]].drop_duplicates().shape[0]
    pays = max(dico, key=dico.get)
    return (
        f"Dans toute l'histoire, le pays non médaillé le plus représenté"
        f" est {pays} avec {dico[pays]} particpants."
    )


print(pays_non_medailles_max_histoire())
