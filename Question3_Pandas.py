import pandas as pd


# Chargement des données
athlete_events = pd.read_csv("donnees_jeux_olympiques/athlete_events.csv")
noc_regions = pd.read_csv("donnees_jeux_olympiques/noc_regions.csv")
data = pd.merge(athlete_events, noc_regions, on="NOC", how="left")


def count_medals(data, country_name, year, season):
    """
    Compte les médailles d'or, d'argent et de bronze pour un pays donné
    en évitant les doublons liés aux épreuves par équipe.
    """
    # Filtrage
    df = data[(data['Year'] == year) & (data['Season'] == season)]
    df = df[df['region'] == country_name]
    df = df.dropna(subset=['Medal'])

    # Grouper par épreuve pour éviter les doublons (1 médaille par équipe)
    grouped = df.groupby(['Event', 'Medal']).size().reset_index()

    # Compter les médailles
    counts = {
        'Gold': (grouped['Medal'] == 'Gold').sum(),
        'Silver': (grouped['Medal'] == 'Silver').sum(),
        'Bronze': (grouped['Medal'] == 'Bronze').sum()
    }

    return counts


# Affichage
def affichage_medaille_pays_JO(country, year, season):
    medal_counts = count_medals(data, country, year, season)
    total = medal_counts['Gold'] + medal_counts['Silver'] + medal_counts['Bronze']

    # Affichage
    print(f"Médailles {country} aux JO {season} de {year} :")
    print(f"Or     : {medal_counts['Gold']}")
    print(f"Argent : {medal_counts['Silver']}")
    print(f"Bronze : {medal_counts['Bronze']}")
    print(f"Total : {total}")


# Exemple :
# affichage_medaille_pays_JO("France", 2016, "Summer")
