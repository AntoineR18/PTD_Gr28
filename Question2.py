# Trouvez des bornes inférieures et supérieures pour le nombre de médailles
# par nation pour les Jeux Olympiques de 2016.

from lecture_donnees import (
    athletes_medailles,
    sports_par_annee,
    sport_collectif_par_annee,
)

# Création des liste de sports spécifiques à 2016
sports_2016 = sports_par_annee["2016"]
sports_co_2016 = sport_collectif_par_annee["2016"]

entete = athletes_medailles[0]
donnees = athletes_medailles[1:]

idx_noc = entete.index("NOC")
idx_sport = entete.index("Sport")
idx_event = entete.index("Event")
idx_medal = entete.index("Medal")

# Création d'une liste des pays par NOC
liste_noc = set()
for ligne in athletes_medailles:
    liste_noc.add(ligne[idx_noc])

# Pour chaque pays, on crée un dictionnaire des sports collectifs pour
# vérifier s'ils ont déjà été traités ou non.
events_co_2016_noc = {
    noc: {event: False for event in sports_co_2016} for noc in liste_noc
}

medailles_2016 = {}
for ligne in athletes_medailles[:50]:
    noc = ligne[idx_noc]
    sport = ligne[idx_sport]
    event = ligne[idx_event]
    medal = ligne[idx_medal]
    if noc not in medailles_2016:
        medailles_2016[noc] = 0
    if event not in sports_co_2016:
        print(idx_event)
        medailles_2016[noc] += 1
    # else:
    #     events_co_2016_noc[event] = True
    #     medailles_2016 += 1
print(medailles_2016)
