import pandas as pd

# Chargement global des données (à faire une seule fois)
athletes_path = "donnees_jeux_olympiques/athlete_events.csv"
nocs_path = "donnees_jeux_olympiques/noc_regions.csv"

df_athletes = pd.read_csv(athletes_path)
df_nocs = pd.read_csv(nocs_path)

# Correction du nom de pays pour USA
df_nocs.loc[df_nocs["NOC"] == "USA", "region"] = "United States"

# Fusion des données une fois pour toutes
df_merged = df_athletes.merge(df_nocs[["NOC", "region"]], on="NOC", how="left")


def calculer_bornes_medailles_par_nation_pandas(annee):
    """
    Calcule les bornes inférieure et supérieure du nombre total de médailles
    par pays pour une année donnée à partir des données pandas.

    :param annee: int ou str, année des JO
    :return: tuple (borne_min, borne_max)
    """
    annee = int(annee)

    df_year = df_merged[
        (df_merged["Year"] == annee) & (df_merged["Medal"].notna())
    ].copy()

    # Détection des épreuves collectives
    collective_events = set(
        (df_year.groupby("Event").
         filter(lambda x: x["Team"].nunique() > 1)["Event"].unique())
    )

    # Marquage des épreuves collectives
    df_year["IsTeamEvent"] = df_year["Event"].isin(collective_events)

    # Suppression des doublons pour les épreuves collectives
    df_year_dedup = pd.concat([
        df_year[~df_year["IsTeamEvent"]],
        df_year[df_year["IsTeamEvent"]].drop_duplicates(subset=["Team",
                                                                "Event",
                                                                "Medal"]),
    ])

    # Comptage des médailles
    medailles_par_pays = (
        df_year_dedup.groupby("region")["Medal"].value_counts().unstack(fill_value=0)
    )
    medailles_par_pays["Total"] = medailles_par_pays.sum(axis=1)

    # Retour des bornes
    return (medailles_par_pays["Total"].min(), medailles_par_pays["Total"].max())


def afficher_bornes_medailles_par_nation_pandas(annee):
    """
    Affiche les bornes inférieure et supérieure du nombre total de médailles
    par pays pour une année donnée (en utilisant la version pandas).

    :param annee: int ou str
    """
    try:
        borne_min, borne_max = calculer_bornes_medailles_par_nation_pandas(annee)
        print(f"En {annee}, le nombre de médailles par pays varie de {borne_min}"
              f" à {borne_max}.")
    except Exception as e:
        print(f"Erreur lors du traitement de l'année {annee} : {e}")
