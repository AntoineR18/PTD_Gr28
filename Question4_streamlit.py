# Objectif interface graphique
# faire pip install streamlit dans le terminal si vous avez pas

# pour lancer l'application :

import streamlit as st
from Question4_panda import comp_meda_moy_age


def set_backgrnd(image_url):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


# set_backgrnd("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Olympic_rings_without_rims.svg/2560px-Olympic_rings_without_rims.svg.png")
# set_backgrnd("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTDNdgJWyLwhwzPFbIsea2aqDSrCgR6llsmFg&s")
set_backgrnd("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ47kAo_eTdFrc7IFgcfPc6lQd6iDJRQJQgxNPvfhOa_FQhrdbDG3Z61eOeHyPPR9sPdkM&usqp=CAU")

st.title(":rainbow[Question 4 : Faut-il être jeune pour gagner une médaille ?]")
st.write(
    "Cette application permet de comparer l'obtention des médailles des athlètes "
    "en fonction de leur âge et de leur sexe."
)

# liste_sport =
# sport = st.selectbox("Sélectionner le sport étudié", options=liste_sport)
sport = st.text_input("Entrer le sport étudié (en anglais!!)")
genre = st.selectbox("Sélectionner le genre étudié", ["Homme", "Femme"])
methode = st.selectbox("Sélectionner la méthode", ["Médiane", "Moyenne"])

if st.button("Comparer !!!!!"):
    if genre == "Homme":
        genre = "M"
    else:
        genre = "F"
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
