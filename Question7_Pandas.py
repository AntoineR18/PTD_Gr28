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

    count = df.shape[0]

    texte = (
        f"📊 Nombre de participants"
        f"{' en ' + str(annee) if annee else ''}"
        f"{' du pays ' + pays if pays else ''}"
        f"{' de sexe ' + sexe if sexe else ''}"
        f"{' avec médaille' if medaille is True else ''}"
        f"{' sans médaille' if medaille is False else ''} : {count}"
    )

    print(texte)

    with open("Resultat/Question7.txt", "w", encoding="utf-8") as f:
        f.write(texte + "\n")

    return df.shape[0]

# print(nb_participants(pays="EGY", medaille=False))
