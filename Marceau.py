# questions

# Mckael Felps

# Trouvez des bornes inférieures et supérieures pour le nombre de médailles par nation pour les
# Jeux Olympiques de 2016

# indice 10 d'une ligne cest l'année
from lecture_donnees import donnees_athlete_events
from lecture_donnees import donnees_noc_regions

donnees_athlete_events
donnees_noc_regions

for i in donnees_athlete_events
:
    nation = {}
    if i[10] == 2016:
        if i[7] in nation:
            nation[i[7]] += 1
        else:
            nation[i[7]] = 0
return max(nation[k] for k in nation), min(nation[k] for k in nation)
