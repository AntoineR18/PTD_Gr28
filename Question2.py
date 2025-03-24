# Trouvez des bornes inférieures et supérieures pour le nombre de médailles
# par nation pour les Jeux Olympiques de 2016.

from lecture_donnees import donnees_athlete_events
from lecture_donnees import donnees_noc_regions

# from compte_medailles import medailles_par_annee_et_pays

# medaille_pays_2016 = medailles_par_annee_et_pays["2016"]
# for pays in medaille_pays_2016.keys():
#     medaille_pays_2016[pays] = medaille_pays_2016[pays]["Total"]
# borne_sup = max(medaille_pays_2016.values())
# borne_inf = min(medaille_pays_2016.values())
# print(borne_inf, borne_sup)

medailles_2016 = {}
for ligne in donnees_athlete_events[1:]:
    code_noc = ligne[7]
    annee = ligne[9]
    if ligne[-1] != "Gold" or annee != "2016":
        continue
    if code_noc not in medailles_2016:
        medailles_2016[code_noc] = 0
    medailles_2016[code_noc] += 1
print(medailles_2016)
