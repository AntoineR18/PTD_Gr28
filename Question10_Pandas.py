# Question 10 :
# Établir la liste des athlètes ayant changé de nationalité au cours de leur carrière.

import pandas as pd

df = pd.read_csv("donnees_jeux_olympiques/athlete_events.csv")
df_unique = df[['Name', 'NOC']].drop_duplicates()

# Grouper par nom et compter le nombre de nationalités différentes
nat_ch = df_unique.groupby('Name')['NOC'].nunique()

# on sélectionne les athlètes avec au moins deux nationalités.
changed_nationality = nat_ch[nat_ch > 1]
athletes_changed_nationality = changed_nationality.index.tolist()


def afficher_list():
    """
    Affiche et enregistre la liste des athlètes ayant changé de nationalité
    au cours de leur carrière.
    """
    print("Athlètes ayant changé de nationalité :")
    for nom in athletes_changed_nationality:
        print(nom)

    # Écriture dans un fichier texte
    with open("resultat/athletes_changed_nationality.txt", "w", encoding="utf-8") as f:
        for nom in athletes_changed_nationality:
            f.write(nom + "\n")

# Commentaire :
# il est impsosible de distinguer les athlètes qui étaient déjà porteurs d'une double
# nationalité et ont changé de pays pour lesquels ils compètent, de ceux qui ont obtenu
# une nouvelle nationalité au cours de leur carrière.
