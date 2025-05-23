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
    table = table.dropna(subset=["Age"])
    return table


def moyenne_age_sport(genre: str, sport: str) -> float:
    """
    Retourne la moyenne d'âge des athlètes pour un sport et un genre donné.

    Parameters:
    -----------
    genre : str
        Le genre des athlètes (M ou F).
    sport : str
        Le sport étudié.

    Returns:
    --------
    float
        La moyenne d'âge pour le sport et le genre donné.
    """
    if genre not in {"M", "F"}:
        raise ValueError("Le genre doit être 'M' ou 'F'")
    # Filtrer les données directement
    table = dta[(dta["Sex"] == genre) & (dta["Sport"] == sport)]
    # Calculer la moyenne directement sur la colonne 'Age'
    moyenne_age = table["Age"].mean()
    return moyenne_age


# Calcul des médianes des ages pour chaque sport sport selon le genre
def mediane_age_sport(genre: str, sport: str):
    """
    Retourne un tableau contenant les médianes d'age selon le sport et le genre donné.

    parameters :
    -------------
    genre : str
        Le genre des athlètes (M ou F).

    returns :
    -------------
    table : DataFrame
        Un tableau contenant les médianes d'age pour un sport et genre donné.
    """
    if genre != "M" and genre != "F":
        raise ValueError("Le genre doit être 'M' ou 'F'")
    table = dta[(dta["Sex"] == genre) & (dta["Sport"] == sport)]
    mediane_age = table["Age"].median()
    return mediane_age


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
        borne = moyenne_age_sport(genre, sport)
    elif methode == "mediane":
        borne = mediane_age_sport(genre, sport)
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
        f"Pour le sport {sport} ({genre}, méthode : {methode}) :  \n"
        f"Nombre de médailles pour les plus jeunes : {nb_med_jeunes}  \n"
        f"Nombre de médailles pour les plus âgés : {nb_med_ages}"
    )

    print(resultat)

    with open("Resultat/Question4_Pandas.txt", "w", encoding="utf-8") as f:
        f.write(resultat + "\n")
    return resultat  # important sinon streamlit sort rien
