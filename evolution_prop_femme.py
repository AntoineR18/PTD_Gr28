import pandas as pd
import matplotlib.pyplot as plt

# Charger le fichier CSV
df = pd.read_csv("donnees_jeux_olympiques/athlete_events.csv")

# Garder uniquement les colonnes pertinentes
df_filtered = df[["Year", "Sex"]]

# Filtrer uniquement les femmes
femmes_par_annee = df_filtered[df_filtered["Sex"] == "F"].groupby("Year").size()

# Nombre total d'athlètes par année (pour info ou pour calculer proportion)
total_par_annee = df_filtered.groupby("Year").size()

# Proportion de femmes par année
proportion_femmes = (femmes_par_annee / total_par_annee) * 100

# Tracer le graphique
plt.figure(figsize=(12, 6))
plt.plot(proportion_femmes.index,
         proportion_femmes.values,
         marker='o',
         linewidth=2,
         color="hotpink")
plt.title("Évolution de la proportion de femmes aux Jeux Olympiques (été + hiver)",
          fontsize=14)
plt.xlabel("Année", fontsize=12)
plt.ylabel("Proportion de femmes (%)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
