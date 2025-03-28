import pandas as pd

# Chargement des fichiers CSV
athletes_path = "donnees_jeux_olympiques/athlete_events.csv"
nocs_path = "donnees_jeux_olympiques/noc_regions.csv"

df_athletes = pd.read_csv(athletes_path)
df_nocs = pd.read_csv(nocs_path)

# Correction du nom de pays pour le code NOC "USA"
df_nocs.loc[df_nocs["NOC"] == "USA", "region"] = "United States"

# Fusion des données pour associer les pays aux athlètes
df_athletes_merged = df_athletes.merge(df_nocs[["NOC", "region"]], on="NOC", how="left")

# Filtrage : médailles uniquement pour l'année 2016
df_2016 = df_athletes_merged[
    (df_athletes_merged["Year"] == 2016) &
    (df_athletes_merged["Medal"].notna())
].copy()

# Détection des épreuves collectives
# (plusieurs équipes différentes dans une même épreuve)
collective_events_2016 = df_2016.groupby("Event").filter(
    lambda x: x["Team"].nunique() > 1
)["Event"].unique()
collective_events_2016 = set(collective_events_2016)

# Marquage des épreuves collectives
df_2016["IsTeamEvent"] = df_2016["Event"].isin(collective_events_2016)

# Suppression des doublons pour les épreuves collectives
df_2016_dedup = pd.concat([
    df_2016[~df_2016["IsTeamEvent"]],  # épreuves individuelles : on garde tout
    df_2016[df_2016["IsTeamEvent"]].drop_duplicates(subset=["Team", "Event", "Medal"])
])

# Comptage des médailles par pays
medailles_par_pays_2016 = (df_2016_dedup.groupby("region")["Medal"]
                           .value_counts().unstack(fill_value=0))

# Ajout de la colonne Total
medailles_par_pays_2016["Total"] = medailles_par_pays_2016.sum(axis=1)

# Calcul des bornes inférieure et supérieure
borne_inferieure = medailles_par_pays_2016["Total"].min()
borne_superieure = medailles_par_pays_2016["Total"].max()

print(f"La borne inférieur est : {borne_inferieure}\n"
      f"La borne supérieure est : {borne_superieure}")
