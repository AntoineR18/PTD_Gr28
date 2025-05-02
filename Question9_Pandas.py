import pandas as pd
import matplotlib.pyplot as plt


def plot_proportion_femmes(saison=None):
    """
    Affiche l'évolution de la proportion de femmes aux Jeux Olympiques.

    Paramètres :
    - saison : None (par défaut) pour été + hiver,
               "summer" pour JO d'été,
               "winter" pour JO d'hiver
    """
    # Charger le fichier CSV
    df = pd.read_csv("donnees_jeux_olympiques/athlete_events.csv")

    # Filtrage par saison si spécifié
    if saison is not None:
        saison = saison.capitalize()  # pour être tolérant à "summer"/"Summer"
        df = df[df["Season"] == saison]

    # Garder uniquement les colonnes pertinentes
    df_filtered = df[["Year", "Sex"]]

    # Filtrer uniquement les femmes
    femmes_par_annee = df_filtered[df_filtered["Sex"] == "F"].groupby("Year").size()

    # Nombre total d'athlètes par année
    total_par_annee = df_filtered.groupby("Year").size()

    # Proportion de femmes par année
    proportion_femmes = (femmes_par_annee / total_par_annee) * 100

    # Titre adapté
    titre = "Évolution de la proportion de femmes aux JO"
    if saison == "Summer":
        titre += " d'été"
    elif saison == "Winter":
        titre += " d'hiver"
    else:
        titre += " d'été et d'hiver"

    # Tracer le graphique
    plt.figure(figsize=(12, 6))
    plt.plot(proportion_femmes.index,
             proportion_femmes.values,
             marker='o',
             linewidth=2,
             color="hotpink")
    plt.title(titre, fontsize=14)
    plt.xlabel("Année", fontsize=12)
    plt.ylabel("Proportion de femmes (%)", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


plot_proportion_femmes()          # été + hiver
plot_proportion_femmes("summer")  # seulement été
plot_proportion_femmes("winter")  # seulement hiver
