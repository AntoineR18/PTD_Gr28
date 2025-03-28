import pandas as pd

# Charger le fichier CSV
df_athletes = pd.read_csv("donnees_jeux_olympiques/athlete_events.csv")

# Filtrer les lignes correspondant à "Michael Fred Phelps, II" avec Medal != NA
df_phelps = df_athletes[
    (df_athletes["Name"] == "Michael Fred Phelps, II") &
    (df_athletes["Medal"].notna())
]

# Compter les médailles par type
medals_count = df_phelps["Medal"].value_counts()

# Ajouter une ligne "Total"
medals_count["Total"] = medals_count.sum()

# Afficher le résultat
print(medals_count)
