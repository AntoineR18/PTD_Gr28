# Question 8 :
# Dans quels épreuves, les Etats-Unis ont-ils gagné une médaille en 2016 ?

from lecture_donnees import athletes_medailles,

entete = athletes_medailles[0]
donnees = athletes_medailles[1:]

idx_annee = entete.index("Year")
idx_event = entete.index("Event")
idx_noc = entete.index("NOC")

medailles_par_event: {}
for ligne in donnees:
    if ligne[idx_annee] != "2016" or ligne[idx_noc] != "USA":
        continue
    event = ligne[idx_event]
    if event not in medailles_par_event:
        medailles_par_event[event] = 0
    medailles_par_event