# PTD_Groupe28

# Traitement de données sur les Jeux Olympiques 🏅

Ce projet propose une interface interactive permettant de réaliser des traitements de données sur une base relative aux Jeux Olympiques. Il s’inscrit dans le cadre d’un projet de traitement de données (PTD).

## 🎯 Objectif

L'utilisateur peut explorer différentes analyses statistiques et visualisations autour des Jeux Olympiques grâce à une interface conviviale, en sélectionnant les questions et en répondant aux invites.

## 🚀 Lancement de l'application

### 1. Prérequis

Dans l'interface (interface.py) on peut installer tout les bibliothèques via la commande Install.

Assurez-vous d’avoir Python 3.x installé, ainsi que les bibliothèques suivantes :

- pandas
- matplotlib
- numpy
- scikit-learn
- streamlit
- plotly
- pycountry
- seaborn
- subprocess

Vous pouvez les installer avec la commande suivante :

```bash
pip install pandas matplotlib numpy scikit-learn streamlit plotly pycountry seaborn
```

### 2. Préparer les données

Placez la base de données dans un dossier nommé **`donnees_jeux_olympiques`**, à la racine du projet. Ce dossier est indispensable au bon fonctionnement de l’application.

### 3. Lancer l’interface

Utilisez la commande suivante :

```bash
python interface.py
```

L’interface s’ouvre en ligne de commande et vous propose une liste de questions. Sélectionnez le numéro de la question, suivez les instructions, et profitez des résultats !

## 📁 Structure du projet (exemple)

```text
PTD_Groupe28/
├── donnees_jeux_olympiques/     # Dossier contenant les fichiers CSV de données
├── interface.py                 # Interface principale du projet
├── QuestionX.py                 # Fichiers associés aux différentes analyses
├── Probleme.py                  # Code pour l'apprentissage superviser
├── noc_country.py               # Fichier pour la convertion
├── lecture_donnees.py           # Module pour lire les données
├── compte_medailles.py          # Module auxilière pour Q1 et Q2
└── README.md                    # Ce fichier
```

## 👥 Auteurs

- Maxime Roux
- Claire Robin
- Antoine Rustenholz
- Marceau Rozé

## 📄 Licence

Projet sous licence [MIT](https://opensource.org/licenses/MIT).

## 🧪 Tests

Aucun test unitaire n'est fourni : les vérifications ont été effectuées en amont dans l'implémentation interactive.
