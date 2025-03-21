import os
import csv
from lecture_donnees import donnees_athlete_events, donnees_noc_regions

# === 1. Préparation des données ===

# Dictionnaire code NOC → nom de pays
noc_to_country = {}
for ligne in donnees_noc_regions[1:]:  # on saute l'en-tête
    code_noc = ligne[0]
    nom_pays = ligne[1]
    noc_to_country[code_noc] = nom_pays

# Récupération des en-têtes
entetes = donnees_athlete_events[0]
donnees_athlete_events = donnees_athlete_events[1:]

# Indices utiles
annee_idx = entetes.index("Year")
noc_idx = entetes.index("NOC")
medaille_idx = entetes.index("Medal")

# === 2. Construction du dictionnaire de médailles ===

# Structure : {année: {pays: {"Gold": ..., "Silver": ..., "Bronze": ..., "Total": ...}}}
medailles_par_annee_et_pays = {}

for ligne in donnees_athlete_events:
    annee = ligne[annee_idx]
    code_noc = ligne[noc_idx]
    medaille = ligne[medaille_idx]

    if medaille not in ("Gold", "Silver", "Bronze"):
        continue  # Pas de médaille => on saute

    pays = noc_to_country.get(code_noc, code_noc)  # nom du pays ou code si inconnu
    pays = pays.strip().title()  # uniformisation (ex : "france" → "France")

    if annee not in medailles_par_annee_et_pays:
        medailles_par_annee_et_pays[annee] = {}

    if pays not in medailles_par_annee_et_pays[annee]:
        medailles_par_annee_et_pays[annee][pays] = {
            "Gold": 0,
            "Silver": 0,
            "Bronze": 0,
            "Total": 0
        }

    medailles_par_annee_et_pays[annee][pays][medaille] += 1
    medailles_par_annee_et_pays[annee][pays]["Total"] += 1

# === 3. Fonction d'accès aux données ===

def medaille_pays_annee(pays, annee, type_medaille):
    """
    Renvoie le nombre de médailles pour un pays et une année donnés.

    Parameters
    ----------
    pays : str
        Nom du pays (ex. "France"). La casse et les espaces sont ignorés.
    annee : int or str
        Année des Jeux Olympiques (ex. 2012).
    type_medaille : str
        Type de médaille : "Gold", "Silver", "Bronze" ou "Total". La casse est ignorée.

    Returns
    -------
    int
        Nombre de médailles correspondant au pays, à l'année et au type demandé.
        Retourne 0 si aucune donnée n'existe.

    Examples
    --------
    >>> medaille_pays_annee("France", 2012, "Gold")
    82

    >>> medaille_pays_annee("usa", "2016", "total")
    121
    """
    annee = str(annee)
    pays = pays.strip().title()
    type_medaille = type_medaille.strip().title()

    if annee not in medailles_par_annee_et_pays:
        return 0
    if pays not in medailles_par_annee_et_pays[annee]:
        return 0
    if type_medaille not in medailles_par_annee_et_pays[annee][pays]:
        return 0

    return medailles_par_annee_et_pays[annee][pays][type_medaille]
