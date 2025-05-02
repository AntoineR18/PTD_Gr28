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


def plot_medaille_global_ete_vs_hiver(df):
    """
    Affiche la répartition globale des médailles entre les JO d'été et d'hiver.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame contenant les données des athlètes olympiques,
        avec au minimum les colonnes "Season" et "Medal".

    Returns
    -------
    None
        Affiche un graphique matplotlib représentant la proportion (%) des médailles
        obtenues lors des JO d'été et d'hiver.
    """
    # Garder uniquement les lignes avec une médaille
    df_medals = df[df["Medal"].notna()]

    # Compter les médailles par saison
    season_counts = df_medals["Season"].value_counts(normalize=True) * 100

    # Tracer le graphique
    plt.figure(figsize=(6, 4))
    season_counts.plot(kind="bar", color=["coral", "deepskyblue"])
    plt.title("Répartition globale des médailles - Été vs Hiver")
    plt.ylabel("Proportion (%)")
    plt.xticks(rotation=0)
    plt.ylim(0, 100)
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.show()


def plot_part_medaille_par_pays_dans_saison(saison, df, top_n=10):
    """
    Affiche la proportion des médailles gagnées par chaque pays pour une saison donnée,
    relativement au total des médailles distribuées dans cette saison (été ou hiver).

    Parameters
    ----------
    saison : str
        "Summer" ou "Winter".

    df : pandas.DataFrame
        DataFrame contenant les données des athlètes olympiques avec les colonnes
        "Season", "NOC" et "Medal".

    top_n : int
        Nombre de pays à afficher (les plus médaillés). Les autres sont regroupés.

    Returns
    -------
    None
        Affiche un graphique matplotlib.
    """
    # Filtrer les médailles pour la saison choisie
    df_medals = df[(df["Medal"].notna()) & (df["Season"] == saison)]

    # Compter les médailles par pays (NOC)
    country_medal_counts = df_medals["NOC"].value_counts(normalize=True) * 100

    # Garder les top_n pays
    top_countries = country_medal_counts.head(top_n)

    # Tracer le graphique
    plt.figure(figsize=(9, 6))
    top_countries.sort_values(ascending=False).plot(kind='bar', color='mediumpurple')
    plt.title(f"Part des médailles par pays - JO {saison}")
    plt.ylabel("Proportion (%)")
    plt.xlabel("Pays (NOC)")
    plt.xticks(rotation=45)
    plt.ylim(0, 100)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()


def plot_medaille_normalisee_pays(pays, df):
    df_medals = df[df["Medal"].notna()].copy()

    # Groupe par année + saison pour connaître le total de médailles distribuées
    # par édition
    total_medals_by_game = (
        df_medals.groupby(["Year", "Season"]).size().reset_index(name="Total_Medals"))

    # Groupe par année + saison + pays pour savoir combien ce pays a gagné
    # cette année-là
    country_medals = df_medals[df_medals["NOC"] == pays]
    country_by_game = (country_medals.groupby(["Year", "Season"]).
                       size().reset_index(name="Country_Medals"))

    # Merge des deux
    merged = pd.merge(country_by_game, total_medals_by_game, on=["Year", "Season"])
    merged["Medal_Share"] = merged["Country_Medals"] / merged["Total_Medals"]

    # Moyenne par saison
    season_avg = merged.groupby("Season")["Medal_Share"].mean() * 100

    # Affichage
    plt.figure(figsize=(6, 4))
    season_avg.plot(kind='bar', color=["gold", "skyblue"])
    plt.title(f"Part moyenne des médailles pour {pays} - Été vs Hiver")
    plt.ylabel("Part moyenne des médailles (%)")
    plt.xticks(rotation=0)
    plt.ylim(0, season_avg.max() * 1.2)
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.show()


plot_medaille_global_ete_vs_hiver(df)
plot_medaille_pays_selon_saison("USA", df)  # Pour la France

