# Question 4 : Comparaison l'obtention des médailles des athlètes en fonction de leur
# âge et de leur sexe.

from lecture_donnees import donnees_athlete_events


def table_sport(genre: str):
    if genre != "M" and genre != "F":
        raise ValueError("Le genre doit être 'M' ou 'F'")
    table_sport = []
    for ligne in donnees_athlete_events:
        if ligne[2] == genre:
            table_sport.append(ligne[12])
    table_sport = list(set(table_sport))
    return table_sport


def liste_ages_par_sport(donnees_athlete_events: list, genre: str, sport: str):
    if genre != "M" and genre != "F":
        raise ValueError("Le genre doit être 'M' ou 'F'")
    if sport not in table_sport(genre):
        raise ValueError("Le sport n'est pas dans la liste des sports")
    liste_ages = []
    for ligne in donnees_athlete_events[1:]:  # On commence à la 2ème ligne
        if ligne[2] == genre and ligne[12] == sport:
            age = ligne[3]
            if age != "NA":
                age = int(age)
                liste_ages.append(age)
    liste_ages.sort()  # on l'ordonne, utile pour la médiane
    return liste_ages


# On va faire une fonction qui calcule la moyenne et une qui calcule la médiane
def moyenne_ages(liste_ages: list):
    n = len(liste_ages)
    somme = 0
    for age in liste_ages:
        somme += age
    moyenne = somme / n
    return moyenne


def mediane_ages(liste_ages: list):
    n = len(liste_ages)
    if n % 2 == 0:
        mediane = (liste_ages[n // 2] + liste_ages[n // 2 - 1]) / 2
    else:
        mediane = liste_ages[n // 2]
    return mediane


def comp_meda_age(sport: str, methode: str, genre: str):
    """
    Compare l'obtention des médailles des athlètes en fonction de leur âge et de leur
    sexe.

    """
    if genre != "M" and genre != "F":
        raise ValueError("Le genre doit être 'M' ou 'F'")
    if sport not in table_sport(genre):
        raise ValueError("Le sport n'est pas dans la liste des sports")
    if methode != "moyenne" and methode != "mediane":
        raise ValueError("La méthode doit être 'moyenne' ou 'mediane'")
    liste_ages_sport = liste_ages_par_sport(donnees_athlete_events, genre, sport)
    if methode == "moyenne":
        borne = moyenne_ages(liste_ages_sport)
    if methode == "médiane":
        borne = mediane_ages(liste_ages_sport)
    # On initialise les compteurs de médailles
    nb_med_jeunes = 0
    nb_med_ages = 0
    # On parcourt les données pour ce sport
    for ligne in donnees_athlete_events[1:]:
        age = ligne[3]
        sport_ligne = ligne[12]
        medal = ligne[14]
        sexe = ligne[2]
        if age != 'NA' and sport_ligne == sport and medal != 'NA' and sexe == genre:
            age = float(age)
            if age < borne:
                nb_med_jeunes += 1
            else:
                nb_med_ages += 1

    # On affiche les résultats
    print(f"Pour le sport {sport} :")
    print(f"Nombre de médailles pour les plus jeunes : {nb_med_jeunes}")
    print(f"Nombre de médailles pour les plus âgés : {nb_med_ages}")


comp_meda_age("Swimming", "moyenne", "M")
comp_meda_age("Trampolining", "moyenne", "M")
comp_meda_age("Gymnastics", "moyenne", "M")
