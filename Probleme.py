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
def preprocess_athletes_data(df, drop_duplicates=True):
    df = df[['ID', 'Name', 'Sex', 'Age', 'Height', 'Weight', 'Sport']].copy()

    # Recodage du sexe : M → 0, F → 1
    df['Sex'] = df['Sex'].map({'M': 0, 'F': 1})

    # Supprimer les lignes où Age, Height ou Weight sont manquants
    df = df.dropna(subset=['Age', 'Height', 'Weight'])

    # Supprimer les doublons d'athlètes si demandé
    if drop_duplicates:
        df = df.drop_duplicates(subset='ID', keep='first')

    return df.reset_index(drop=True)


# Création des deux versions pour affichage
df_with_duplicates = preprocess_athletes_data(athletes_df, drop_duplicates=False)
df_without_duplicates = preprocess_athletes_data(athletes_df, drop_duplicates=True)


# Fonction pour tracer les distributions, avec option pour effectif ou pourcentage
def plot_distributions(df, mode='pourcentage'):
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))

    # Définir les poids si on est en mode pourcentage
    density = None
    weights = None
    if mode == 'pourcentage':
        weights = [100 / len(df)] * len(df)
        density = None

    # Âge
    axes[0, 0].hist(df['Age'], bins=30, edgecolor='black', weights=weights)
    axes[0, 0].set_title('Distribution de l\'Âge')
    axes[0, 0].set_xlabel('Âge')
    axes[0, 0].set_ylabel('%' if mode == 'pourcentage' else 'Effectif')

    # Taille
    axes[0, 1].hist(df['Height'], bins=30, edgecolor='black', weights=weights)
    axes[0, 1].set_title('Distribution de la Taille')
    axes[0, 1].set_xlabel('Taille (cm)')
    axes[0, 1].set_ylabel('%' if mode == 'pourcentage' else 'Effectif')

    # Poids
    axes[1, 0].hist(df['Weight'], bins=30, edgecolor='black', weights=weights)
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
    plt.show()


# Afficher en pourcentage
# plot_distributions(df_without_duplicates, mode='pourcentage')


# Créons une liste de tuples (variable_num, variable_cat)
quantitative_vars = ['Age', 'Height', 'Weight']
categorical_vars = ['Sex', 'Sport']

# Génération des combinaisons possibles
tests = [(q, c) for q in quantitative_vars for c in categorical_vars]

# Affichage de la liste des tests disponibles
# tests


def plot_boxplot(df, variable_num, variable_qual):
    """
    Affiche un boxplot de variable_num (quantitative) en fonction de variable_qual
      (qualitative).
    """
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x=variable_qual, y=variable_num)
    plt.title(f'{variable_num} selon {variable_qual}')
    plt.xlabel(variable_qual)
    plt.ylabel(variable_num)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


# Exemple d'appel de la fonction
# plot_boxplot(df_without_duplicates, variable_num='Weight', variable_qual='Sex')
# plot_boxplot(df_without_duplicates, variable_num='Weight', variable_qual='Sport')

# 1. Préparation des données
df = df_without_duplicates.copy()
caractéristiques = ['Age', 'Height', 'Weight']
scaler = StandardScaler()
X_norm = scaler.fit_transform(df[caractéristiques])

# 2. ACP
acp_model = PCA(n_components=3)
X_proj = acp_model.fit_transform(X_norm)
df_acp = pd.DataFrame(X_proj, columns=['PC1', 'PC2', 'PC3'])
df_acp['Sex'] = df['Sex'].values
df_acp['Sport'] = df['Sport'].values


# 3. Fonction : filtrer les sports + catégorie Autre
def filtrer_sports_avec_autre(df, nb_sports=10, mode='frequent'):
    sports_uniques = df['Sport'].value_counts()
    if mode == 'frequent':
        sports_choisis = sports_uniques.head(nb_sports).index
    elif mode == 'random':
        sports_choisis = np.random.choice(sports_uniques.index, size=nb_sports,
                                          replace=False)
    else:
        raise ValueError("Mode invalide. Utilisez 'frequent' ou 'random'.")
    df_copie = df.copy()
    df_copie['Sport'] = df_copie['Sport'].apply(lambda s: s if s in sports_choisis
                                                else 'Autre')
    return df_copie


# 4. Fonction d'affichage
def plot_pca_individuals(pca_df, color_by=None):
    plt.figure(figsize=(10, 7))
    if color_by is None:
        plt.scatter(pca_df['PC1'], pca_df['PC2'], alpha=0.5, s=10)
        plt.title('Projection dans le plan des composantes principales (PC1 vs PC2)')
    else:
        groups = pca_df.groupby(color_by)
        for name, group in groups:
            plt.scatter(group['PC1'], group['PC2'], alpha=0.5, s=10, label=name)
        plt.title(f'Projection dans le plan (PC1 vs PC2) - Couleur : {color_by}')
        plt.legend(loc='best', markerscale=2, fontsize=8)
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


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
    plt.show()


# Fonction simple pour afficher la liste des sports disponibles dans df_acp
def lister_sports(df):
    """
    Affiche la liste des sports uniques présents dans un DataFrame ACP.
    """
    sports = sorted(df['Sport'].unique())
    for sport in sports:
        print(sport)


lister_sports(df_acp)
highlight_one_sport(df_acp, 'Archery')

# CLUSTERING
# 2. Clustering K-means (k=4)
k = 4
X_kmeans = df_acp[['PC1', 'PC2']].values
kmeans = KMeans(n_clusters=k, random_state=42)
df_acp['Cluster'] = kmeans.fit_predict(X_kmeans)


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
