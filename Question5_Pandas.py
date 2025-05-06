import pandas as pd
import matplotlib.pyplot as plt

# Importation et sélection des données utiles

dta = pd.read_csv("donnees_jeux_olympiques/athlete_events.csv")
dta_noc = pd.read_csv("donnees_jeux_olympiques/noc_regions.csv")
dta_utile = dta[["ID", "NOC", "Year", "Medal"]]


# Pays non médaillé le plus représenté sur une année donnée.


def pays_non_medaille_max_annee_panda(annee):

    # Initialisation du dictionnaire résultat.
    # Il contiendra les couples pays: nombre d'athlètes pour tous les
    # pays non médaillés l'année demandée.
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


print(pays_non_medaille_max_annee_panda(1912))


# Diagramme en barres des pays non médaillés sur une année


def diagramme_annee(annee):

    # On récupère le dictionnaire des pays non médaillés et leur nombre
    # de participants.
    dico = {}
    dta_annee = dta_utile[dta_utile["Year"] == annee]

    for noc in dta_annee["NOC"].unique():
        dta_pays = dta_annee[dta_annee["NOC"] == noc]
        if not dta_pays["Medal"].isna().all():
            continue
        dico[noc] = dta_pays["ID"].nunique()

    # On transforme le dictionnaire en dataframe et on ne conserve que les pays
    # avec au moins 10 participants pour ne pas surcharger le graphe.
    df = pd.DataFrame(list(dico.items()), columns=["Pays", "Nombre_participants"])
    df = df[df["Nombre_participants"] > 9]

    # Tri décroissant
    df = df.sort_values(by="Nombre_participants", ascending=False)

    # Création du graphe
    df.plot.bar(
        x="Pays",
        y="Nombre_participants",
        color="hotpink",
        edgecolor="black",
        legend=False,
    )

    # Personnalisation du graphe
    plt.title("Nombre d'athlètes par pays non médaillés en 2016")
    plt.xlabel("Pays")
    plt.ylabel("Nombre d'athlètes")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


diagramme_annee(2016)


# Diagramme en barres des pays non médaillés au cours de l'histoire


def diagramme_histoire():

    # Création de la liste exhaustive des années olympiques
    annees = [annee for annee in range(1896, 1993, 4)]
    annees.pop(annees.index(1916))
    annees.pop(annees.index(1940))
    annees.pop(annees.index(1944))
    annees.append(1906)
    annees.extend([annee for annee in range(1994, 2017, 2)])
    annees.sort()

    # Création du dictionnaire résultat.
    # Il contient, pour chaque année,
    dico = {}

    for annee in annees:

        dico_annee = {}
        dta_annee = dta_utile[dta_utile["Year"] == annee]

        for noc in dta_annee["NOC"].unique():
            dta_pays = dta_annee[dta_annee["NOC"] == noc]
            if not dta_pays["Medal"].isna().all():
                continue
            dico_annee[noc] = dta_pays["ID"].nunique()

        pays = max(dico_annee, key=dico_annee.get)

        dico[(annee, pays)] = dico_annee[pays]

    # Conversion en dataframe
    df = pd.DataFrame(list(dico.items()), columns=["Pays", "Nombre_participants"])

    # Tri décroissant
    df = df.sort_values(by="Nombre_participants", ascending=False)

    df.plot.bar(
        x="Pays",
        y="Nombre_participants",
        color="hotpink",
        edgecolor="black",
        legend=False,
    )

    plt.title("Pays non médaillé le plus représenté sur chaque édition")
    plt.xlabel("Année")
    plt.ylabel("Nombre d'athlètes")
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()


diagramme_histoire()
