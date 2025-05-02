# Objectif interface graphique
# faire pip install streamlit dans le terminal si vous avez pas

# pour lancer l'application :

import streamlit as st
from Question4_panda import comp_meda_moy_age
from Question4 import table_sport
# import base64
# import os
# (servent pour la fonction background mais flm)


st.title(":rainbow[Question 4 : Faut-il être jeune pour gagner une médaille ?]")
st.write(
    "Cette application permet de comparer l'obtention des médailles des athlètes "
    "en fonction de leur âge et de leur sexe."
)

# liste_sport =
# sport = st.selectbox("Sélectionner le sport étudié", options=liste_sport)
# sport = st.text_input("Entrer le sport étudié (en anglais!!)")
genre = st.selectbox("Sélectionner le genre étudié", ["Homme", "Femme"])
if genre == "Homme":
    genre = "M"
else:
    genre = "F"
liste_sport = table_sport(genre)
sport = st.selectbox("Sélectionner le sport étudié", options=liste_sport)
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


# options graphiques :
# fonction pour le background: (flemme)

# def set_blurred_background(image_filename):
#     # Encode l'image en base64
#     image_path = os.path.join("images", image_filename)
#     # Check if file exists
#     if not os.path.exists(image_path):
#         st.error(f"Image file not found: {image_path}")
#         return  # Stop the function if the image is missing
#     with open(image_path, "rb") as image_file:
#         encoded = base64.b64encode(image_file.read()).decode()

#     # Injecte le CSS avec flou uniquement
#     st.markdown(f"""
#         <style>
#         .stApp {{
#             background-image: url("data:image/png;base64,{encoded}");
#             background-size: cover;
#             background-position: center;
#             background-repeat: no-repeat;
#             background-attachment: fixed;
#             filter: blur(5px);
#         }}
#         </style>
#     """, unsafe_allow_html=True)


# set_blurred_background("logo_jo.png")
