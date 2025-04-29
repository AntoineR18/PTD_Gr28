import pandas as pd

from lecture_donnees import (
    donnees_athlete_events,
    donnees_noc_regions,
)

data = {"Pays": [], "années de participation": []}
df_noc = pd.DataFrame(data, columns=["Pays", "années de participation"])

for ligne in donnees_athlete_events[1 : len(donnees_athlete_events)]:
    L = 0
    année_a_mettre = ligne[9]
    if ligne[7] == "SGP":
        noc = "SIN"
    elif ligne[7] in ("VNM", "VIE"):
        noc = "VNM"
    else:
        noc = ligne[7]
    if noc in df_noc["Pays"]:
        id_ligne = df_noc[df_noc["Pays"] == noc].index[0]
        val1 = df_noc.loc(id_ligne, "année de la première participation")
        nouv_val = max(val1, année_a_mettre)
        df_noc[id_ligne, "année de la première participation"] = nouv_val
    else:
        nouv_ligne = {"Pays": noc, "année de la première participation": année_a_mettre}
        df_noc.loc[len(df_noc)] = nouv_ligne


# df["Nom_du_pays"] = annee_arrivee
# for pays_noc in (donnees_noc_regions):
# if pays_noc[0] == noc:
# if pays_noc[2] == "":
# pays_a_mettre = pays_noc[1]
# else:
# pays_a_mettre = pays_noc[2]
# break
