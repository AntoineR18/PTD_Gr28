import os
import csv


def lire_csv(chemin):
    """
    Lit un fichier CSV et retourne son contenu sous forme de liste de listes.

    Parameters
    ----------
    chemin : str
        Chemin vers le fichier CSV.

    Returns
    -------
    list of list
        Table du fichier CSV (avec l'en-tête en première ligne).
    """
    table = []
    with open(chemin, "r", encoding="utf-8") as fichier:
        lecteur = csv.reader(fichier)
        for ligne in lecteur:
            table.append(ligne)
    return table


def lister_sports_par_annee(donnees_athletes):
    """
    Retourne un dictionnaire contenant pour chaque année la liste des sports
    distincts.

    Parameters
    ----------
    donnees_athletes : list of list
        Données brutes du fichier athlete_events.csv.

    Returns
    -------
    dict of set
        Dictionnaire {année : ensemble des sports pratiqués cette année}.
    """
    entete = donnees_athletes[0]
    donnees = donnees_athletes[1:]

    idx_year = entete.index("Year")
    idx_sport = entete.index("Sport")

    sports_par_annee = {}

    for ligne in donnees:
        annee = ligne[idx_year]
        sport = ligne[idx_sport]
        if annee not in sports_par_annee:
            sports_par_annee[annee] = set()
        sports_par_annee[annee].add(sport)

    return sports_par_annee


# Chargement des deux bases
chemin_athletes = os.path.join("donnees_jeux_olympiques", "athlete_events.csv")
chemin_noc = os.path.join("donnees_jeux_olympiques", "noc_regions.csv")

donnees_athlete_events = lire_csv(chemin_athletes)
donnees_noc_regions = lire_csv(chemin_noc)

# Création du tableau des médaillés
athletes_medailles = []
for ligne in donnees_athlete_events:
    if ligne[-1] != "NA":
        athletes_medailles.append(ligne)

# Création de la structure globale de sports par année
# ----------------------------------------------------
# sports_par_annee est un dictionnaire de la forme suivante :
# {
#     "2016": {"Basketball", "Judo", "Athletics", ...},
#     "2012": {"Swimming", "Tennis", ...},
#     ...
# }
# Exemple d'utilisation :
#   On peut accéder à tous les sports des JO de 2016 avec :
#       sports_par_annee["2016"]
# Cela permet d’avoir une base claire pour travailler sans doublons par année.
sports_par_annee = lister_sports_par_annee(donnees_athlete_events)


def dico_epreuves_collectives(donnees_athletes):
    """
    Détecte les épreuves collectives pour chaque année à partir des données
    d'athlètes, en considérant aussi le sexe pour éviter les confusions entre
    épreuves masculines et féminines.

    Parameters
    ----------
    donnees_athletes : list of list
        Données brutes du fichier athlete_events.csv.

    Returns
    -------
    dict of set
        Dictionnaire {année : ensemble des épreuves collectives détectées}.
    """
    entete = donnees_athletes[0]
    donnees = donnees_athletes[1:]

    idx_year = entete.index("Year")
    idx_sport = entete.index("Sport")
    idx_event = entete.index("Event")
    idx_team = entete.index("Team")
    idx_medal = entete.index("Medal")
    idx_sex = entete.index("Sex")

    from collections import defaultdict

    regroupement = defaultdict(list)

    for ligne in donnees:
        annee = ligne[idx_year]
        sport = ligne[idx_sport]
        event = ligne[idx_event]
        team = ligne[idx_team]
        medal = ligne[idx_medal]
        sex = ligne[idx_sex]

        if medal not in ("Gold", "Silver", "Bronze"):
            continue  # Ignore les non-médaillés

        cle = (annee, event, sport, team, medal, sex)
        regroupement[cle].append(ligne)

    epreuves_collectives = defaultdict(set)

    for (annee, event, *_), participants in regroupement.items():
        if len(participants) > 1:
            epreuves_collectives[annee].add(event)

    return dict(epreuves_collectives)


# Dictionnaire des épreuves collectives par année.
# Exemple : sport_collectif_par_annee["2016"] =
#   {"Basketball Men's Basketball",
#    "Athletics Men's 4 x 100 metres Relay", ...}
# Permet d’éviter les doublons lors du comptage des médailles collectives.
sport_collectif_par_annee = dico_epreuves_collectives(donnees_athlete_events)
