import pandas as pd

# Importation et sélection des données utiles

dta = pd.read_csv("donnees_jeux_olympiques/athlete_events.csv")
dta_utile = dta[["ID", "Sex", "NOC", "Year", "Medal"]]


def nb_participants(annee=None, pays=None, sexe=None, medaille=None):
    df = dta_utile.copy()

    if annee is not None:
        df = df[df["Year"] == annee]
    if pays is not None:
        df = df[df["NOC"] == pays]
    if sexe is not None:
        df = df[df["Sex"] == sexe]

    if medaille is True:
        df = df[df["Medal"].notna()]
    elif medaille is False:
        df = df[df["Medal"].isna()]
    df = df.drop_duplicates(subset=["ID", "Year"])
    return df.shape[0]


# print(nb_participants(pays="EGY", medaille=False))
