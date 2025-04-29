import pandas as pd

# Importation des données et sélection des athlètes masculins
dta = pd.read_csv("donnees_jeux_olympiques/athlete_events.csv")


# Sélection des colonnes Sport, Age, Sexe et médailles
def table_sport(genre: str):
    """
    Retourne un tableau contenant les sports, ages et médailles des athlètes pour un
    genre donné.
    """
    if genre != "M" and genre != "F":
        raise ValueError("Le genre doit être 'M' ou 'F'")
    table = dta[["Sport", "Age", "Sex", "Medal"]]
    table = table[table["Sex"] == genre]
    table = table.dropna(subset=["Age", "Medal"])
    return table


# Calcul des moyennes d'age pour chaque sport selon le genre
def moyenne_age_sport(genre: str):
    """
    Retourne un tableau contenant les moyennes d'age pour chaque sport selon le genre
    donné.
    """
    if genre != "M" and genre != "F":
        raise ValueError("Le genre doit être 'M' ou 'F'")
    table = dta[dta["Sex"] == genre]
    return table.dropna(subset=['Age']).groupby("Sport")["Age"].mean()


# Calcul des médianes des ages pour chaque sport sport selon le genre
def mediane_age_sport(genre: str):
    """
    Retourne un tableau contenant les médianes d'age pour chaque sport selon le genre
    donné.
    """
    if genre != "M" and genre != "F":
        raise ValueError("Le genre doit être 'M' ou 'F'")
    table = table_sport(genre)
    return table.groupby("Sport")["Age"].median()


# # Recherche du sport avec la plus petite moyenne d'âge
# sport_min_age = moyenne_age_sport.idxmin()
# moyenne_min_age = moyenne_age_sport.min()
# print(
#     f"Le sport avec la plus petite moyenne d'âge est {sport_min_age} avec une moyenne"
#     f" de {moyenne_min_age:.1f} ans."
# )


def comp_meda_moy_age(sport: str, methode: str, genre: str):
    """
    Compare l'obtention des médailles des athlètes en fonction de leur âge et de leur
    sexe."""
    # Vérifier si le sport est dans la liste des sports
    table = table_sport(genre)
    if sport not in table["Sport"].values:
        raise ValueError("Le sport rentré n'est pas dans la liste des sports")
    if methode != "moyenne" and methode != "mediane":
        raise ValueError("La méthode doit être 'moyenne' ou 'mediane'")
    if genre != "M" and genre != "F":
        raise ValueError("Le genre doit être 'M' ou 'F'")
    if methode == "moyenne":
        borne = moyenne_age_sport(genre)[sport]
    elif methode == "mediane":
        borne = mediane_age_sport(genre)[sport]
    # Compter les médailles pour les plus jeunes et les plus âgés
    # On créé d'abord la table pr le sport donné
    table_s = table[table["Sport"] == sport].dropna(subset=["Age"])
    nb_med_jeunes = (
        (table_s["Age"] < borne) & (table_s["Medal"].notna())
    ).sum()
    nb_med_ages = (
        (table_s["Age"] >= borne) & (table_s["Medal"].notna())
    ).sum()
    # Afficher le résultat
    print(f"Pour le sport {sport} :")
    print(f"Nombre de médailles pour les plus jeunes : {nb_med_jeunes}")
    print(f"Nombre de médailles pour les plus agés : {nb_med_ages}")


# Test des fonctions avec les sports spécifiés
comp_meda_moy_age("Swimming", "moyenne", "M")
comp_meda_moy_age("Trampolining", "moyenne", "M")
comp_meda_moy_age("Gymnastics", "moyenne", "M")
