# Question 10 :
# Établir la liste des athlètes ayant changé de nationalité au cours de leur carrière.

import pandas as pd

df = pd.read_csv("donnees_jeux_olympiques/athlete_events.csv")
df_unique = df[['Name', 'NOC']].drop_duplicates()

# Grouper par nom et compter le nombre de NOC différents
nat_ch = df_unique.groupby('Name')['NOC'].nunique()

changed_nationality = nat_ch[nat_ch > 1]
athletes_changed_nationality = changed_nationality.index.tolist()

print("Athlètes ayant changé de nationalité :")
print(athletes_changed_nationality)

 
# for name in athletes_changed_nationality:
#     nocs = df_unique[df_unique['Name'] == name]['NOC'].unique()
#     print(f"{name} : {list(nocs)}")
