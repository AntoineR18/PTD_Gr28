# L'objectif est de créer une carte permettant de visualiser les pays qui ont recu le
# plus d'athlètes ayant changé de nationalité.

import pandas as pd
import plotly.express as px
import pycountry
from Question10_Pandas import athletes_changed_nationality


df = pd.read_csv("donnees_jeux_olympiques/athlete_events.csv")
# d'abord je vais vérifier que la liste des NOCS correspond bien à la liste des pays
# ISO-3.
# J'utilise pycontry pour  récupérer la liste des pays et leurs codes ISO-3.
iso3_list = [country.alpha_3 for country in pycountry.countries]
noc_list = df['NOC'].unique()  # Liste des NOC uniques dans le DataFrame

# Je vais créer un set pour les NOC et les ISO3 pour faciliter la comparaison
noc_set = set(noc_list)
iso3_set = set(iso3_list)

# Trouver les codes NOC qui ne sont pas des ISO3 valides
invalid_nocs = noc_set - iso3_set


# Nombre de dissimilarités
def afficher_noc_invalide():
    print(f"Nombre de NOC non valides : {len(invalid_nocs)}")
    print("NOC non reconnus comme ISO-3 :", invalid_nocs)


# Je vais maintenant remplacer les NOC non valides par des codes ISO-3 valides. On fait
# un dictionnaire de correspondance entre les NOC non valides et les ISO-3 valides.
noc_to_iso3 = {
    'MRI': 'MUS',  # Maurice
    'EUN': 'RUS',  # Équipe unifiée (ancienne URSS)
    'TCH': 'CZE',  # Tchécoslovaquie -> République tchèque
    'BRU': 'BRN',  # Brunei
    'URU': 'URY',  # Uruguay
    'MTN': 'MNT',  # Monténégro
    'IOA': 'IOC',  # Comité International Olympique (pas un pays)
    'BIZ': 'BIZ',  # Bizerte (pas reconnu comme un pays)
    'BAH': 'BHS',  # Bahreïn
    'CAM': 'KHM',  # Cambodge
    'UNK': 'UNK',  # Inconnu ou non spécifié
    'MAS': 'MYS',  # Malaisie
    'LBA': 'LBY',  # Libye
    'MON': 'MCO',  # Monaco
    'MAW': 'MWI',  # Malawi
    'VIN': 'VCT',  # Saint-Vincent-et-les-Grenadines
    'BUR': 'MMR',  # Birmanie
    'SUD': 'SDN',  # Soudan
    'KOS': 'KOS',  # Kosovo (reconnu partiellement)
    'ANT': 'NLD',  # Antilles néerlandaises -> Pays-Bas
    'YMD': 'YMD',  # Yéménite ou entité non définie
    'NIG': 'NGA',  # Nigéria
    'INA': 'IDN',  # Indonésie
    'BER': 'BMU',  # Bermudes
    'CAY': 'CYM',  # Îles Caïmans
    'TAN': 'TAN',  # Tanzanie
    'NCA': 'NIC',  # Nicaragua
    'OMA': 'OMN',  # Oman
    'RSA': 'ZAF',  # Afrique du Sud
    'VAN': 'VUT',  # Vanuatu
    'NED': 'NLD',  # Pays-Bas
    'PHI': 'PHL',  # Philippines
    'AHO': 'ABW',  # Aruba
    'NGR': 'NGA',  # Nigéria
    'CHI': 'CHL',  # Chili
    'SCG': 'SRB',  # Serbie-et-Monténégro -> Serbie
    'IRI': 'IRN',  # Iran
    'ANG': 'AGO',  # Angola
    'BUL': 'BGR',  # Bulgarie
    'TOG': 'TGO',  # Togo
    'YUG': 'SRB',  # Yougoslavie -> Serbie
    'GER': 'DEU',  # Allemagne
    'HON': 'HND',  # Honduras
    'KSA': 'SAU',  # Arabie Saoudite
    'YAR': 'YAR',  # Yémen arabe (historique)
    'KUW': 'KWT',  # Koweït
    'DEN': 'DNK',  # Danemark
    'CGO': 'COG',  # République du Congo
    'ISV': 'ISV',  # Îles Vierges des États-Unis
    'LIB': 'LBY',  # Libye
    'GEQ': 'GNQ',  # Guinée équatoriale
    'ARU': 'ABW',  # Aruba
    'ZIM': 'ZWE',  # Zimbabwe
    'BHU': 'BTN',  # Bhoutan
    'LES': 'LSO',  # Lesotho
    'GUI': 'GIN',  # Guinée
    'ANZ': 'AUS',  # Australie (ancien code pour l'équipe olympique)
    'BAR': 'BRB',  # Barbade
    'BOT': 'BWA',  # Botswana
    'WIF': 'FIJ',  # Fidji
    'TPE': 'TPE',  # Taïwan
    'POR': 'PRT',  # Portugal
    'ESA': 'ESA',  # Salvador (historique)
    'RHO': 'ZWE',  # Zimbabwe (anciennement Rhodésie)
    'ROT': 'ROU',  # Roumanie
    'IVB': 'VGB',  # Îles Vierges britanniques
    'MGL': 'MNG',  # Mongolie
    'BOH': 'CZE',  # Bohême (historique, maintenant République tchèque)
    'SLO': 'SVN',  # Slovénie
    'ASA': 'ASM',  # Samoa américaines
    'FIJ': 'FJI',  # Fidji
    'PLE': 'PLE',  # Palestine (reconnu partiellement)
    'NFL': 'NFL',  # National Football League (pas un pays)
    'SUI': 'CHE',  # Suisse
    'PAR': 'PRY',  # Paraguay
    'VIE': 'AUT',  # Autriche (Vienne est une ville)
    'CRT': 'CRI',  # Costa Rica
    'FRG': 'DEU',  # Allemagne de l'Ouest (avant la réunification)
    'ALG': 'DZA',  # Algérie
    'NEP': 'NPL',  # Népal
    'NBO': 'KEN',  # Kenya
    'MYA': 'MMR',  # Myanmar (Birmanie)
    'SAA': 'SAU',  # Arabie Saoudite
    'CHA': 'CHN',  # Chine
    'TGA': 'TON',  # Tonga
    'ZAM': 'ZMB',  # Zambie
    'GUA': 'GTM',  # Guatemala
    'PUR': 'PUR',  # Porto Rico
    'GRN': 'GRD',  # Grenade
    'SKN': 'KNA',  # Saint-Christophe-et-Niévès
    'CRC': 'CRI',  # Costa Rica
    'MAD': 'MDG',  # Madagascar
    'GRE': 'GRC',  # Grèce
    'BAN': 'BGD',  # Bangladesh
    'HAI': 'HTI',  # Haïti
    'SRI': 'LKA',  # Sri Lanka
    'SEY': 'SYC',  # Seychelles
    'SOL': 'SLB',  # Îles Salomon
    'GDR': 'DEU',  # Allemagne de l'Est (avant la réunification)
    'URS': 'RUS',  # Union soviétique (ancienne URSS)
    'SAM': 'WSM',  # Samoa
    'UAR': 'ARE',  # Émirats arabes unis
    'UAE': 'ARE',  # Émirats arabes unis
    'GAM': 'GMB',  # Gambie
    'CRO': 'HRV',  # Croatie
    'GBS': 'GNB'   # Guinée-Bissau
}

# On remplace les NOC non valides par les ISO-3 valides dans le DataFrame :
df['NOC'] = df['NOC'].replace(noc_to_iso3)

# L'objectif est ensuite de créer une liste contenant le nombre de pays vers lesquels
# les athlètes ont changé de nationalité.
# Pour cela, nous récupérons la liste des pays pour lesquels chaque athlète a participé,
# et nous retirons le pays de sa première participation pour ne compter que les
# changements.


def get_new_nationalities(df, athlete_names):
    """
    Pour chaque athlète ayant changé de nationalité, retourne la liste des nouveaux pays
    qu'il a représentés après sa première participation.

    parameters:
    df : DataFrame contenant les données des athlètes
    athlete_names : liste de noms d'athlètes ayant changé de nationalité

    returns:
    athlete_transfers : liste des nouveaux pays représentés par les athlètes
    """
    athlete_transfers = []

    for name in athlete_names:
        # Extraire les participations pour chaque athlète avec année et NOC.
        # On sélectionne les années à partir de 1993 pour éviter les complications avec
        # la fin de L'URSS.
        athlete_data = df[(df['Name'] == name) &
                          (df['Year'] >= 1993)][['NOC',
                                                 df.columns[9]]].drop_duplicates()
        # On sélectionne pour chaque athlète la première année de participation
        first_year = athlete_data[df.columns[9]].min()

        # On définit le premier NOC comme celui de la première participation. On
        # sélectionne pour chaque athlète le NOC de sa première participation.
        first_nocs = athlete_data[athlete_data[df.columns[9]]
                                  == first_year]['NOC'].unique()

        # à partir de la première participation, on créé une liste des changements de
        # nationalité. On sélectionne les NOC qui ne sont pas la première nationalité
        # pour chaque athlète.
        new_nocs = [noc for noc in athlete_data['NOC'].unique()
                    if noc not in first_nocs]

        # Ajouter les nouveaux NOC à la liste finale
        athlete_transfers.extend(new_nocs)

    return athlete_transfers


def get_new_nationalities_opti(df):
    """
    Détecte les athlètes ayant changé de nationalité et retourne les nouveaux pays.

    Parameters
    ----------
    df : pandas.DataFrame
        Le DataFrame complet des données olympiques.

    Returns
    -------
    list of str
        Codes ISO des nouveaux pays d’accueil.
    """
    # Ne garder que les colonnes utiles, années récentes et médaillés
    df_recent = df[df["Year"] >= 1993][["Name", "NOC", "Year"]].drop_duplicates()

    # Grouper par nom d'athlète
    grouped = df_recent.groupby("Name")["NOC"].nunique()

    # Ne garder que ceux ayant eu plusieurs NOC
    noms_ayant_change = grouped[grouped > 1].index

    # Extraire les lignes correspondantes
    transferts = df_recent[df_recent["Name"].isin(noms_ayant_change)]

    # Dernière année de participation pour chaque athlète
    transferts = transferts.sort_values("Year").drop_duplicates("Name", keep="last")

    # Extraction des NOC finaux
    nocs_finaux = transferts["NOC"].tolist()

    # Mapper les NOC vers les codes ISO3
    import pycountry
    iso_countries = []
    for noc in nocs_finaux:
        try:
            country = pycountry.countries.get(alpha_3=noc)
            if country:
                iso_countries.append(noc)
        except Exception:
            continue

    return iso_countries


# Récupérer la liste de tous les pays "d'arrivée" après changement de nationalité
new_noc_list = get_new_nationalities(df, athletes_changed_nationality)
# new_noc_list = get_new_nationalities_opti(df)

# Compter le nombre d'athlètes reçus par pays
noc_counts = pd.Series(new_noc_list).value_counts().reset_index()
noc_counts.columns = ['NOC', 'Nb_Athletes']


# Afficher la carte
def afficher_carte():
    carte = px.choropleth(
        noc_counts,
        locations="NOC",
        color="Nb_Athletes",
        hover_name="NOC",
        color_continuous_scale="Purples",
        projection="natural earth",
        title="Pays ayant reçu des athlètes après changement de nationalité à partir"
        " de 1993",
    )

    # Sauvegarde en PNG
    carte.write_html("resultat/carte_transferts_nationalite.html")

    carte.show()
