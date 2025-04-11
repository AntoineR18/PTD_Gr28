import pandas as pd

# importation des données, et sélection des athlètes masculins
dta = pd.read_csv('donnees_jeux_olympiques/athlete_events.csv')
dta_h = dta[dta['Sex'] == 'M']

# Je sélectionne les colonnes Sport, Age, et médailles.
dta_h = dta_h[['Sport', 'Age', 'Medal']]
dta_h = dta_h.dropna(subset=['Age'])

# Je calcule les moyennes d'âge par sport
moyenne_age_sport = dta_h.groupby('Sport')['Age'].mean()

# On cherche le sport avec la plus petite moyenne d'âge
sport_min_age = moyenne_age_sport.idxmin()
moyenne_min_age = moyenne_age_sport.min()
print(f"Le sport avec la plus petite moyenne d'âge est {sport_min_age} avec une moyenne"
      f" de {moyenne_min_age:.1f} ans.")
# On retrouve bien la natation, avec une moyenne de 21,6 ans


def comp_meda_moy_age(sport: str):
    # Vérifier si le sport est dans la liste des sports
    if sport not in moyenne_age_sport.index:
        raise ValueError("Le sport rentré n'est pas dans la liste des sports")
    age_moyen_sport = moyenne_age_sport[sport]
    dta_h_sport = dta_h[dta_h['Sport'] == sport]
    if dta_h_sport['Age'] < age_moyen_sport[sport]:
        nb_med_jeunes = dta_h_sport
    nb_med_vieux = dta_h_sport['Age'] >= age_moyen_sport['Medal'].notna().sum()

    print(f"Pour le sport {sport} :")
    print(f"Nombre de médailles pour les plus jeunes : {nb_med_jeunes}")
    print(f"Nombre de médailles pour les plus agés : {nb_med_vieux}")


comp_meda_moy_age("Swimming")
comp_meda_moy_age("Trampolining")
comp_meda_moy_age("Gymnastics")
