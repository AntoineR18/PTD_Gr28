import importlib
import sys
import subprocess
import time
import os

# Créer le dossier 'Resultat' s'il n'existe pas (afin de sauvegarder les résultats)
os.makedirs("Resultat", exist_ok=True)


def main():
    streamlit_process = None

    while True:
        print("=== Menu PTD Groupe 28 ===")
        print("Install - Installer les dépendances nécessaires au projet.")
        print(
            "1 - Question 1 : Déterminer le nombre de médailles gagnées par"
            " Michael Phelps."
        )
        print("1p - Question 1 (pandas) : Question 1 + Le type de médaille.")
        print(
            "2 - Question 2 : Calculer les bornes de médailles par pays pour"
            " une année donnée."
        )
        print("2p - Question 2 (pandas) : Idem avec pandas.")
        print(
            "3 - Question 3 : Synthèse des médailles obtenues par un pays sur une"
            " année donnée."
        )
        print(
            "3p - Question 3 (pandas) : Synthèse des médailles obtenues par un pays sur"
            "une année donnée."
        )
        print(
            "3s - Question 3. Bonnus (streamlit)  : Application"
            " interactive des médailles."
        )
        print(
            "4 - Question 4 : Comparaison des performances des athlètes"
            " selon leur âge"
        )
        print(
            "4p - Question 4 (pandas) : Comparaison des performances des athlètes"
            " selon leur âge"
        )
        print(
            "4s - Question 4 (streamlit) : Comparaison des performances des athlètes"
            " selon leur âge"
        )
        print(
            "5 - Question 5 : Parmi les pays n’ayant obtenu aucune médaille sur une"
            " édition donnée, identifier le pays ayant le plus de participants."
        )
        print("5pa - Question 5.a (pandas)")
        print("5pb - Question 5.b (pandas) : Histogramme pour une année")
        print("5pc - Question 5.c (pandas) : Histogramme sur toute l'histoire")
        print(
            "6 - Question 6 : Donner, pour chaque pays, sa première participation"
            " aux Jeux Olympiques"
        )
        print("6p - Question 6 (pandas + matplotlib) : Avec une frise chronologique")
        print("7 - Question 7 : Nombre de participants selon certains filtres.")
        print(
            "8a - Question 8.a : Répartition des médailles par"
            " saison pour un pays donné."
        )
        print("8b - Question 8.b : Répartition globale des médailles - Été vs Hiver.")
        print("8c - Question 8.c : Top pays médaillés pour une saison donnée.")
        print("8d - Question 8.d : Part moyenne des médailles pour un pays.")
        print("9 - Question 9 : Proportion de femmes aux JO (par saison ou toutes).")
        print("10 - Question 10 : Établir la liste des athlètes ayant changé de"
              " nationalité au cours de leur carrière.")
        print("10c - Question 10 : Version carte.")
        print("noc - Conversion entre code NOC et pays")
        print("Streamlit_Fermeture - Fermer  Streamlit")
        print("--- Partie problème ---")
        print("AppNonSup - Accéder au résultat de la partie apprentissage"
              " non supervise")
        print("0. Quitter")

        choix = input("Votre choix : ")

        try:
            if choix == "Install":
                try:
                    packages = [
                        "pandas",
                        "matplotlib",
                        "numpy",
                        "scikit-learn",
                        "streamlit",
                        "plotly",
                        "pycountry",
                        "seaborn",
                        "subprocess"
                    ]

                    print("🔍 Vérification des dépendances...\n")

                    to_install = []

                    for pkg in packages:
                        try:
                            importlib.import_module(pkg)
                            print(f"✅ {pkg} est déjà installé.")
                        except ImportError:
                            print(f"❌ {pkg} n'est pas installé.")
                            to_install.append(pkg)

                    if not to_install:
                        print("\n🎉 Tous les packages nécessaires sont déjà installés.")
                        return

                    print("\n📦 Packages manquants à installer :")
                    print(", ".join(to_install))
                    confirmer = input("Souhaitez-vous installer les packages"
                                      " manquants ? (o/n) : ").lower()

                    if confirmer == "o":
                        python_exec = sys.executable
                        for pkg in to_install:
                            print(f"🔧 Installation de {pkg}...")
                            subprocess.check_call([python_exec,
                                                   "-m",
                                                   "pip",
                                                   "install",
                                                   pkg])
                        print("\n✅ Installation terminée.")
                    else:
                        print("⛔ Installation annulée par l'utilisateur.")

                except Exception as e:
                    print(f"❌ Une erreur est survenue pendant l'installation : {e}")
            elif choix == "1":
                t0 = time.time()
                import Question1
                Question1.afficher_resultat()
                t1 = time.time()
                print(f"⌛ Temps d'exécution : {t1 - t0:.3f} secondes")

            elif choix.lower() == "1p":
                t0 = time.time()
                import Question1_Pandas
                Question1_Pandas.afficher_resultat()
                t1 = time.time()
                print(f"⌛ Temps d'exécution : {t1 - t0:.3f} secondes")
            elif choix == "2":
                annee = int(input("Entrez l'année des JO : "))
                t0 = time.time()
                import Question2
                Question2.afficher_bornes_medailles(annee)
                t1 = time.time()
                print(f"⌛ Temps d'exécution : {t1 - t0:.3f} secondes")
            elif choix.lower() == "2p":
                annee = int(input("Entrez l'année des JO : "))
                t0 = time.time()
                import Question2_Pandas
                Question2_Pandas.afficher_bornes_medailles_par_nation_pandas(annee)
                t1 = time.time()
                print(f"⌛ Temps d'exécution : {t1 - t0:.3f} secondes")
            elif choix == "3":
                pays = input("Entrez le nom du pays : ")
                annee = input("Entrez l'année des JO : ")
                t0 = time.time()
                import Question3
                Question3.affichage_medaille_pays_JO(pays, annee)
                t1 = time.time()
                print(f"⌛ Temps d'exécution : {t1 - t0:.3f} secondes")
            elif choix.lower() == "3p":
                pays = input("Entrez le nom du pays : ")
                annee = int(input("Entrez l'année des JO : "))
                saison = input("Entrez la saison (Summer/Winter) : ")
                import Question3_Pandas

                Question3_Pandas.affichage_medaille_pays_JO(pays, annee, saison)
                t1 = time.time()
                print(f"⌛ Temps d'exécution : {t1 - t0:.3f} secondes")
            elif choix.lower() == "3s":
                if streamlit_process is None or streamlit_process.poll() is not None:
                    print("Lancement de l'application Streamlit...")
                    python_exec = sys.executable
                    streamlit_process = subprocess.Popen(
                        [python_exec, "-m", "streamlit", "run", "Question3_"
                         "Pandas_Streamlit.py"]
                    )
                else:
                    print("Streamlit est déjà en cours.")
            elif choix == "4":
                sport = input("Entrez le nom du sport en anglais (ex: Swimming) : ")
                methode = input("Méthode (moyenne/mediane) : ").lower()
                genre = input("Genre (M/F) : ").upper()
                t0 = time.time()
                import Question4

                Question4.comp_meda_age(sport, methode, genre)
                t1 = time.time()
                print(f"⌛ Temps d'exécution : {t1 - t0:.3f} secondes")
            elif choix.lower() == "4p":
                sport = input("Entrez le nom du sport en anglais (ex: Swimming) : ")
                methode = input("Méthode (moyenne/mediane) : ").lower()
                genre = input("Genre (M/F) : ").upper()
                t0 = time.time()
                import Question4_Pandas

                Question4_Pandas.comp_meda_moy_age(sport, methode, genre)
                t1 = time.time()
                print(f"⌛ Temps d'exécution : {t1 - t0:.3f} secondes")
            elif choix.lower() == "4s":
                if streamlit_process is None or streamlit_process.poll() is not None:
                    python_exec = sys.executable
                    print("Lancement de l'application Streamlit...")
                    streamlit_process = subprocess.Popen(
                        [python_exec, "-m", "streamlit", "run",
                         "Question4_streamlit.py"]
                    )
                else:
                    print("Streamlit est déjà en cours.")
            elif choix == "5":
                annee = int(input("Entrez l'année des JO : "))
                t0 = time.time()
                import Question5

                resultat = Question5.pays_non_medaille_max_annee(annee)
                print(resultat)
                t1 = time.time()
                print(f"⌛ Temps d'exécution : {t1 - t0:.3f} secondes")
            elif choix.lower() == "5pa":
                annee = int(input("Entrez l'année des JO : "))
                t0 = time.time()
                import Question5_Pandas

                resultat = Question5_Pandas.pays_non_medaille_max_annee_panda(annee)
                print(resultat)
                t1 = time.time()
                print(f"⌛ Temps d'exécution : {t1 - t0:.3f} secondes")
            elif choix.lower() == "5pb":
                annee = int(input("Entrez l'année des JO : "))
                import Question5_Pandas
                Question5_Pandas.diagramme_annee(annee)
            elif choix.lower() == "5pc":
                import Question5_Pandas
                Question5_Pandas.diagramme_histoire()
            elif choix == "6":
                pays = input("Entrez le nom du pays (ex: France) : ")
                t0 = time.time()
                import Question6

                Question6.afficher_annee_adhesion_depuis_tableau(pays)
                t1 = time.time()
                print(f"⌛ Temps d'exécution : {t1 - t0:.3f} secondes")
            elif choix.lower() == "6p":
                t0 = time.time()
                import Question6_Pandas
                # L'import suffit à exécuter la question et le graphique.
                Question6_Pandas.plot_frise_participations_jo()
                t1 = time.time()
                print(f"⌛ Temps d'exécution : {t1 - t0:.3f} secondes")
            elif choix == "7":
                import Question7_Pandas

                annee_input = input("Filtrer par année ? (ex: 2016 ou vide) : ").strip()
                annee = int(annee_input) if annee_input else None

                pays_input = input("Filtrer par pays (code NOC, ex: FRA)"
                                   " ou vide : ").strip().upper()
                pays = pays_input if pays_input else None

                sexe_input = input("Filtrer par sexe (M/F) ou vide : ").strip().upper()
                sexe = sexe_input if sexe_input in ("M", "F") else None

                medaille_input = input("Filtrer par médaillé ? (o = oui, n = non, "
                                       "vide = tous) : ").strip().lower()
                if medaille_input == "o":
                    medaille = True
                elif medaille_input == "n":
                    medaille = False
                else:
                    medaille = None

                Question7_Pandas.nb_participants(annee=annee, pays=pays, sexe=sexe,
                                                 medaille=medaille)

            elif choix.lower() == "8a":
                pays = input("Entrez le code NOC du pays (ex: FRA, USA, CHN) : ")
                import Question8_Pandas

                Question8_Pandas.plot_medaille_pays_selon_saison(pays.upper())
            elif choix.lower() == "8b":
                import Question8_Pandas

                Question8_Pandas.plot_medaille_global_ete_vs_hiver()
            elif choix.lower() == "8c":
                saison = input("Saison (Summer/Winter) : ")
                top_n = int(input("Nombre de pays à afficher (ex: 10) : "))
                import Question8_Pandas

                Question8_Pandas.plot_part_medaille_par_pays_dans_saison(saison, top_n)
            elif choix.lower() == "8d":
                pays = input("Entrez le code NOC du pays (ex: FRA, USA) : ")
                import Question8_Pandas

                Question8_Pandas.plot_medaille_normalisee_pays(pays.upper())
            elif choix == "9":
                saison = input("Saison (summer/winter) ou "
                               "vide pour les deux : ").strip().lower()
                if saison == "":
                    saison = None
                import Question9_Pandas
                Question9_Pandas.plot_proportion_femmes(saison)
            elif choix.lower() == "10":
                import Question10_Pandas
                Question10_Pandas.afficher_list()
            elif choix.lower() == "10c":
                import Question10_Carte
                option = input("Voulez-vous compter les allées venues ? (o/n)")
                if option.lower() == "o":
                    option = True
                else:
                    option = False
                Question10_Carte.afficher_carte(option)
            elif choix.lower() == "noc":
                from noc_country import noc_to_country, country_to_noc
                sous_choix = input("Tapez 1 pour convertir NOC → pays,"
                                   " ou 2 pour pays → NOC : ")

                if sous_choix == "1":
                    code = input("Entrez le code NOC (ex : FRA, USA, CHN) : ").upper()
                    pays = noc_to_country(code)
                    if pays:
                        print(f"✅ Le code {code} correspond à : {pays}")
                    else:
                        print(f"❌ Aucun pays trouvé pour le code : {code}")
                elif sous_choix == "2":
                    nom = input("Entrez le nom du pays (ex : France, China) : ")
                    noc = country_to_noc(nom)
                    if noc:
                        print(f"✅ Le pays {nom} a pour code : {noc}")
                    else:
                        print(f"❌ Aucun code trouvé pour le pays : {nom}")
                else:
                    print("Choix invalide.")
            elif choix == "Streamlit_Fermeture":
                if streamlit_process is not None and streamlit_process.poll() is None:
                    print("Fermeture de Streamlit...")
                    streamlit_process.terminate()
                    streamlit_process = None
                else:
                    print("Aucune application Streamlit en cours.")
            elif choix.lower() == "appnonsup":
                print("=--= Liste des choix pour l'apprentissage non supervisée =--=")
                print("1. Afficher la distribution des variables")
                print("2. Boxplot comparaison de variable")
                print("3. ACP : Nuage de points + Cercle des correlations")
                print("4. ACP : Nuage de points pour un sport")
                print("5. Clustering : K-means")
                print("6. Repartiton par sport")
                choix_app = input("Votre choix : ")
                import Probleme
                if choix_app == "1":
                    Probleme.plot_distributions()
                elif choix_app == "2":
                    var1 = input("Choix de la première variable (Age, Height, Weight):")
                    var2 = input("Choix de la seconde variable (Sex, Sport)")
                    Probleme.plot_boxplot(var1, var2)
                elif choix_app == "3":
                    Probleme.plot_cercle_correlation()
                    Probleme.plot_pca_individuals()
                elif choix_app == "4":
                    Probleme.plot_cercle_correlation()
                    Probleme.highlight_one_sport(
                        input("Donner le sport (Archery, Gymnastics, Basketball,...):"))
                elif choix_app == "5":
                    print("k est fixé à 4")
                    Probleme.plot_methode_coude()
                    Probleme.plot_kmeans_clusters()
                elif choix_app == "6":
                    Probleme.repartition_sport_par_cluster(
                        input("Donner le sport (Archery, Gymnastics, Basketball,...):"))
                else:
                    print("Erreur dans ton choix !")
            elif choix == "0":
                if streamlit_process is not None and streamlit_process.poll() is None:
                    print("Fermeture de Streamlit avant de quitter...")
                    streamlit_process.terminate()
                print("À bientôt !")
                break
            else:
                print("Choix invalide. Réessayez.")
        except Exception as e:
            print(f"❌ Erreur : {e}")
        input("\nAppuyez sur Entrée pour continuer...")


if __name__ == "__main__":
    main()
