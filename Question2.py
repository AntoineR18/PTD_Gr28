# --------------------------------------
# Fichier inutile car déjà codé en Panda
# --------------------------------------


# from lecture_donnees import (
#     athletes_medailles,
#     sports_par_annee,
#     sport_collectif_par_annee,
# )

# # Création des liste de sports spécifiques à 2016
# sports_2016 = sports_par_annee["2016"]
# sports_co_2016 = list(sport_collectif_par_annee["2016"])

# entete = athletes_medailles[0]
# donnees = athletes_medailles[1:]

# idx_annee = entete.index("Year")
# idx_noc = entete.index("NOC")
# idx_sport = entete.index("Sport")
# idx_event = entete.index("Event")
# idx_medal = entete.index("Medal")

# # Création d'une liste des pays par NOC
# liste_noc = set()
# for ligne in donnees:
#     liste_noc.add(ligne[idx_noc])

# # Pour chaque pays, on crée un dictionnaire des sports collectifs pour
# # vérifier s'ils ont déjà été traités ou non.
# events_co_2016_noc = {
#     noc: {event: False for event in sports_co_2016} for noc in liste_noc
# }

# # Création du dictionnaire du nombre de médailles par pays en 2016
# medailles_2016 = {}
# for ligne in donnees:
#     annee = ligne[idx_annee]
#     if annee != "2016":
#         continue
#     noc = ligne[idx_noc]
#     sport = ligne[idx_sport]
#     event = ligne[idx_event]
#     medal = ligne[idx_medal]
#     if noc not in medailles_2016:
#         medailles_2016[noc] = 0
#     if event not in sports_co_2016:
#         medailles_2016[noc] += 1
#     else:
#         if not events_co_2016_noc[noc][event]:
#             medailles_2016[noc] += 1
#             events_co_2016_noc[noc][event] = True

# # Dictionnaire contenant les vraies données de 2016
# vraies_medailles_2016 = {
#     "ITA": 28,
#     "AZE": 18,
#     "FRA": 42,
#     "IRI": 8,
#     "RUS": 56,
#     "AUS": 29,
#     "ESP": 17,
#     "JOR": 1,
#     "NED": 19,
#     "GBR": 67,
#     "USA": 121,
#     "NZL": 18,
#     "RSA": 10,
#     "INA": 3,
#     "GER": 42,
#     "NGR": 1,
#     "CAN": 22,
#     "TUR": 8,
#     "UZB": 13,
#     "IOA": 2,
#     "ARM": 4,
#     "SRB": 8,
#     "NIG": 1,
#     "BRA": 19,
#     "JAM": 11,
#     "NOR": 4,
#     "CUB": 11,
#     "COL": 8,
#     "TUN": 3,
#     "KOR": 21,
#     "DEN": 15,
#     "SWE": 11,
#     "JPN": 41,
#     "MAS": 5,
#     "ETH": 8,
#     "SUI": 7,
#     "KAZ": 17,
#     "QAT": 1,
#     "UKR": 11,
#     "SVK": 4,
#     "ROU": 4,
#     "CRO": 10,
#     "BEL": 6,
#     "HUN": 15,
#     "GEO": 7,
#     "BAH": 2,
#     "ARG": 4,
#     "CHN": 70,
#     "KEN": 13,
#     "PRK": 7,
#     "POL": 11,
#     "CIV": 2,
#     "FIJ": 1,
#     "BUL": 3,
#     "PHI": 1,
#     "LTU": 4,
#     "MGL": 2,
#     "CZE": 10,
#     "EST": 1,
#     "MEX": 5,
#     "VEN": 3,
#     "AUT": 1,
#     "BLR": 9,
#     "ISR": 2,
#     "GRE": 6,
#     "THA": 6,
#     "VIE": 2,
#     "TPE": 3,
#     "EGY": 3,
#     "GRN": 1,
#     "BRN": 2,
#     "SLO": 4,
#     "KOS": 1,
#     "ALG": 2,
#     "IND": 2,
#     "POR": 1,
#     "IRL": 2,
#     "TJK": 1,
#     "BDI": 1,
#     "DOM": 1,
#     "FIN": 1,
#     "PUR": 1,
#     "MAR": 1,
#     "SGP": 1,
#     "UAE": 1,
#     "TTO": 1,
# }

# pays_faux = {
#     noc: {"temoin": vraies_medailles_2016[noc], "test": medailles_2016[noc]}
#     for noc in vraies_medailles_2016.keys()
#     if vraies_medailles_2016[noc] != medailles_2016[noc]
# }

# nb_medailles = list(medailles_2016.values())
# nb_medailles.sort()
# print(nb_medailles)

# borne_inf, borne_sup = nb_medailles[1], nb_medailles[-1]
# pays_inf, pays_sup = nb_medailles.index(borne_inf), nb_medailles(borne_sup)
# print(medailles_2016)
# print(
#     f"La borne inférieure pour le nombre de médailles vaut {borne_inf}"
#     f" tandis que le borne supérieure s'élève à {borne_sup}."
# )
