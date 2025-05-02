# Objectif interface graphique
# faire pip install streamlit dans le terminal si vous avez pas

# pour lancer l'application :

import streamlit as st
from Question4_panda import comp_meda_moy_age
from Question4 import table_sport


st.title(":rainbow[Question 4 : Comment varie l'obtention des médailles selon l'âge des"
         " athlètes ?]")
st.write(
    "Cette application permet de comparer l'obtention des médailles des athlètes "
    "en fonction de leur âge et de leur sexe."
)

genre = st.selectbox("Sélectionner le genre étudié", ["Homme", "Femme"])
if genre == "Homme":
    genre = "M"
else:
    genre = "F"
liste_sport = table_sport(genre)  # on récupère la liste des sports
sport = st.selectbox("Sélectionner le sport étudié", options=liste_sport)

st.write(
    "Choix de la méthode pour séparer les athètes en deux groupes : selon la médiane ou"
    " la moyenne de l'âge des athlètes pour un sport donné et un genre donné."
    )
methode = st.selectbox("Sélectionner la méthode", ["Médiane", "Moyenne"])

if st.button("Comparer !!!!!"):
    # if genre == "Homme":
    #     genre = "M"
    # else:
    #     genre = "F"
    if methode == "Médiane":
        methode = "mediane"
    else:
        methode = "moyenne"
    result = comp_meda_moy_age(sport, methode, genre)
    st.write(result)

# Pour lancer l'application, exécutez la commande suivante dans le terminal :
# python -m streamlit run "chemin d'accès au fichier"

# pour avoir le chemin d'accès on peut faire clic droit sur le fichier et copier le
# "path" ou "relative path" hassoul
# sinon vous éxécutez le code et ça met le chemin d'accès en bleu dans le terminal, vous
# le copiez :)
