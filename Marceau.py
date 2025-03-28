# questions

# Mckael Felps

# Trouvez des bornes inférieures et supérieures pour le nombre de
# médailles par nation pour les
# Jeux Olympiques de 2016

# indice 10 d'une ligne cest l'année
from lecture_donnees import donnees_athlete_events
from lecture_donnees import donnees_noc_regions

donnees_athlete_events
donnees_noc_regions


def rep_question2(annee):
    for i in donnees_athlete_events:
        nation = {}
        if i[9] == annee:
            if i[-1] != "NA":
                if i[6] in nation:
                    nation[i[6]] += 1
                else:
                    nation[i[6]] = 0
            print(nation)
    return max(nation), min(nation[k] for k in nation)


print(rep_question2(2016))
