from lecture_donnees import (
    donnees_athlete_events,
    donnees_noc_regions,
)


pays = []
pays_final = []
for ligne in donnees_athlete_events:
    L = 0
    if ligne[7] == "SGP":
        noc = "SIN"
    elif ligne[7] in ("VNM", "VIE"):
        noc = "VNM"
    else:
        noc = ligne[7]
    for i in range(1, len(pays)):
        if pays[i][0] == noc:
            L = 1
            if ligne[9] not in pays[i]:
                pays[i].append(ligne[9])
    if L == 0:
        pays.append([noc, ligne[9]])


for pays_i in pays:
    pays_final.append([pays_i[0], min(pays_i[1 : len(pays_i)])])
print(pays_final)
