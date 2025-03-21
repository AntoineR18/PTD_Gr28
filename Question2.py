# Trouvez des bornes inférieures et supérieures pour le nombre de médailles
# par nation pour les Jeux Olympiques de 2016.

from lecture_donnees import donnees_athlete_events
from lecture_donnees import donnees_noc_regions

JO_2016 = []
for ligne in donnees_athlete_events:
    if 