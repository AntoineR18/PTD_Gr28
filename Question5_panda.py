import pandas as pd
import matplotlib.pyplot as plt

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


# Diagramme en barres des pays non médaillés

import pandas as pd
import matplotlib.pyplot as plt


def pays_non_medaille_diagramme(annee):
    dico = {}
    dta_annee = dta_utile[dta_utile["Year"] == annee]

    for noc in dta_annee["NOC"].unique():
        dta_pays = dta_annee[dta_annee["NOC"] == noc]
        if not dta_pays["Medal"].isna().all():
            continue
        dico[noc] = dta_pays["ID"].nunique()

    return dico


# Obtenir les données
dico = pays_non_medaille_diagramme(2016)

# Transformer en DataFrame
df = pd.DataFrame(list(dico.items()), columns=["Pays", "Nombre_participants"])

# Tracer l'histogramme
df["Nombre_participants"].hist(bins=10, color="red", edgecolor="black")

plt.title("Nombre d'athlètes des pays non médaillés (2016)")
plt.xlabel("Nombre d'athlètes")
plt.ylabel("Nombre de pays")
plt.tight_layout()
plt.show()
