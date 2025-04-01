import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("donnees_jeux_olympiques/athlete_events.csv")


def plot_medaille_pays_selon_saison(pays, df):
    """
    Affiche un graphique montrant la répartition des médailles entre les JO d'été et
    d'hiver pour un pays donné.

    Parameters
    ----------
    country : str
        Code NOC (National Olympic Committee) du pays (ex: 'FRA', 'USA', 'CHN').

    df : pandas.DataFrame
        DataFrame contenant les données des athlètes olympiques, avec au minimum
        les colonnes "Games", "NOC" et "Medal".

    Returns
    -------
    None
        Affiche un graphique matplotlib représentant la proportion (%) des médailles
        obtenues lors des JO d'été et d'hiver.
    """
    # On garde que les médailles
    df_medals = df[df["Medal"].notna()]

    df_country = df_medals[df_medals["NOC"] == pays]

    # Déterminer la saison à partir de la colonne "Games"
    df_country["Season"] = df_country["Games"].apply(
        lambda x: "Summer" if "Summer" in x else "Winter"
    )

    # Compter le nombre de médailles par saison
    season_comptage = df_country["Season"].value_counts(normalize=True) * 100

    # Tracer un graphique en barres
    plt.figure(figsize=(6, 4))
    season_comptage.plot(kind='bar', color=["gold", "skyblue"])
    plt.title(f"Répartition des médailles {pays} - Été vs Hiver")
    plt.ylabel("Proportion (%)")
    plt.xticks(rotation=0)
    plt.ylim(0, 100)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()


plot_medaille_pays_selon_saison("FRA", df)  # Pour la France
