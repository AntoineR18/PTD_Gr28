import pandas as pd

# Importation des données et sélection des athlètes masculins
dta = pd.read_csv("donnees_jeux_olympiques/athlete_events.csv")


def table_sport(genre: str):
    """
    Retourne un tableau contenant les sports, ages et médailles des athlètes pour un
    genre donné.

    parameters :
    -------------
    genre : str
        Le genre des athlètes (M ou F).

    returns :
    -------------
    table : DataFrame
        Un tableau contenant les sports, ages et médailles des athlètes pour un genre
        donné.
    """
    if genre != "M" and genre != "F":
        raise ValueError("Le genre doit être 'M' ou 'F'")
    table = dta[["Sport", "Age", "Sex", "Medal"]]
    table = table[table["Sex"] == genre]
    table = table.dropna(subset=["Age", "Medal"])
    return table


def moyenne_age_sport(genre: str):
    """
    Retourne un tableau contenant les moyennes d'age pour chaque sport selon le genre
    donné.

    parameters :
    -------------
    genre : str
        Le genre des athlètes (M ou F).

    returns :
    -------------
    table : DataFrame
        Un tableau contenant les moyennes d'age pour chaque sport selon le genre
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

    parameters :
    -------------
    genre : str
        Le genre des athlètes (M ou F).

    returns :
    -------------
    table : DataFrame
        Un tableau contenant les médianes d'age pour chaque sport selon le genre
        donné.
    """
    if genre != "M" and genre != "F":
        raise ValueError("Le genre doit être 'M' ou 'F'")
    table = dta[dta["Sex"] == genre]
    return table.groupby("Sport")["Age"].median()


def comp_meda_moy_age(sport: str, methode: str, genre: str):
    """
    Compare l'obtention des médailles des athlètes en fonction de leur âge et de leur
    sexe.

    parameters :
    -------------
    sport : str
        Le sport étudié.
    methode : str
        La méthode utilisée pour séparer les athlètes en deux groupes : 'moyenne' ou
        'mediane'.
    genre : str
        Le genre des athlètes (M ou F).

    returns :
    -------------
    resultat : str
        Un message indiquant le nombre de médailles pour les plus jeunes et les plus
        âgés.
    """
    # On vérifie qu'il y a pas d'erreurs dans les paramètres
    table = table_sport(genre)
    if sport not in table["Sport"].values:
        raise ValueError("Le sport rentré n'est pas dans la liste des sports")
    if methode != "moyenne" and methode != "mediane":
        raise ValueError("La méthode doit être 'moyenne' ou 'mediane'")
    if genre != "M" and genre != "F":
        raise ValueError("Le genre doit être 'M' ou 'F'")
    # on définit la borne selon la méthode choisie
    if methode == "moyenne":
        borne = moyenne_age_sport(genre)[sport]
    elif methode == "mediane":
        borne = mediane_age_sport(genre)[sport]
    # Compter les médailles pour les plus jeunes et les plus âgés
    # On créé d'abord la table pour le sport donné
    table_s = table[table["Sport"] == sport].dropna(subset=["Age"])
    # ensuite on fait la somme des médailles (not NA) pour ceux dont l'age est inférieur
    # ou supérieur à la borne
    nb_med_jeunes = (
        (table_s["Age"] < borne) & (table_s["Medal"].notna())
    ).sum()
    nb_med_ages = (
        (table_s["Age"] >= borne) & (table_s["Medal"].notna())
    ).sum()
    # Afficher le résultat
    resultat = (
        f"Pour le sport {sport} :  \n"
        f"Nombre de médailles pour les plus jeunes : {nb_med_jeunes}  \n"
        f"Nombre de médailles pour les plus âgés : {nb_med_ages}"
    )  # important d'avoir les espaces avant le \n pour le retour à la ligne (surtout
    # pour streamlit)
    print(resultat)
    return resultat  # important sinon streamlit sort rien


def affichage_comparaison_medailles_age(sport: str, methode: str, genre: str):
    """
    Affiche la comparaison du nombre de médailles entre les athlètes plus jeunes
    et plus âgés pour un sport donné, selon la méthode choisie.

    :param sport: nom du sport (ex: "Swimming")
    :param methode: 'moyenne' ou 'mediane'
    :param genre: 'M' ou 'F'
    """
    try:
        resultat = comp_meda_moy_age(sport, methode, genre)
        print("\n--- Résultat ---")
        print(resultat)
    except ValueError as e:
        print(f"Erreur : {e}")


# Test des fonctions avec les sports spécifiés
comp_meda_moy_age("Swimming", "moyenne", "M")
comp_meda_moy_age("Trampolining", "mediane", "F")
comp_meda_moy_age("Gymnastics", "mediane", "M")
