import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

from lecture_donnees import (
    donnees_noc_regions,
)


dt = pd.read_csv("donnees_jeux_olympiques/athlete_events.csv", header=0)
df = pd.DataFrame(dt)
df_grouped = df.groupby("NOC")["Year"].min()
df_grouped_ss_VIE = df_grouped.drop("VIE")


index_resultat = df_grouped_ss_VIE.index

nouv_index = []
for i in index_resultat:
    if i == "SGP":
        noc = "SIN"
    else:
        noc = i
    for ligne in donnees_noc_regions:
        if ligne[0] == noc:
            if ligne[2] == "":
                nouv_index.append(ligne[1])
            else:
                nouv_index.append(ligne[2])
            break

df_grouped_ss_VIE.index = nouv_index


data = df_grouped_ss_VIE.sort_values()


grouped = data.groupby(data.values)

years = sorted(grouped.groups.keys())
num_years = len(years)

# On choisit la couleur de notre frise (colormap)
colormap = cm.plasma

# Normaliser les années pour qu'elles correspondent à la colormap (entre 0 et 1)
normalize = plt.Normalize(vmin=min(years), vmax=max(years))
scalarMap = cm.ScalarMappable(norm=normalize, cmap=colormap)

# Initialisation de la figure
fig, ax = plt.subplots(figsize=(14, 4))

# Frise centrale
ax.hlines(0, data.min() - 4, data.max() + 4, color="black", linewidth=2)

# Création ésdes groupes de pays nom : "Groupe 1", "Groupe 2", etc.
groupe_labels = {}
for i, year in enumerate(years):
    countries = grouped.get_group(year).index.tolist()
    label = f"Groupe {i+1}"
    groupe_labels[label] = list(countries)
    color = scalarMap.to_rgba(year)  # Obtenir la couleur correspondante à l'année
    ax.plot(year, 0, "o", color=color, markersize=8)  # Appliquer la couleur au point
    ax.text(year, 0.3, label, ha="center", va="bottom", fontsize=9, rotation=45)
    ax.text(year, -0.3, str(year), ha="center", va="top", fontsize=8, rotation=315)

# Ajustements visuels
ax.set_ylim(-1, 1)
ax.set_xlim(data.min() - 4, data.max() + 4)
ax.set_yticks([])
ax.set_xlabel("Année")
ax.set_title("Les premières participations aux JO des pays (regroupés)")


def list_groupe():
    # Affichage du dictionnaire des groupes
    for label, countries in groupe_labels.items():
        print(f"{label} : {', '.join(countries)}")


# Dictionnaire pour retrouver les pays par point (x, y)
points = {}
scatters = []

for i, year in enumerate(years):
    countries = grouped.get_group(year).index.tolist()
    color = scalarMap.to_rgba(year)
    sc = ax.plot(year, 0, "o", color=color, markersize=8, picker=5)  # active le clic
    points[(year, 0)] = countries
    scatters.append(sc[0])  # on stocke les objets graphiques


def on_pick(event):
    artist = event.artist
    x = artist.get_xdata()[0]
    y = artist.get_ydata()[0]
    countries = points.get((x, y), [])
    print(f"\nPays ayant débuté en {int(x)} : {', '.join(countries)}")


fig.canvas.mpl_connect("pick_event", on_pick)

plt.tight_layout()
plt.show()
