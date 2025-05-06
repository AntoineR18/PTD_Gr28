import importlib
import sys
import subprocess


def main():
    streamlit_process = None

    while True:
        print("=== Menu PTD Groupe 28 ===")
        print("Install. Installer les dépendances nécessaires au projet.")
        print(
            "1. Question 1 : Déterminer le nombre de médailles gagnées par"
            " Michael Phelps."
        )
        print("2. Question 1 (pandas) : Question 1 + Le type de médaille.")
        print(
            "3. Question 2 : Calculer les bornes de médailles par pays pour"
            " une année donnée."
        )
        print("4. Question 2 (pandas) : Idem avec pandas.")
        print(
            "5. Question 3 : Synthèse des médailles obtenues par un pays sur une"
            " année donnée."
        )
        print(
            "6. Question 3 (pandas) : Synthèse des médailles obtenues par un pays sur"
            "une année donnée."
        )
        print(
            "7. Question 3 bonnus (streamlit)  : Application"
            " interactive des médailles."
        )
        print(
            "8. Question 4 : Comparaison des performances des athlètes"
            " selon leur âge"
        )
        print(
            "9. Question 4 (pandas) : Comparaison des performances des athlètes"
            " selon leur âge"
        )
        print(
            "10. Question 4 (streamlit) : Comparaison des performances des athlètes"
            " selon leur âge"
        )
        print(
            "11. Question 5 : Parmi les pays n’ayant obtenu aucune médaille sur une"
            " édition donnée, identifier le pays ayant le plus de participants."
        )
        print("12. Question 5 (pandas)")
        print(
            "13. Question 6 : Donner, pour chaque pays, sa première participation"
            " aux Jeux Olympiques"
        )
        print("14. Question 6 (pandas + matplotlib) : Avec une frise chronologique")
        print(
            "15. Question 8.1 : Répartition des médailles par"
            " saison pour un pays donné."
        )
        print("16. Question 8.2 : Répartition globale des médailles - Été vs Hiver.")
        print("17. Question 8.3 : Top pays médaillés pour une saison donnée.")
        print("18. Question 8.4 : Part moyenne des médailles pour un pays.")
        print("Streamlit_Fermeture. Fermer  Streamlit")
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
                    confirmer = input(
                        "Souhaitez-vous installer les packages" " manquants ? (o/n) : "
                    ).lower()

                    if confirmer == "o":
                        python_exec = sys.executable
                        for pkg in to_install:
                            print(f"🔧 Installation de {pkg}...")
                            subprocess.check_call(
                                [python_exec, "-m", "pip", "install", pkg]
                            )
                        print("\n✅ Installation terminée.")
                    else:
                        print("⛔ Installation annulée par l'utilisateur.")

                except Exception as e:
                    print(f"❌ Une erreur est survenue pendant l'installation : {e}")
            elif choix == "1":
                import Question1

                # L'import suffit à exécuter
                Question1.afficher_resultat()
            elif choix == "2":
                import Question1_Pandas

                # L'import suffit à exécuter le graphique.
                Question1_Pandas.afficher_resultat()
            elif choix == "3":
                annee = int(input("Entrez l'année des JO : "))
                import Question2

                Question2.afficher_bornes_medailles(annee)
            elif choix == "4":
                annee = int(input("Entrez l'année des JO : "))
                import Question2_Pandas

                Question2_Pandas.afficher_bornes_medailles_par_nation_pandas(annee)
            elif choix == "5":
                pays = input("Entrez le nom du pays : ")
                annee = input("Entrez l'année des JO : ")
                import Question3

                Question3.affichage_medaille_pays_JO(pays, annee)
            elif choix == "6":
                pays = input("Entrez le nom du pays : ")
                annee = int(input("Entrez l'année des JO : "))
                saison = input("Entrez la saison (Summer/Winter) : ")
                import Question3_Pandas

                Question3_Pandas.affichage_medaille_pays_JO(pays, annee, saison)
            elif choix == "7":
                if streamlit_process is None or streamlit_process.poll() is not None:
                    print("Lancement de l'application Streamlit...")
                    streamlit_process = subprocess.Popen(
                        ["streamlit", "run", "Question3_" "Pandas_Streamlit.py"]
                    )
                else:
                    print("Streamlit est déjà en cours.")
            elif choix == "8":
                sport = input("Entrez le nom du sport en anglais (ex: Swimming) : ")
                methode = input("Méthode (moyenne/mediane) : ").lower()
                genre = input("Genre (M/F) : ").upper()
                import Question4

                Question4.comp_meda_age(sport, methode, genre)
            elif choix == "9":
                sport = input("Entrez le nom du sport en anglais (ex: Swimming) : ")
                methode = input("Méthode (moyenne/mediane) : ").lower()
                genre = input("Genre (M/F) : ").upper()
                import Question4_Pandas

                Question4_Pandas.comp_meda_moy_age(sport, methode, genre)
            elif choix == "10":
                if streamlit_process is None or streamlit_process.poll() is not None:
                    print("Lancement de l'application Streamlit...")
                    streamlit_process = subprocess.Popen(
                        ["streamlit", "run", "Question4_Pandas.py"]
                    )
                else:
                    print("Streamlit est déjà en cours.")
            elif choix == "11":
                annee = int(input("Entrez l'année des JO : "))
                import Question5

                resultat = Question5.pays_non_medaille_max_annee(annee)
                print(resultat)
            elif choix == "12":
                annee = int(input("Entrez l'année des JO : "))
                import Question5_Pandas

                resultat = Question5_Pandas.pays_non_medaille_max_annee_panda(annee)
                print(resultat)
            elif choix == "13":
                pays = input("Entrez le nom du pays (ex: France) : ")
                import Question6

                Question6.afficher_annee_adhesion_depuis_tableau(pays)
            elif choix == "14":
                import Question6_Pandas

                # L'import suffit à exécuter la question et le graphique.
                Question6_Pandas.plot_frise_participations_jo()
            elif choix == "15":
                pays = input("Entrez le code NOC du pays (ex: FRA, USA, CHN) : ")
                import Question8_Pandas

                Question8_Pandas.plot_medaille_pays_selon_saison(pays)
            elif choix == "16":
                import Question8_Pandas

                Question8_Pandas.plot_medaille_global_ete_vs_hiver()
            elif choix == "17":
                saison = input("Saison (Summer/Winter) : ")
                top_n = int(input("Nombre de pays à afficher (ex: 10) : "))
                import Question8_Pandas

                Question8_Pandas.plot_part_medaille_par_pays_dans_saison(saison, top_n)
            elif choix == "18":
                pays = input("Entrez le code NOC du pays (ex: FRA, USA) : ")
                import Question8_Pandas

                Question8_Pandas.plot_medaille_normalisee_pays(pays)

            elif choix == "Streamlit_Fermeture":
                if streamlit_process is not None and streamlit_process.poll() is None:
                    print("Fermeture de Streamlit...")
                    streamlit_process.terminate()
                    streamlit_process = None
                else:
                    print("Aucune application Streamlit en cours.")
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
