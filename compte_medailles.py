import lecture_donnees

# === 1. Préparation des données ===

# Dictionnaire code NOC → nom de pays
noc_to_country = {}
for ligne in lecture_donnees.donnees_noc_regions[1:]:  # on saute l'en-tête
    code_noc = ligne[0]
    nom_pays = ligne[1]
    noc_to_country[code_noc] = nom_pays

# Récupération des en-têtes
entetes = lecture_donnees.donnees_athlete_events[0]
donnees_athlete_events = lecture_donnees.donnees_athlete_events[1:]

# Indices utiles
annee_idx = entetes.index("Year")
noc_idx = entetes.index("NOC")
medaille_idx = entetes.index("Medal")
event_idx = entetes.index("Event")  # pour détecter les épreuves collectives

# Structure pour éviter les doublons sur les épreuves collectives
epreuves_deja_comptees = set()  # Contiendra les tuples (annee, event, noc)

# === 2. Construction du dictionnaire de médailles (corrigé) ===

# Structure : {année: {pays: {"Gold": ..., "Silver": ..., "Bronze": ..., "Total": ...}}}
medailles_par_annee_et_pays = {}

# Structure pour éviter les doublons sur les épreuves collectives
epreuves_deja_comptees = set()  # Contiendra les tuples (annee, event, noc, medal)

for ligne in donnees_athlete_events:
    annee = ligne[annee_idx]
    code_noc = ligne[noc_idx]
    medaille = ligne[medaille_idx]

    if medaille not in ("Gold", "Silver", "Bronze"):
        continue  # Pas de médaille => on saute

    event = ligne[event_idx]
    est_collectif = event in lecture_donnees.sport_collectif_par_annee.get(annee, set())
    cle = (annee, event, code_noc, medaille)

    if est_collectif:
        if cle in epreuves_deja_comptees:
            continue  # Médaille collective déjà comptée pour cette médaille
        epreuves_deja_comptees.add(cle)

    pays = noc_to_country.get(code_noc, code_noc).strip().title()

    if annee not in medailles_par_annee_et_pays:
        medailles_par_annee_et_pays[annee] = {}

    if pays not in medailles_par_annee_et_pays[annee]:
        medailles_par_annee_et_pays[annee][pays] = {
            "Gold": 0,
            "Silver": 0,
            "Bronze": 0,
            "Total": 0,
        }

    medailles_par_annee_et_pays[annee][pays][medaille] += 1
    medailles_par_annee_et_pays[annee][pays]["Total"] += 1


# === 3. Fonction d'accès aux données ===


def medaille_pays_annee(pays, annee, type_medaille):
    """
    Renvoie le nombre de médailles pour un pays et une année donnés.
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


print(medailles_par_annee_et_pays["2016"]["Usa"]["Total"])
