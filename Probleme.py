import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans


# Charger le fichier CSV
athletes_df = pd.read_csv("donnees_jeux_olympiques/athlete_events.csv")


# Fonction pour filtrer les colonnes utiles et supprimer les doublons selon le choix
def preprocess_donnees_athletes(df, drop_duplicates=True):
    df = df[['ID', 'Name', 'Sex', 'Age', 'Height', 'Weight', 'Sport']].copy()

    # Recodage du sexe : M → 0, F → 1
    df['Sex'] = df['Sex'].map({'M': 0, 'F': 1})

    # Supprimer les lignes où Age, Height ou Weight sont manquants
    df = df.dropna(subset=['Age', 'Height', 'Weight', 'Sex'])

    # Supprimer les doublons d'athlètes si demandé
    if drop_duplicates:
        df = df.drop_duplicates(subset='ID', keep='first')

    return df.reset_index(drop=True)


# Création des deux versions pour affichage
df_avec_doublons = preprocess_donnees_athletes(athletes_df, drop_duplicates=False)
df_sans_doublons = preprocess_donnees_athletes(athletes_df, drop_duplicates=True)


# Fonction pour tracer les distributions, avec option pour effectif ou pourcentage
def plot_distributions(df, mode='pourcentage'):
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # Définir les poids si on est en mode pourcentage
    poids = None
    if mode.lower() == 'pourcentage':
        poids = [100 / len(df)] * len(df)
    else:
        mode = 'Effectif'

    # Âge
    axes[0, 0].hist(df['Age'], bins=30, edgecolor='black', weights=poids)
    axes[0, 0].set_title('Distribution de l\'Âge')
    axes[0, 0].set_xlabel('Âge')
    axes[0, 0].set_ylabel('%' if mode == 'pourcentage' else 'Effectif')

    # Taille
    axes[0, 1].hist(df['Height'], bins=30, edgecolor='black', weights=poids)
    axes[0, 1].set_title('Distribution de la Taille')
    axes[0, 1].set_xlabel('Taille (cm)')
    axes[0, 1].set_ylabel('%' if mode == 'pourcentage' else 'Effectif')

    # Poids
    axes[1, 0].hist(df['Weight'], bins=30, edgecolor='black', weights=poids)
    axes[1, 0].set_title('Distribution du Poids')
    axes[1, 0].set_xlabel('Poids (kg)')
    axes[1, 0].set_ylabel('%' if mode == 'pourcentage' else 'Effectif')

    # Sexe
    sex_counts = df['Sex'].value_counts(normalize=(mode == 'pourcentage')).sort_index()
    labels = ['Homme', 'Femme']
    values = sex_counts.values * (100 if mode == 'pourcentage' else len(df))
    axes[1, 1].bar(labels, values)
    axes[1, 1].set_title('Répartition Hommes / Femmes')
    axes[1, 1].set_ylabel('%' if mode == 'pourcentage' else 'Effectif')

    plt.tight_layout()
    plt.savefig("Resultat/Apprentissage_répartition.png")
    plt.show()


# Afficher en pourcentage
# plot_distributions(df_avec_doublons, mode='pourcentage')


# Créons une liste de tuples (variable_num, variable_cat)
quantitative_vars = ['Age', 'Height', 'Weight']
categorical_vars = ['Sex', 'Sport']

# Génération des combinaisons possibles
tests = [(q, c) for q in quantitative_vars for c in categorical_vars]

# Affichage de la liste des tests disponibles
# tests


# Analyse buvariée
def plot_boxplot(df, variable_quant, variable_qual):
    """
    Affiche un boxplot de variable_quant (quantitative) en fonction de variable_qual
      (qualitative).
    """
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x=variable_qual, y=variable_quant)
    plt.title(f'{variable_quant} selon {variable_qual}')
    plt.xlabel(variable_qual)
    plt.ylabel(variable_quant)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("Resultat/Apprentissage_Bivariée.png")
    plt.show()


# Exemple d'appel de la fonction
# plot_boxplot(df_sans_doublons, variable_num='Age', variable_qual='Sex')
# plot_boxplot(df_sans_doublons, variable_num='Weight', variable_qual='Sport')

# 1. Préparation des données avec option pour inclure ou non "Sex"
def preparer_donnees(df_source, utiliser_sex=True):
    df = df_source.copy()
    if utiliser_sex:
        caractéristiques = ['Age', 'Height', 'Weight', 'Sex']
    else:
        caractéristiques = ['Age', 'Height', 'Weight']
    scaler = StandardScaler()
    X_norm = scaler.fit_transform(df[caractéristiques])
    return X_norm, caractéristiques, df


# 2. ACP
def appliquer_acp(X_norm, df, n_components=3):
    acp_modele = PCA(n_components=n_components)
    X_proj = acp_modele.fit_transform(X_norm)
    df_acp = pd.DataFrame(X_proj, columns=[f'PC{i+1}' for i in range(n_components)])
    df_acp['Sex'] = df['Sex'].values
    df_acp['Sport'] = df['Sport'].values
    return acp_modele, df_acp


# Choix : inclure ou non la variable 'Sex' dans l'ACP
utiliser_sex = False  # mettre True pour inclure 'Sex'

X_norm, carac_utilisees, df = preparer_donnees(df_sans_doublons, utiliser_sex)
acp_modele, df_acp = appliquer_acp(X_norm, df)


# 3. Fonction : filtrer les sports + catégorie Autre
def filtrer_sports_avec_autre(df, nb_sports=10, mode='frequence'):
    sports_uniques = df['Sport'].value_counts()
    if mode == 'frequence':
        sports_choisis = sports_uniques.head(nb_sports).index
    elif mode == 'random':
        sports_choisis = np.random.choice(sports_uniques.index, size=nb_sports,
                                          replace=False)
    else:
        raise ValueError("Mode invalide. Utilisez 'frequence' ou 'random'.")
    df_copie = df.copy()
    df_copie['Sport'] = df_copie['Sport'].apply(lambda s: s if s in sports_choisis
                                                else 'Autre')
    return df_copie


# 4. Fonction d'affichage
def plot_cercle_correlation(pca_modele, carac):
    pcs = pca_modele.components_[:2, :]
    corvars = pcs.T

    var_PC1 = pca_modele.explained_variance_ratio_[0] * 100
    var_PC2 = pca_modele.explained_variance_ratio_[1] * 100

    fig, ax = plt.subplots(figsize=(8, 8))

    for i in range(len(carac)):
        x, y = corvars[i]
        ax.arrow(0, 0, x, y, head_width=0.03, head_length=0.03, fc="red", ec="red")
        ax.text(x * 1.15, y * 1.15, carac[i], fontsize=12, ha="center", va="center")

    cercle = plt.Circle((0, 0), 1, color="blue", fill=False)
    ax.add_artist(cercle)

    ax.set_xlim(-1.1, 1.1)
    ax.set_ylim(-1.1, 1.1)
    ax.axhline(0, color="grey", linestyle="--")
    ax.axvline(0, color="grey", linestyle="--")
    ax.set_xlabel(f"PC1 ({var_PC1:.1f}%)")
    ax.set_ylabel(f"PC2 ({var_PC2:.1f}%)")
    ax.set_title("Cercle des corrélations")
    ax.set_aspect("equal")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("Resultat/Apprentissage_ACP_cercle_correlation.png")
    plt.show()


def plot_pca_individuals(pca_df, pca_modele, color_by=None):
    var_PC1 = pca_modele.explained_variance_ratio_[0] * 100
    var_PC2 = pca_modele.explained_variance_ratio_[1] * 100

    plt.figure(figsize=(10, 7))
    if color_by is None:
        plt.scatter(pca_df["PC1"], pca_df["PC2"], alpha=0.5, s=10)
        plt.title("Projection dans le plan des composantes principales (PC1 vs PC2)")
    else:
        groups = pca_df.groupby(color_by)
        for name, group in groups:
            plt.scatter(group["PC1"], group["PC2"], alpha=0.5, s=10, label=name)
        plt.title(f"Projection dans le plan (PC1 vs PC2) - Couleur : {color_by}")
        plt.legend(loc="best", markerscale=2, fontsize=8)

    plt.xlabel(f"PC1 ({var_PC1:.1f}%)")
    plt.ylabel(f"PC2 ({var_PC2:.1f}%)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("Resultat/Apprentissage_ACP.png")
    plt.show()


# plot_cercle_correlation(acp_modele, caractéristiques)
plot_pca_individuals(df_acp, acp_modele)

# 5. Application : sports les plus fréquents + "Autre"
# df_acp_catégorise = filtrer_sports_avec_autre(df_acp, nb_sports=8, mode='frequent')
# plot_pca_individuals(df_acp_catégorise, color_by='Sport')


# 6. Si on choisi nous le sport :
# Fonction spécifique pour un seul sport
def highlight_one_sport(df, sport_cible):
    """
    Affiche les individus dans le plan ACP :
    - sport_cible : str, sport à mettre en évidence
    - les autres sports sont affichés en gris
    """
    plt.figure(figsize=(10, 7))

    df_autres = df[df['Sport'] != sport_cible]
    plt.scatter(df_autres['PC1'], df_autres['PC2'], color='lightgray',
                alpha=0.3, s=10, label='Autres sports')

    df_s = df[df['Sport'] == sport_cible]
    plt.scatter(df_s['PC1'], df_s['PC2'], alpha=0.7, s=20, label=sport_cible)

    plt.title(f'ACP - Sport mis en évidence : {sport_cible}')
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(str(f"Resultat/Apprentissage_ACP_{sport_cible}"))
    plt.show()


# Fonction simple pour afficher la liste des sports disponibles dans df_acp
def lister_sports(df):
    """
    Affiche la liste des sports uniques présents dans un DataFrame ACP.
    """
    sports = sorted(df['Sport'].unique())
    for sport in sports:
        print(sport)


# lister_sports(df_acp)
# highlight_one_sport(df_acp, "Gymnastics")

# CLUSTERING
# 2. Clustering K-means (k=4)
k = 4
X_kmeans = df_acp[['PC1', 'PC2']].values
kmeans = KMeans(n_clusters=k, random_state=42)
df_acp['Cluster'] = kmeans.fit_predict(X_kmeans)


# Méthode du coude :
def plot_methode_coude(X, k_max=10):
    inerties = []
    ks = range(1, k_max + 1)

    for k in ks:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(X)
        inerties.append(kmeans.inertia_)

    plt.figure(figsize=(8, 5))
    plt.plot(ks, inerties, marker='o')
    plt.xticks(ks)
    plt.xlabel("Nombre de clusters (k)")
    plt.ylabel("Inertie intra-cluster (somme des distances)")
    plt.title("Méthode du coude pour choisir k")
    plt.grid(True)

    plt.savefig("Resultat/Apprentissage_Kmeans_Coude.png")

    plt.show()


# 3. Visualisation des clusters
def plot_kmeans_clusters(df, k):
    plt.figure(figsize=(10, 7))
    for i in range(k):
        cluster_data = df[df['Cluster'] == i]
        plt.scatter(cluster_data['PC1'], cluster_data['PC2'], label=f'Cluster {i}',
                    s=10, alpha=0.6)
    plt.title(f'K-means avec k={k} (ACP)')
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("Resultat/Apprentissage_Kmeans.png")
    plt.show()


# 4. Affichage
plot_kmeans_clusters(df_acp, k)


# 5. Analyse des sports par cluster
# Fonction pour afficher la part (%) des sports dans chaque cluster par rapport à
# leur effectif total
def pourcentage_sports_par_cluster(df, n=5):
    """
    Affiche pour chaque cluster les n sports les plus représentés en proportion
    du total de ce sport (i.e., parmi tous les boxeurs, combien sont dans ce cluster).
    """
    clusters = sorted(df['Cluster'].unique())
    sports_totaux = df['Sport'].value_counts()

    for cluster in clusters:
        print(f"\n🌀 Cluster {cluster} :")
        cluster_df = df[df['Cluster'] == cluster]
        sport_counts_in_cluster = cluster_df['Sport'].value_counts()

        # Calcul du pourcentage d'appartenance au cluster par rapport au total
        # de ce sport
        sport_percentage = ((sport_counts_in_cluster / sports_totaux * 100)
                            .dropna().sort_values(ascending=False))
        print(sport_percentage.head(n).round(1).astype(str) + ' %')


# Appel de la fonction avec les 5 sports les plus concentrés dans chaque cluster
pourcentage_sports_par_cluster(df_acp, n=5)
