# Objectif interface graphique
# faire pip install streamlit dans le terminal si vous avez pas

# pour lancer l'application :

import streamlit as st
from Question4_panda import comp_meda_moy_age


st.title(":rainbow[Question 4 : Faut-il être jeune pour gagner une médaille ?]")
st.write(
    "Cette application permet de comparer l'obtention des médailles des athlètes "
    "en fonction de leur âge et de leur sexe."
)

sport = st.text_input("Entrer le sport étudié (en anglais!!)")
genre = st.selectbox("Sélectionner le genre étudié", ["Homme", "Femme"])
methode = st.selectbox("Sélectionner la méthode", ["Médiane", "Moyenne"])

if st.button("Comparer !!!!!"):
    try:
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
    except ValueError as e:
        st.error(e)  # Affiche l'erreur dans l'interface graphique
    except Exception as e:  # Pour gérer d'autres exceptions
        st.error("Une erreur est survenue : {}".format(e))


# Pour lancer l'application, exécutez la commande suivante dans le terminal :
# python -m streamlit run "chemin d'accès au fichier"

# pour avoir le chemin d'accès on peut faire clic droit sur le fichier et copier le
# "relative path" hassoul
# sinon vous éxécutez le code et ça met le chemin d'accès en bleu dans le terminal, vous
# le copiez :)
